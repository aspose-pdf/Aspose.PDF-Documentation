---
title: إضافة أشكال خطية إلى PDF في Java
linktitle: إضافة خط
type: docs
weight: 40
url: /java/add-line/
description: تعرف على كيفية رسم أشكال الخطوط والخطوط المصممة في ملفات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال الخطوط في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال خطية إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي إنشاء خطوط من صفائف الإحداثيات، وتطبيق التصميم واللون المتقطع، ورسم الخطوط عبر منطقة الصفحة بأكملها.
---
## أضف خطًا متقطعًا

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) وقم بتكوين إحداثياته.
1. أضف [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## أضف خطًا ملونًا منقطًا أو متقطعًا

يستخدم `addDottedDashedLine` نفس الإحداثيات وإعدادات الشرطة، ولكنه ينطبق أيضًا على `Color.getRed()`.

## ارسم خطوطًا عبر الصفحة

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) وقم بتكوين إحداثياته.
1. أضف [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
