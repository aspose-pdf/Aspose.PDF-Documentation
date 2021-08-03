---
title: Replace Image in Existing PDF File
linktitle: Replace Image
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: This section describes about replace image in existing PDF file using Java library.
lastmod: "2021-06-05"
---

The [XImages](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) collection’s [Replace](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) method allows you to replace an image in an existing PDF file.

The Images collection can be found in a page’s Resources collection. To replace an image:

1. Open the PDF file using the Document object.
2. Replace a particular image, save the updated PDF file using Save method of the Document object.

The following code snippet shows you how to replace an image in a PDF file.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Open document
        Document pdfDocument = new Document("input.pdf");
        // Replace a particular image
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Save updated PDF file
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```
