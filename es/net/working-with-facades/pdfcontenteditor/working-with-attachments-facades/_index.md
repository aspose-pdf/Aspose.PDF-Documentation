---
title: Trabajando con Adjuntos - Fachadas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/working-with-attachments-facades/
description: Esta sección explica cómo trabajar con Adjuntos - Fachadas utilizando la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "La función Trabajando con Adjuntos - Fachadas en Aspose.PDF for .NET permite a los usuarios gestionar fácilmente los archivos adjuntos dentro de documentos PDF. Con funcionalidades para agregar, recuperar y eliminar varios tipos de archivos programáticamente utilizando la clase PdfContentEditor, esta función simplifica el proceso de mejorar la interactividad de PDF al permitir que los adjuntos se integren sin problemas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
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
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

En esta sección, explicaremos cómo trabajar con adjuntos en PDF utilizando Aspose.PDF for .NET Fachadas. Un adjunto es un archivo adicional que se adjunta a un documento principal, puede ser una variedad de tipos de archivos, como pdf, word, imagen u otros archivos. Aprenderás cómo agregar adjuntos a pdf, obtener la información de un adjunto y guardarlo en un archivo, eliminar el adjunto de PDF programáticamente con C#.

## Agregar Adjuntos desde un Archivo en un PDF Existente

Puedes agregar un adjunto en un archivo PDF existente utilizando la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). El adjunto se puede agregar desde un archivo en el disco utilizando la ruta del archivo. Puedes agregar un adjunto utilizando el método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método toma dos argumentos: la ruta del archivo y la descripción del adjunto. Primero, necesitas abrir el archivo PDF existente y agregar el adjunto en él. Luego puedes guardar el archivo PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

El siguiente fragmento de código te muestra cómo agregar un adjunto desde un archivo. Por ejemplo, agreguemos el archivo MP3.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Agregar Adjuntos desde un Stream en un PDF Existente

El adjunto se puede agregar en un archivo PDF desde un stream – FileStream – utilizando el método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método toma tres argumentos: stream, nombre del adjunto y descripción del adjunto. Para agregar un adjunto, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, puedes llamar al método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) para agregar el adjunto. Finalmente, puedes llamar al método Save para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo agregar un adjunto desde un Stream.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Eliminar Todos los Adjuntos de un Archivo PDF Existente

El método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite eliminar todos los adjuntos de un archivo PDF existente. Llama al método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Finalmente, debes llamar al método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todos los adjuntos de un archivo PDF existente.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}