---
title: Use FloatingBox for PDF Layout in Java
linktitle: Using FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: Learn how to use FloatingBox for text layout, multi-column content, and precise positioning in PDF documents with Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Create and position styled FloatingBox containers in PDF with Java
Abstract: This article explains how to use FloatingBox in Aspose.PDF for Java. It covers placing text in bordered floating containers, creating repeating multi-column layouts, using background colors, absolute offsets, and horizontal or vertical alignment options.
---
## Create and add a simple floating box

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create the [FloatingBox](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/floatingbox/) and configure its layout and border settings.
1. Add the required [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) content to the [FloatingBox](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/floatingbox/).
1. Add the [FloatingBox](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/floatingbox/) to the page and save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void createAndAddFloatingBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("Lorem ipsum dolor sit amet."));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```
