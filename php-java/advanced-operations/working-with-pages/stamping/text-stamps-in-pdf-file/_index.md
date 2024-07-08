---
title: Add Text stamps in PDF programmatically
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF file using the TextStamp class with PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Text Stamp with Java

Aspose.PDF for PHP via Java provides [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class to add a text stamp in a PDF file. The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class provides necessary methods to specify font size, font style, and font color etc for stamp object. In order to add text stamp, first you need to create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and a [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) object using required methods. After that, you may call [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp in the PDF document.

The following code snippet shows you how to add text stamp in the PDF file.

```php

    // Open document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // create text stamp
    $textStamp = new TextStamp("Sample Stamp");
    // set whether stamp is background
    $textStamp->setBackground(true);
    // set origin
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // rotate stamp
    $textStamp->setRotate((new Rotation())->On90);    
    // set text properties
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // add stamp to particular page
    $pages->get_Item(1)->addStamp($textStamp);

    // Save output document
    $document->save($outputFile);
    $document->close();
```

## Define alignment for TextStamp object

Adding watermarks to PDF documents is one of the frequent demanded features and Aspose.PDF for PHP via Java is fully capable of adding Image as well as Text watermarks. The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class provides the feature to add text stamps over the PDF file. Recently there has been a requirement to support the feature to specify the alignment of text when using [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) object. So in order to fulfill this requirement, we have introduced setTextAlignment(..) method in [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class. By using this method, you can specify the Horizontal text alignment.

The following code snippets shows an example on how to load an existing PDF document and add [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) over it.

```php

    // Open document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // instantiate FormattedText object with sample string
    $text = new FormattedText("This");

    // add new text line to FormattedText
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // create text stamp
    $textStamp = new TextStamp($text);

    // specify the Horizontal Alignment of text stamp as Center aligned
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // specify the Vertical Alignment of text stamp as Center aligned
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // specify the Text Horizontal Alignment of TextStamp as Center aligned
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // set top margin for stamp object
    $textStamp->setTopMargin(20);
    
    // add stamp to particular page
    $pages->get_Item(1)->addStamp($textStamp);

    // Save output document
    $document->save($outputFile);
    $document->close();  
```

## Fill Stroke Text as Stamp in PDF File

We have implemented setting of rendering mode for text adding and editing scenarios. To render stroke text please create [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) object and set RenderingMode to TextRenderingMode.StrokeText and also select color for StrokingColor property. Later, bind TextState to the stamp using bindTextState() method.

Following code snippet demonstrates adding Fill Stroke Text:

```php

   // Create TextState object to transfer advanced properties
    $ts = new TextState();
        
    // Set color for stroke
    $ts->setStrokingColor((new Color())->getGray());

    // Set text rendering mode
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Load an input PDF document
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Bind TextState
    $stamp->bindTextState($ts);
    
    // Set X,Y origin
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Add Stamp
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```
