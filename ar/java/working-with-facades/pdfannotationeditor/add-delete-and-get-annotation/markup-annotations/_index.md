---
title: التعليقات التوضيحية الترميزية باستخدام Java
linktitle: التعليقات التوضيحية الترميزية
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية المميزة والتسطير والمتعرجة والشطب وفحصها وحذفها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية الترميزية في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للعلامات النصية وفحصها وإزالتها في مستندات PDF باستخدام Java. ويغطي التعليقات التوضيحية المميزة والتسطير والمتعرج والشطب بناءً على أمثلة Java الخاصة بالمستودع.
---
## أضف تعليقات توضيحية مميزة أو مسطرة أو متعرجة أو مشطبة

1. افتح ملف PDF المُدخل وحدد منطقة الصفحة التي يجب أن يظهر فيها التعليق التوضيحي للعلامة.
2. قم بإنشاء نوع التعليق التوضيحي المطلوب وقم بتكوين بيانات التعريف أو الخصائص المرئية الخاصة به.
3. أضف التعليق التوضيحي إلى مجموعة الصفحات واحفظ المستند.

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
