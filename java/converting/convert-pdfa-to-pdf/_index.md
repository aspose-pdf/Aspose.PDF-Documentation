---
title: Convert PDF/A to PDF format using Java
linktitle: Convert PDF/A to PDF format
type: docs
weight: 110
url: /java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: This topic show you how to Aspose.PDF allows to convert PDF/A file to PDF document with Java library. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF/A document to PDF

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive
">PDF/A</abbr> restriction from the original document. Class [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) has method RemovePdfaCompliance(..) to remove
the PDF compliance information from input/source file.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFAtoPDF {

    private ConvertPDFAtoPDF() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        ConvertPDFA_to_PDF();
        ConvertPDFAtoPDFAdvanced();
    }

    public static void ConvertPDFA_to_PDF() {
        String pdfaDocumentFileName = Paths.get(_dataDir.toString(), "PDFAToPDF.pdf").toString();
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFAToPDF_out.pdf").toString();

        // Create Document object
        Document pdfDocument = new Document(pdfaDocumentFileName);

        // Remove PDF/A compliance information
        pdfDocument.removePdfaCompliance();

        // Save output in XML format
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```java
    public static void ConvertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = Paths.get(_dataDir.toString(), "PDFAToPDF.pdf").toString();
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFAToPDF_out.pdf").toString();

        // Create Document object
        Document pdfDocument = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        pdfDocument.getPages().add();

        // Save updated document
        pdfDocument.save(pdfDocumentFileName);
    }
```
