---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /java/text-annotation/
description: Aspose.PDF for Java allows you to Add, Get, and Delete Text Annotation from your PDF document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Guide on handling text annotations in a PDF document
Abstract: This tutorial provides a comprehensive guide on handling various types of annotations in a PDF document using Aspose.PDF for Java. It begins with instructions on adding a Text Annotation to a PDF file, explaining that annotations are associated with specific pages and can be managed via the Annotations collection of a Page object. The tutorial includes a code example demonstrating how to create and add a Text Annotation, detailing steps such as setting the annotation's properties and adding it to the PDF. The guide also covers the creation of Free Text Annotations, which display text directly on the page, using the PdfContentEditor.CreateFreeText method. A code snippet is provided to illustrate the process. Furthermore, the tutorial explains how to retrieve and delete Free Text Annotations from a PDF document. It includes code examples showing how to filter and manipulate annotations using the AnnotationSelector class. Additionally, the tutorial describes how to delete all annotations from a page and retrieve all annotations using the AnnotationCollection class. 
SoftwareApplication: java
---

Add, Delete, and Get Annotation are similar for different kinds of annotations. Let take as example a Text Annotation.

## How to add Text Annotation into existing PDF file

In this tutorial, you will learn how to add the text to an existing PDF document. The text tool lets you add text anywhere in the document. A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page's Annotations collection with the Add method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Annotations collection.

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
}
```

## Add New (or Create) Free Text Annotation

A free text annotation displays text directly on the page. The PdfContentEditor.CreateFreeText method allows creating this type of annotation. In the following snippet, we add free text annotation above the first occurrence of the string.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Free Text Demo");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```

## Get Free Text Annotation

Aspose.PDF for Java allows you to get Free Text Annotation from your PDF document.

Please, check the next code snippet to resolve this task:

```java
public static void GetFreeTextAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Delete Free Text Annotation

Aspose.PDF for Java allows you to delete Free Text Annotation from your PDF document.

Please, check the next code snippet to resolve this task:

```java
  public static void DeleteFreeTextAnnotation() {
         // Load the PDF file
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Filter annotations using AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // delete annotations
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Delete All Annotations from Page of PDF File

A [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection contains all the annotations for that particular page. To delete all the annotations from a page, call the *Delete* method of the AnnotationCollectoin collection.

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

Aspose.PDF allows you to get annotations from an entire document, or from a given page. To get all annotations from the page in a PDF document, loop through the [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) collection of desired page resources. The following code snippet shows you how to get all the annotations of a page.

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
