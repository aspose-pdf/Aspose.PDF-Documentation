---
title: Use FloatingBox for PDF Layout in Java
linktitle: Using FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: Learn how to use FloatingBox for text layout, multi-column content, and precise positioning in PDF documents with Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Create and position styled FloatingBox containers in PDF with Java
Abstract: This article explains how to use FloatingBox in Aspose.PDF for Java. It covers placing text in bordered floating containers, creating repeating multi-column layouts, using background colors, absolute offsets, and horizontal or vertical alignment options.
---
## Create and add a simple floating box

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

## Create multi-column layout

`multiColumnLayout` and `multiColumnLayout2` configure `ColumnInfo` with three columns and add repeating text fragments to the same floating box.

## Background, offsets, and alignment

The example class also demonstrates:

- `backgroundSupport`
- `offsetSupport`
- `alignTextToFloat`
