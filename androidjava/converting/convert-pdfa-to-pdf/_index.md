---
title: Convert PDF/A to PDF 
linktitle: Convert PDF/A to PDF
type: docs
weight: 350
url: /androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: To convert PDF/A to PDF you should remove restrictions from the original document. Aspose.PDF for Android via Java allows you to solve this problem easly and simply.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive
">PDF/A</abbr> restriction from the original document. Class [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) has method RemovePdfaCompliance(..) to remove
the PDF compliance information from input/source file.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```



