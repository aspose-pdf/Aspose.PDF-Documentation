---
title: Add Pages in PDF 
linktitle: Add Pages
type: docs
weight: 10
url: /java/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using Java library.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on how to add or insert pages in a PDF file using Aspose.PDF for Java
Abstract: This article provides a guide on how to add or insert pages in a PDF file using Aspose.PDF for Java. It details two main operations - inserting an empty page at a specified location within a PDF and adding an empty page at the end of a PDF document. The article includes Java code snippets demonstrating these functionalities. To insert a page at a specific location, the user must create a `Document` object, utilize the `PageCollection`'s `insert` method, and save the updated document. The provided code also shows how to align a new page's size with an existing page's parameters by copying page properties. To add a page at the end of a document, the `add` method of `PageCollection` is used without parameters. Each process concludes by saving the modified PDF with the `save` method.
SoftwareApplication: java
---

## Add or Insert Page in a PDF File

Aspose.PDF for Java lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. You need to pass the location you want to insert the blank page to to the insert method.
This section shows how to add pages to a PDF with Aspose.PDF for Java.

### Insert Empty Page in a PDF File at Desired Location

The following code snippet shows how to insert an empty page into a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) collection's Insert method with specified index.
1. Save the output PDF using the Save method.

The following code snippet shows you how to insert a page in a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Add page
        document.getPages().add();

        // Insert a empty page in a PDF
        document.getPages().insert(2);

        // Save updated PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

In example above, we added empty page with default parameters. If you need to make page size the same as another page in document you shold add
a few lines of code:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Add page
        Page page1 = document.getPages().add();

        // Insert a empty page in a PDF
        Page page2 = document.getPages().insert(2);
        ;
        // copy page parameters from page 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Save updated PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the input PDF file.
1. Call the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) collection's Add method, without any parameters.
1. Save the output PDF using the Save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Add page
        document.getPages().add();

        // Insert an empty page at the end of a PDF file
        document.getPages().add();

        // Save updated PDF
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```