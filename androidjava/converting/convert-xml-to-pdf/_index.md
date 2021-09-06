---
title: Convert XML to PDF 
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF library presents several ways to convert XML to PDF. You can use the XslFoLoadOptions or do this with an incorrect file structure.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF.

Consider option using XML document based on XSL-FO standard.

## Convert XSL-FO to PDF

The conversion of XSL-FO files to PDF can be implemented using [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) object with [XslFoLoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  but sometimes you can meet with the incorrect file structure. 

```java
package com.aspose.pdf.examples;
/**
 * Convert XML to PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Initialize document object

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Instantiate a Document object by calling its empty constructor
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // Save resultant PDF file
        pdfDocument.save(pdfDocumentFileName);
    }
    
    ```
    
 ## Convert XSL-FO to PDF with set error handling strategy
    
    ```java
    
    public static void Convert_XSLFO_to_PDF_Adv() throws IOException {
        // Initialize document object

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
        // Set error handling strategy
        options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;

        // Instantiate a Document object by calling its empty constructor
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // Save resultant PDF file
        pdfDocument.save(pdfDocumentFileName);
    }

}
```