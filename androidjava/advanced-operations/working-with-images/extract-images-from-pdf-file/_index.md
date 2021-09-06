---
title: Extract Images from PDF File
linktitle: Extract Images
type: docs
weight: 30
url: /androidjava/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using Java library.
lastmod: "2021-06-05"
---

Each page holds a [Resources](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Resources) collection, and this, in turn, holds the Images collection, were all images in a page are kept. The [XImage](https://apireference.aspose.com/java/pdf/com.aspose.pdf/XImage) object gets a given image in the Images collection.

To extract and image from a page:

Get the image from the Images collection using the image index.
Use the [XImage](https://apireference.aspose.com/java/pdf/com.aspose.pdf/XImage) object’s save(..) method to save the extracted image.

The following code snippet shows you how to extract images from the PDF file.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Open document
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Extract a particular image
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Save output image
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Save updated PDF file
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```