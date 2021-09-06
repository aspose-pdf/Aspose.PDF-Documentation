---
title: Convert Text to PDF 
linktitle: Convert Text to PDF
type: docs
weight: 300
url: /androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Java allows you to convert plain text file to PDF or to convert pre-formatted text file to PDF. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Java** provides the capability to convert Text files to PDF format. In this article, we demonstrate how easily and efficiently we can convert a text file to PDF using Aspose.PDF.

When you need to convert a Text file to PDF, initially read the source text file in some reader. We have used StringBuilder to read the Text file contents. Instantiate Document object and add a new page in the Pages collection. Create a new object of TextFragment and pass StringBuilder object to its constructor. Add a new paragraph in Paragraphs collection using TextFragment object and save the resultant PDF file using the Save method of Document class.

## Convert plain text file to PDF

```java
package com.aspose.pdf.examples;
/**
 * Convert TXT to PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Initialize document object

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Instantiate a Document object by calling its empty constructor
        Document pdfDocument = new Document();

        // Add a new page in Pages collection of Document
        Page page = pdfDocument.getPages().add();

        // Create an instance of TextFragmet and pass the text from reader object to its
        // constructor as argument
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Add a new text paragraph in paragraphs collection and pass the TextFragment
        // object
        page.getParagraphs().add(text);

        // Save resultant PDF file
        pdfDocument.save(pdfDocumentFileName);
    }
```
## Convert pre-formatted text file to PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Read the text file as array of string
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Instantiate a Document object by calling its empty constructor
        Document pdfDocument = new Document();

        // Add a new page in Pages collection of Document
        Page page = pdfDocument.getPages().add();

        // Set left and right margins for better presentation
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Create an instance of TextFragment and
                // pass the line to its
                // constructor as argument
                TextFragment text = new TextFragment(line);

                // Add a new text paragraph in paragraphs collection and pass the TextFragment
                // object
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}

```


