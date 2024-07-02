---
title: Add Page Number to PDF 
linktitle: Add Page Number
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF for PHP via Java allows you to add Page Number Stamp to your PDF file using PageNumber Stamp class.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.
**Aspose.PDF for PHP via Java** allows you to add page numbers with PageNumberStamp.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

You can use [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class to add a page number stamp in a PDF document. The [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class provides methods to create a page number based stamp like format, margins, alignments, starting number etc. In order to add page number stamp, you need to create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and a [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) object with required properties. After that, you can call [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp in PDF file. You can also set the font attributes of the page number stamp.

The following code snippet shows you how to add page numbers in a PDF file.

```php

    // Open document
    $document = new Document($inputFile);

    // Create page number stamp
    $pageNumberStamp = new PageNumberStamp();

    // Whether the stamp is background
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Set text properties
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Add stamp to particular page
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Save output document
    $document->save($outputFile);
    $document->close();
```


