---
title: Cambiar tamaños de página en archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/changing-page-sizes-in-a-pdf-file/
description: Intenta aprender cómo cambiar los tamaños de página en un archivo PDF utilizando la clase PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "La función de la clase PdfPageEditor en Aspose.Pdf permite a los usuarios cambiar fácilmente el tamaño de las páginas de una o varias páginas dentro de un archivo PDF. Al utilizar la propiedad PageSize y la propiedad Pages, los usuarios pueden seleccionar entre varios tamaños de página predefinidos y aplicarlos de manera efectiva, mejorando la flexibilidad y personalización de los diseños de documentos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Detalles de implementación

La clase [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor) en el [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) contiene una propiedad llamada [PageSize](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) que se puede utilizar para cambiar el tamaño de página de una página individual o de múltiples páginas a la vez. La propiedad Pages se puede utilizar para asignar los números de las páginas a las que se debe aplicar el nuevo tamaño de página. La clase PageSize contiene una lista de diferentes tamaños de página como sus miembros. Cualquiera de los miembros de esta clase se puede asignar a la propiedad PageSize de la clase [PdfPageEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfpageeditor). También puede obtener el tamaño de página de cualquier página utilizando el método GetPageSize y pasando el número de página.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```