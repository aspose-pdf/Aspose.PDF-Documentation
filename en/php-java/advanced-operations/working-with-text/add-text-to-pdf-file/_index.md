---
title: Add Text to PDF file 
linktitle: Add Text to PDF file
type: docs
weight: 10
url: /php-java/add-text-to-pdf-file/
description: Explore how to add text to PDF files in PHP using Aspose.PDF for easy content editing.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

To add text to existing PDF file:

1. Open the input PDF using the Document object.
1. Get the particular page to which you want to add the text.
1. Create a text fragment with the content "Aspose.PDF".
1. Set the position of the text fragment on the page.
1. Set the text properties of the text fragment.
1. Create a TextBuilder object for the page.
1. Append the text fragment to the PDF page.
4. Save the resulting PDF document to the output file.

## Adding Text

The following code snippet shows you how to add text in an existing PDF file.

```php

    // Open document
    $document = new Document($inputFile);
    
    // get particular page
    $page = $document->getPages()->add();
    
    // create text fragment
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // set text properties
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // create TextBuilder object
    $textBuilder = new TextBuilder($page);
    // append the text fragment to the PDF page
    $textBuilder->appendText($textFragment);

    // Save resulting PDF document.    
    $document->save($outputFile);
    $document->close();
```

