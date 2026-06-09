---
title: Add Text to PDF in Java
linktitle: Add Text to PDF
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: Learn how to add text, HTML fragments, lists, links, and custom fonts to PDF documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add text, links, HTML, and fonts to PDF files with Java
Abstract: This article explains how to add and style text in PDF documents using Aspose.PDF for Java. It covers simple text insertion, paragraph layout, hyperlinks, right-to-left text, font styling, transparency, borders, HTML and LaTeX fragments, gradient text, and custom fonts loaded from files or streams.
---
Aspose.PDF for Java supports both straightforward text insertion and more advanced text layout and styling flows.

## Add a simple text fragment

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create the [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and set its [Position](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/position/).
1. Add the [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) to the page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addTextSimpleCase(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```
