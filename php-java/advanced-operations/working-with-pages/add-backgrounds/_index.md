---
title: Add background to PDF 
linktitle: Add backgrounds
type: docs
weight: 110
url: /php-java/add-backgrounds/
descriptions: Add background image to the your PDF file using PHP. Use the BackgroundArtifact object.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for PHP via Java, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object using PHP.

```php

    // Open document
    $document = new Document($inputFile);

    // Add a new page to document object
    $page = $document->getPages()->add();

    // Create BackgroundArtifact object    
    $background = new BackgroundArtifact();

    // Specify the image for backgroundArtifact object
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Add backgroundArtifact to artifacts collection of page
    $page->getArtifacts()->add($background);

    // Save updated PDF file
    $document->save($outputFile);
    $document->close();
```
