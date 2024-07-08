---
title: Convert PDF file to HTML format 
linktitle: Convert PDF file to HTML format
type: docs
weight: 50
url: /php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: This topic show you how to Aspose.PDF allows to convert PDF file to HTML format with PHP library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for PHP provides many features for converting various file formats to PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into HTML format and save the images from the PDF file in a particular folder.

{{% alert color="success" %}}
**Try to convert PDF to HTML online**

Aspose.PDF for PHP presents you online free application ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion.

## Convert PDF pages to HTML

Aspose.PDF for PHP provides many features for converting various file formats to PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into HTML format and save the images from the PDF file in a particular folder.

The following code snippet shows you all the possible options that you can use when converting PDF to HTML.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOption = new HtmlSaveOptions();

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOption);
```

## Convert PDF to HTML - Splitting Output to Multi-page HTML

Aspose.PDF for PHP supports the feature to convert PDF documents to various output formats including HTML. However when converting large PDF files (comprised of multiple pages), you may have a requirement to save individual PDF page to separate HTML file.

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion. Please try using the following code snippet.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOption = new HtmlSaveOptions();

// Specify to split the output into multiple pages
$saveOption->setSplitIntoPages(true);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOption);
```

## Convert PDF to HTML - Avoid Saving Images in SVG Format

The default output format for saving images when converting from PDF to HTML is SVG. During conversion, some images from PDF are transformed into SVG vector images. This could be slow. Instead, the images could be transformed into PNG. To allow this, Aspose.PDF has the option to use SVG for vectors or to create PNGs.

In order to completely remove the rendering of images as SVG format when converting PDF files to HTML format, please try using the following code snippet.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOption = new HtmlSaveOptions();

// Specify the folder where SVG images are saved during PDF to HTML conversion
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOption);
```

## Compressing SVG Images During Conversion

To compress SVG images during PDF to HTML conversion, please try using the following code:

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOptions);
```

## Convert PDF to HTML - Specify Images Folder

By default, when converting a PDF file to HTML, the images in the PDF are saved in a separate folder created in same directory that the output HTML is created. But sometimes, it is necessary to specify a different folder for saving images to when generating HTML files. To accomplish this, we introduced the [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).
[setSpecialFolderForAllImages method](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) is used to specify the target folder for storing images.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOptions);
```

## Transparent Text rendering

In case the source/input PDF file contains transparent texts shadowed by foreground images, then there might be text rendering issues. So in order to cater such scenarios, SaveShadowedTextsAsTransparentTexts and SaveTransparentTexts properties can be used.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOptions);
```

## PDF document layers rendering

We can render PDF document layers in separate layer type element during PDF to HTML conversion:

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new HtmlSaveOptions object for saving the document as HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// Save the document as HTML using the specified save options
$document->save($outputFile, $saveOptions);
```

PDF to HTML conversion is one of Aspose.PDF's most popular features because it makes it possible to view the content of PDF files on various platforms without using a PDF document viewer. The output HTML accords with to WWW standards and can easily be displayed in all web browsers. Using this feature, the PDF files can be viewed over hand held devices because you do not need to install any PDF viewing application but can use a simple web browser.
