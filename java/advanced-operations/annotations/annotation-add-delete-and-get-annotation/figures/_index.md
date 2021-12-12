---
title: PDF Figures Annotations
linktitle: Figures Annotations
type: docs
weight: 30
url: /java/figures-annotation/
description: This article describes how to add, get, and delete figures annotations from your PDF document with Aspose.PDF for Java
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Square or Circle Annotations

Square and Circle annotations shall display, respectively, a rectangle or an ellipse on the page. When opened, they shall display a pop-up window containing the text of the associated note.
Square annotations are like Circle annotations (instances of the Aspose.Pdf.Annotations.CircleAnnotation class) apart from the shape.

Steps for creating Square and Circle Annotations:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Create new [Circle Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/circleannotation) and set Circle parameters (new Rectangle, title, color, InteriorColor, Opacity).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation).
1. Next we need to create [Square Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation).
1. Set the same Square parameters (new Rectangle, title, color, InteriorColor, Opacity).
1. After we need to Add Square and Circle Annotations to the page.

The following code snippet shows you how to add Circle Annotations in a PDF page.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // Load the PDF file
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Create Polygon Annotation
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // Create Square Annotation
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Add annotation to the page
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

As an example, we will see the following result of adding Square and Circle annotations to a PDF document:

![Circle and Square Annotation demo](circle_demo.png)

## Get Circle Annotation

Please try using the following code snippet to Get Circle Annotation from PDF document.

