---
title: Convertir Documentos con Microsoft Azure App Service
linktitle: Convertir Documentos con Microsoft Azure App Service
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/converting-documents-with-microsoft-azure-app-service/
description: Descubre cómo convertir documentos PDF con Microsoft Azure App Service y Aspose.PDF for .NET, optimizando los flujos de trabajo de documentos en la nube.
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
    "abstract": "Desbloquea el poder de la conversión de documentos con la nueva función que permite a los usuarios convertir sin problemas archivos PDF en varios formatos, incluyendo DOCX, HTML, JPG y PNG, utilizando Microsoft Azure App Service. Esta función aprovecha Aspose.PDF for .NET, proporcionando una solución robusta y eficiente para manejar transformaciones de documentos dentro de aplicaciones en la nube. Mejora tu flujo de trabajo integrando esta capacidad de conversión en tus proyectos de Azure hoy.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

Este artículo proporciona instrucciones detalladas paso a paso para convertir documentos PDF en Microsoft Azure utilizando Aspose.PDF for .NET y Azure App Service.

## Requisitos Previos

* Visual Studio 2022 Community Edition con desarrollo de Azure instalado o Visual Studio Code.
* Cuenta de Azure: Necesitas una suscripción de Azure, crea una cuenta gratuita antes de comenzar.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Crear Recursos de Azure

### Crear App Service

1. Ve al Portal de Azure (https://portal.azure.com).
2. Crea un nuevo Grupo de Recursos.
3. Crea un nuevo App Service:
   - Elige el runtime .NET 6 (LTS).
   - Selecciona el nivel de precios apropiado.
4. Crea un recurso de Application Insights para el registro.

## Crear Proyecto

### Crear Proyecto en Visual Studio

1. Abre Visual Studio 2022.
2. Haz clic en "Crear un nuevo proyecto".
3. Selecciona "ASP.NET Core Web API".
4. Nombra tu proyecto "PdfConversionService".
5. Selecciona ".NET 6.0" o posterior.
6. Haz clic en "Crear".

### Crear Proyecto en Visual Studio Code

#### Instalar Requisitos Previos

1. Extensiones de Visual Code:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. Instalar Azure CLI:
- Windows: Descarga desde el sitio web de Microsoft.
- macOS: `brew install azure-cli`.
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### Configurar Proyecto

1. Abre el proyecto en Visual Studio Code:
```bash
code .
```

2. Agrega paquetes NuGet creando/actualizando `PdfConverterApp.csproj`:
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

3. Agrega configuración:
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

4. Crea la estructura del proyecto:
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## Instalar Paquetes NuGet Requeridos

En Visual Studio abre la Consola del Administrador de Paquetes y ejecuta:
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

En Visual Studio Code ejecuta:
```bash
dotnet restore
```

## Configurar Licencia de Aspose

En Visual Studio:

1. Copia tu archivo de licencia de Aspose.PDF al proyecto.
2. Haz clic derecho en el archivo de licencia y selecciona "Propiedades".
3. Establece "Copiar en el Directorio de Salida" en "Copiar siempre".
4. Agrega el código de inicialización de la licencia en Program.cs:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

### Crear código

En Visual Studio:
1. Haz clic derecho en la carpeta Controllers.
2. Agrega → Nuevo Elemento → Controlador API - Vacío.
3. Nombra tu archivo "PdfController.cs".

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

## Configurar ajustes de la aplicación

1. Abre appsettings.json.
2. Agrega configuración:
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
Reemplaza `Your-Connection-StringG` con tu cadena de conexión real del Portal de Azure.

## Probar Localmente

En Visual Studio:
1. Presiona F5 para ejecutar la aplicación.
2. Se abrirá la interfaz de usuario de Swagger.
3. Prueba el endpoint /api/pdf/convert:
   - Haz clic en "Probar".
   - Sube un archivo PDF.
   - Selecciona el formato de salida.
   - Ejecuta y verifica la conversión.

En Visual Studio Code:
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## Desplegar en Azure

En Visual Studio:
1. Haz clic derecho en el proyecto.
2. Selecciona "Publicar".
3. Elige "Azure" como destino.
4. Selecciona "Azure App Service (Windows)".
5. Selecciona tu suscripción y App Service.
6. Haz clic en "Publicar".

En Visual Studio Code:
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

## Configurar Azure App Service

1. Ve al Portal de Azure.
2. Abre tu App Service.
3. Configura los ajustes:
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## Probar el Servicio Desplegado

Usa Postman o curl para probar:
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## Formatos Soportados

La lista de formatos soportados se puede encontrar [aquí](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Solución de Problemas

### Opciones de Configuración Importantes

1. **Límites de Tamaño de Archivo**
Agrega a web.config:
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

2. **CORS** (si es necesario)
En Program.cs:
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

3. **Autenticación** (si es necesario)
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
    "headline": "Trabajando con documentos PDF usando Microsoft Azure App Service",
    "alternativeHeadline": "Usando Microsoft Azure App Service para procesar documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, operaciones avanzadas en pdf, microsoft azure, app service",
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
                "areaServed": "US",
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
    "url": "/net/converting-documents-with-microsoft-azure-app-service/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-app-service/"
    },
    "dateModified": "2024-10-25",
    "description": "Aspose.PDF for .NET puede procesar documentos utilizando Microsoft Azure App Service."
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