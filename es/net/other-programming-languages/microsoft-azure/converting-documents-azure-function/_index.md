---
title: Convertir Documentos con la función de Microsoft Azure
linktitle: Convertir Documentos con la función de Microsoft Azure
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/converting-documents-with-microsoft-azure-function/
description: Aprenda a convertir documentos PDF utilizando Microsoft Azure Functions con Aspose.PDF for .NET, habilitando el procesamiento de documentos en la nube.
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting Documents with Microsoft Azure function",
    "alternativeHeadline": "Integrate PDF Conversion with Microsoft Azure Functions",
    "abstract": "La nueva función de conversión de documentos impulsada por Microsoft Azure permite a los usuarios transformar eficientemente archivos PDF en varios formatos como DOCX, HTML y JPEG utilizando Aspose.PDF for .NET y Azure Functions. Esta funcionalidad permite una integración fluida con los recursos de Azure, asegurando un procesamiento de archivos rápido y confiable adaptado para desarrolladores que buscan mejorar sus aplicaciones.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1256",
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
    "url": "/net/converting-documents-with-microsoft-azure-function/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-function/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

Este artículo proporciona instrucciones detalladas paso a paso para convertir documentos PDF en Microsoft Azure utilizando Aspose.PDF for .NET y la función de Azure.

## Requisitos Previos

* Visual Studio 2022 Community Edition con desarrollo de Azure instalado o Visual Studio Code.
* Cuenta de Azure: Necesita una suscripción de Azure, cree una cuenta gratuita antes de comenzar.
* SDK de .NET 6.
* Aspose.PDF for .NET.

## Crear Recursos de Azure

### Crear Cuenta de Almacenamiento

