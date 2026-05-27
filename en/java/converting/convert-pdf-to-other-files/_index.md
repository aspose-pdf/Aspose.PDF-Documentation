---
title: Convert PDF to EPUB, Text, XPS, and More in Java
linktitle: Convert PDF to other formats
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-05-27"
description: Learn how to convert PDF files to EPUB, LaTeX, Markdown, text, XPS, and MobiXML in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to Convert PDF to other formats in Java
Abstract: This article explains how to convert PDF files into EPUB, TeX, Markdown, text, XPS, and MobiXML formats using Aspose.PDF for Java, with format-specific save options where needed.
---
## Convert PDF to EPUB, TeX, Markdown, text, XPS, or MobiXML

The conversion examples use the PDF `Document` as the source and save with format-specific options or target formats.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        EpubSaveOptions saveOptions = new EpubSaveOptions();
        saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
        document.save(outputFile.toString(), saveOptions);
    }
}
```

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
}
```

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
}
```
