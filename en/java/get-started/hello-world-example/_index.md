---
title: Example of Hello World using Java
linktitle: Hello World Example
type: docs
weight: 20
url: /java/hello-world-example/
description: This sample demonstrates how to create a simple PDF document with styled Hello World text using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World example via Java
Abstract: This article provides a Hello World example for Aspose.PDF for Java. The example creates a new PDF document, adds a page, creates a TextFragment with custom position, font, and colors, appends the text to the page with TextBuilder, and saves the result as a PDF file.
---
A "Hello World" example is the shortest path to understanding the basic PDF creation workflow. In this article, the example creates a new PDF, places a styled text fragment on the page, and saves the output file.

The Java example follows these steps:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) object.
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) to the document.
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) with the text `Hello, world!`.
1. Set the text position, font, font size, background color, and foreground color.
1. Create a [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) for the page.
1. Append the text fragment to the page.
1. Save the PDF document.

The following Java code is based on `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
