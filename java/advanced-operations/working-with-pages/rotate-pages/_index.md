---
title: Rotate PDF Pages programmatically Java
linktitle: Rotate PDF Pages
type: docs
weight: 60
url: /java/rotate-pages/
description: Change page orientation and fitting the page content to the new page orientation using Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Change Page Orientation

This article describes how to update or change the page orientation of pages in an existing PDF file.

Aspose.PDF for Java has feature to change the page orientation from landscape to portrait and vice versa. To change the page orientation, set the page’s [MediaBox](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) using the following code snippet.

You can also change page orientation by setting rotation angle using Rotate() method.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // //  We must to move page upper in order to compensate changing page size
            // // (lower edge of the page is 0,0 and information is usually placed from the
            // //  Top of the page. That's why we move lover edge upper on difference between
            // //  Old and new height.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // Sometimes we also need to set CropBox (if it was set in original file)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Setting Rotation angle of page
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Save output file
        pdfDocument.save(_dataDir);
    }    
}
```


