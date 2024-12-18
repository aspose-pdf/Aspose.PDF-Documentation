---
title: Работа с вложениями - Фасады
type: docs
weight: 50
url: /ru/net/working-with-attachments-facades/
description: Этот раздел объясняет, как работать с вложениями - Фасады с использованием класса PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

В этом разделе мы объясним, как работать с вложениями в PDF, используя Aspose.PDF для .NET Facades. Вложение - это дополнительный файл, который прикреплен к основному документу, это может быть различный тип файла, такой как PDF, Word, изображение или другие файлы. Вы узнаете, как добавлять вложения в PDF, получать информацию о вложении и сохранять его в файл, удалять вложение из PDF программно с помощью C#.

## Добавление вложения из файла в существующий PDF

Вы можете добавить вложение в существующий PDF-файл, используя класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Вложение можно добавить из файла на диске, используя путь к файлу. Вы можете добавить вложение, используя метод [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Этот метод принимает два аргумента: путь к файлу и описание вложения. Сначала вам нужно открыть существующий PDF-файл и добавить в него вложение. Затем вы можете сохранить выходной PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

Следующий фрагмент кода показывает, как добавить вложение из файла. Например, давайте добавим MP3-файл.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## Добавление вложения из потока в существующий PDF

Вложение можно добавить в PDF-файл из потока – FileStream – с помощью метода [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Этот метод принимает три аргумента: поток, имя вложения и описание вложения. Чтобы добавить вложение, нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и привязать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вы можете вызвать метод [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) для добавления вложения. Наконец, вы можете вызвать метод Save, чтобы сохранить обновленный PDF-файл. Следующий фрагмент кода показывает, как добавить вложение из потока.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Удаление всех вложений из существующего PDF файла

Метод [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет удалить все вложения из существующего PDF файла. Вызовите метод [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Наконец, вы должны вызвать метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) для сохранения обновленного PDF файла. Следующий фрагмент кода показывает, как удалить все вложения из существующего PDF файла.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```