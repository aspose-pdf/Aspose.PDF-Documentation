---
title: إضافة أشكال دائرية إلى PDF في Java
linktitle: أضف دائرة
type: docs
weight: 20
url: /java/add-circle/
description: تعرف على كيفية رسم الأشكال الدائرية وتعبئتها في ملفات PDF بلغة Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكالًا دائرية في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال دائرية إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي رسم الخطوط العريضة للدائرة، وملء الدوائر بالألوان، ووضع النص داخل شكل دائرة.
---
## إضافة مخطط دائرة

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [الدائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) وقم بتكوين شكله الهندسي.
1. أضف [الدائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. قم بتعيين خصائص الشكل التي يتطلبها المثال، بما في ذلك [اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## أضف دائرة مليئة بالنص

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [الدائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) وقم بتكوين شكله الهندسي.
1. أضف [الدائرة](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. قم بتعيين خصائص الشكل التي يتطلبها المثال، بما في ذلك [اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) و[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
