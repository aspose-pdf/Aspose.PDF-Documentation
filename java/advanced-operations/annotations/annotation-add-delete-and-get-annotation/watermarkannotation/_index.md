---
title: PDF Watermark Annotation 
linktitle: Watermark Annotation
type: docs
weight: 130
url: /java/watermarkannotation/
description: The Watermark Annotation in the text uses to represent graphics on the page. Check code snippet to resolve this task. 
lastmod: "2021-02-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Watermark Annotation 

A watermark annotation shall be used to represent graphics that shall be printed at a fixed size and position on a page, regardless of the dimensions of the printed page.

You can add Watermark Text using [WatermarkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using opacity property.

Please check the following code snippet to add WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        
        //Create Annotation
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        //Add annotaiton into Annotation collection of Page
        page.getAnnotations().add(wa);

        //Create TextState for Font settings
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        //Set opacity level of Annotaiton Text
        wa.setOpacity(0.5);
                
        //Add Text to Annotation
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        //Save the Document        
        document.save(_dataDir + "sample_watermark.pdf");
    }
```
## Get Watermark Annotation

```java
    public static void GetWatermarkAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Delete Watermark Annotation

```java
    public static void DeleteWatermarkAnnotation() {
         // Load the PDF file
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Filter annotations using AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();
 
         // delete annotations
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
}
```