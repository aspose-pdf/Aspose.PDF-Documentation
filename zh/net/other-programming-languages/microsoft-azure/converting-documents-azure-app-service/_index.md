---
title: 使用 Microsoft Azure 应用服务转换文档
linktitle: 使用 Microsoft Azure 应用服务转换文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/converting-documents-with-microsoft-azure-app-service/
description: 了解如何使用 Microsoft Azure 应用服务和 Aspose.PDF for .NET 转换 PDF 文档，优化云中的文档工作流程。
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting Documents with Microsoft Azure App service",
    "alternativeHeadline": "Convert PDF Documents with Azure App Service Easily",
    "abstract": "通过新功能释放文档转换的力量，该功能允许用户无缝地将 PDF 文件转换为多种格式，包括 DOCX、HTML、JPG 和 PNG，使用 Microsoft Azure 应用服务。此功能利用 Aspose.PDF for .NET，提供了一个强大而高效的解决方案，用于处理云应用中的文档转换。通过将此转换功能集成到您的 Azure 项目中，提升您的工作流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1042",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/converting-documents-with-microsoft-azure-app-service/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-app-service/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

本文提供了在 Microsoft Azure 中使用 Aspose.PDF for .NET 和 Azure 应用服务转换 PDF 文档的详细逐步说明。

## 先决条件

* 安装了 Azure 开发的 Visual Studio 2022 Community Edition 或 Visual Studio Code。
* Azure 帐户：您需要一个 Azure 订阅，在开始之前创建一个免费帐户。
* .NET 6 SDK。
* Aspose.PDF for .NET。

## 创建 Azure 资源

### 创建应用服务

1. 转到 Azure 门户 (https://portal.azure.com)。
2. 创建一个新的资源组。
3. 创建一个新的应用服务：
   - 选择 .NET 6 (LTS) 运行时。
   - 选择适当的定价层。
4. 创建一个应用程序洞察资源以进行日志记录。

## 创建项目

### 创建 Visual Studio 项目

1. 打开 Visual Studio 2022。
2. 点击“创建新项目”。
3. 选择“ASP.NET Core Web API”。
4. 将您的项目命名为“PdfConversionService”。
5. 选择“.NET 6.0”或更高版本。
6. 点击“创建”。

### 创建 Visual Studio Code 项目

#### 安装先决条件

1. Visual Code 扩展：
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. 安装 Azure CLI：
- Windows：从 Microsoft 网站下载。
- macOS：`brew install azure-cli`。
- Linux：`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`。

#### 配置项目

1. 在 Visual Studio Code 中打开项目：
```bash
code .
```

2. 通过创建/更新 `PdfConverterApp.csproj` 添加 NuGet 包：
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

3. 添加配置：
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

4. 创建项目结构：
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## 安装所需的 NuGet 包

在 Visual Studio 中打开包管理器控制台并运行：
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

在 Visual Studio Code 中运行：
```bash
dotnet restore
```

## 配置 Aspose 许可证

在 Visual Studio 中：

1. 将您的 Aspose.PDF 许可证文件复制到项目中。
2. 右键单击许可证文件，选择“属性”。
3. 将“复制到输出目录”设置为“始终复制”。
4. 在 Program.cs 中添加许可证初始化代码：
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

### 创建代码

在 Visual Studio 中：
1. 右键单击 Controllers 文件夹。
2. 添加 → 新项 → API 控制器 - 空。
3. 将您的文件命名为“PdfController.cs”。

```csharp
// PdfController.cs
using Microsoft.AspNetCore.Mvc;

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
            {
                return BadRequest("No file uploaded");
            }

            // Validate input file is PDF
            if (!file.ContentType.Equals("application/pdf", StringComparison.OrdinalIgnoreCase))
            {
                return BadRequest("File must be a PDF");
            }

            using var inputStream = file.OpenReadStream();
            using var document = new Aspose.Pdf.Document(inputStream);
            using var outputStream = new MemoryStream();

            switch (outputFormat.ToLower())
            {
                case "docx":
                    document.Save(outputStream, Aspose.Pdf.SaveFormat.DocX);
                    return File(outputStream.ToArray(),
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        "converted.docx");

                case "html":
                    document.Save(outputStream, Aspose.Pdf.SaveFormat.Html);
                    return File(outputStream.ToArray(),
                        "text/html",
                        "converted.html");

                case "jpg":
                case "jpeg":
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice();
                    jpegDevice.Process(document.Pages[1], outputStream);
                    return File(outputStream.ToArray(),
                        "image/jpeg",
                        "converted.jpg");

                case "png":
                    var pngDevice = new Aspose.Pdf.Devices.PngDevice();
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

## 配置应用程序设置

1. 打开 appsettings.json。
2. 添加配置：
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
将 `Your-Connection-StringG` 替换为您在 Azure 门户中的实际连接字符串。

## 本地测试

在 Visual Studio 中：
1. 按 F5 运行应用程序。
2. Swagger UI 将打开。
3. 测试 /api/pdf/convert 端点：
   - 点击“试用”。
   - 上传 PDF 文件。
   - 选择输出格式。
   - 执行并验证转换。

在 Visual Studio Code 中：
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## 部署到 Azure

在 Visual Studio 中：
1. 右键单击项目。
2. 选择“发布”。
3. 选择“Azure”作为目标。
4. 选择“Azure 应用服务 (Windows)”。
5. 选择您的订阅和应用服务。
6. 点击“发布”。

在 Visual Studio Code 中：
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

## 配置 Azure 应用服务

1. 转到 Azure 门户。
2. 打开您的应用服务。
3. 配置设置：
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## 测试已部署的服务

使用 Postman 或 curl 进行测试：
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## 支持的格式

支持的格式列表可以在 [这里](https://docs.aspose.com/pdf/net/supported-file-formats/) 找到。

## 故障排除

### 重要配置选项

1. **文件大小限制**
添加到 web.config：
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

2. **CORS**（如有需要）
在 Program.cs 中：
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

3. **身份验证**（如有需要）
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        // Configure JWT options
    });
```

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Microsoft Azure 应用服务处理 PDF 文档",
    "alternativeHeadline": "使用 Microsoft Azure 应用服务处理 PDF 文档",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf 中的高级操作, microsoft azure, 应用服务",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/converting-documents-with-microsoft-azure-app-service/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-app-service/"
    },
    "dateModified": "2024-10-25",
    "description": "Aspose.PDF for .NET 可以使用 Microsoft Azure 应用服务处理文档。"
}
</script>

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "",
    "softwareVersion": "2024.10",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>