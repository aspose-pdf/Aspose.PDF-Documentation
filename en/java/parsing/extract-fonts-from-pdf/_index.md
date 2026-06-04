---
title: Extract Fonts from PDF via Java
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Use Aspose.PDF for Java to inspect and extract the fonts used in a PDF document.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Fonts from PDF using Java
Abstract: This article explains how to inspect the fonts used in a PDF document with Aspose.PDF for Java. It shows how to open a PDF, call `getFontUtilities().getAllFonts()`, and iterate through the resulting font objects to read their names.
---
Use font extraction when you need to audit document typography, inspect embedded resources, or verify font usage before conversion or archival workflows.

1. Open the source PDF document.
1. Get all fonts used in the document.
1. Iterate through the extracted fonts.
1. Print each font name.

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