```java
public static void GetCircleAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Delete Circle Annotation

The following code snippet shows how to Delete Circle Annotation from PDF file.

```java
public static void DeleteCircleAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> circleAnnotations = annotationSelector.getSelected();

        for (Annotation ca : circleAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```

## Add Polygon and Polyline Annotations

The Polyline tool allows you to create shapes and outlines with an arbitrary number of sides on the document.

**Polygon Annotations** represent polygons on a page. They can have any number of vertices connected by straight lines.

**Polyline Annotations** are also similar to polygons, the only difference is that the first and last vertices are not implicitly connected.

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
```

## How to add Line Annotation into existing PDF file

The purpose of a Line Annotation is to display a single straight line on the page. When opened, it shall display a pop-up window containing the text of the associated note.
This feature additional entries specific to a line annotation. These entries are encrypted in the form of letters, for example, LL, BS, IC, and so on.

Also, Line Annotation can include a caption to a line annotation, which is specified by setting Cap to `true`.

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

## How to add Ink Annotation to PDF file

An Ink Annotation represents a freehand "scribble" composed of one or more disjoint paths. When opened, it shall display a pop-up window containing the text of the associated note.

The [InkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) represents freehand scribble composed of one or more disjoint points. Please try using the following code snippet to add InkAnnotation in PDF document.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // Load the PDF file
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            //data in ppts, received from a mouse or other pointing device
            double ppts[] = { 328.002, 222.017, 328.648, 222.017, 329.294, 222.017, 329.617, 222.34, 330.91, 222.663,
                    331.556, 222.663, 332.203, 222.986, 333.495, 223.633, 334.141, 223.956, 334.788, 224.279, 335.434,
                    224.602, 336.08, 224.602, 336.727, 224.925, 337.373, 225.248, 337.696, 225.248, 338.342, 225.572,
                    338.989, 225.895, 341.897, 225.895, 343.513, 226.218, 346.098, 226.218, 348.683, 226.541, 350.622,
                    226.541, 352.238, 226.541, 353.208, 226.541, 353.854, 226.541, 355.146, 226.541, 356.439, 226.541,
                    357.732, 226.541, 358.378, 226.541, 359.024, 226.541, 360.64, 226.541, 361.286, 226.541, 361.933,
                    226.541, 362.256, 226.541, 362.902, 226.541, 363.548, 226.541, 363.872, 226.541, 363.872, 226.218,
                    365.164, 226.218, 365.487, 226.218, 365.811, 226.218, 367.103, 226.218, 367.749, 226.218, 368.719,
                    226.218, 370.012, 226.218, 370.981, 226.218, 371.627, 226.218, 372.597, 225.895, 372.92, 225.895,
                    373.243, 225.895, 373.243, 225.572, 373.566, 225.572, 374.213, 225.248, 374.536, 225.248, 375.182,
                    224.602, 375.182, 224.279, 375.828, 223.956, 376.475, 223.31, 377.121, 222.986, 377.767, 222.986,
                    378.414, 222.017, 379.383, 221.371, 379.706, 220.724, 380.029, 219.432, 380.676, 219.109, 380.676,
                    218.462, 381.645, 217.493, 381.968, 217.17, 381.968, 216.523, 382.291, 215.554, 382.615, 215.231,
                    382.615, 214.261, 382.938, 213.292, 382.938, 212.645, 382.938, 211.999, 382.938, 211.353, 382.938,
                    210.707, 382.938, 209.737, 382.938, 208.768, 382.938, 208.444, 382.615, 207.475, 382.615, 206.829,
                    382.291, 206.505, 382.291, 205.859, 381.968, 204.89, 381.968, 204.243, 381.645, 203.92, 380.999,
                    203.274, 380.999, 202.951, 380.676, 202.305, 380.353, 201.658, 380.029, 201.335, 380.029, 200.689,
                    380.029, 200.366, 379.383, 199.719, 379.06, 199.719, 378.737, 199.073, 377.767, 198.103, 377.121,
                    197.780, 376.475, 197.457, 375.505, 196.488, 374.859, 196.165, 374.536, 195.841, 372.92, 195.195,
                    371.951, 194.549, 370.658, 194.226, 368.719, 193.902, 367.426, 193.256, 366.457, 193.256, 363.872,
                    192.933, 362.902, 192.933, 361.61, 192.61, 359.024, 192.61, 357.409, 192.61, 356.439, 192.61,
                    353.531, 192.61, 352.561, 192.61, 350.945, 192.61, 349.007, 192.933, 348.36, 193.256, 347.391,
                    193.256, 346.098, 193.902, 345.452, 193.902, 344.806, 193.902, 343.513, 193.902, 342.867, 193.902,
                    342.220, 193.902, 341.574, 193.902, 341.251, 194.226, 340.928, 194.226, 340.928, 194.549, 340.605,
                    194.549, 340.605, 194.872, 339.635, 195.195, 339.635, 195.518, 338.989, 195.518, 338.989, 195.841,
                    338.666, 196.165, 338.019, 196.811, 338.019, 197.134, 337.373, 197.457, 336.404, 198.427, 335.757,
                    198.427, 335.434, 198.75, 334.141, 199.719, 333.818, 199.719, 333.818, 200.042, 332.849, 200.366,
                    332.203, 200.366, 331.556, 201.335, 330.91, 201.981, 330.587, 202.305, 330.264, 202.305, 329.294,
                    202.628, 328.971, 202.951, 328.002, 203.274, 328.002, 203.597, 327.355, 204.243, 326.709, 204.567,
                    326.386, 204.89, 326.063, 205.536, 325.416, 205.859, 325.093, 205.859, 324.447, 205.859, 324.124,
                    206.182, 324.124, 206.505, 323.477, 206.829, 323.477, 207.152, 323.477, 207.798, 322.831, 207.798,
                    322.831, 208.121, 322.831, 208.444, 322.508, 208.444, 322.508, 209.091, 322.185, 209.414, 322.185,
                    209.737, 322.185, 210.383, 322.185, 211.03, 322.185, 211.353, 322.185, 211.676, 322.185, 212.322,
                    323.154, 213.292, 323.154, 213.938, 324.447, 214.584, 325.093, 215.877, 325.416, 216.2, 325.416,
                    216.846, 325.739, 217.17, 326.063, 217.493, 326.386, 218.139, 326.709, 218.139, 326.709, 218.462,
                    327.032, 219.109, 327.032, 219.432, 327.032, 219.755, 327.355, 220.078, 327.355, 220.401, 327.678,
                    221.371, 328.002, 221.371, 328.002, 222.017, 328.325, 222.663, 328.648, 222.663, 328.971, 222.986,
                    329.294, 223.31, 329.617, 223.956, 329.617, 224.279 };

            //convert data to points
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("Aspose User");
            ia.setColor(Color.getRed());
            ia.setCapStyle(CapStyle.Rounded);

            Border border = new Border(ia);
            border.setWidth(3);
            ia.setOpacity(0.75);

            page.getAnnotations().add(ia);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## Get InkAnnotation from your PDF

You can get [InkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) with the next code snippet:

```java
public static void GetInkAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## Delete InkAnnotation

Aspose.PDF for Java allows you to delete [InkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) from your PDF file.

```java
public static void DeleteInkAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> InkAnnotations = annotationSelector.getSelected();

        for (Annotation ca : InkAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```