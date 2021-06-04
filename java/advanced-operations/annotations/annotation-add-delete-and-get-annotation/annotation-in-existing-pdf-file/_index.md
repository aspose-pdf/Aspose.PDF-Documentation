---
title: PDF Text Annotation
linktitle: PDF Text Annotation
type: docs
weight: 10
url: /java/pdf-annotation-in-existing-pdf-file/
description: This page describes how to add an annotation in an existing PDF file. Also, you may delete all or particular annotations from a page of a PDF file.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Add, Delete, and Get Annotation are similar for different kinds of annotations. Let take as example a Text Annotation.

## How to add Text Annotation into existing PDF file

In this tutorial, you will learn how to add the text to an existing PDF document. The text tool lets you add text anywhere in the document. A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page’s Annotations collection with the Add method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) object’s Annotations collection.

The following code snippet shows you how to add an annotation in a PDF page.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Sample contents for the annotation");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
```

## Delete All Annotations from Page of PDF File

A [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) object’s [AnnotationCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection contains all the annotations for that particular page. To delete all the annotations from a page, call the *Delete* method of the AnnotationCollectoin collection.

The following code snippet shows you how to delete all the annotations from a particular page.

```java
    public static void DeleteTextAnnotation() {
         // Load the PDF file
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Filter annotations using AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();
 
         // delete annotations
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Get All Annotations from Page of PDF Document

Aspose.PDF allows you to get annotations from an entire document, or from a given page. To get all annotations from the page in a PDF document, loop through the [AnnotationCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection of desired page resources. The following code snippet shows you how to get all the annotations of a page.

```java
  public static void GetTextAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```
