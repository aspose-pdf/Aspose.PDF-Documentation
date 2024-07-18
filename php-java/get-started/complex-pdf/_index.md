---
title: Creating a complex PDF 
linktitle: Creating a complex PDF
type: docs
weight: 60
url: /php-java/complex-pdf-example/
description: Aspose.PDF for PHP via Java allows you to create more complex documents that contain images, text fragments, and tables in one document.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [Hello, World](/pdf/php-java/hello-world-example/) example showed simple steps to create a PDF document using Aspose.PDF. In this article, we will take a look at creating a more complex document with Aspose.PDF for PHP via Java. As an example, we'll take a document from a fictitious company that operates passenger ferry services.

If we create a document from scratch we need to follow certain steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) to the document object. So, now our document will have one page.
1. Add a [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). It's a complex operation based on low level actions with PDF operators.
    - Load image from stream
    - Add image to Images collection of Page Resources
    - Using GSave operator: this operator saves current graphics state.
    - Create a [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) object.
    - Using ConcatenateMatrix operator: defines how image must be placed.
    - Using Do operator: this operator draws image.
    - Using GRestore operator: this operator restores graphics state.
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) for header. For the header we will use Arial font with font size 24pt and center alignment.
1. Add header to the page [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) for description. For the description we will use Arial font with font size 24pt and center alignment.
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Save a document "Complex.pdf".

```php

    $document = new Document();
    //Add page
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Add image
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Add Header
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("New ferry routes in Fall 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Add description
    $descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Add table
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Departs City");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Departs Island");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```
