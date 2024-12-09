---
title: Extract Attachments from PDF File
type: docs
weight: 10
url: /java/extract-attachments/
description: Learn how to extract attachments from a PDF file in Java with Aspose.PDF for managing document-related files.
lastmod: "2021-06-05"
draft: false
---

One of the main category under the extraction capabilities of [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) is the attachment extraction. This category provides a set of methods, which not only help extract the attachments but also provides the methods which can give you the attachment related information i.e. [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) and [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) methods provide attachment information and attachment name respectively. In order to extract and then get attachments we use [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) and [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--) methods.

The following code snippet shows you how to use PdfExtractor methods:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Extract attachments
        pdfExtractor.extractAttachment();

        // Get attachment names
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Extracting and storing...");
            // Get extracted attachments
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```
