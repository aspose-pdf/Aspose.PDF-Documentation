---
title: Move PDF Pages 
linktitle: Move PDF Pages
type: docs
weight: 20
url: /php-java/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Moving a Page from one PDF Document to Another

This topic explains how to move page from one PDF document to the end of another document using PHP.
To move an page we should:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file
1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the destination PDF file
1. Add the page to the output document. Save the output file
1. Delete the page from the input document. Save the modified input document
1. Close the documents
1. Save, and close the output document

The following code snippet shows you how to move one page.

```php

    // Open document
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Save output file
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Save output document
    $document->save($outputFile);
    $document->close();
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file.
1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the destination PDF file.
1. Define the pages to be copied from the input document to the output document
1. Run loop through array:
    1. Get the page at the specified index from the input document.
    1. Add page to the destination document.
1. Save the output PDF using the Save method.
1. Delete page in source document using array.
1. Save the source PDF using the Save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```php

    // Open document
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Save output files
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the source PDF file.
1. Get Page from the the [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's.
1. Add page to the new location.
1. Delete the page at index 2.
1. Save the output PDF using the save method.

```php

    // Open document
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Save output file
    $document->save($outputFile);
    $document->close();      
```
