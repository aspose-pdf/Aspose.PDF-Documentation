---
title: إضافة أشكال إهليلجية إلى PDF في Java
linktitle: إضافة إهليلج
type: docs
weight: 60
url: /ar/java/add-ellipse/
description: تعلم كيفية رسم وملء وتسمية أشكال الإهليلج في ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال إهليلجية في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال إهليلجية إلى مستندات PDF باستخدام Aspose.PDF for Java. تغطي الإهليلجات المخططة، الإهليلجات المملوءة، ووضع قطع النص داخل أشكال الإهليلج.
---
## إضافة حدود إهليلجية

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية وإضافتها إلى الصفحة.
1. إنشاء [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) الشكل وتكوين هندسته.
1. إضافة [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. قم بتعيين خصائص الشكل المطلوبة في المثال، بما في ذلك [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) و [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

يضيف المثال الكامل إهليلجين مخططين مختلفين إلى نفس الرسم البياني.

## إضافة إهليلجيات مملوءة

`createEllipseFilled` يملأ نقطتين بـ `Color.getGreenYellow()` و `Color.getDarkRed()`.

## إضافة نص داخل الإهليلجيات

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وتعيين خيارات تنسيق النص المطلوبة.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية وإضافتها إلى الصفحة.
1. إنشاء [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) الشكل وتكوين هندسته.
1. إضافة [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
