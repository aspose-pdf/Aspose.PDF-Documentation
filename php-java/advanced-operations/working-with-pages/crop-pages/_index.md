---
title: Crop PDF Pages using PHP
linktitle: Crop Pages
type: docs
weight: 80
url: /php-java/crop-pages/
description: You may get page properties, such as the width, height, bleed-, crop- and trimbox using Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF for PHP via Java allows you to access these properties.

- **Media box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **Bleed box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size ("trimmed"), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **Trim box**: The trim box indicates the final size of a document after printing and trimming.
- **Art box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **Crop box**: The crop box is the "page" size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat. For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.
- **Page.Rect**: the intersection (commonly visible rectangle) of the MediaBox and DropBox. The picture below illustrates these properties.
For further details, please visit [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

The snippet below show how to crop the page:

```php

    // Open document
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // Create new Box Rectangle
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // Save output document
    $document->save($outputFile);
    $document->close();
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.
![Figure 2. Cropped Page](crop_page2.png)