1. Vaya al Portal de Azure (https://portal.azure.com).
2. Haga clic en "Crear un recurso".
3. Busque "Cuenta de almacenamiento".
4. Haga clic en "Crear".
5. Complete los detalles:
   - Suscripción: Elija su suscripción.
   - Grupo de recursos: Cree uno nuevo o seleccione uno existente.
   - Nombre de la cuenta de almacenamiento: Ingrese un nombre único.
   - Región: Elija la región más cercana.
   - Rendimiento: Estándar.
   - Redundancia: LRS (almacenamiento redundante localmente).
6. Haga clic en "Revisar + crear".
7. Haga clic en "Crear".

### Crear Contenedor

1. Abra su cuenta de almacenamiento.
2. Vaya a "Contenedores" bajo "Almacenamiento de datos".
3. Haga clic en "+ Contenedor".
4. Nómbralo "pdfdocs".
5. Establezca el nivel de acceso público en "Privado".
6. Haga clic en "Crear".

## Crear Proyecto

### Crear Proyecto en Visual Studio

1. Abra Visual Studio 2022.
2. Haga clic en "Crear un nuevo proyecto".
3. Seleccione "Funciones de Azure".
4. Nombre su proyecto "PdfConverterAzure".
5. Elija ".NET 6.0" o posterior y "disparador HTTP".
6. Haga clic en "Crear".

### Crear Proyecto en Visual Studio Code

#### Instalar Requisitos Previos

1. Extensiones de Visual Code:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Instalar Azure Functions Core Tools:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Instalar Azure CLI:
- Windows: Descargue desde el sitio web de Microsoft.
- macOS: `brew install azure-cli`.
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### Configurar Proyecto

1. Abra el proyecto en Visual Studio Code:
```bash
code .
```

2. Agregue paquetes NuGet creando/actualizando `PdfConverterApp.csproj`:
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

## Instalar Paquetes NuGet Requeridos

En Visual Studio, abra la Consola del Administrador de Paquetes y ejecute:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

En Visual Studio Code, ejecute:
```bash
dotnet restore
```

## Configurar Conexión de Almacenamiento de Azure

Obtenga las Claves de Acceso para la cuenta de almacenamiento en Claves de acceso en el Portal de Azure. Estas claves se utilizarán para autenticar su aplicación.

1. Abra `local.settings.json`:
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

2. Reemplace `YOUR_STORAGE_CONNECTION_STRING` con su cadena de conexión de almacenamiento real del Portal de Azure.

## Configurar Licencia de Aspose

En Visual Studio:

1. Copie su archivo de licencia de Aspose.PDF al proyecto.
2. Haga clic derecho en el archivo de licencia y seleccione "Propiedades".
3. Establezca "Copiar en el directorio de salida" en "Copiar siempre".
4. Agregue el código de inicialización de la licencia en el Program.cs:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

## Crear código

Cree un nuevo archivo `PdfConverter.cs`:

```csharp
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

        // Open PDF document
        var document = new Aspose.Pdf.Document(sourceStream);

        // Create output stream
        using var outputStream = new MemoryStream();
        string targetBlobName = Path.GetFileNameWithoutExtension(sourceBlobName);

        // Convert based on format
        switch (targetFormat.ToLower())
        {
            case "docx":
                targetBlobName += ".docx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.DocX);
                break;

            case "html":
                targetBlobName += ".html";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Html);
                break;

            case "xlsx":
                targetBlobName += ".xlsx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Excel);
                break;

            case "pptx":
                targetBlobName += ".pptx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Pptx);
                break;

            case "jpeg":
            case "jpg":
                targetBlobName += ".jpg";
                foreach (var page in document.Pages)
                {
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(new Aspose.Pdf.Devices.Resolution(300));
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

Cree un nuevo archivo `ConvertPdfFunction.cs`:

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
        [HttpTrigger(AuthorizationLevel.Function, "post"), Route = "convert"] HttpRequest req,
        ILogger log)
    {
        try
        {
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
}
```

```csharp
// Startup.cs
[assembly: FunctionsStartup(typeof(PdfConverterAzure.Functions.Startup))]
namespace PdfConverterAzure.Functions
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            // Read configuration
            var config = builder.GetContext().Configuration;

            // Register services
            builder.Services.AddLogging();

            // Register Azure Storage
            builder.Services.AddSingleton(x => 
                new BlobServiceClient(config["AzureWebJobsStorage"]));

            // Configure Aspose License
            var license = new Aspose.Pdf.License();
            license.SetLicense("Aspose.PDF.lic");
        }
    }
}
```

## Probar Localmente

En Visual Studio:
1. Inicie el emulador de almacenamiento de Azure.
2. Ejecute el proyecto en Visual Studio.
3. Use Postman o curl para probar:

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

En Visual Studio Code:
1. Inicie la aplicación de función:
```bash
func start
```

2. Cargue un PDF para probar:
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Use Postman o curl para probar:
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Desplegar en Azure

En Visual Studio:
1. Haga clic derecho en el proyecto en Visual Studio.
2. Seleccione "Publicar".
3. Elija "Aplicación de Función de Azure".
4. Seleccione su suscripción.
5. Cree una nueva o seleccione una Aplicación de Función existente.
6. Haga clic en "Publicar".

En Visual Studio Code:
1. Presione F1 o Ctrl+Shift+P.
2. Seleccione "Funciones de Azure: Desplegar en Aplicación de Función".
3. Elija su suscripción.
4. Seleccione la aplicación de función creada anteriormente.
5. Haga clic en "Desplegar".

## Configurar Aplicación de Función de Azure

1. Vaya al Portal de Azure.
2. Abra su Aplicación de Función.
3. Vaya a "Configuración".
4. Agregue configuraciones de aplicación:
   - Clave: "ContainerName".
   - Valor: "pdfdocs".
5. Guarde los cambios.

## Probar el Servicio Desplegado

Use Postman o curl para probar:
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Formatos Soportados

La lista de formatos soportados se puede encontrar [aquí](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Solución de Problemas

### Opciones de Configuración Importantes

1. Agregar autenticación:
```csharp
[FunctionName("ConvertPdf")]
public async Task<IActionResult> Run(
    [HttpTrigger(AuthorizationLevel.Function, "post", Route = "convert")] HttpRequest req,
    ClaimsPrincipal principal,
    ILogger log)
{
    // Check authentication
    if (!principal.Identity.IsAuthenticated)
    {
        return new UnauthorizedResult();
    }
    // ...
}
```

2. Para archivos grandes, considere:
   - Aumentar el tiempo de espera de la función.
   - Usar un plan de consumo con más memoria.
   - Implementar carga/descarga en fragmentos.
   - Agregar seguimiento de progreso.

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con documentos PDF usando la función de Microsoft Azure",
    "alternativeHeadline": "Usando la función de Microsoft Azure para procesar documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, operaciones avanzadas en pdf, microsoft azure, función",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
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
                "contactType": "ventas",
                "areaServed": "EE. UU.",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/converting-documents-with-microsoft-azure-function/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-function/"
    },
    "dateModified": "2024-10-25",
    "description": "Aspose.PDF for .NET puede procesar documentos utilizando la función de Microsoft Azure."
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