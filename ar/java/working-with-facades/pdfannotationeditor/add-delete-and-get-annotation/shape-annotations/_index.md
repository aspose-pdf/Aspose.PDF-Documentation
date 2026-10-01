---
title: تعليقات الأشكال عبر Java
linktitle: تعليقات الأشكال
type: docs
weight: 40
url: /ar/java/pdfannotationeditor-class/shape-annotations/
description: تعلم كيفية إضافة وفحص وحذف تعليقات المربع والدائرة والمتعدد الحدود والخط المتعدد في مستندات PDF باستخدام Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: العمل مع تعليقات PDF الهندسية في Java
Abstract: تشرح هذه المقالة كيفية إنشاء وفحص وإزالة التعليقات الهندسية في مستندات PDF باستخدام Java. وتغطي تعليقات المربع والدائرة والمتعدد الحدود والخط المتعدد مع اللون والشفافية والنافذة المنبثقة وتكوين النقاط.
---
## إضافة تعليقات الأشكال

1. افتح ملف PDF المدخل واختر الصفحة والمستطيل اللذين سيحتويان على التعليق التوضيحي للشكل.
2. أنشئ التعليق التوضيحي للشكل المطلوب، ثم عيّن عنوانه وألوانه وشفافيته والنقاط عند الحاجة.
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
