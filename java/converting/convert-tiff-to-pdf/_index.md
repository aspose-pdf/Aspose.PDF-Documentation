---
title: Convert TIFF to PDF 
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /java/convert-tiff-to-pdf/
lastmod: "2021-02-05"
description: Aspose.PDF for Java allows converting multi-page or multi-frame TIFF images to PDF applications. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** file format supported, be it a single frame or multi-frame <abbr title="Tag Image File Format">TIFF</abbr> image. It means that you can convert the TIFF image to PDF in your Java applications. 

TIFF or TIF, Tagged Image File Format, represents raster images that are meant for usage on a variety of devices that comply with this file format standard. TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image. So you can convert the TIFF image to PDF in your Java applications. Therefore, we will consider an example of converting multi-page TIFF image to multi-page PDF document with below steps:

1. Instantiate an instance of Document class
1. Load input TIFF image
1. Get FrameDimension of the frames
1. Add new page for each frame
1. Finally, save images to PDF pages

Moreover, the following code snippet shows how to convert multi-page or multi-frame TIFF image to PDF:

```java
package com.aspose.pdf.examples;

/**
 * Convert TIFF to PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTIFFtoPDF {

    private ConvertTIFFtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        // Initialize document object
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Load sample BMP image file
        image.setFile(Paths.get(_dataDir.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(), "TIFFtoPDF.pdf").toString());
    }
}

```
