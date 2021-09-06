---
title: Add PDF Header and Footer with Aspose.PDF
linktitle: Add PDF Header and Footer
type: docs
weight: 70
url: /androidjava/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Java allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF stamps are often used in contracts, reports, and restricted materials, to prove that the documents have been reviewed and marked as "read", "qualified", or "confidential", etc. This article will show you how we can add image stamps and text stamps to PDF documents by using **Aspose.PDF for Java**.

If you will read the above code snippets line by line, you must find that the syntax and code logic is quite easy to understand. 

## Adding Text in Header of PDF File

You can use [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class to add text in the header of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the header, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the header of the PDF.

You need to set the TopMargin property in such a way that it adjusts the text in the header area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Top.

The following code snippet shows you how to add text in the header of a PDF file with Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Create header
        TextStamp textStamp = new TextStamp("Header Text");

        // Set properties of the stamp
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Add header on all pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Save updated document
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Adding Text in Footer of PDF File

You can use TextStamp class to add text in the footer of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the footer, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the footer of the PDF.

The following code snippet shows you how to add text in the footer of a PDF file with Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Create footer
        TextStamp textStamp = new TextStamp("Footer Text");
        // Set properties of the stamp
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Add footer on all pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Save updated PDF file
        pdfDocument.save(_dataDir);
    }
```

## Adding Image in Header of PDF File

You can use [ImageStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) class to add image in the header of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the header, you need to create a Document object and a Image Stamp object using required properties. After that, you can call [AddStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) method of the Page to add the image in the header of the PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Open document
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Create header
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Set properties of the stamp
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Add header on all pages
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Save updated PDF file
pdfDocument.save(_dataDir);
}
```

The following code snippet shows you how to add image in the header of a PDF file with Java.

## Adding Image in Footer of PDF File

You can use Image Stamp class to add image in the footer of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the footer, you need to create a Document object and an Image Stamp object using required properties. After that, you can call AddStamp method of the Page to add the image in the footer of the PDF.

{{% alert color="primary" %}}

You need to set the BottomMargin property in such a way that it adjusts the image in the footer area of your PDF. You also need to set [HorizontalAlignment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) to `Center` and [VerticalAlignment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) to `Bottom`.

{{% /alert %}}

The following code snippet shows you how to add image in the footer of a PDF file with Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Create footer
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Set properties of the stamp
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Add footer on all pages
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Save updated PDF file
        pdfDocument.save(_dataDir);
    }
```

## Adding different Headers in one PDF File

We know that we can add TextStamp in Header/Footer section of the document by using TopMargin or Bottom Margin properties, but sometimes we may have the requirement to add multiple header/footers in a single PDF document. **Aspose.PDF for Java** explains how to do this.

In order to accomplish this requirement, we will create individual [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) objects (number of objects depends upon the number of Header/Footers required)and will add them to PDF document. We may also specify different formatting information for individual stamp object. In following example, we have created [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object and three   [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) objects and then we have used [AddStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) method of the Page to add the text in the header section of the PDF. The following code snippet shows you how to add image in the footer of a PDF file with Aspose.PDF for Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // Open source document
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Create three stamps
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // Set stamp alignment (place stamp on page top, centered horiznotally)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Specify the font style as Bold
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Set the text fore ground color information as red
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Specify the font size as 14
        stamp1.getTextState().setFontSize(14);

        // Now we need to set the vertical alignment of 2nd stamp object as Top
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Set Horizontal alignment information for stamp as Center aligned
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Set the zooming factor for stamp object
        stamp2.setZoom (10);

        // Set the formatting of 3rd stamp object
        // Specify the Vertical alignment information for stamp object as TOP
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Set the Horizontal alignment inforamtion for stamp object as Center aligned
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // Set the rotation angle for stamp object
        stamp3.setRotateAngle(35);
        // Set pink as background color for stamp
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // Change the font face information for stamp to Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // First stamp is added on first page;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // Second stamp is added on second page;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // Third stamp is added on third page.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Save updated PDF file
        pdfDocument.save(_dataDir);
    }

}
```
