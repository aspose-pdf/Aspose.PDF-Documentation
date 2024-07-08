---
title: Convert HTML to PDF
linktitle: Convert HTML to PDF
type: docs
weight: 40
url: /php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: This topic show you how to Aspose.PDF allows to convert HTML and MHTML formats to PDF file.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Overview

This article explains how to convert HTML to PDF using PHP. The code is very simple, just load HTML to Document class and save it as output PDF. Converting MHTML to PDF in Java is also similar. It covers the following topics

## Java HTML to PDF Converter Library

**Aspose.PDF for PHP via Java** is a PDF manipulation API that lets you convert any existing HTML documents to PDF seamlessly.
The process of converting HTML to PDF can be flexibly customized.

## Convert HTML to PDF

The following Java code sample shows how to convert an HTML document to a PDF.

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) class.
1. Initialize [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) object.
1. Save output PDF document by calling [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) method.

```php
    // Create an instance of HtmlLoadOptions to specify the load options for the HTML file
    $loadOption = new HtmlLoadOptions();

    // Create a new Document object and load the HTML file
    $document = new Document($inputFile, $loadOption);

    // Save the document as a PDF file
    $document->save($outputFile);
```

## Advanced conversion from HTML to PDF

The HTML Conversion engine has several options that allow us to control the conversion process.

### Media Queries Support

1. Create a HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. [Set Print or Screen](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-) mode.
1. Initialize [Document object](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Save output PDF document.

Media queries are a popular technique for delivering a tailored style sheet to different devices. We can set device type using [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) class.

```php

    // Create an instance of HtmlLoadOptions to specify the load options for the HTML file
    $htmlMediaType = new HtmlMediaType();

    // Set Print or Screen mode
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Create a new Document object and load the HTML file
    $document = new Document($inputFile, $loadOption);

    // Save the document as a PDF file
    $document->save($outputFile);
```

### Enable (disable) font embedding

1. Add new Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Disable font embedding.
1. Save a new Document.

HTML pages often use fonts (i.g. fonts from local folder, Google Fonts, etc). We can also control the embedding of fonts in a document using a [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-) property.

```php

    // Create an instance of HtmlLoadOptions to specify the load options for the HTML file
    $loadOption = new HtmlLoadOptions();

    // Disable font embedding
    $loadOption->setEmbedFonts(true);

    // Create a new Document object and load the HTML file
    $document = new Document($inputFile, $loadOption);

    // Save the document as a PDF file
    $document->save($outputFile);
```

## Convert MHTML to PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, short for MIME HTML, is a web page archive format used to combine resources that are typically represented by external links (such as images, Flash animations, Java applets, and audio files) with HTML code into a single file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Next code snippet show how to covert MHTML files to PDF format with Java:

```php

    // Create a new instance of the MhtLoadOptions class.
    $loadOption = new MhtLoadOptions();

    // Create a new instance of the Document class and load the MHTML file.
    $document = new Document($inputFile, $loadOption);

    // Save the document as a PDF file.
    $document->save($outputFile);
```
