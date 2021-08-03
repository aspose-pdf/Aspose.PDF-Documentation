---
title: PDF Line Annotation
linktitle: Line Annotation
type: docs
weight: 40
url: /java/line-annotation/
description: This article shows how you can add, get, and delete line annotation from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The purpose of a Line Annotation is to display a single straight line on the page. When opened, it shall display a pop-up window containing the text of the associated note.
This feature additional entries specific to a line annotation. These entries are encrypted in the form of letters, for example, LL, BS, IC, and so on.

Also, Line Annotation can include a caption to a line annotation, which is specified by setting Cap to `true`.

## How to add Line Annotation into existing PDF file

The next feature allows the effect of applying a caption to a Line Annotation that has a leader offset.
Also, this kind of annotation allows you to define Line ending styles.

Steps with which we create an Line annotation:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Create new [Line Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/lineannotation) and set Line parameters (new Rectangle, new Point, title, color, width, StartingStyle and EndingStyle).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation).
1. After we can Add annotation to the page

The following code snippet shows how to add Line Annotation to a PDF file:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // Load the PDF file
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Create Line Annotation
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // Add annotation to the page
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## Get Line Annotation

Please try using the following code snippet to Get Line Annotation in PDF document.

```java
    public static void GetLineAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## Delete Line Annotation

The following code snippet shows how Delete Line Annotation from a PDF file.

```java
   public static void DeleteLineAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}   
```
