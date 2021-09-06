---
title: PDF Caret Annotation
linktitle: Caret Annotation
type: docs
weight: 90
url: /androidjava/caret-annotation/
description: This section describes how to add, get, and delete Caret annotation from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to add Caret Annotation into existing PDF file

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.

Steps with which we create an Line annotation:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Create new [Caret Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the insertion of text.
1. Create new [StrikeOutAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) and set parameters (new Rectangle, title, color, new QuadPoints and new points, Subject, InReplyTo,ReplyType).
1. After we can Add annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        // This annotation is used to indicate the insertion of text
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // This annotation is used to indicate the replacement of text
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```

## Get Caret Annotation

Please try using the following code snippet to Get Caret Annotation in PDF document

```java
    public static void GetCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }

```

## Delete Caret Annotation

The following code snippet shows how Delete Caret Annotation from a PDF file.

```java
public static void DeleteCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // delete annotation
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
}
```
