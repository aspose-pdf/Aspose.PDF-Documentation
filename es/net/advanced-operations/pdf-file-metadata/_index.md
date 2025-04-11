---
title: Trabajando con metadatos de archivos PDF en C#
linktitle: Metadatos de archivos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 200
url: /es/net/pdf-file-metadata/
description: Explora cómo extraer y gestionar metadatos de PDF, como autor y título, en .NET usando Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata in C#",
    "alternativeHeadline": "Extracting and Managing PDF Metadata in C#",
    "abstract": "Desbloquea el poder de la gestión de archivos PDF con nuestra nueva función para desarrolladores de C#, que permite un acceso fluido a los metadatos de archivos PDF. Obtén información sobre las propiedades del archivo, extrae metadatos XMP y actualiza fácilmente la información del documento, agilizando tu proceso de manejo de documentos. Experimenta una funcionalidad mejorada para mantener y manipular metadatos PDF de manera eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF file metadata, C# PDF manipulation, get PDF file information, set PDF file information, XMP metadata, Aspose.PDF for .NET, document properties, PDF metadata management",
    "wordcount": "834",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2024-11-25",
    "description": "Esta sección explica cómo obtener información de archivos PDF, cómo obtener metadatos XMP de un archivo PDF, establecer información de archivos PDF."
}
</script>

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Obtener información del archivo PDF

Para obtener información específica de un archivo PDF, primero necesitas obtener el objeto [DocumentInfo](https://reference.aspose.com/pdf/es/net/aspose.pdf/documentinfo) utilizando la propiedad [Info](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/properties/info) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Una vez que se recupera el objeto [DocumentInfo](https://reference.aspose.com/pdf/es/net/aspose.pdf/documentinfo), puedes obtener los valores de las propiedades individuales. El siguiente fragmento de código te muestra cómo obtener información del archivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;

        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;
        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Establecer información del archivo PDF

Aspose.PDF for .NET te permite establecer información específica del archivo para un PDF, información como autor, fecha de creación, asunto y título. Para establecer esta información:

1. Crea un objeto [DocumentInfo](https://reference.aspose.com/pdf/es/net/aspose.pdf/documentinfo).
1. Establece los valores de las propiedades.
1. Guarda el documento actualizado utilizando el método Save de la clase Document.

El siguiente fragmento de código te muestra cómo establecer información del archivo PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        // Specify custom timezone
        docInfo.CreationTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Tokyo Standard Time").GetUtcOffset(docInfo.CreationDate);
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";
        docInfo.Producer = "Custom producer";
        docInfo.Creator = "Custom creator";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        // Specify custom timezone
        docInfo.CreationTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Tokyo Standard Time").GetUtcOffset(docInfo.CreationDate);
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";
        docInfo.Producer = "Custom producer";
        docInfo.Creator = "Custom creator";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtener metadatos XMP de un archivo PDF

Aspose.PDF te permite acceder a los metadatos XMP de un archivo PDF. Para obtener los metadatos de un archivo PDF:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) y abre el archivo PDF de entrada.
1. Obtén los metadatos del archivo utilizando la propiedad [Metadata](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/properties/metadata).

El siguiente fragmento de código te muestra cómo obtener metadatos del archivo PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Establecer metadatos XMP en un archivo PDF

Aspose.PDF te permite establecer metadatos en un archivo PDF. Para establecer metadatos:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document).
1. Establece los valores de metadatos utilizando la propiedad [Metadata](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/properties/metadata).
1. Guarda el documento actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save) del objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document).

El siguiente fragmento de código te muestra cómo establecer metadatos en un archivo PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Insertar metadatos con prefijo

Algunos desarrolladores necesitan crear un nuevo espacio de nombres de metadatos con un prefijo. El siguiente fragmento de código muestra cómo insertar metadatos con prefijo.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}
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