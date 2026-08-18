---
title: التعليقات التوضيحية للشكل عبر Java
linktitle: التعليقات التوضيحية للأشكال
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية المربعة والدائرة والمضلعة والمتعددة الخطوط وفحصها وحذفها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية الهندسية لملفات PDF في Java
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية الهندسية وفحصها وإزالتها في مستندات PDF باستخدام Java. وهو يغطي التعليقات التوضيحية المربعة والدائرة والمضلعة والمتعددة الخطوط مع تكوين اللون والعتامة والنوافذ المنبثقة والنقطة.
---
## إضافة التعليقات التوضيحية للشكل

1. افتح ملف PDF المُدخل واختر الصفحة والمستطيل الذي سيحتوي على التعليق التوضيحي للشكل.
2. قم بإنشاء تعليق توضيحي للشكل المطلوب، ثم قم بتعيين عنوانه وألوانه وعتامةه ونقاطه عند الحاجة.
3. أضف التعليق التوضيحي إلى الصفحة واحفظ ملف PDF المعدل.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```
