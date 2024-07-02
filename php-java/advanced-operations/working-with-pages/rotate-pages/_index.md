---
title: Rotate PDF Pages programmatically 
linktitle: Rotate PDF Pages
type: docs
weight: 60
url: /php-java/rotate-pages/
description: Change page orientation and fitting the page content to the new page orientation using Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Change Page Orientation

This article describes how to update or change the page orientation of pages in an existing PDF file.

Aspose.PDF for PHP via Java has feature to change the page orientation from landscape to portrait and vice versa. 

1. Open the document using the specified input file.
1. Get all the pages of the document.
1. Iterate through each page and set the rotation to 90 degrees.
1. Save the modified document to the specified output file.
1. Close the document.

```php

    // Open document
    $document = new Document($inputFile);    
    
    $pages = $document->getPages();
    
    foreach ($pages as $page) {
        $page->setRotate((new Rotation())->getOn90());
    }

    // Save output document
    $document->save($outputFile);
    $document->close();
```


