---
title: PDF Free Text Annotation
linktitle: Free Text Annotation
type: docs
weight: 30
url: /java/free-text-annotation/
description: This article teaches how to add Free Text Annotation to PDF using Aspose.PDF for Java. Learn more about how to set Callout for such annotation.
lastmod: "2021-01-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

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