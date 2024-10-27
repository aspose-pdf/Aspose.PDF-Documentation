---
title: Converting Documents with Microsoft Azure App service
linktitle: Converting Documents with Microsoft Azure App service
type: docs
weight: 10
url: /net/converting-documents-with-microsoft-azure-app-service/
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

This article provides detailed step-by-step instructions for converting PDF documents in Microsoft Azure using Aspose.PDF for .NET and Azure App service.

## Prerequisites

The following code snippet tested with:

* Visual Studio 2022 Community Edition with installed Azure development or Visual Studio Code.
* Azure Account: You need an Azure subscription, create a free account before begin.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Create Azure Resources

### Create App Service
1. Go to Azure Portal (https://portal.azure.com).
2. Create new Resource Group
3. Create new App Service:
   - Choose .NET 6 (LTS) runtime
   - Select appropriate pricing tier
4. Create Application Insights resource for logging.

## Create Project

### Create Visual Studio Project
1. Open Visual Studio 2022.
2. Click "Create a new project".
3. Select "ASP.NET Core Web API".
4. Name your project "PdfConversionService".
5. Select ".NET 6.0" or later.
6. Click "Create".

### Create Visual Studio Code Project
#### Install Prerequisites
1. Visual Code extensions:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. Install Azure CLI:
- Windows: Download from Microsoft's website
- macOS: `brew install azure-cli`
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`

#### Configure Project
1. Open project in Visual Studio Code:
```bash
code .
```

2. Add NuGet packages by creating/updating `PdfConverterApp.csproj`:
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.22.0" />
    <PackageReference Include="Microsoft.Extensions.Logging.AzureAppServices" Version="8.0.10" />
  </ItemGroup>
</Project>
```

3. Add configuration:
```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (web)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net6.0/PdfConversionService.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "stopAtEntry": false,
            "env": {
                "ASPNETCORE_ENVIRONMENT": "Development"
            }
        }
    ]
}
```

3. Create project structure:
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## Install Required NuGet Packages
In Visual Studio open Package Manager Console and run:
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

In Visual Studio Code run:
```bash
dotnet restore
```

## Configure Aspose License
In Visual Studio:
1. Copy your Aspose.PDF license file to the project.
2. Right-click on the license file.
3. Set "Copy to Output Directory" to "Copy always".
4. Add license initialization code in Program.cs:
   ```csharp
   var license = new Aspose.Pdf.License();
   license.SetLicense("Aspose.PDF.lic");
   ```

### Create code
In Visual Studio:
1. Right-click on Controllers folder
2. Add → New Item → API Controller Class
3. Name your file "PdfController.cs"

```csharp
// PdfController.cs
using Microsoft.AspNetCore.Mvc;
using Aspose.Pdf;
using Aspose.Pdf.Devices;

[ApiController]
[Route("api/[controller]")]
public class PdfController : ControllerBase
{
    private readonly ILogger<PdfController> _logger;

    public PdfController(ILogger<PdfController> logger)
    {
        _logger = logger;
    }

    [HttpPost("convert")]
    public async Task<IActionResult> ConvertPdf(
        IFormFile file,
        [FromQuery] string outputFormat = "docx")
    {
        try
        {
            if (file == null || file.Length == 0)
                return BadRequest("No file uploaded");

            // Validate input file is PDF
            if (!file.ContentType.Equals("application/pdf", StringComparison.OrdinalIgnoreCase))
                return BadRequest("File must be a PDF");

            using var inputStream = file.OpenReadStream();
            using var document = new Document(inputStream);
            using var outputStream = new MemoryStream();

            switch (outputFormat.ToLower())
            {
                case "docx":
                    document.Save(outputStream, SaveFormat.DocX);
                    return File(outputStream.ToArray(), 
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        "converted.docx");

                case "html":
                    document.Save(outputStream, SaveFormat.Html);
                    return File(outputStream.ToArray(), 
                        "text/html", 
                        "converted.html");

                case "jpg":
                case "jpeg":
                    var jpegDevice = new JpegDevice();
                    jpegDevice.Process(document.Pages[1], outputStream);
                    return File(outputStream.ToArray(), 
                        "image/jpeg", 
                        "converted.jpg");

                case "png":
                    var pngDevice = new PngDevice();
                    pngDevice.Process(document.Pages[1], outputStream);
                    return File(outputStream.ToArray(), 
                        "image/png", 
                        "converted.png");

                default:
                    return BadRequest("Unsupported output format");
            }
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error converting PDF");
            return StatusCode(500, "Internal server error");
        }
    }
}
```

```csharp
// Program.cs
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Add logging
builder.Services.AddApplicationInsightsTelemetry();
builder.Services.AddLogging(logging =>
{
    logging.AddConsole();
    logging.AddDebug();
    logging.AddAzureWebAppDiagnostics();
});

var app = builder.Build();

// Initialize license
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

## Configure application settings
1. Open appsettings.json.
2. Add configuration:
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ApplicationInsights": {
    "ConnectionString": "Your-Connection-String"
  }
}
```
Replace `Your-Connection-StringG` with your actual connection string from Azure Portal.

## Test Locally
In Visual Studio:
1. Press F5 to run the application
2. Swagger UI will open
3. Test the /api/pdf/convert endpoint:
   - Click "Try it out"
   - Upload a PDF file
   - Select output format
   - Execute and verify the conversion

In Visual Studio Code:
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## Deploy to Azure
In Visual Studio:
1. Right-click on the project
2. Select "Publish"
3. Choose "Azure" as target
4. Select "Azure App Service (Windows)"
5. Select your subscription and App Service
6. Click "Publish"

In Visual Studio Code:
```bash
dotnet publish -c Release

az webapp deployment source config-zip \
    --resource-group $resourceGroup \
    --name $appName \
    --src bin/Release/net6.0/publish.zip

az webapp deploy \
    --resource-group $resourceGroup \
    --name $appName \
    --src-path "Aspose.PDF.lic" \
    --target-path "site/wwwroot/Aspose.PDF.lic"
```

## Configure Azure App Service
1. Go to Azure Portal
2. Open your App Service
3. Configure settings:
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## Test the Deployed Service
Use Postman or curl to test:
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```
## Supported Formats
The list of supported formats can be found [here](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Trobleshooting
### Important Configuration Options

1. **File Size Limits**
Add to web.config:
```xml
<configuration>
  <system.webServer>
    <security>
      <requestFiltering>
        <requestLimits maxAllowedContentLength="104857600" />
      </requestFiltering>
    </security>
  </system.webServer>
</configuration>
```

2. **CORS** (if needed)
In Program.cs:
```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigin",
        builder => builder
            .WithOrigins("https://your-frontend-domain.com")
            .AllowAnyMethod()
            .AllowAnyHeader());
});
```

3. **Authentication** (if needed)
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        // Configure JWT options
    });
```

