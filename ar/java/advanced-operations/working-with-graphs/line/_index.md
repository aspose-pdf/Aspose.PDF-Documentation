---
title: إضافة أشكال الخط إلى PDF في Java
linktitle: إضافة خط
type: docs
weight: 40
url: /ar/java/add-line/
description: تعلم كيفية رسم أشكال الخط والخطوط المصممة في ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال الخط في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال الخط إلى مستندات PDF باستخدام Aspose.PDF for Java. يغطي المقال إنشاء الخطوط من مصفوفات الإحداثيات، وتطبيق نمط متقطع ولون، ورسم الخطوط عبر كامل مساحة الصفحة.
---
## إضافة خط متقطع

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفها إلى الصفحة.
1. إنشاء [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) شكل وقم بتكوين إحداثياته.
1. أضف [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## أضف خطًا منقطًا أو متقطعًا ملونًا

`addDottedDashedLine` يستخدم نفس الإحداثيات وإعدادات الشرط، لكنه يطبق أيضًا `Color.getRed()`.

## ارسم خطوطًا عبر الصفحة

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفها إلى الصفحة.
1. إنشاء [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) شكل وقم بتكوين إحداثياته.
1. أضف [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
