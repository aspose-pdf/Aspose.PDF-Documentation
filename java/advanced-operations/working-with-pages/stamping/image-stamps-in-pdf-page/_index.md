---
title: Add Image stamps in PDF programmatically with Java
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF for Java library.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Image Stamp in PDF File

You can use [ImageStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ImageStamp) class to add an image as a stamp in PDF document. The [ImageStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ImageStamp) class provides methods to specify height, width, and opacity etc.

To add an image stamp:

1. Create a [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document) object and an ImageStamp object using required properties.
1. Call the Page class [addStamp(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page) class to add the stamp to the PDF.

The following code snippet shows how to add image stamp in the PDF file.

```java
public static void AddImageStampInPDFFile() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Create image stamp
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Add stamp to particular page
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Save output document
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```

## Control Image Quality when Adding Stamp

The [ImageStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ImageStamp) class lets you add an image as a stamp in a PDF document. It also allows you to control the image quality when adding an image as a watermark in a PDF file. To allow this, a method named setQuality(...) has been added to the [ImageStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ImageStamp) class. A similar method can also be found in the [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/Stamp) class of the com.aspose.pdf.facades package. 

The following code snippet shows you how to control image quality when adding as stamp in the PDF file.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Create image stamp
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```

## Image Stamp as Background in Floating Box

Aspose.PDF API lets you add image stamp as background in a floating box. The BackgroundImage property of FloatingBox class can be used to set the background image stamp for a floating box as shown in following code sample.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Instantiate Document object
        Document doc = new Document();
        // Add page to PDF document
        Page page = doc.getPages().add();

        // Create FloatingBox object
        FloatingBox aBox = new FloatingBox(200, 100);

        // Set left position for FloatingBox
        aBox.setLeft(40);
        // Set Top position for FloatingBox
        aBox.setTop(80);
        // Set the Horizontal alignment for FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.getParagraphs().add(new TextFragment("main text"));
        // Set border for FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Add background image
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Set background color for FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Add FloatingBox to paragraphs collection of page object
        page.getParagraphs().add(aBox);
        // Save the PDF document
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```
