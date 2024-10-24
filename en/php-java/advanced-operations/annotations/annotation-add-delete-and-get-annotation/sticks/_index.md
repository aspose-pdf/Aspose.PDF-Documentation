---
title: PDF Sticky Annotations 
linktitle: Sticky Annotation
type: docs
weight: 50
url: /php-java/sticky-annotations/
description: This topic about sticky annotations, as an example we shows the Watermark Annotation in the text. It uses to represent graphics on the page. Check code snippet to resolve this task.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Watermark Annotation

A watermark annotation shall be used to represent graphics that shall be printed at a fixed size and position on a page, regardless of the dimensions of the printed page.

You can add Watermark Text using [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using opacity property.

Please check the following code snippet to add WatermarkAnnotation.

```php

    // Open document
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // get particular page
    $page = $document->getPages()->get_Item(1);
    
    //Create Annotation
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Add annotation into Annotation collection of Page
    $page->getAnnotations()->add($wa);

    //Create TextState for Font settings
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Set opacity level of Annotation Text
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    //Add Text to Annotation
    $wa->setTextAndState($watermarkStrings, $ts);

    // Save resulting PDF document.    
    $document->save($outputFile);
    $document->close();
```

