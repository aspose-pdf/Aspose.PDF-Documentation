---
title: إضافة أشكال القوس إلى PDF في Java
linktitle: إضافة Arc
type: docs
weight: 10
url: /ar/java/add-arc/
description: تعلم كيفية رسم وتعبئة أشكال القوس في ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال القوس في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال القوس إلى مستندات PDF باستخدام Aspose.PDF for Java. وتغطي رسم عدة أقواس محددة بألوان مختلفة وإنشاء قطاع قوس مملوء بدمج قوس مع خط إغلاق.
---
Aspose.PDF for Java يستخدم `Graph` مع كائنات الشكل مثل `Arc` و `Line` لرسم الرسومات المتجهية.

## إضافة مخططات القوس

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفه إلى الصفحة.
1. إنشاء [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) شكل وتكوين هندسته.
1. أضف الـ [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) إلى الـ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. عيّن خصائص الشكل المطلوبة في المثال، بما في ذلك [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

المثال الكامل يضيف ثلاثة أقواس ذات أقطار وزوايا وألوان مختلفة إلى نفس الرسم البياني.

## أضف قطعة قوس مملوءة

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفه إلى الصفحة.
1. إنشاء [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) شكل وتكوين إحداثياته.
1. إنشاء [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) شكل وتكوين هندسته.
1. أضف الـ [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) و [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) إلى الـ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
