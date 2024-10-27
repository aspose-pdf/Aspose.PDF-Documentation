---
title: Converting Documents with Microsoft Azure function
linktitle: Converting Documents with Microsoft Azure function
type: docs
weight: 20
url: /net/converting-documents-with-microsoft-azure-function/
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

This article provides detailed step-by-step instructions for converting PDF documents in Microsoft Azure using Aspose.PDF for .NET and Azure function.

## Prerequisites

The following code snippet tested with:

* Visual Studio 2022 Community Edition with installed Azure development or Visual Studio Code.
* Azure Account: You need an Azure subscription, create a free account before begin.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Create Azure Resources

### Create Storage Account
1. Go to Azure Portal (https://portal.azure.com).
2. Click "Create a resource".
3. Search for "Storage account".
4. Click "Create".
5. Fill in the details:
   - Subscription: Choose your subscription.
   - Resource group: Create new or select existing.
   - Storage account name: Enter a unique name.
   - Region: Choose nearest region.
   - Performance: Standard.
   - Redundancy: LRS (Locally redundant storage).
6. Click "Review + create".
7. Click "Create".

### Create Container
1. Open your storage account.
2. Go to "Containers" under "Data storage".
3. Click "+ Container".
4. Name it "pdfdocs".
5. Set public access level to "Private".
6. Click "Create".

## Create Project

### Create Visual Studio Project
1. Open Visual Studio 2022.
2. Click "Create a new project".
3. Select "Azure Functions".
4. Name your project "PdfConverterAzure".
5. Choose ".NET 6.0" or later and "HTTP trigger".
6. Click "Create".

### Create Visual Studio Code Project
#### Install Prerequisites
1. Visual Code extensions:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Install Azure Functions Core Tools:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Install Azure CLI:
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
    <AzureFunctionsVersion>v4</AzureFunctionsVersion>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Sdk.Functions" Version="4.1.1" />
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Azure.Storage.Blobs" Version="12.14.1" />
    <PackageReference Include="Microsoft.Azure.WebJobs.Extensions.Storage" Version="5.0.1" />
  </ItemGroup>
</Project>
```

## Install Required NuGet Packages
In Visual Studio open Package Manager Console and run:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

In Visual Studio Code run:
```bash
dotnet restore
```

## Configure Azure Storage Connection
Get Access Keys for the storage account under Access keys in the Azure Portal. These keys will be used to authenticate your application.

1. Open `local.settings.json`:
```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "YOUR_STORAGE_CONNECTION_STRING",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet",
        "ContainerName": "pdfdocs"
    }
}
```

2. Replace `YOUR_STORAGE_CONNECTION_STRING` with your actual storage connection string from Azure Portal.

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

## Create code
Create a new file `PdfConverter.cs`:

```csharp
using Aspose.Pdf;
using Azure.Storage.Blobs;
using System;
using System.IO;
using System.Threading.Tasks;

public class PdfConverter
{
    private readonly BlobContainerClient _containerClient;

    public PdfConverter(string connectionString, string containerName)
    {
        _containerClient = new BlobContainerClient(connectionString, containerName);
    }

