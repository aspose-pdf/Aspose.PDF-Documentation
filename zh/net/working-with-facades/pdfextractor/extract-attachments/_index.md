---
title: 从 PDF 文件中提取附件
type: docs
weight: 10
url: /zh/net/extract-attachments/
description: 本节介绍如何使用 PdfExtractor 类从 pdf 中提取附件。
lastmod: "2021-06-05"
---

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 提取功能的主要类别之一是附件提取。 这个类别提供了一组方法，不仅有助于提取附件，还提供了可以提供附件相关信息的方法，即 [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) 和 [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) 方法分别提供附件信息和附件名称。为了提取并获取附件，我们使用 [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) 和 [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) 方法。

以下代码片段向您展示了如何使用 PdfExtractor 方法：

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // 提取附件
    pdfExtractor.ExtractAttachment();

    // 获取附件名称
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extracting and storing...");
         // 获取提取的附件
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```