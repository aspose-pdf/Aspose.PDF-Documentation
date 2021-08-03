---
title: Convert PNG to PDF 
linktitle: Convert PNG to PDF
type: docs
weight: 200
url: /java/convert-png-to-pdf/
lastmod: "2021-06-05"
description: This article shows how to convert PNG to PDF with Aspose.PDF library in your Java applications. You can convert PNG images to PDF format using simple steps. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** support feature to convert PNG images to PDF format. Check the next code snippet for realizing you task.

<abbr title="Portable Network Graphics">PNG</abbr> refers to a type of raster image file format that use loseless compression, that makes it popular among its users.

You can convert PNG to PDF image using the below steps:

1. Load input PNG image
1. Read height and width values
1. Create new document and add Page
1. Set page dimensions
1. Save output file

Moreover, the code snippet below shows how to convert PNG to PDF in your Java applications:

```java
package com.aspose.pdf.examples;

/**
 * Convert PNG to PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialize document object
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Load sample BMP image file
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```
