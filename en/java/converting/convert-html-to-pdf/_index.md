---
title: Convert HTML to PDF file in Java
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Explore how to convert HTML content into PDF format using Aspose.PDF in Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: 
Abstract: This article provides a comprehensive guide on converting HTML and MHTML documents to PDF format using Java, with a focus on utilizing the Aspose.PDF for Java API. It outlines step-by-step instructions and code samples for basic conversion tasks, such as loading HTML documents into a Document object and saving them as PDF files. It also delves into advanced conversion features, including media queries support, font embedding options, and managing external resource loading. Additionally, the article offers online conversion tools for both HTML and MHTML formats to PDF, allowing users to explore the functionality and quality of the conversion process.
---

## Overview

This article explains how to convert HTML to PDF using Java. The code is very simple, just load HTML to Document class and save it as output PDF. Converting MHTML to PDF in Java is also similar. It covers the following topics

- [Java HTML to PDF](#convert-html-to-pdf)
- [Java MHTML to PDF](#convert-mhtml-to-pdf)
- [Java Convert HTML to PDF](#convert-html-to-pdf)
- [Java Convert MHTML to PDF](#convert-mhtml-to-pdf)
- [Java PDF from HTML](#convert-html-to-pdf)
- [Java PDF from MHTML](#convert-mhtml-to-pdf)
- [Java HTML to PDF Converter - How to Convert WebPage to PDF](#convert-html-to-pdf)
- [Java HTML to PDF Library, API or Code to Render, Save, Generate or Create PDF Programmatically from HTML](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java** is a PDF manipulation API that lets you convert any existing HTML documents to PDF seamlessly.
The process of converting HTML to PDF can be flexibly customized.

## Convert HTML to PDF

The following Java code sample shows how to convert an HTML document to a PDF.

1. Create an instance of the [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) class.
1. Initialize [Document](https://reference.aspose.com/page/java/com.aspose.page/document) object.
1. Save output PDF document by calling **Document.save(String)** method.

```java
// Open the source PDF document
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instantiate HTML SaveOptions object
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Save the document
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Try to convert HTML to PDF online**

Aspose presents you online free application ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Advanced conversion from HTML to PDF

The HTML Conversion engine has several options that allow us to control the conversion process.

### Media Queries Support

1. Create a HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Set Print or Screen mode. 
1. Initialize [Document object](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Save output PDF document. 

Media queries are a popular technique for delivering a tailored style sheet to different devices. We can set device type using [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) property.

```java
// Create a HTML LoadOptions
HtmlLoadOptions options = new HtmlLoadOptions();

// Set Print or Screen mode
options.setHtmlMediaType(HtmlMediaType.Print);

// Initialize document object
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Save output PDF document
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```

### Enable (disable) font embedding

1. Add new Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Enable/Disable font embedding.
1. Save a new Document.

HTML pages often use fonts (i.g. fonts from local folder, Google Fonts, etc). We can also control the embedding of fonts in a document using a [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--) property.

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Enable/Disable font embedding
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Manage external resource loading

The Conversion Engine provides a mechanism that allows you to control the loading of certain resources associated with the HTML document.
The [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) class has the property [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) with which we can define the behavior of the resource loader.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Creating clear template resource for replacing:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Return empty byte array in case i.imgur.com server
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Process resources with default resource loader
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Convert MHTML to PDF

{{% alert color="success" %}}
**Try to convert MHTML to PDF online**

Aspose.PDF for Java presents you online free application ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion MHTML to PDF using Free App](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, short for MIME HTML, is a web page archive format used to combine resources that are typically represented by external links (such as images, Flash animations, Java applets, and audio files) with HTML code into a single file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Next code snippet show how to covert MHTML files to PDF format with Java:

```java
// Create an instance of MhtLoadOptions to specify the load options for the
// MHTML file.
MhtLoadOptions options = new MhtLoadOptions();

// Set the path of the MHTML file.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Load the MHTML file into a Document object.
Document document = new Document(mhtmlFileName, options);

// Save the document as a PDF file.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Close the document.
document.close();
```
