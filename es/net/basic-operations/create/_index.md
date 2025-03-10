---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "La nueva función en Aspose.PDF for .NET permite a los desarrolladores crear documentos PDF programáticamente utilizando C# y VB.NET, agilizando el proceso para varias aplicaciones .NET como WinForms y ASP.NET. Con métodos simples para agregar páginas y texto, los usuarios pueden generar fácilmente archivos PDF personalizados desde cero, mejorando la funcionalidad de su aplicación y la experiencia del usuario.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Aspose.PDF for .NET API te permite crear y leer archivos PDF usando C# y VB.NET. La API se puede utilizar en una variedad de aplicaciones .NET, incluyendo WinForms, ASP.NET y varias otras. En este artículo, vamos a mostrar cómo usar Aspose.PDF for .NET API para generar y leer archivos PDF fácilmente en aplicaciones .NET.

## Cómo crear un archivo PDF usando C#

Para crear un archivo PDF usando C#, se pueden seguir los siguientes pasos.

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Agrega un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la colección [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) del objeto Document.
1. Agrega [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) a la colección [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Guarda el documento PDF resultante.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

En este caso, creamos un documento PDF de una página con tamaño de página A4, orientación vertical. Nuestra página contendrá un "Hola, Mundo" en la parte superior izquierda de la página.