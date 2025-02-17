---
title: Delete PDF Pages programmatically 
linktitle: Delete PDF Pages
type: docs
weight: 40
url: /java/delete-pages/
description: You can delete pages from your PDF file using Java library.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to delete pages from a PDF file using Aspose.PDF for Java
Abstract: This article provides a guide on how to delete pages from a PDF file using Aspose.PDF for Java. It explains the process of utilizing the `PageCollection` class to remove a specific page by calling the `delete()` method with the desired page index. After modifying the PDF, the document must be saved using the `save` method to retain the changes. The article includes a Java code snippet illustrating the procedure - first, open the PDF document with `Document pdfDocument = new Document(_dataDir + "sample.pdf");`, then delete a specific page using `pdfDocument.getPages().delete(2);`, and finally save the updated document with `pdfDocument.save(_dataDir + "DeleteParticularPage_out.pdf");`. This step-by-step approach demonstrates the practical application of removing a page from a PDF file programmatically.
SoftwareApplication: java
---

You can delete pages from a PDF file using Aspose.PDF for Java. To delete a particular page from the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) simply call the delete() method and specify the index of the particular page you want to delete. Then call the save method to save the updated PDF file.

## Delete Page from PDF File

1. Call the Delete method and specify the page's index
1. Call the Save method to save the updated PDF file
The following code snippet shows how to delete a particular page from the PDF file using Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Delete a particular page
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Save updated PDF
    pdfDocument.save(_dataDir);    

  }
```
