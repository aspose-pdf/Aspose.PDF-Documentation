---
title: Working with Attachments - Facades
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: This section explains how to working with Attachments - Facades using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Add Attachment from a File in an Existing PDF

You can add an attachment in an existing PDF file using [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. The attachment can be added from a file on the disk using the file path. You can add attachment using [AddDocumentAttachment](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method. This method takes two arguments: file path and attachment description. First, you need to open the existing PDF file and add the attachement into it. Then you can save the output PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). 

The following code snippet shows you how to add attachment from a file. For example, let's add the MP3 file.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```

## Add Attachment from a Stream in an Existing PDF

Attachment can be added in a PDF file from a stream – FileStream – using [AddDocumentAttachment](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method. This method takes three arguments: stream, attachment name, and attachment description. In order to add attachment, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you can call [AddDocumentAttachment](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) method to add the attachment. Finally, you can call Save method to save the updated PDF file. The following code snippet shows you how to add attachment from a Stream.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Delete All Attachments from an Existing PDF File

[DeleteAttachments](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) method of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to delete all the attachments from an existing PDF file. Call the [DeleteAttachments](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) method. Finally, you have to call [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to delete all attachments from an existing PDF file.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
    ```
