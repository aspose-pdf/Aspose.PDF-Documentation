---
title: Convert Other File Formats to PDF in Java
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-04"
description: Learn how to convert EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD, and TeX files to PDF in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: How to Convert other file formats to PDF in Java
Abstract: This article explains how to convert multiple source file formats to PDF using Aspose.PDF for Java. It covers EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, text, XML, XPS, and XSL-FO conversion workflows using format-specific load options and preprocessing steps where needed.
---
## Convert formats with dedicated load options

Examples such as EPUB, Markdown, OFD, XPS, TeX, PostScript, and EPS use a `Document` constructor with the appropriate load options and then save directly to PDF.

1. Open the source EPUB file with EPUB load options.
1. Create the PDF document from the source file.
1. Save the output PDF document.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

1. Open the source XPS file with XPS load options.
1. Create the PDF document from the source file.
1. Save the output PDF document.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

## Convert text to PDF

1. Read the source text file content with UTF-8 encoding.
1. Create a new PDF document.
1. Add a page to the document.
1. Create a text fragment from the source text and add it to the page.
1. Save the output PDF document.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
}
```
