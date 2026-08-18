---
title: إضافة أشكال مستطيلة إلى PDF في Java
linktitle: إضافة مستطيل
type: docs
weight: 50
url: /java/add-rectangle/
description: تعرف على كيفية رسم الأشكال المستطيلة وتعبئتها في ملفات PDF بلغة Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال مستطيلة في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال مستطيلة إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي المستطيلات المحددة، والتعبئة الصلبة، والتعبئة المتدرجة، وشفافية ألفا، والتحكم في الترتيب Z للأشكال المتداخلة.
---
## أضف مخططًا مستطيلًا

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) وقم بتكوين شكله الهندسي.
1. أضف [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## املأ المستطيل بلون ثابت أو متدرج

تتضمن أمثلة المستطيل ما يلي:

- `createRectangleFilled` للحصول على تعبئة صلبة باستخدام `Color.getRed()`
- `addDrawingWithGradientFill` للتعبئة `GradientAxialShading`

## استخدم شفافية ألفا

`createRectangleWithAlphaColorChannel` يطبق الألوان الشفافة باستخدام `Color.fromArgb(...)` بحيث تظل المستطيلات المتداخلة مرئية.

## التحكم بالترتيب z للمستطيلات

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. قم بتعيين حجم [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المطلوب.
1. أضف أشكال [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) التي تم تكوينها إلى الصفحة المستهدفة بالترتيب z المطلوب.
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
