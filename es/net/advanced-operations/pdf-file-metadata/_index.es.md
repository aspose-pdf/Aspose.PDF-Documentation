---
title: Trabajando con Metadatos de Archivos PDF | C#
linktitle: Metadatos de Archivo PDF
type: docs
weight: 140
url: /net/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener Metadatos XMP de un archivo PDF, establecer Información de Archivo PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Metadatos de Archivos PDF | C#",
    "alternativeHeadline": "Cómo obtener Metadatos de Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, metadatos de archivo pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección explica cómo obtener información de archivos PDF, cómo obtener Metadatos XMP de un archivo PDF, establecer Información de Archivo PDF."
}
</script
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtener Información del Archivo PDF

Para obtener información específica de un archivo PDF, primero necesitas obtener el objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) usando la propiedad [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Una vez que el objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) es recuperado, puedes obtener los valores de las propiedades individuales. El siguiente fragmento de código muestra cómo obtener información del archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Obtener información del documento
DocumentInfo docInfo = pdfDocument.Info;
// Mostrar información del documento
Console.WriteLine("Autor: {0}", docInfo.Author);
Console.WriteLine("Fecha de Creación: {0}", docInfo.CreationDate);
Console.WriteLine("Palabras clave: {0}", docInfo.Keywords);
Console.WriteLine("Fecha de Modificación: {0}", docInfo.ModDate);
Console.WriteLine("Asunto: {0}", docInfo.Subject);
Console.WriteLine("Título: {0}", docInfo.Title);
```
## Configurar la Información del Archivo PDF

Aspose.PDF para .NET te permite configurar información específica del archivo para un PDF, información como autor, fecha de creación, asunto y título. Para configurar esta información:

1. Crea un objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
2. Establece los valores de las propiedades.
3. Guarda el documento actualizado usando el método Save de la clase Document.

{{% alert color="primary" %}}

Ten en cuenta que no puedes establecer valores para los campos *Application* y *Producer*, porque se mostrarán Aspose Ltd. y Aspose.PDF para .NET x.x.x en estos campos.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo configurar la información del archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Especificar la información del documento
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "Información PDF";
docInfo.Title = "Configuración de la Información del Documento PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Guardar el documento de salida
pdfDocument.Save(dataDir);
```

## Obtener Metadatos XMP de Archivo PDF

Aspose.PDF te permite acceder a los metadatos XMP de un archivo PDF. Para obtener los metadatos de un archivo PDF:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) y abre el archivo PDF de entrada.
1. Obtén los metadatos del archivo usando la propiedad [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

El siguiente fragmento de código te muestra cómo obtener metadatos del archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Obtener propiedades
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Establecer Metadatos XMP en un Archivo PDF

Aspose.PDF te permite establecer metadatos en un archivo PDF.
Aspose.PDF permite configurar los metadatos en un archivo PDF.

1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Establece los valores de los metadatos usando la propiedad [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Guarda el documento actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

El siguiente fragmento de código muestra cómo configurar los metadatos en un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Establecer propiedades
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Apodo";
pdfDocument.Metadata["xmp:CustomProperty"] = "Valor Personalizado";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Guardar documento
pdfDocument.Save(dataDir);
```
## Insertar Metadatos con Prefijo

Algunos desarrolladores necesitan crear un nuevo espacio de nombres de metadatos con un prefijo. El siguiente fragmento de código muestra cómo insertar metadatos con prefijo.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Se eliminó el prefijo Xmlns
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Guardar documento
pdfDocument.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

Claro, por favor proporcione el documento o el contenido específico que necesita traducir al español, manteniendo el formato Markdown original y las especificaciones que ha mencionado.
