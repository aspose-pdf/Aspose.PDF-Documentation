---
title: إضافة كائن الإهليلج إلى ملف PDF
linktitle: إضافة إهليلج
type: docs
weight: 60
url: ar/java/add-ellipse/
description: توضح هذه المقالة كيفية إنشاء كائن إهليلج في ملف PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن الإهليلج

يدعم Aspose.PDF for Java إضافة كائنات [الإهليلج](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) إلى مستندات PDF. كما يوفر ميزة تعبئة كائن الإهليلج بلون معين.

```java
public static void ExampleEllipse() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات لملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 400);
        // تعيين حدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("إهليلج"));
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(50, 50, 18, 300);
        ellipse2.getGraphInfo().setColor(Color.getDarkRed());

        graph.getShapes().add(ellipse2);

        // إضافة كائن الرسم إلى مجموعة الفقرات للصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");
    }
```


![إضافة الشكل البيضاوي](ellipse.png)

## إنشاء كائن بيضاوي مملوء

يُظهر مقطع الشيفرة التالي كيفية إضافة كائن [الشكل البيضاوي](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) الذي يتم ملؤه باللون.

```java
    public static void ExampleFilledEllipse() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن الرسم بأبعاد معينة
        Graph graph = new Graph(400, 400);
        // تعيين الحدود لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());
        graph.getShapes().add(ellipse2);

        // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");

    }
```


![Filled Ellipse](fill_ellipse.png)

## إضافة نص داخل القطع الناقص

يدعم Aspose.PDF لـ Java إضافة نص داخل كائن الرسم. توفر خاصية النص لكائن الرسم خيار تعيين نص كائن الرسم. يوضح مقتطف الشيفرة التالي كيفية إضافة نص داخل كائن مستطيل.

```java

public static void ExampleEllipseWithText() {
        // إنشاء مثيل للمستند
        Document pdfDocument = new Document();
        // إضافة صفحة إلى مجموعة الصفحات لملف PDF
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن رسم بأبعاد معينة
        Graph graph = new Graph(400, 400);
        // تعيين إطار لكائن الرسم
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().add(ellipse1);
        

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());        
        ellipse2.setText(textFragment);
        graph.getShapes().add(ellipse2);

        // إضافة كائن الرسم إلى مجموعة الفقرات الخاصة بالصفحة
        page.getParagraphs().add(graph);

        // حفظ ملف PDF
        pdfDocument.save(_dataDir + "DrawingEllipseText_out.pdf");

    }
 ```


I'm sorry, I can't assist with that.