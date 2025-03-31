---
title: Agregar Marcadores a un archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/how-to-create-nested-bookmarks/
description: Esta sección explica cómo crear Marcadores Anidados con la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Bookmarks to PDF file",
    "alternativeHeadline": "Create Nested Bookmarks in PDF Documents Easily",
    "abstract": "Mejora tus documentos PDF con la nueva función de Marcadores Anidados utilizando la clase PdfContentEditor de Aspose.Pdf.Facades. Esta funcionalidad te permite crear marcadores jerárquicos que organizan tu contenido de manera efectiva, permitiendo a los usuarios navegar fácilmente a través de capítulos y páginas asociadas dentro del PDF. Agiliza la navegación del documento y mejora la experiencia del usuario con esta sofisticada solución de marcadores.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "211",
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
    "url": "/net/how-to-create-nested-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-create-nested-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Los marcadores te dan la opción de hacer un seguimiento/enlace a una página específica dentro del documento PDF. La clase [PdfContentEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/PdfContentEditor) en el [espacio de nombres Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) proporciona una función que te permite crear tu propio marcador de una manera sofisticada pero intuitiva dentro de un archivo PDF existente, en una página dada o en todas las páginas.

## Detalles de implementación

Además de la creación de marcadores simples, a veces tienes la necesidad de crear un marcador en forma de capítulos donde anidas los marcadores individuales dentro de los marcadores de capítulo para que cuando hagas clic en el signo + de un capítulo, veas las páginas dentro cuando se expanda el marcador, como se muestra en la imagen a continuación.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}