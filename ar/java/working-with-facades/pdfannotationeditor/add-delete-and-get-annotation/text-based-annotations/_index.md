---
title: التعليقات التوضيحية القائمة على النص باستخدام Java
linktitle: التعليقات التوضيحية النصية
type: docs
weight: 10
url: /ar/java/pdfannotationeditor-class/text-based-annotations/
description: تعرف على كيفية إضافة وفحص وحذف التعليقات التوضيحية للنص، والنص الحر، وتعليقات التشطيب في مستندات PDF باستخدام Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية النصية في PDF باستخدام Java
Abstract: تُوضح هذه المقالة كيفية إنشاء وقراءة وإزالة التعليقات التوضيحية القائمة على النص في مستندات PDF باستخدام Java. وتغطي التعليقات التوضيحية النصية، وتعليقات النص الحر، وتعليقات التشطيب بناءً على أمثلة Java.
---
## إضافة تعليق توضيحي نصي

1. افتح ملف PDF الإدخال وحدد الصفحة التي يجب وضع التعليق النصي عليها.
2. إنشاء `TextAnnotation`, حدد مستطيله، واضبط عنوانه، وموضوعه، وعلاماته، ولونه.
3. أضف التعليق إلى الصفحة واحفظ المستند المحدث.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## إضافة ملاحظة نصية حرة

1. حمِّل ملف PDF المصدر وحدد الصفحة المستهدفة والمستطيل للملاحظة النصية الحرة.
2. إنشاء `FreeTextAnnotation`, تهيئة المظهر الافتراضي وضبط العنوان واللون.
3. أضف التعليق إلى الصفحة واحفظ النتيجة.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
