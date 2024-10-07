---
title: 附件操作 - Facades
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: 本节解释如何使用 PdfContentEditor 类处理附件 - Facades。
lastmod: "2021-06-05"
draft: false
---

在本节中，我们将解释如何使用 Aspose.PDF for .NET Facades 在 PDF 中处理附件。附件是附加到主文档的附加文件，可以是多种文件类型，如 pdf、word、图像或其他文件。您将学习如何向 pdf 添加附件、获取附件信息并将其保存到文件，使用 C# 从 PDF 中删除附件。

## 从现有 PDF 文件中添加附件

您可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类在现有 PDF 文件中添加附件。 附件可以通过文件路径从磁盘上的文件添加。您可以使用 [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法添加附件。此方法需要两个参数：文件路径和附件描述。首先，您需要打开现有的 PDF 文件并将附件添加到其中。然后，您可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存输出的 PDF 文件。

以下代码片段向您展示如何从文件中添加附件。例如，让我们添加 MP3 文件。

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## 从现有 PDF 中的流添加附件

可以使用 [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法从流 – FileStream – 向 PDF 文件中添加附件。此方法需要三个参数：流、附件名称和附件描述。为了添加附件，您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入的 PDF 文件。之后，您可以调用 [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) 方法来添加附件。最后，您可以调用 Save 方法来保存更新后的 PDF 文件。以下代码片段向您展示了如何从流中添加附件。

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## 从现有 PDF 文件中删除所有附件

[DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 方法属于 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类，允许您从现有 PDF 文件中删除所有附件。调用 [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) 方法。最后，您必须调用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法来保存更新后的 PDF 文件。以下代码片段向您展示如何从现有 PDF 文件中删除所有附件。

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```