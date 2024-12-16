---
title: إضافة كائن قوس إلى ملف PDF
linktitle: إضافة قوس
type: docs
weight: 10
url: /ar/java/add-arc/
description: توضح هذه المقالة كيفية إنشاء كائن قوس إلى ملف PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن قوس

يدعم Aspose.PDF لـ Java ميزة إضافة كائنات الرسم (مثل الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. كما يقدم ميزة ملء كائن القوس بلون معين.

اتبع الخطوات أدناه:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) بأبعاد معينة

1. تعيين [الحدود](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) لكائن الرسم

1. إضافة كائن [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) إلى مجموعة الفقرات في الصفحة

1. حفظ ملف PDF الخاص بنا

يوضح مقتطف الشيفرة التالي كيفية إضافة كائن [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة صفحات ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 400);
        // تعيين الحدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // إضافة كائن الرسم إلى مجموعة الفقرات للصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## إنشاء كائن قوس مملوء

يوضح المثال التالي كيفية إضافة كائن قوس مملوء باللون وأبعاد معينة.

```java
    public static void ExampleFilledArc() {
        // إنشاء مثيل لمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 400);
        // تعيين الحدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![قوس ممتلئ](filled_arc.png)