---
title: إضافة كائن خط إلى ملف PDF
linktitle: إضافة خط
type: docs
weight: 40
url: /java/add-line/
description: يشرح هذا المقال كيفية إنشاء كائن خط في ملف PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن خط

يدعم Aspose.PDF for Java ميزة إضافة كائنات الرسوم (مثل الرسوم، الخط، المستطيل، إلخ.) إلى مستندات PDF. يمكنك أيضًا إضافة كائن [خط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) حيث يمكنك تحديد نمط الشرطات، اللون وتنسيقات أخرى لعنصر الخط.

اتبع الخطوات التالية:

1. أنشئ مثيل [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) إلى مجموعة الصفحات في ملف PDF.

1. أنشئ مثيل [رسم](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. أضف كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة.

1. قم بإنشاء مثيل [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. قم بتعيين عرض الخط.

1. أضف كائن [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) إلى مجموعة الأشكال لكائن Graph.

1. احفظ ملف PDF الخاص بك.

يوضح مقتطف الشيفرة التالي كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) مملوء باللون.

```java
 public static void ExampleLine() {
        // إنشاء مثيل Document
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();
        // إنشاء مثيل Graph
        Graph graph = new Graph(100, 400);

        // إضافة كائن الرسم البياني إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(graph);

        // إنشاء مثيل Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن Graph
        graph.getShapes().add(line);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## كيفية إضافة خط متقطع إلى مستند PDF الخاص بك

```java
public static void ExampleDashedLine() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph canvas = new Graph(100, 400);
        // إضافة كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة
        page.getParagraphs().add(canvas);

        // إنشاء كائن خط
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // تعيين اللون لكائن الخط
        line.getGraphInfo().setColor(Color.getRed());
        // تحديد مصفوفة التقطيع لكائن الخط
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // تعيين مرحلة التقطيع لمثيل الخط
        line.getGraphInfo().setDashPhase(1);
        // إضافة الخط إلى مجموعة الأشكال في كائن الرسم
        canvas.getShapes().add(line);
        // حفظ مستند PDF
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


دعونا نتحقق من النتيجة:

![Dashed Line](dash_line.png)

## رسم خط عبر الصفحة

يمكننا أيضًا استخدام كائن الخط لرسم تقاطع بدءًا من الزاوية السفلية اليسرى إلى الزاوية العلوية اليمنى ومن الزاوية العلوية اليسرى إلى الزاوية السفلية اليمنى.

يرجى إلقاء نظرة على مقتطف الكود التالي لتحقيق هذا المتطلب.

```java
    public static void ExampleLineAcrossPage() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();
        // تعيين هامش الصفحة على جميع الجوانب كـ 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // إنشاء كائن الرسم مع العرض والارتفاع مساويين لأبعاد الصفحة
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // إنشاء كائن الخط الأول بدءًا من الزاوية السفلية اليسرى إلى الزاوية العلوية اليمنى من الصفحة
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // إضافة الخط إلى مجموعة الأشكال في كائن الرسم
        graph.getShapes().add(line);
        // رسم خط من الزاوية العلوية اليسرى للصفحة إلى الزاوية السفلية اليمنى للصفحة
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // إضافة الخط إلى مجموعة الأشكال في كائن الرسم
        graph.getShapes().add(line2);
        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![رسم خط](draw_line.png)