---
title: PDF Figures Annotations
linktitle: Figures Annotations
type: docs
weight: 30
url: /java/figures-annotation/
description: يصف هذا المقال كيفية إضافة واستخراج وحذف تعليقات الأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF for Java
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة تعليقات مربعة أو دائرية

تعليقات المربعات والدوائر تعرض على التوالي، مستطيل أو قطع ناقص على الصفحة. عند فتحها، تعرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة. تعليقات المربعات تشبه تعليقات الدوائر (حالات من فئة Aspose.Pdf.Annotations.CircleAnnotation) باستثناء الشكل.

خطوات إنشاء تعليقات المربعات والدوائر:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. قم بإنشاء [تعليق دائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf/circleannotation) جديد وقم بتعيين معايير الدائرة (مستطيل جديد، عنوان، لون، لون داخلي، شفافية).
1. قم بإنشاء [تعليق منبثق](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation) جديد.
1. بعد ذلك نحتاج إلى إنشاء [تعليق مربع](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation).
1. قم بتعيين نفس معايير المربع (مستطيل جديد، عنوان، لون، لون داخلي، شفافية).
1. بعد ذلك نحتاج إلى إضافة تعليقات المربع والدائرة إلى الصفحة.

يوضح لك مقتطف الشفرة التالي كيفية إضافة تعليقات دائرة في صفحة PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // تحميل ملف PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // إنشاء تعليق مضلع
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // إنشاء تعليق مربع
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // إضافة تعليق إلى الصفحة
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


كمثال، سنرى النتيجة التالية لإضافة تعليقات توضيحية على شكل مربع ودائرة إلى مستند PDF:

![عرض توضيحي للتعليقات التوضيحية على شكل دائرة ومربع](circle_demo.png)

## الحصول على التعليق التوضيحي للدائرة

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على التعليق التوضيحي للدائرة من مستند PDF.

```java
public static void GetCircleAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## حذف التعليق التوضيحي للدائرة

يعرض مقتطف الشيفرة التالي كيفية حذف التعليق التوضيحي للدائرة من ملف PDF.

```java
public static void DeleteCircleAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
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

## إضافة تعليقات متعددة الأضلاع والخطوط المتعددة

تتيح لك أداة الخط المتعدد إنشاء أشكال ومخططات بعدد عشوائي من الجوانب على المستند.

**تعليقات متعددة الأضلاع** تمثل الأشكال متعددة الأضلاع على الصفحة. يمكن أن تحتوي على أي عدد من الرؤوس المتصلة بخطوط مستقيمة.

**تعليقات الخطوط المتعددة** تشبه أيضًا الأشكال متعددة الأضلاع، والفرق الوحيد هو أن الرأس الأول والأخير غير متصلين ضمنيًا.

خطوات إنشاء تعليقات توضيحية للعديد من الأضلاع والخطوط المتعددة:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. إنشاء تعليق توضيحي جديد لـ [Polygon Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation) وضبط معايير المضلع (مستطيل جديد، نقاط جديدة، العنوان، اللون، InteriorColor و Opacity).
1. إنشاء [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation) جديد.
1. بعد ذلك، إنشاء تعليق توضيحي لـ [PolyLine Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation) وتكرار جميع الإجراءات.
1. بعد ذلك يمكننا إضافة التعليقات إلى الصفحة.

يظهر مقتطف الشيفرة التالي كيفية إضافة تعليقات توضيحية للمضلع والخطوط المتعددة إلى ملف PDF:

```java
 package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // تحميل ملف PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // إنشاء تعليق توضيحي للمضلع
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // إنشاء تعليق توضيحي للخط المتعدد
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // إضافة التعليق إلى الصفحة
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## الحصول على التعليقات التوضيحية متعددة الأضلاع والخطوط المضلعة

يرجى محاولة استخدام مقتطف الكود التالي للحصول على التعليقات التوضيحية متعددة الأضلاع والخطوط المضلعة في مستند PDF.

```java
    public static void GetPolyAnnotation() {
        // تحميل ملف PDF
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

## حذف التعليقات التوضيحية متعددة الأضلاع والخطوط المضلعة

يوضح مقتطف الكود التالي كيفية حذف التعليقات التوضيحية متعددة الأضلاع والخطوط المضلعة من ملف PDF.

```java
        public static void DeletePolyAnnotation() {
        // تحميل ملف PDF
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


## كيفية إضافة تعليق خطي إلى ملف PDF موجود

الغرض من التعليق الخطي هو عرض خط مستقيم واحد على الصفحة. عند فتحه، سيتم عرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة. 
تتميز هذه الخاصية بإضافات محددة لتعليق خطي. هذه الإضافات مشفرة في شكل حروف، على سبيل المثال، LL، BS، IC، وهكذا.

أيضًا، يمكن أن يتضمن التعليق الخطي عنوانًا للتعليق الخطي، والذي يتم تحديده عن طريق تعيين Cap إلى `true`.

الميزة التالية تسمح بتأثير تطبيق عنوان على تعليق خطي يحتوي على إزاحة قائد.
أيضًا، يتيح لك هذا النوع من التعليقات تحديد أنماط نهاية الخط.

الخطوات التي نستخدمها لإنشاء تعليق خطي:

1. تحميل ملف PDF - [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) جديد.
2. إنشاء [تعليق خطي](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation) جديد وضبط معايير الخط (مستطيل جديد، نقطة جديدة، العنوان، اللون، العرض، نمط البداية ونمط النهاية).

1. إنشاء [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation) جديد.
1. بعد ذلك يمكننا إضافة التعليق التوضيحي إلى الصفحة

يوضح مقتطف الشيفرة التالي كيفية إضافة تعليق توضيحي خطي إلى ملف PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // تحميل ملف PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // إنشاء تعليق توضيحي خطي
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // إضافة التعليق التوضيحي إلى الصفحة
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## الحصول على تعليق الخط

يرجى محاولة استخدام مقطع الشيفرة التالي للحصول على تعليق الخط في مستند PDF.

```java
    public static void GetLineAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## حذف تعليق الخط

يُظهر مقطع الشيفرة التالي كيفية حذف تعليق الخط من ملف PDF.

```java
   public static void DeleteLineAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}
```

## كيفية إضافة تعليق حبر إلى ملف PDF

يمثل تعليق الحبر "خربشة" حرة تتكون من مسار واحد أو أكثر غير متصلين.
 عند الفتح، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة.

يمثل [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) الخربشة اليدوية المكونة من نقطة أو أكثر غير متصلة. يرجى محاولة استخدام مقطع الشيفرة التالي لإضافة InkAnnotation في مستند PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // تحميل ملف PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            // البيانات في ppts، المستلمة من فأرة أو جهاز تأشير آخر
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

            // تحويل البيانات إلى نقاط
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("مستخدم Aspose");
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

## الحصول على InkAnnotation من ملف PDF الخاص بك

يمكنك الحصول على [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) باستخدام الكود التالي:

```java
public static void GetInkAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## حذف InkAnnotation

تسمح لك Aspose.PDF for Java بحذف [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) من ملف PDF الخاص بك.

```java
public static void DeleteInkAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
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