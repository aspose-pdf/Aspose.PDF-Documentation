---
title: Add Pages in PDF 
linktitle: Add Pages
type: docs
weight: 10
url: /php-java/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add or Insert Page in a PDF File

Aspose.PDF for PHP via Java lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file. You need to pass the location you want to insert the blank page to to the insert method.
This section shows how to add pages to a PDF with Aspose.PDF for PHP via Java.

### Insert Empty Page in a PDF File at Desired Location

The following code snippet shows how to insert an empty page into a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the input PDF file.
1. Add page, and insert it in a PDF.
1. Save the output PDF using the Save method.

The following code snippet shows you how to insert a page in a PDF file.

```php

    // Open document
    $document = new Document($inputFile);

    // Add page
    $document->getPages()->add();

    // Insert an empty page in a PDF
    $document->getPages()->insert(2);

    // Save output document
    $document->save($outputFile);
    $document->close();
```

In example above, we added empty page with default parameters. If you need to make page size the same as another page in document you shold add
a few lines of code:

```php

    // Open document
    $document = new Document($inputFile);

    // Add page
    $page1 = $document->getPages()->add();

    // Insert an empty page in a PDF
    $page2 = $document->getPages()->insert(2);

    // copy page parameters from page 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // Save output document
    $document->save($outputFile);
    $document->close();
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class object with the input PDF file.
1. Add page, and insert it in a PDF.
1. Save the output PDF using the save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```php

    // Open document
    $document = new Document($inputFile);

    // Add page
    $document->getPages()->add();

    // Insert an empty page in a PDF
    $document->getPages()->insert(2);

    // Save output document
    $document->save($outputFile);
    $document->close();
```