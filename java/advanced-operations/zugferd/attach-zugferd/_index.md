---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in Java
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Attach ZUGFeRD to PDF

We recommend following steps to attach ZUGFeRD to PDF:

* Define a path variable that points to a folder where the input and output PDF files are located.
* Define a string variable path that stores the path to the PDF file that will be processed. Use the `Paths.get`` method to combine parts of full path.
* Create a try-with-resources statement that ensures that the Document object created from the path variable will be closed automatically after the statement ends. The Document object represents the PDF document that will be modified and saved.
* Create a [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) object by providing the path and description of another file, which contains invoice metadata conforming to the ZUGFeRD standard.
* Add properties to the file specification object, such as the description, MIME type, and AFrelationship. The AFrelationship indicates how the embedded file is related to the PDF document. In this case, it is set to "Alternative", meaning the embedded file is an alternative representation of the PDF content.
* Add the file specification object to the document's embedded files collection. File name should be specified to ZUGFeRD standard, e.g. "factur-x.xml".
* Convert the document to PDF/A-3U format, a subset of PDF that ensures the long-term preservation of electronic documents. PDF/A-3U allows embedding files of any format in PDF documents.
* Save the converted document as a new PDF file (e.g. "ZUGFeRD-res.pdf").
* Close the try-with-resources statement and release the Document object.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Invoice metadata conforming to ZUGFeRD standard";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Add attachment to document's attachment collection
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```
