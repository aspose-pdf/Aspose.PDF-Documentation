---
title: Add Image stamps in PDF programmatically 
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /php-java/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF for PHP via Java library.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Image Stamp in PDF File

You can use [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) class to add an image as a stamp in PDF document. The [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) class provides methods to specify height, width, and opacity etc.

To add an image stamp:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and an ImageStamp object using required properties.
1. Call the Page class [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp to the PDF.

The following code snippet shows how to add image stamp in the PDF file.

```php

    // Open document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Create image stamp
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Add stamp to particular page
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Save output document
    $document->save($outputFile);
    $document->close()
```

## Control Image Quality when Adding Stamp

The [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) class lets you add an image as a stamp in a PDF document. It also allows you to control the image quality when adding an image as a watermark in a PDF file. To allow this, a method named setQuality(...) has been added to the [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) class. A similar method can also be found in the [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) class of the com.aspose.pdf.facades package.

The following code snippet shows you how to control image quality when adding as stamp in the PDF file.

```php

    // Open document
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Create image stamp
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Save output document
    $document->save($outputFile);
    $document->close();        
```

## Image Stamp as Background in Floating Box

Aspose.PDF API lets you add image stamp as background in a floating box. The BackgroundImage property of FloatingBox class can be used to set the background image stamp for a floating box as shown in following code sample.

This code snippet demonstrates the process of creating a PDF document and adding a FloatingBox to it. The FloatingBox contains a text fragment, a border, a background image, and a background color. The resulting document is then saved to an output file.

```php

    // Open document
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Add page to PDF document
    $page = $pages->add();

    // Create FloatingBox object
    $aBox = new FloatingBox(200, 100);

    // Set left position for FloatingBox
    $aBox->setLeft(40);

    // Set Top position for FloatingBox
    $aBox->setTop(80);

    // Set the Horizontal alignment for FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Add text fragment to paragraphs collection of FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("main text"));

    // Set border for FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Add background image
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Set background color for FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Add FloatingBox to paragraphs collection of page object
    $page->getParagraphs()->add($aBox);
    
    // Save output document
    $document->save($outputFile);
    $document->close();
```
