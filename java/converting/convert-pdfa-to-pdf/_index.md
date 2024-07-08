---
title: Convert PDF/A to PDF format 
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

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive">PDF/A</abbr> restriction from the original document. Class [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) has method RemovePdfaCompliance(..) to remove
the PDF compliance information from input/source file.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Create Document object
    Document document = new Document(pdfaDocumentFileName);

    // Remove PDF/A compliance information
    document.removePdfaCompliance();

    // Save output in XML format
    document.save(documentFileName);
    document.close();
}
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Create Document object
    Document document = new Document(pdfaDocumentFileName);

    // Adding a new (empty) page removes PDF/A compliance information.
    document.getPages().add();

    // Save updated document
    document.save(documentFileName);
    document.close();
}
```
