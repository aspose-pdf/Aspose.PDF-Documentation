---
title: Извлечение вложений из PDF файла
type: docs
weight: 10
url: /ru/net/extract-attachments/
description: В этом разделе объясняется извлечение вложений из pdf с помощью класса PdfExtractor.
lastmod: "2021-06-05"
---

Одна из основных категорий в рамках возможностей извлечения пространства имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) — это извлечение вложений. This category provides a set of methods, which not only help extract the attachments but also provides the methods which can give you the attachment related information i.e. [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) and [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) methods provide attachment information and attachment name respectively. In order to extract and then get attachments we use [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) and [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) methods.

Эта категория предоставляет набор методов, которые не только помогают извлекать вложения, но и предоставляют методы, которые могут дать вам информацию, связанную с вложениями, т.е. методы [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) и [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) предоставляют информацию о вложении и имя вложения соответственно. Для извлечения и получения вложений мы используем методы [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) и [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

The following code snippet shows you how to use PdfExtractor methods:

Следующий фрагмент кода показывает, как использовать методы PdfExtractor:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Extract attachments
    pdfExtractor.ExtractAttachment();

    // Get attachment names
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extracting and storing...");
         // Get extracted attachments
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```