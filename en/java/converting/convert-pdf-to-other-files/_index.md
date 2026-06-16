---
title: Convert PDF to EPUB, Text, XPS, and More in Java
linktitle: Convert PDF to other formats
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Learn how to convert PDF files to EPUB, LaTeX, Markdown, text, XPS, and MobiXML in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to Convert PDF to other formats in Java
Abstract: This article explains how to convert PDF files into EPUB, TeX, Markdown, text, XPS, and MobiXML formats using Aspose.PDF for Java, with format-specific save options where needed.
---
Aspose.PDF for Java can export PDF documents into text, ebook, print, and markup-oriented output formats.

## Convert PDF to EPUB

Use this example when a PDF document should be exported to the EPUB ebook format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`EpubSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/epubsaveoptions/) and set the recognition mode to `Flow`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is exported as reflowable EPUB markup.
1. Save the converted EPUB file.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Convert PDF to TeX

Use this example when PDF content should be exported into TeX markup.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`TeXSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/texsaveoptions/) for TeX serialization.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is emitted as TeX markup.
1. Save the resulting TeX file.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to plain text

Use this example when a PDF document should be exported as a text file.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create a [`TextDevice`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.devices/textdevice/) to extract textual content from PDF pages.
1. Call `device.process(document.getPages().get_Item(1), outputFile.toString())` to write the first page as plain text.
1. Save the text output file.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to XPS

Use this example when a PDF document should be converted into XPS format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`XpsSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xpssaveoptions/) and enable embedded TrueType fonts.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF is serialized as XPS with embedded font resources.
1. Save the converted XPS file.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to Markdown

Use this example when PDF content should be exported as Markdown.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/markdownsaveoptions/) and configure the image resource directory plus HTML image-tag output.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is emitted as Markdown with external image resources.
1. Save the generated Markdown file.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to Mobi XML

Use this example when PDF content should be exported into Mobi-compatible XML.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Select [`SaveFormat`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/saveformat/) `MobiXml` as the target serialization format.
1. Call `document.save(outputFile.toString(), SaveFormat.MobiXml)` so the PDF is exported as Mobi-compatible XML.
1. Save the converted file.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
