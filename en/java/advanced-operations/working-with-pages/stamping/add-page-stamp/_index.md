---
title: Add Page Stamps to PDF in Java
linktitle: Adding Page Stamps
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Learn how to add PDF page stamps as overlays or backgrounds in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add page-based stamps to PDF files with Java
Abstract: This article explains how to add a page stamp to a PDF document using Aspose.PDF for Java. The example loads another PDF page as a stamp, configures it as a background, and applies it to a target page.
---
## Add a PDF page as a stamp

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the [PdfPageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfpagestamp/) object from the source PDF page.
1. Configure the required [PdfPageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfpagestamp/) placement options.
1. Add the configured stamp to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```
