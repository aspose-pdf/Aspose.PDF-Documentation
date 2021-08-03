---
title: Set Image Size
linktitle: Set Image Size
type: docs
weight: 80
url: /java/set-image-size/
description: This section describes how to set image size PDF file using Java library.
lastmod: "2021-06-05"
---

It is possible to set the size of an image that’s being added to a PDF file. In order to set size, you can use [setFixWidth](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) and [setFixHeight](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) methods of com.aspose.pdf.Image Class. 

The following code snippet demonstrates how to set the size of an image:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Instantiate Document object
        Document doc = new Document();
        // add page to pages collection of PDF file
        Page page = doc.getPages().add();
        // Create an image instance
        Image img = new Image();
        // Set Image Width and Height in Points
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Set image type as SVG
        img.setFileType (ImageFileType.Svg);
        // Path for source file
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Set page properties
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // save resultant PDF file
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```
