---
title: Add Text stamps in PDF programmatically
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF file using the TextStamp class with Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Text Stamp with Java

Aspose.PDF for Java provides [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class to add a text stamp in a PDF file. The [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class provides necessary methods to specify font size, font style, and font color etc for stamp object. In order to add text stamp, first you need to create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object and a [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) object using required methods. After that, you may call [addStamp(..)](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp in the PDF document.

The following code snippet shows you how to add text stamp in the PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // open document
        Document pdfDocument = new Document("input.pdf");
        // create text stamp
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // set whether stamp is background
        textStamp.setBackground(true);
        // set origin
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // rotate stamp
        textStamp.setRotate(Rotation.on90);
        // set text properties
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // add stamp to particular page
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // save output document
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Define alignment for TextStamp object

Adding watermarks to PDF documents is one of the frequent demanded features and Aspose.PDF for Java is fully capable of adding Image as well as Text watermarks. The [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class provides the feature to add text stamps over the PDF file. Recently there has been a requirement to support the feature to specify the alignment of text when using [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) object. So in order to fulfill this requirement, we have introduced setTextAlignment(..) method in [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class. By using this method, you can specify the Horizontal text alignment.

The following code snippets shows an example on how to load an existing PDF document and add [TextStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) over it.

```java
    public static void DefineAlignmentTextStamp() {
        // Instantiate Document object with input file
        Document pdfDocument = new Document("input.pdf");
        // instantiate FormattedText object with sample string
        FormattedText text = new FormattedText("This");
        
        // add new text line to FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // create TextStamp object using FormattedText
        TextStamp stamp = new TextStamp(text);
        // specify the Horizontal Alignment of text stamp as Center aligned
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // specify the Vertical Alignment of text stamp as Center aligned
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // specify the Text Horizontal Alignment of TextStamp as Center aligned
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // set top margin for stamp object
        stamp.setTopMargin(20);
        // add stamp to all pages of PDF file
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // save output document
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Fill Stroke Text as Stamp in PDF File

We have implemented setting of rendering mode for text adding and editing scenarios. To render stroke text please create [TextState](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextState) object and set RenderingMode to TextRenderingMode.StrokeText and also select color for StrokingColor property. Later, bind TextState to the stamp using BindTextState() method.

Following code snippet demonstrates adding Fill Stroke Text:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Create TextState object to transfer advanced properties
        TextState ts = new TextState();
        
        // Set color for stroke
        ts.setStrokingColor(Color.getGray());
        
        // Set text rendering mode
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Load an input PDF document
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Bind TextState
        stamp.bindTextState(ts);
        // Set X,Y origin
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Add Stamp
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```
