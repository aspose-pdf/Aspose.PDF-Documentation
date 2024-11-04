---
title: Trabajando con Adjuntos - Fachadas
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: Esta sección explica cómo trabajar con Adjuntos - Fachadas usando la Clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

En esta sección, explicaremos cómo trabajar con adjuntos en PDF usando Aspose.PDF para .NET Facades. Un adjunto es un archivo adicional que se adjunta a un documento principal, puede ser una variedad de tipos de archivos, como pdf, word, imagen, u otros archivos. Aprenderás cómo agregar adjuntos a pdf, obtener la información de un adjunto, guardarlo en un archivo, eliminar el adjunto del PDF programáticamente con C#.

## Agregar Adjunto desde un Archivo en un PDF Existente

Puedes agregar un adjunto en un archivo PDF existente usando la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). El archivo adjunto se puede agregar desde un archivo en el disco usando la ruta del archivo. Puede agregar un adjunto usando el método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método toma dos argumentos: ruta del archivo y descripción del adjunto. Primero, necesita abrir el archivo PDF existente y agregar el adjunto en él. Luego puede guardar el archivo PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

El siguiente fragmento de código le muestra cómo agregar un adjunto desde un archivo. Por ejemplo, vamos a agregar el archivo MP3.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## Añadir un Adjunto desde un Stream en un PDF Existente

El adjunto se puede agregar en un archivo PDF desde un stream – FileStream – utilizando el método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método toma tres argumentos: stream, nombre del adjunto y descripción del adjunto. Para agregar un adjunto, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y enlazar el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, puedes llamar al método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) para agregar el adjunto. Finalmente, puedes llamar al método Save para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo agregar un adjunto desde un Stream.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Eliminar Todos los Adjuntos de un Archivo PDF Existente

El método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite eliminar todos los adjuntos de un archivo PDF existente. Llama al método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Finalmente, debes llamar al método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todos los adjuntos de un archivo PDF existente.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```