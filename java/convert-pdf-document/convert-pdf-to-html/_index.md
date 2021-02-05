---
title: Convert PDF to HTML 
linktitle: Convert PDF to HTML
type: docs
weight: 100
url: /java/convert-pdf-to-html/
lastmod: "2021-02-04"
description: This article describes how to convert a PDF file into HTML. Aspose.PDF for Java provides the capability to convert HTML files into PDF format.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Java provides many features for converting various file formats to PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into HTML format and save the images from the PDF file in a particular folder.

{{% alert color="primary" %}}

Try online: You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-html](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion. 

## Convert PDF pages to HTML

Aspose.PDF for Java provides many features for converting various file formats to PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into HTML format and save the images from the PDF file in a particular folder.

The following code snippet shows you all the possible options that you can use when converting PDF to HTML.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoHTML {

    private ConvertPDFtoHTML() {

    }

    // The path to the documents directory.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoHTML_Simple();
        ConvertPDFtoHTML_SplittingOutput();
        ConvertPDFtoHTML_SpecifyFolderforStoringSVGFiles();
        ConvertPDFtoHTML_CompressingSVGImagesDuringConversion();
        ConvertPDFtoHTML_SpecifyingImagesFolder();
        ConvertPDFtoHTML_CreateSubsequentFilesBodyContentsOnly();

    }

    public static void ConvertPDFtoHTML_Simple() {
        // Open the source PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

        // Save the file into MS document format
        pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
    }
```
## Convert PDF to HTML - Splitting Output to Multi-page HTML

Aspose.PDF for Java supports the feature to convert PDF documents to various output formats including HTML. However when converting large PDF files (comprised of multiple pages), you may have a requirement to save individual PDF page to separate HTML file.

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion. Please try using the following code snippet.

```java
    public static void ConvertPDFtoHTML_SplittingOutput() {
        // Open the source PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

        // Instantiate HTML SaveOptions object
        HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

        // Specify to split the output into multiple pages
        htmlOptions.setSplitIntoPages(true);

        // Save the document
        pdfDocument.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
```
## Convert PDF to HTML - Avoid Saving Images in SVG Format

The default output format for saving images when converting from PDF to HTML is SVG. During conversion, some images from PDF are transformed into SVG vector images. This could be slow. Instead, the images could be transformed into PNG. To allow this, Aspose.PDF has the option to use SVG for vectors or to create PNGs.

In order to completely remove the rendering of images as SVG format when converting PDF files to HTML format, please try using the following code snippet.

```java
    public static void ConvertPDFtoHTML_SpecifyFolderforStoringSVGFiles() {
        // Load the PDF file
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");

        // Instantiate HTML save options object
        HtmlSaveOptions newOptions = new HtmlSaveOptions();

        // Specify the folder where SVG images are saved during PDF to HTML conversion
        newOptions.SpecialFolderForSvgImages = _dataDir.toString();

        // Save the output file
        doc.save(_dataDir + "SaveSVGFiles_out.html", newOptions);
    }
```
## Compressing SVG Images During Conversion 

To compress SVG images during PDF to HTML conversion, please try using the following code:

```java
    public static void ConvertPDFtoHTML_CompressingSVGImagesDuringConversion() {
        // Load the PDF file
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");

        // Create HtmlSaveOption with tested feature
        HtmlSaveOptions newOptions = new HtmlSaveOptions();

        // Compress the SVG images if there are any
        newOptions.setCompressSvgGraphicsIfAny(true);
        doc.save(_dataDir + "SaveSVGFiles_out.html", newOptions);
    }
```
## Convert PDF to HTML - Specify Images Folder

By default, when converting a PDF file to HTML, the images in the PDF are saved in a separate folder created in same directory that the output HTML is created. But sometimes, it is necessary to specify a different folder for saving images to when generating HTML files. To accomplish this, we introduced the [SaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/SaveOptions). SpecialFolderForAllImages property. It is used to specify the target folder for storing images.

```java
    public static void ConvertPDFtoHTML_SpecifyingImagesFolder() {

        // Load the PDF file
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");

        HtmlSaveOptions newOptions = new HtmlSaveOptions();

        // Specify the separate folder to save images
        newOptions.SpecialFolderForAllImages = _dataDir.toString();

        doc.save(_dataDir + "SaveSVGFiles_out.html", newOptions);
    }
```
## Create Subsequent Files with Body Contents Only

With the following simple code snippet, you can split the output HTML into pages. In the output pages, all HTML objects must go exactly where they go now (fonts processing and output, CSS creation and output, images creation and output), except that the output HTML will contain contents currently placed inside thetags (now “body” tags will be omitted). 

```java
    public static void ConvertPDFtoHTML_CreateSubsequentFilesBodyContentsOnly() {
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");

        HtmlSaveOptions options = new HtmlSaveOptions();
        // This is the tested setting
        options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
        options.setSplitIntoPages(true);

        doc.save(_dataDir + "CreateSubsequentFiles_out.html", options);
    }
```
## Transparent Text rendering 

In case the source/input PDF file contains transparent texts shadowed by foreground images, then there might be text rendering issues. So in order to cater such scenarios, SaveShadowedTextsAsTransparentTexts and SaveTransparentTexts properties can be used.

```java
    public static void ConvertPDFtoHTML_TransparentTextRendering() {
        
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");
        
        // Instantiate HTML SaveOptions object
        HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
        htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
        htmlOptions.SaveTransparentTexts = true;
        
        // Save the document
        doc.save(_dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
```
## PDF document layers rendering 

We can render PDF document layers in separate layer type element during PDF to HTML conversion:

```java
    public static void onvertPDFtoHTML_PDF_DocumentLayersRendering() {
        
        Document doc = new Document(_dataDir + "PDFToHTML.pdf");        
        // Instantiate HTML SaveOptions object
        
        HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

        // Specify to render PDF document layers separately in output HTML
        htmlOptions.setConvertMarkedContentToLayers(true);

        // Save the document
        doc.save(_dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```
PDF to HTML conversion is one of Aspose.PDF's most popular features because it makes it possible to view the content of PDF files on various platforms without using a PDF document viewer. The output HTML accords with to WWW standards and can easily be displayed in all web browsers. Using this feature, the PDF files can be viewed over hand held devices because you do not need to install any PDF viewing application but can use a simple web browser.

