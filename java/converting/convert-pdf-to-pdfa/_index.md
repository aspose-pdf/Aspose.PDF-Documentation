---
title: Convert PDF File to PDF/A 
linktitle: Convert PDF File to PDF/A 
type: docs
weight: 180
url: /java/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: This topic show you how to Aspose.PDF for Java allows to convert a PDF file to a PDF/A compliant PDF file.  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF allows you to convert a PDF file to a PDF/A compliant PDF file. Before doing so, the file must be validated. This article explains how.

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own "representation" of PDF/A conformance. Please check this article on [PDF/A validation tools](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

Before converting the PDF to a PDF/A compliant file, validate the PDF using the validate method. The validation result is stored in an XML file and then this result is also passed to the convert method. You can also specify the action for the elements which can not be converted using the [ConvertErrorAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) enumeration.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF to PDF/A_1b Conversion

The following code snippet shows how to convert PDF files to PDF/A-1b compliant PDF.

```java
package com.aspose.pdf.examples;

import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoPDFA {

    private ConvertPDFtoPDFA() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples/");

    public static void main(String[] args) {
        ConvertPDFtoPDFa1b();
        ValidatePDF_A_1B();
    }

    public static void ConvertPDFtoPDFa1b() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert(_dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

To perform validation only, use the following line of code:

```java
    public static void ValidatePDF_A_1B() {
        
        // Open document
        Document pdfDocument = new Document(_dataDir + "ValidatePDFAStandard.pdf");

        // Validate PDF for PDF/A-1a
        if (pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B))
        {
            System.out.println("Valid");
        }
        else
        {
            System.out.println("Non valid");
        }
    }
```

## PDF to PDF/A_3b Conversion

From [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), the API also supports converting PDF files to PDF/A_3b format.

```java
    public static void ConvertPDFtoPDFa3b() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3a Conversion

From [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), the API also supports converting PDF files to PDF/A_3a format.

```java
    public static void ConvertPDFtoPDFa3a() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_2a Conversion

Starting release of [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), the API offers the feature to convert PDF files to PDF/A3 format.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

Starting release of Aspose.PDF for Java 17.2.0, the API offers the feature to convert PDF files to PDF/A_3U format.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## Create PDF/A-3 and attach XML file

Aspose.PDF for Java offers the feature to convert PDF files to PDF/A format and it also supports the capabilities of adding files as an attachment to PDF document. In case you have a requirement to attach files to PDF/A compliance format, then we recommend using PDF_A_3A value from com.aspose.pdf.PdfFormat enumeration, the PDF/A_3a is the format that provides the feature to attach any file format as an attachment to PDF/A compliant file. However, once the file is attached, you should convert it into Pdf-3a format again, in order to fix metadata. Please take a look over the following code snippet.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // add page to PDF file
        doc.getPages().add();
        // load XML file
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Sample xml file");
        // Add attachment to document's attachment collection
        doc.getEmbeddedFiles().add(fileSpecification);
        // perform PDF/A_3a conversion
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* or PDF_A_3B */, ConvertErrorAction.Delete);
        // save final PDF file
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
    
}
```
