---
title: Agregar un archivo adjunto a un documento PDF
linktitle: Agregar un archivo adjunto a un documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-attachment-to-pdf-document/
description: Esta página describe cómo agregar un archivo adjunto a un archivo PDF con la biblioteca Aspose.PDF para .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Attachment to a PDF document",
    "alternativeHeadline": "Easily Attach Files to Your PDF Documents",
    "abstract": "Aspose.PDF for .NET ahora ofrece una forma eficiente de mejorar tus documentos PDF al permitir a los usuarios agregar sin problemas varios archivos adjuntos, incluidos archivos de texto e imágenes. Esta funcionalidad simplifica el proceso de incrustar información adicional dentro de un PDF, asegurando que los datos esenciales estén fácilmente accesibles dentro de tus documentos. Optimiza la gestión de tus documentos con esta poderosa característica y mejora la experiencia del usuario manteniendo todos los recursos relevantes juntos",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Adding attachments to PDF, PDF file types, Aspose.PDF for .NET, FileSpecification object, Document object, EmbeddedFiles collection, PDF document manipulation, C# PDF library, PDF attachment functionality, Aspose.Drawing integration",
    "wordcount": "309",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Esta página describe cómo agregar un archivo adjunto a un archivo PDF con la biblioteca Aspose.PDF para .NET"
}
</script>

Los archivos adjuntos pueden contener una amplia variedad de información y pueden ser de varios tipos de archivos. Este artículo explica cómo agregar un archivo adjunto a un archivo PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.Drawing](/pdf/net/drawing/).

1. Crea un nuevo proyecto en C#.
1. Agrega una referencia a la DLL de Aspose.PDF.
1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crea un objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) con el archivo que estás agregando y la descripción del archivo.
1. Agrega el objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) a la colección [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), utilizando el método Add de la colección.

La colección [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) contiene todos los archivos adjuntos en el archivo PDF. El siguiente fragmento de código te muestra cómo agregar un archivo adjunto en un documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddEmbeddedFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"))
    {
        // Setup new file to be added as attachment
        Aspose.Pdf.FileSpecification fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "test.txt", "Sample text file");

        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);

        // Save PDF document
        document.Save(dataDir + "AddAnnotations_out.pdf");
    }
}
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