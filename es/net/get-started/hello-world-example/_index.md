---
title: Ejemplo de Hola Mundo usando el lenguaje C#
linktitle: Ejemplo de Hola Mundo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/hello-world-example/
description: Esta muestra demuestra cómo crear un documento PDF simple con el texto Hola Mundo usando Aspose.PDF
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta muestra demuestra cómo crear un documento PDF simple con el texto Hola Mundo usando Aspose.PDF",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

Un ejemplo de "Hola Mundo" se utiliza tradicionalmente para introducir características de un lenguaje de programación o software con un caso de uso simple.

Aspose.PDF for .NET es una API PDF rica en características que permite a los desarrolladores integrar capacidades de creación, manipulación y conversión de documentos PDF en sus aplicaciones .NET. Soporta trabajar con muchos formatos de archivo populares, incluyendo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivo de imagen. En este artículo, estamos creando un documento PDF que contiene el texto "¡Hola Mundo!". Después de instalar Aspose.PDF for .NET en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Agregar una [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) al objeto documento.
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).
1. Agregar TextFragment a la colección de [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la página.
1. [Guardar](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) el documento PDF resultante.

El siguiente fragmento de código es un programa Hola Mundo para exhibir el funcionamiento de la API Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

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