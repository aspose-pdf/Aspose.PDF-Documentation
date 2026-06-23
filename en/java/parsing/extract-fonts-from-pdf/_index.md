---
title: Extract Fonts from PDF via Java
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Use Aspose.PDF for Java to inspect and extract the fonts used in a PDF document.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Fonts from PDF using Java
Abstract: This article explains how to inspect the fonts used in a PDF document with Aspose.PDF for Java. It shows how to open a PDF, call `getFontUtilities().getAllFonts()`, and iterate through the resulting font objects to read their names.
---
Use font extraction when you need to audit document typography, inspect embedded resources, or verify font usage before conversion or archival workflows.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Call `document.getFontUtilities().getAllFonts()` to collect every [Font](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/font/) resource referenced by the document.
1. Iterate through the extracted [Font](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/font/) objects and read each font name from the font metadata.
1. Print the font names so the document typography can be audited or exported.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
