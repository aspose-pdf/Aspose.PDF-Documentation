---
title: Convert Other File Formats to PDF in Java
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-09"
description: Learn how to convert EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD, and TeX files to PDF in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: How to Convert other file formats to PDF in Java
Abstract: This article explains how to convert multiple source file formats to PDF using Aspose.PDF for Java. It covers EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, text, XML, XPS, and XSL-FO conversion workflows using format-specific load options and preprocessing steps where needed.
---
## Convert formats with dedicated load options

Examples such as EPUB, Markdown, OFD, XPS, TeX, PostScript, and EPS use a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor with the appropriate load options and then save directly to PDF.

1. Open the source EPUB file with [EpubLoadOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/epubloadoptions/).
1. Create the PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) from the source file.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

1. Open the source XPS file with [XpsLoadOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xpsloadoptions/).
1. Create the PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) from the source file.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
}
```

## Convert text to PDF

1. Read the source text file content with UTF-8 encoding.
1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) from the source text and add it to the page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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
