---
title: Split PDF programmatically
linktitle: Split PDF files
type: docs
weight: 60
url: /php-java/split-document/
description: This topic shows how to split PDF pages into individual PDF files in your PHP applications. 
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

You can split PDF files using Aspose.PDF and get the results online at this link: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

This topic shows how to split PDF pages with Aspose.PDF for PHP via Java into individual PDF files in your PHP applications. To split PDF pages into single page PDF files using PHP, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) collection.
1. For each iteration, create a new Document object and add the individual [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object into the empty document.
1. Save the new PDF using Save method.

The following PHP code snippet shows you how to split PDF pages into individual PDF files.

```php

    // Open document
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Loop through all the pages
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```
