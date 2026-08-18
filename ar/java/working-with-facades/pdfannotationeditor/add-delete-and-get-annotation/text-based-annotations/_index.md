---
title: التعليقات التوضيحية المستندة إلى النص باستخدام Java
linktitle: التعليقات التوضيحية النصية
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: تعرف على كيفية إضافة وفحص وحذف النص والنص الحر والشروح التوضيحية في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية النصية بتنسيق PDF في Java
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية المستندة إلى النص وقراءتها وإزالتها في مستندات PDF باستخدام Java. وهو يغطي التعليقات التوضيحية النصية، والتعليقات التوضيحية النصية الحرة، والتعليقات التوضيحية المشطبة استنادًا إلى تطبيقات أمثلة Java.
---
## إضافة تعليق توضيحي للنص

1. افتح ملف PDF المُدخل واستهدف الصفحة التي يجب وضع التعليق التوضيحي النصي فيها.
2. أنشئ `TextAnnotation` وحدد مستطيله وعيّن عنوانه وموضوعه وأعلامه ولونه.
3. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند المحدث.

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

## أضف تعليقًا توضيحيًا نصيًا مجانيًا

1. قم بتحميل ملف PDF المصدر وحدد الصفحة المستهدفة والمستطيل للملاحظة النصية المجانية.
2. قم بإنشاء `FreeTextAnnotation`، وقم بتهيئة مظهره الافتراضي، وقم بتعيين العنوان واللون.
3. أضف التعليق التوضيحي إلى الصفحة واحفظ النتيجة.

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
