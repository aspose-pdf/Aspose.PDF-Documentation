---
title: Convert PDF to EPUB, Text, XPS, and More in Java
linktitle: Convert PDF to other formats
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-09"
description: Learn how to convert PDF files to EPUB, LaTeX, Markdown, text, XPS, and MobiXML in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to Convert PDF to other formats in Java
Abstract: This article explains how to convert PDF files into EPUB, TeX, Markdown, text, XPS, and MobiXML formats using Aspose.PDF for Java, with format-specific save options where needed.
---
## Convert PDF to EPUB, TeX, Markdown, text, XPS, or MobiXML

The conversion examples use the PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) as the source and save with format-specific options or target formats.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create [EpubSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/epubsaveoptions/) for the conversion.
1. Set the EPUB content recognition mode.
1. Save the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) in EPUB format.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        EpubSaveOptions saveOptions = new EpubSaveOptions();
        saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
        document.save(outputFile.toString(), saveOptions);
    }
}
```

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create `MarkdownSaveOptions` for the conversion.
1. Set the resources directory name and enable HTML image tags.
1. Save the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) in Markdown format.

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

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create [XpsSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xpssaveoptions/) for the conversion.
1. Enable embedded TrueType fonts in the XPS output.
1. Save the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) in XPS format.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
}
```
