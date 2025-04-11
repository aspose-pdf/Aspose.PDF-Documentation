---
title: Eliminar páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/delete-pdf-pages/
description: Esta sección explica cómo eliminar páginas PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "Elimina sin esfuerzo páginas específicas de tus documentos PDF utilizando Aspose.PDF for .NET Facades. Al utilizar la clase PdfFileEditor, puedes eliminar páginas no deseadas tanto de rutas de archivos como de flujos, simplificando tu proceso de edición de PDF con un control preciso sobre el resultado final. Mejora tus capacidades de gestión de documentos con esta eficiente función de eliminación de páginas",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Si deseas eliminar un número de páginas del archivo PDF que se encuentra en el disco, puedes utilizar la sobrecarga del método [Delete](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) que toma los siguientes tres parámetros: ruta del archivo de entrada, array de números de página a eliminar y ruta del archivo PDF de salida. El segundo parámetro es un array de enteros que representa todas las páginas que deben ser eliminadas. Las páginas especificadas se eliminan del archivo de entrada y el resultado se guarda como archivo de salida. El siguiente fragmento de código te muestra cómo eliminar páginas PDF utilizando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## Eliminar páginas PDF utilizando flujos

El método [Delete](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor) también proporciona una sobrecarga que te permite eliminar las páginas del archivo PDF de entrada, mientras que tanto los archivos de entrada como de salida están en los flujos. Esta sobrecarga toma los siguientes tres parámetros: flujo de entrada, array de enteros de páginas PDF a eliminar y flujo de salida. El siguiente fragmento de código te muestra cómo eliminar páginas PDF utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```