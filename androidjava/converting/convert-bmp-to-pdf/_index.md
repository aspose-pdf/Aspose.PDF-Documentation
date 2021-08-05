---
title: Convert BMP to PDF 
linktitle: Convert BMP to PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: You may easily convert BMP bitmap files to PDF used to store digital bitmap images separately from the display device using Aspose.PDF. for Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP images are Files having extension .BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format.
You can convert BMP to PDF with Aspose.PDF for Java API. Therefore, you can follow the following steps to convert BMP images:

1. Initialize a new Document
1. Load sample BMP image file
1. Finally, save the output PDF file

So the following code snippet follows these steps and shows how to convert BMP to PDF using Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialize document object
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Load sample BMP image file
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```
