---
title: إضافة كائن دائرة إلى ملف PDF
linktitle: إضافة دائرة
type: docs
weight: 20
url: /ar/java/add-circle/
description: توضح هذه المقالة كيفية إنشاء كائن دائرة لملف PDF الخاص بك باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن دائرة

مثل الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية لعرض البيانات في عدد من الفئات المنفصلة. ومع ذلك، على عكس الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية فقط عندما يكون لديك بيانات لجميع الفئات التي تشكل الكل. لذا دعونا نلقي نظرة على إضافة كائن [الدائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) باستخدام Aspose.PDF for Java.

اتبع الخطوات التالية:

1. أنشئ مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. أنشئ [كائن رسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) بأبعاد معينة

1. تعيين [الحد](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) لكائن الرسم

1. إضافة كائن [الرسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) إلى مجموعة الفقرات في الصفحة

1. حفظ ملف PDF الخاص بنا

```java
public static void ExampleCircle() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات لملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن الرسم بأبعاد معينة
        Graph graph = new Graph(400, 200);
        // تعيين الحد لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


دائرتنا المرسومة ستبدو هكذا:

![رسم دائرة](drawing_circle.png)

## إنشاء كائن دائرة مملوءة

يوضح هذا المثال كيفية إضافة كائن دائرة مملوءة باللون.

```java

    public static void ExampleFilledCircle() {
        // إنشاء مثيل مستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 200);
        // تعيين حد لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


دعونا نرى نتيجة إضافة دائرة مملوءة:

![دائرة مملوءة](filled_circle.png)