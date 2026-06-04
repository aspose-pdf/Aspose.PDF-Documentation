---
title: Add Text Stamps to PDF in Java
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Learn how to add text stamps to PDF documents in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add text stamps to PDF files with Java
Abstract: This article explains how to add text stamps to PDF files using Aspose.PDF for Java. It covers creating a background text stamp, positioning it, rotating it, and customizing font, size, style, and color.
---
## Add a text stamp to a PDF

1. Open the source PDF document.
1. Create a text stamp with the required text.
1. Set the rotation value for the target page.
1. Set the required text formatting options.
1. Save the updated PDF document.
1. Add the stamp to the target page and save the updated PDF.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
