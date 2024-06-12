---
title: Delete PDF Pages programmatically 
linktitle: Delete PDF Pages
type: docs
weight: 40
url: /php-java/delete-pages/
description: You can delete pages from your PDF file using PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Delete Page from PDF File

1. Call the delete method and specify the page’s index
1. Call the save method to save the updated PDF file
The following code snippet shows how to delete a particular page from the PDF file using PHP.

```php

    // Open document
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Delete a particular page
    $pages()->delete(2);

    // Save output document
    $document->save($outputFile);
    $document->close();
```
