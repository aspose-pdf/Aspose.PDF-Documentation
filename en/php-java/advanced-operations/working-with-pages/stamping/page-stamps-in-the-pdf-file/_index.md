---
title: Add PDF Page Stamp to PDF 
linktitle: Page stamps in PDF File
type: docs
weight: 30
url: /php-java/page-stamps-in-the-pdf-file/
description: Add a Page stamp to a PDF file using the PdfPageStamp class with PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Page Stamp 

A [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) can be used when you need to apply a composite stamp containing graphics, text, tables. The following example shows how to use a stamp to create stationery like in using Adobe InDesign, Illustrator, Microsoft Word. Assume we have some input document and we want apply 2 kinds of border with blue and plum color.

```php

    // Open document
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Save output document
    $document->save($outputFile);
    $document->close();  
```