    public async Task<string> ConvertToFormat(string sourceBlobName, string targetFormat)
    {
        // Download source PDF
        var sourceBlob = _containerClient.GetBlobClient(sourceBlobName);
        using var sourceStream = new MemoryStream();
        await sourceBlob.DownloadToAsync(sourceStream);
        sourceStream.Position = 0;

        // Load PDF document
        var pdfDocument = new Document(sourceStream);
        
        // Create output stream
        using var outputStream = new MemoryStream();
        string targetBlobName = Path.GetFileNameWithoutExtension(sourceBlobName);

        // Convert based on format
        switch (targetFormat.ToLower())
        {
            case "docx":
                targetBlobName += ".docx";
                pdfDocument.Save(outputStream, SaveFormat.DocX);
                break;

            case "html":
                targetBlobName += ".html";
                pdfDocument.Save(outputStream, SaveFormat.Html);
                break;

            case "xlsx":
                targetBlobName += ".xlsx";
                pdfDocument.Save(outputStream, SaveFormat.Excel);
                break;

            case "pptx":
                targetBlobName += ".pptx";
                pdfDocument.Save(outputStream, SaveFormat.Pptx);
                break;

            case "jpeg":
            case "jpg":
                targetBlobName += ".jpg";
                foreach (var page in pdfDocument.Pages)
                {
                    var jpegDevice = new JpegDevice(new Resolution(300));
                    jpegDevice.Process(page, outputStream);
                }
                break;

            default:
                throw new ArgumentException($"Unsupported format: {targetFormat}");
        }

        // Upload converted file
        outputStream.Position = 0;
        var targetBlob = _containerClient.GetBlobClient(targetBlobName);
        await targetBlob.UploadAsync(outputStream, true);

        return targetBlob.Uri.ToString();
    }
}
```

Create a new file `ConvertPdfFunction.cs`:

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;
using System;
using System.IO;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc;

public static class ConvertPdfFunction
{
    [FunctionName("ConvertPdf")]
    public static async Task<IActionResult> Run(
        [HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequest req,
        ILogger log)
    {
        try
        {
            SetAsposeLicense();

            // Read request body
            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);

            string sourceBlob = data?.sourceBlob;
            string targetFormat = data?.targetFormat;

            if (string.IsNullOrEmpty(sourceBlob) || string.IsNullOrEmpty(targetFormat))
            {
                return new BadRequestObjectResult("Please provide sourceBlob and targetFormat");
            }

            // Get configuration
            string connectionString = Environment.GetEnvironmentVariable("AzureWebJobsStorage");
            string containerName = Environment.GetEnvironmentVariable("ContainerName");

            // Convert PDF
            var converter = new PdfConverter(connectionString, containerName);
            string resultUrl = await converter.ConvertToFormat(sourceBlob, targetFormat);

            return new OkObjectResult(new { url = resultUrl });
        }
        catch (Exception ex)
        {
            log.LogError(ex, "Error converting PDF");
            return new StatusCodeResult(500);
        }
    }

    private static void SetAsposeLicense()
    {
        var license = new License();

        // Load the license from the embedded resource stream
        using (Stream licenseStream = Assembly.GetExecutingAssembly()
                                              .GetManifestResourceStream("YourNamespace.YourLicenseFileName.lic"))
        {
            if (licenseStream == null)
                throw new FileNotFoundException("Aspose license file not found in resources.");

            license.SetLicense(licenseStream);
        }
    }
}
```

## Test Locally
In Visual Studio:
1. Start the Azure Storage Emulator.
2. Run the project in Visual Studio.
3. Use Postman or curl to test:

```bash
curl -X POST http://localhost:7071/api/ConvertPdf \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

In Visual Studio Code:
1. Start the function app:
```bash
func start
```

2. Upload a PDF to test:
```bash
az storage blob upload \
    --account-name pdfconverterstore \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Use Postman or curl to test:
```bash
curl -X POST http://localhost:7071/api/ConvertPdf \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Deploy to Azure
In Visual Studio:
1. Right-click the project in Visual Studio.
2. Select "Publish".
3. Choose "Azure Function App".
4. Select your subscription.
5. Create new or select existing Function App.
6. Click "Publish".

In Visual Studio Code:
1. Press F1 or Ctrl+Shift+P.
2. Select "Azure Functions: Deploy to Function App".
3. Choose your subscription.
4. Select the function app created above.
5. Click "Deploy".

## Configure Azure Function App
1. Go to Azure Portal.
2. Open your Function App.
3. Go to "Configuration".
4. Add application settings:
   - Key: "ContainerName".
   - Value: "pdfdocs".
5. Save changes.

## Supported Formats
The list of supported formats can be found [here](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Performance
1. Use appropriate memory settings in host.json:
```json
{
    "version": "2.0",
    "functionTimeout": "00:10:00",
    "memoryThreshold": 1536
}
```

2. For large files, consider:
   - Increasing function timeout.
   - Using consumption plan with more memory.
   - Implementing chunked upload/download.
   - Adding progress tracking.