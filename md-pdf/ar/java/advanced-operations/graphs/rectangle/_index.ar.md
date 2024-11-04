---
title: إضافة كائن مستطيل إلى ملف PDF
linktitle: إضافة مستطيل
type: docs
weight: 50
url: /java/add-rectangle/
description: يشرح هذا المقال كيفية إنشاء كائن مستطيل إلى ملف PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن مستطيل

يدعم Aspose.PDF for Java ميزة إضافة كائنات الرسوم (مثل الرسم، الخط، المستطيل إلخ.) إلى مستندات PDF. يمكنك أيضًا إضافة كائن [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) حيث يتوفر لك أيضًا ميزة ملء كائن المستطيل بلون معين، التحكم في ترتيب Z، إضافة لون تعبئة متدرج إلخ.

أولاً، دعونا نلقي نظرة على إمكانية إنشاء كائن مستطيل.

اتبع الخطوات التالية:

1. إنشاء [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) PDF جديد

2. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) إلى مجموعة صفحات ملف PDF

1. أضف [مقطع نصي](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) إلى مجموعة الفقرات في مثيل الصفحة

1. أنشئ مثيل [رسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)

1. تعيين الحدود لكائن [الرسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. أنشئ مثيل مستطيل

1. أضف كائن [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) إلى مجموعة الأشكال في كائن الرسم

1. أضف كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة

1. أضف [مقطع نصي](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) إلى مجموعة الفقرات في مثيل الصفحة

1. واحفظ ملف PDF الخاص بك

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // أنشئ مستند PDF جديد
        Document pdfDocument = new Document();

        // أضف صفحة إلى مجموعة صفحات ملف PDF
        Page page = pdfDocument.getPages().add();

        // أضف مقطع نصي إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(new TextFragment("نص قبل كائن الرسم"));

        // أنشئ مثيل رسم
        Graph graph = new Graph(400, 200);

        // تعيين الحدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // أنشئ مثيل مستطيل
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // أضف كائن المستطيل إلى مجموعة الأشكال في كائن الرسم
        graph.getShapes().add(rect);

        // أضف كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(graph);

        // أضف مقطع نصي إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(new TextFragment("نص بعد كائن الرسم"));

        // احفظ ملف PDF
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل مملوء

يوفر Aspose.PDF for Java أيضًا ميزة ملء كائن المستطيل بلون معين.

يوضح مقتطف الشيفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) مملوء باللون.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // إضافة صفحة إلى مجموعة صفحات ملف PDF
        Page page = pdfDocument.getPages().add();
        // إنشاء مثيل Graph
        Graph graph = new Graph(100, 400);

        // إضافة كائن الرسم البياني إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(graph);

        // إنشاء مثيل مستطيل
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // تحديد لون التعبئة لكائن الرسم البياني
        rect.getGraphInfo().setFillColor(Color.getRed());

        // إضافة كائن المستطيل إلى مجموعة الأشكال في كائن الرسم البياني
        graph.getShapes().add(rect);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


انظر إلى نتيجة المستطيل المملوء بلون صلب:

![المستطيل المملوء](fill_rectangle.png)

## إضافة رسم بتعبئة تدرجية

يدعم Aspose.PDF لـ Java ميزة إضافة كائنات الرسم إلى مستندات PDF وأحيانًا يتطلب الأمر ملء كائنات الرسم بلون متدرج. لملء كائنات الرسم بلون متدرج، نحتاج إلى تعيين setPatterColorSpace مع كائن gradientAxialShading كما يلي.

يظهر مقتطف الشيفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) الذي يتم ملؤه بلون متدرج.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // تحديد لون تعبئة متدرج لكائن الرسم وملئه
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![مستطيل متدرج](gradient.png)

## إنشاء مستطيل مع قناة لون ألفا

يدعم Aspose.PDF for Java ملء كائن المستطيل بلون معين. يمكن أن يحتوي كائن المستطيل أيضًا على قناة لون ألفا لإعطاء مظهر شفاف. يوضح مقطع الشيفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) مع قناة لون ألفا.

يمكن لبكسلات الصورة تخزين معلومات حول عتامة اللون بالإضافة إلى قيمة اللون. هذا يسمح بإنشاء صور بمناطق شفافة أو شبه شفافة.

بدلاً من جعل لون معين شفافًا، يقوم كل بكسل بتخزين معلومات حول مدى عتامته. تُسمى بيانات العتامة هذه قناة ألفا وعادة ما يتم تخزينها بعد قنوات الألوان للبكسل.

في مقطع الشيفرة الخاص بنا، استخدمنا طريقة [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) من [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color).
 نحتاج إلى تحديد القيم حيث أن أول 3 قيم هي مكونات اللون، يتم تحديدها في النطاق من 0 إلى 255، والأخيرة هي مستوى الشفافية (قناة الألفا)، يتم تحديدها بأرقام كسرية من 0 إلى 1.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن Graph
        Graph graph = new Graph(100, 400);

        // إنشاء كائن مستطيل بأبعاد محددة
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // إضافة كائن المستطيل إلى مجموعة الأشكال الخاصة بكائن Graph
        graph.getShapes().add(rect1);

        // إنشاء كائن مستطيل ثاني
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // إضافة كائن Graph إلى مجموعة الفقرات الخاصة بكائن الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![قناة ألفا المستطيلة اللون](rectangle_color.png)

## التحكم في ترتيب Z للمستطيل

يدعم Aspose.PDF لـ Java ميزة إضافة كائنات الرسوم (مثل الرسم البياني، الخط، المستطيل، إلخ) إلى مستندات PDF. عند إضافة أكثر من نسخة من نفس الكائن داخل ملف PDF، يمكننا التحكم في عرضها عن طريق تحديد ترتيب Z. يُستخدم ترتيب Z أيضًا عندما نحتاج إلى عرض الكائنات فوق بعضها البعض.

يُظهر مقطع الكود التالي الخطوات اللازمة لعرض كائنات [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) فوق بعضها البعض.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // إنشاء مستطيل جديد بلون أحمر وترتيب Z كـ 0 وأبعاد معينة
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // إنشاء مستطيل جديد بلون أزرق وترتيب Z كـ 0 وأبعاد معينة
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // إنشاء مستطيل جديد بلون أخضر وترتيب Z كـ 0 وأبعاد معينة
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // حفظ ملف PDF الناتج
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![التحكم في ترتيب Z](control.png)