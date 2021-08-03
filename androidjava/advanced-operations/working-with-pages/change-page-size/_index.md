---
title: Change PDF Page Size Programmatically with Java
linktitle: Change PDF Page Size
type: docs
weight: 50
url: /java/change-page-size/
description: Change Page Size from your PDF file using Java library.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Change PDF Page Size

Aspose.PDF for Java lets you change PDF page size with simple lines of code in your Java applications. This topic explains how to update/change the page dimensions (size) of an existing PDF file.

The [Page](https://apireference.aspose.com/pdf//java/com.aspose.pdf/page) class contains the SetPageSize(...) method which lets you set the page size. The code snippet below updates page dimensions in a few easy steps:

1. Load the source PDF file.
1. Get the pages into the [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) object.
1. Get a given page.
1. Call the SetPageSize(..) method to update its dimensions.
1. Call the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class' Save(..) method to generate the PDF file with updated page dimensions.

{{% alert color="primary" %}}

Please note that the height and width properties use points as basic unit, where 1 inch = 72 points and 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 points.

{{% /alert %}}

The following code snippet shows how to change the PDF page dimensions to A4 size.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Open first document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Get page collection
        PageCollection pageCollection = pdfDocument.getPages();

        // Get particular page
        Page pdfPage = pageCollection.get_Item(1);

        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Save the updated document
        pdfDocument.save(_dataDir);
    }
```

## Get PDF Page Size

You can read PDF page size of an existing PDF file using Aspose.PDF for Java. The following code sample shows how to read PDF page dimensions using Java.

```java
    public static void GetPDFPageSize() {
        
        // Open first document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Adds a blank page to pdf document
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Get page height and width information
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Rotate page at 90 degree angle
        page.setRotate (Rotation.on90);

        // Get page height and width information
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Save the updated document
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```
