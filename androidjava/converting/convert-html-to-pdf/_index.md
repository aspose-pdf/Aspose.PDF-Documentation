---
title: Convert HTML to PDF 
linktitle: Convert HTML to PDF
type: docs
weight: 280
url: /androidjava/convert-html-to-pdf/
lastmod: "2021-06-05"
description: You can convert HTML to PDF in a way convenient for you, in a quick way, and in an advanced way. Also, the way is described here Convert Web page to PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Java provides the capability to convert HTML pages to PDF format. The [HtmlLoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) class supports the feature to load HTML contents and then save the output in PDF format.

## How to convert HTML file to PDF Simple variant:

1. Create a HTML [LoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions).
1. Initialize [Document object](<https://apireference.aspose.com/page/java/com.aspose.page/document>).
1. Save output PDF document.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;
Simple
public final class ConvertHTMLtoPDF {

    private ConvertHTMLtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {

        ConvertHTMLtoPDF_();
        ConvertHTMLtoPDFAdvanced_MediaType();
    }

    private static void ConvertHTMLtoPDF_Simple() {
        // Create a HTML LoadOptions
        HtmlLoadOptions options = new HtmlLoadOptions();

        // Initialize document object
        String htmlFileName = Paths.get(_dataDir.toString(), "test.html").toString();
        Document document = new Document(htmlFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(), "HTMLtoPDF.pdf").toString());
    }
```
 And after you can see Advanced_MediaType:
 
 1. Create a HTML [LoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions).
 1. Set Print or Screen mode. 
 1. Initialize [Document object](<https://apireference.aspose.com/page/java/com.aspose.page/document>).
 1. Save output PDF document. 
 
```java
    private static void ConvertHTMLtoPDFAdvanced_MediaType() {
        // Create a HTML LoadOptions
        HtmlLoadOptions options = new HtmlLoadOptions();

        // Set Print or Screen mode
        options.setHtmlMediaType(HtmlMediaType.Print);

        // Initialize document object
        String htmlFileName = Paths.get(_dataDir.toString(), "test.html").toString();
        Document document = new Document(htmlFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(), "HTMLtoPDF.pdf").toString());
    }
```
## Convert HTML to PDF Advanced_EmbedFonts:

1. Add new Html [LoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions).
1. Disable font embedding.
1. Save a new Document.
2. 
```java
    public static void ConvertHTMLtoPDFAdvanced_EmbedFonts() {

        HtmlLoadOptions options = new HtmlLoadOptions();
        // Disable font embedding
        options.setEmbedFonts(true);

        Document document = new Document(_dataDir + "test_fonts.html", options);
        document.save(_dataDir + "html_test.PDF");
    }
```
Next example:

1. Creating a clear template resource for replacing.
1. Return empty byte array in case i.imgur.com server.
1. Process resources with default resource loader.
1. Save a new Document.

```java
    public static void ConvertHTMLtoPDFAdvanced_DummyImage() {
        HtmlLoadOptions options = new HtmlLoadOptions();
        options.CustomLoaderOfExternalResources = new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Creating clear template resource for replacing:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Return empty byte array in case i.imgur.com server
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Process resources with default resource loader
                    res.LoadingCancelled = true;
                    return res;
                }
            }
        };

        Document pdfDocument = new Document(_dataDir + "test.html", options);
        pdfDocument.save(_dataDir + "html_test.PDF");
    }

}
```

