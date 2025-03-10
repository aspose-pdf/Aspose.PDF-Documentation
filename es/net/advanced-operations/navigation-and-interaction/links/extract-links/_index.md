---
title: Extraer enlaces del archivo PDF
linktitle: Extraer enlaces
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/extract-links/
description: Descubre cómo extraer hipervínculos de documentos PDF en .NET utilizando Aspose.PDF para la gestión de contenido y el análisis de enlaces.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Links from the PDF File",
    "alternativeHeadline": "Effortlessly Extract Links from PDF Files",
    "abstract": "Extrae enlaces de archivos PDF sin problemas utilizando C# con la nueva clase AnnotationSelector. Esta función permite a los desarrolladores identificar y extraer fácilmente anotaciones de enlace de páginas específicas de un documento PDF, mejorando las capacidades de manipulación de PDF para aplicaciones que requieren una extracción precisa de enlaces.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Links, PDF extraction, C# PDF library, AnnotationSelector class, LinkAnnotation objects, PDF document manipulation, Aspose.PDF library, extract links from PDF",
    "wordcount": "303",
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
    "url": "/net/extract-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Extrae enlaces de PDF con C#. Este tema te explica cómo extraer enlaces utilizando la clase AnnotationSelector."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Extraer enlaces del archivo PDF

Los enlaces se representan como anotaciones en un archivo PDF, por lo que para extraer enlaces, extrae todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).

1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtén la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) de la que deseas extraer enlaces.
1. Utiliza la clase [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) de la página especificada.
1. Pasa el objeto [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) al método Accept del objeto Page.
1. Obtén todas las anotaciones de enlace seleccionadas en un objeto IList utilizando la propiedad Selected del objeto [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector).

El siguiente fragmento de código te muestra cómo extraer enlaces de un archivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractLinks.pdf"))
    {
        // Extract actions
        var page = document.Pages[1];
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
        page.Accept(selector);
        var list = selector.Selected;
        var annotation = (Aspose.Pdf.Annotations.Annotation)list[0];

        // Save PDF document
        document.Save(dataDir + "ExtractLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ExtractLinks.pdf");

    // Extract actions
    var page = document.Pages[1];
    var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
    page.Accept(selector);
    var list = selector.Selected;
    var annotation = (Aspose.Pdf.Annotations.Annotation)list[0];

    // Save PDF document
    document.Save(dataDir + "ExtractLinks_out.pdf");
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