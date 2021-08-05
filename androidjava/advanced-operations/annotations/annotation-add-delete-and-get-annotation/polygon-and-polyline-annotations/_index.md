---
title: PDF Polygon/Polyline Annotations
linktitle: Polygon/Polyline Annotations
type: docs
weight: 60
url: /androidjava/polygon-and-polyline-annotations/
description: Aspose.PDF for Java allows you to add, get, and delete the polygon and polyline annotations from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The Polyline tool allows you to create shapes and outlines with an arbitrary number of sides on the document.

**Polygon Annotations** represent polygons on a page. They can have any number of vertices connected by straight lines.

**Polyline Annotations** are also similar to polygons, the only difference is that the first and last vertices are not implicitly connected.

## Add Polygon and Polyline Annotations 

Steps with which we create Polygon and Polyline annotations:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Create new [Polygon Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation) and set Polygon parameters (new Rectangle, new Points, title, color, InteriorColor and Opacity).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation). 
1. Next, Create a [PolyLine Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation) and repeat all actions.
1. After we can Add annotations to the page.

The following code snippet shows how to add Polygon and Polyline Annotations to PDF file:

```java
 package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // Load the PDF file
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Create Polygon Annotation
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Create PoliLine Annotation
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Add annotation to the page
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }   
```

## Get Polygon and Polyline Annotations

Please try using the following code snippet to Get Polygon and Polyline Annotations in PDF document.

```java        
 public static void GetPolyAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            System.out.printf("[%s]", pa.getRect());
        }
    }       
```

## Delete Polygon and Polyline Annotations

The following code snippet shows how Delete Polygon and Polyline Annotations from a PDF file.

```java
        public static void DeletePolyAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            page.getAnnotations().delete(pa);
        }

        document.save(_dataDir + "Appartments_del.pdf");
    }
}
```
