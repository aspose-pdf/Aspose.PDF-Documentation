---
title: إضافة أشكال القطع الناقص إلى PDF في Java
linktitle: أضف القطع الناقص
type: docs
weight: 60
url: /java/add-ellipse/
description: تعرف على كيفية رسم الأشكال البيضاوية وتعبئتها وتسميتها في ملفات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال القطع الناقص في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال القطع الناقص إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي علامات الحذف المحددة، وعلامات الحذف المملوءة، ووضع أجزاء النص داخل أشكال القطع الناقص.
---
## إضافة الخطوط العريضة للقطع الناقص

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. قم بإنشاء الشكل [القطع الناقص](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) وقم بتكوين شكله الهندسي.
1. أضف [القطع الناقص](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. قم بتعيين خصائص الشكل التي يتطلبها المثال، بما في ذلك [اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) و[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

يضيف المثال الكامل شكلين بيضاويين مختلفين إلى نفس الرسم البياني.

## إضافة علامات الحذف المملوءة

`createEllipseFilled` يملأ شكلين بيضاويين بـ `Color.getGreenYellow()` و`Color.getDarkRed()`.

## إضافة نص داخل علامات الحذف

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. قم بإنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وقم بتعيين خيارات تنسيق النص المطلوبة.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. قم بإنشاء الشكل [القطع الناقص](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) وقم بتكوين شكله الهندسي.
1. أضف [القطع الناقص](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
