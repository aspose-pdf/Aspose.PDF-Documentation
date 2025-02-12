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
TechArticle: true 
AlternativeHeadline: How to generate a PDF document with ZUGFeRD in Aspose.PDF for Java
Abstract: The article outlines a step-by-step guide for attaching a ZUGFeRD-compliant file to a PDF document using Java. It begins by recommending the setup of a path variable to locate input and output PDF files. The process involves creating a `Document` object within a try-with-resources statement to ensure automatic closure. A `FileSpecification` object is then created to link an additional file containing invoice metadata that adheres to the ZUGFeRD standard. Properties such as description, MIME type, and AFrelationship are added to this file specification, indicating its role as an alternative representation of the PDF content. The file is attached to the document's embedded files collection and named according to the ZUGFeRD standard conventions. Subsequently, the document is converted to the PDF/A-3U format, which supports long-term preservation and embedding of files. Finally, the document is saved as a new PDF file, completing the attachment process. A code snippet is provided to demonstrate the implementation of this procedure using
SoftwareApplication: java 
---

## Attach ZUGFeRD to PDF

We recommend the following steps to attach ZUGFeRD to PDF:

* Define a path variable that points to a folder where the input and output PDF files are located.
* Define a string variable path that stores the path to the PDF file that will be processed. Use the `Paths.get`` method to combine parts of the full path.
* Create a try-with-resources statement that ensures that the Document object created from the path variable will be closed automatically after the statement ends. The Document object represents the PDF document that will be modified and saved.
* Create a [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) object by providing the path and description of another file, which contains invoice metadata conforming to the ZUGFeRD standard.
* Add properties to the file specification object, such as the description, MIME type, and AFrelationship. The AFrelationship indicates how the embedded file is related to the PDF document. In this case, it is set to "Alternative", meaning the embedded file is an alternative representation of the PDF content.
* Add the file specification object to the document's embedded files collection. The file name should be specified to ZUGFeRD standard, e.g. "factor-x.xml".
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
