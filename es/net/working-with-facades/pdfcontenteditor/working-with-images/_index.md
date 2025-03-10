---
title: Trabajar con Imágenes usando PdfContentEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/working-with-images-in-pdf
description: Esta sección explica cómo agregar y eliminar imágenes con Aspose.PDF Facades utilizando la clase PdfContentEditor.
lastmod: "2021-06-24"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with Images using PdfContentEditor",
    "alternativeHeadline": "Enhance PDF Images with PdfContentEditor Features",
    "abstract": "Aspose.PDF for .NET ahora ofrece capacidades mejoradas de gestión de imágenes a través de la clase PdfContentEditor, permitiendo a los usuarios eliminar fácilmente imágenes específicas de páginas designadas o eliminar completamente todas las imágenes de archivos PDF. Además, la función permite un reemplazo de imágenes sin problemas, agilizando el proceso de edición y mejorando la personalización del documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "415",
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
    "url": "/net/working-with-images-in-pdf",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images-in-pdf"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Eliminar Imágenes de una Página Particular de PDF (Facades)

Para eliminar las imágenes de una página particular, necesitas llamar al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) con los parámetros pageNumber e index. El parámetro index representa un array de enteros: los índices de las imágenes que se van a eliminar. Primero, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y luego llamar al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Después de eso, puedes guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código te muestra cómo eliminar imágenes de una página particular de PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage(2, new[] { 2 });

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage(2, new[] { 2 });

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Eliminar Todas las Imágenes de un Archivo PDF (Facades)

Todas las imágenes pueden ser eliminadas de un archivo PDF utilizando el método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Llama al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – la sobrecarga sin parámetros – para eliminar todas las imágenes, y luego guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código te muestra cómo eliminar todas las imágenes de un archivo PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage();

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage();

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Reemplazar Imagen en un Archivo PDF (Facades)

la [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite reemplazar tu imagen en un archivo PDF, llama para esto al método [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) y guarda el resultado.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf")))
    {
        editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}