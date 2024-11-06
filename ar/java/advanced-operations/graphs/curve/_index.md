---
title: إضافة كائن منحنى إلى ملف PDF
linktitle: إضافة منحنى
type: docs
weight: 30
url: ar/java/add-curve/
description: تشرح هذه المقالة كيفية إنشاء كائن منحنى في ملف PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن منحنى

المنحنى [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) هو اتحاد متصل لخطوط إسقاطية، كل خط يلتقي بثلاثة خطوط أخرى في نقاط مزدوجة عادية.

يوضح Aspose.PDF for Java كيفية استخدام منحنيات بيزيه في رسوماتك.
تستخدم منحنيات بيزيه بشكل واسع في الرسومات الحاسوبية لنمذجة المنحنيات الملساء. يتم احتواء المنحنى بالكامل داخل الهيكل المحدب لنقاط التحكم الخاصة به، ويمكن عرض النقاط بشكل رسومي واستخدامها للتلاعب بالمنحنى بشكل بديهي.
يتم احتواء المنحنى بالكامل داخل رباعي الأضلاع الذي تكون زواياه النقاط الأربع المعطاة (الهيكل المحدب لها).

في هذه المقالة، سنحقق في منحنيات الرسوم ببساطة، والمنحنيات المملوءة، التي يمكنك إنشاؤها في مستند PDF الخاص بك.

اتبع الخطوات التالية:

1. قم بإنشاء مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. قم بإنشاء [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) بأبعاد معينة.

1. قم بتعيين [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) لكائن الرسم.

1. أضف كائن [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) إلى مجموعة الفقرات في الصفحة.

1. احفظ ملف PDF الخاص بك

```java
    public static void ExampleCurve() {
        // إنشاء مثيل Document
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 200);
        // تعيين الحدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // احفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


الصورة التالية توضح النتيجة التي تم تنفيذها باستخدام كودنا:

![رسم منحنى](drawing_curve.png)

## إنشاء كائن منحنى ممتلئ

يوضح هذا المثال كيفية إضافة كائن منحنى ممتلئ باللون.

```java
    public static void ExampleFilledCurve() {
        // إنشاء مثيل لمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة صفحات ملف الـ PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 200);
        // تعيين حدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف الـ PDF
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


انظر إلى نتيجة إضافة منحنى مملوء:

![منحنى مملوء](filled_curve.png)