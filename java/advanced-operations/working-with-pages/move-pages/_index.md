---
title: Move PDF Pages 
linktitle: Move PDF Pages
type: docs
weight: 20
url: /java/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using Java.
To move an page we should:

1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file.
1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the destination PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's.
1. Add page to the destination document.
1. Save the output PDF using the Save method.
1. Delete page in source document.
1. Save the source PDF using the Save method.

The following code snippet shows you how to move one page.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Save output file
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file.
1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the destination PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
    1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's.
    1. Add page to the destination document.
1. Save the output PDF using the Save method.
1. Delete page in source document using array.
1. Save the source PDF using the Save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Save output files
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's.
1. Add page to the new location (for example to end).
1. Delete page in previous location.
1. Save the output PDF using the Save method.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Save output file
    srcDocument.save(dstFileName);
  }
}
```
