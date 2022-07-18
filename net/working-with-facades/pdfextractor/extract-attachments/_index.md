---
title: Extract Attachments from PDF File
type: docs
weight: 10
url: /net/extract-attachments/
description: This section explains about extracting attachments from pdf with PdfExtractor class.
lastmod: "2021-06-05"
---

One of the main category under the extraction capabilities of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) is the attachment extraction. This category provides a set of methods, which not only help extract the attachments but also provides the methods which can give you the attachment related information i.e. [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) and [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) methods provide attachment information and attachment name respectively. In order to extract and then get attachments we use [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) and [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment) methods.

The following code snippet shows you how to use PdfExtractor methods:

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
