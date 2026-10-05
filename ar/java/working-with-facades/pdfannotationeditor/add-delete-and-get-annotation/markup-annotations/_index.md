---
title: التعليقات التوضيحية باستخدام Java
linktitle: التعليقات التوضيحية
type: docs
weight: 20
url: /ar/java/pdfannotationeditor-class/markup-annotations/
description: تعرّف على كيفية إضافة وفحص وحذف تعليقات التظليل، والتسطير، والمتموجة، والخط المشطوب في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: التعامل مع التعليقات التوضيحية في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء وفحص وإزالة تعليقات النص التوضيحية في مستندات PDF باستخدام Java. وهي تغطي تعليقات التظليل، والتسطير، والمتموجة، والخط المشطوب استنادًا إلى أمثلة Java في المستودع.
---
## إضافة تعليقات تظليل، تسطير، متموجة أو شطب

1. افتح ملف PDF الإدخال وحدد منطقة الصفحة التي يجب أن تظهر فيها تعليقة العلامة التوضيحية.
2. أنشئ نوع التعليقة المطلوب واضبط بيانات التعريف الخاصة به أو خصائصه البصرية.
3. أضف التعليقة إلى مجموعة الصفحات واحفظ المستند.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
