---
title: تعليقات الأمان باستخدام Java
linktitle: تعليقات الأمان
type: docs
weight: 60
url: /ar/java/pdfannotationeditor-class/security-annotations/
description: تعلم كيفية وضع علامة على النص للحذف، وتطبيق تعليقات الحذف، وحذف مناطق الصفحات المختارة في ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: حذف محتوى PDF الحساس في Java باستخدام تعليقات الأمان
Abstract: تشرح هذه المقالة كيفية العمل مع تعليقات الحذف في مستندات PDF باستخدام Java. تغطي وضع علامة على النص المتطابق بتعليقات الحذف، وتطبيق الحذف بشكل دائم، وحذف المناطق المختارة بناءً على مستطيلات وضع الصور المكتشفة.
---
## وضع علامة على النص للحذف

1. حمّل ملف PDF وابحث في جميع الصفحات عن النص الذي يجب حذفه.
2. إنشاء `RedactionAnnotation` لكل جزء نص متطابق وقم بتكوين مظهره.
3. أضف تعليقات الحذف إلى صفحاتها واحفظ المستند.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
