---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in Java
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Learn how to attach ZUGFeRD invoice XML to a PDF and convert it to PDF/A-3A in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Attach ZUGFeRD invoice XML to a PDF document with Java
Abstract: This article explains how to create a PDF/A-3A compliant invoice document using Aspose.PDF for Java. It covers attaching the invoice XML as an embedded file, setting the MIME type and associated-file relationship, converting the PDF to PDF/A-3A, and saving the final ZUGFeRD-ready document.
---
Use the `Document` and `FileSpecification` APIs when you need to package invoice XML inside a PDF for ZUGFeRD-style workflows.

## Attach ZUGFeRD invoice XML to a PDF

1. Open the source PDF invoice document and create a `FileSpecification` for the XML payload.
2. Set the embedded file metadata, attach it to the PDF, and convert the document to `PDF_A_3A`.
3. Save the final output PDF and review the generated conversion log if needed.

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        String description = "Invoice metadata conforming to ZUGFeRD standard";
        FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

        fileSpecification.setMIMEType("text/xml");
        fileSpecification.setAFRelationship(AFRelationship.Alternative);

        document.getEmbeddedFiles().add("factur", fileSpecification);

        String outputFileName = outputFile.toString();
        String logPath = outputFileName.replace(".pdf", "_log.xml");
        document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

