---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 50
url: /php-java/change-page-size/
description: Change Page Size from your PDF file using PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Change PDF Page Size

Aspose.PDF for PHP via Java lets you change PDF page size with simple lines of code in your Java applications. This topic explains how to update/change the page dimensions (size) of an existing PDF file.

The [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) class contains the SetPageSize(...) method which lets you set the page size. The code snippet below updates page dimensions in a few easy steps:

1. Load the source PDF file.
1. Get the pages into the [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) object.
1. Get a given page.
1. Call the setPageSize(..) method to update its dimensions.
1. Call the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class' save(..) method to generate the PDF file with updated page dimensions.

The following code snippet shows how to change the PDF page dimensions to A4 size.

```php

    // Open document
    $document = new Document($inputFile);
      
    // Get page collection
    $pageCollection = $document->getPages();

    // Get particular page
    $page = $pageCollection->get_Item(1);

    // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
    // So A4 dimensions in points will be (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Save output document
    $document->save($outputFile);
    $document->close();
```

## Get PDF Page Size

You can read PDF page size of an existing PDF file using Aspose.PDF for PHP via Java. The following code sample shows how to read PDF page dimensions using PHP.

```php

    // Open document
    $document = new Document($inputFile);
      
    // Adds a blank page to pdf document
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Get page height and width information
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Rotate page at 90 degree angle
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Get page height and width information
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Save output document
    $document->save($outputFile);
    $document->close();
```
