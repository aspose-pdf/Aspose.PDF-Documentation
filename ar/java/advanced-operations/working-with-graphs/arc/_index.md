---
title: إضافة أشكال القوس إلى PDF في Java
linktitle: أضف قوسًا
type: docs
weight: 10
url: /java/add-arc/
description: تعرف على كيفية رسم الأشكال القوسية وتعبئتها في ملفات PDF بلغة Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال قوسية في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال قوسية إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي رسم أقواس متعددة محددة بألوان مختلفة وإنشاء مقطع قوس مملوء من خلال دمج القوس مع خط الإغلاق.
---
يستخدم Aspose.PDF لـ Java `Graph` مع كائنات الشكل مثل `Arc` و`Line` لعرض الرسومات المتجهة.

## إضافة الخطوط العريضة للقوس

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [القوس](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) وقم بتكوين شكله الهندسي.
1. أضف [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) إلى حاوية [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. قم بتعيين خصائص الشكل التي يتطلبها المثال، بما في ذلك [اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

يضيف المثال الكامل ثلاثة أقواس ذات أنصاف أقطار وزوايا وألوان مختلفة إلى نفس الرسم البياني.

## أضف قطعة قوسية مملوءة

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) وقم بتكوين إحداثياته.
1. أنشئ الشكل [القوس](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) وقم بتكوين شكله الهندسي.
1. أضف [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) و[القوس](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
