---
title: إضافة أشكال دائرة إلى PDF في Java
linktitle: إضافة دائرة
type: docs
weight: 20
url: /ar/java/add-circle/
description: تعرّف على كيفية رسم وتعبئة أشكال الدائرة في ملفات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال الدائرة في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال دائرة إلى مستندات PDF باستخدام Aspose.PDF for Java. وتغطي رسم حدود الدائرة، وتعبئة الدوائر باللون، ووضع النص داخل شكل الدائرة.
---
## إضافة حدود دائرة

1. أنشئ PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى الوثيقة.
1. أنشئ كائنًا من الفئة [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية وإضافتها إلى الصفحة.
1. أنشئ كائنًا من الفئة [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) الشكل واضبط هندسته.
1. أضف [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. عيّن خصائص الشكل المطلوبة في المثال، بما في ذلك [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## إضافة دائرة مملوءة بالنص

1. أنشئ PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى الوثيقة.
1. أنشئ كائنًا من الفئة [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية وإضافتها إلى الصفحة.
1. أنشئ كائنًا من الفئة [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) الشكل واضبط هندسته.
1. أضف [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) إلى [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. عيّن خصائص الشكل المطلوبة في المثال، بما في ذلك [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) و [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
