---
title: Convert JPG to PDF 
linktitle: Convert JPG to PDF 
type: docs
weight: 190
url: /java/convert-jpg-to-pdf/
lastmod: "2021-02-05"
description: Learn how to easily convert a JPG images to PDF file. Also, you can convert an image to PDF with the same height and width of the page.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

No need to wonder how to convert JPG to PDF, because Apose.PDF for Java library has best decision.

You can very easy convert a JPG images to PDF with Aspose.PDF for Java by following steps:

1. Initialize object of [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class
1. Load JPG image and add to paragraph
1. Save output PDF

The code snippet below shows how to convert JPG Image to PDF using Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

private ConvertJPEGtoPDF() {
}

private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

public static void main(String[] args) throws FileNotFoundException {
// Initialize document object
Document document = new Document();

Page page = document.getPages().add();
Image image = new Image();

// Load sample JPEG image file
image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
page.getParagraphs().add(image);

// Save output PDF document
document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
}
}
```