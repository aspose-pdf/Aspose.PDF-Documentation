---
title: Cómo combinar PDF usando C#
linktitle: Combinar archivos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/merge-pdf-documents/
description: Esta página explica cómo combinar documentos PDF en un solo archivo PDF con C# o VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Descubre la poderosa capacidad de combinar múltiples documentos PDF en un solo archivo sin esfuerzo usando C# con la biblioteca Aspose.PDF. Esta función permite a los desarrolladores optimizar sus flujos de trabajo al combinar PDFs de manera eficiente, preservando la calidad y la estructura a lo largo del proceso. Perfecto para la integración de software, esta funcionalidad mejora la productividad al simplificar las tareas de gestión de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta página explica cómo combinar documentos PDF en un solo archivo PDF con C# o VB.NET."
}
</script>

## Combinar o unir múltiples PDF en un solo PDF en C#

Combinar PDF en C# no es una tarea sencilla sin usar una biblioteca de terceros. Este artículo muestra cómo combinar múltiples archivos PDF en un solo documento PDF usando Aspose.PDF for .NET. El ejemplo está escrito en C#, pero la API también se puede usar en otros lenguajes de programación .NET como VB.NET. Los archivos PDF se combinan de tal manera que el primero se une al final del otro documento.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Combinar archivos PDF

Para concatenar dos archivos PDF:

1. Crea dos objetos [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), cada uno conteniendo uno de los archivos PDF de entrada.
1. Luego llama al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) para el objeto Document al que deseas agregar el otro archivo PDF.
1. Pasa la colección PageCollection del segundo objeto Document al método Add de la colección PageCollection del primero.
1. Finalmente, guarda el archivo PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo concatenar archivos PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## Ejemplo en vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de combinación de presentaciones.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## También te puede interesar

- [Dividir PDF usando DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Concatenar documentos PDF usando Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Dividir PDF usando Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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