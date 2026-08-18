---
title: الشروح الأمنية باستخدام جافا
linktitle: الشروح الأمنية
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: تعرف على كيفية وضع علامة على النص للتنقيح، وتطبيق التعليقات التوضيحية للتنقيح، وتنقيح مناطق الصفحة المحددة في ملفات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتنقيح محتوى PDF الحساس في Java باستخدام التعليقات التوضيحية الأمنية
Abstract: تشرح هذه المقالة كيفية التعامل مع تعليقات التنقيح التوضيحية في مستندات PDF باستخدام Java. وهو يغطي وضع علامات على النص المطابق باستخدام تعليقات التنقيح التوضيحية، وتطبيق التنقيح بشكل دائم، وتنقيح المناطق المحددة بناءً على مستطيلات موضع الصورة المكتشفة.
---
## وضع علامة على النص للتنقيح

1. قم بتحميل ملف PDF وابحث في جميع الصفحات عن النص الذي يجب تنقيحه.
2. قم بإنشاء `RedactionAnnotation` لكل جزء نص مطابق وقم بتكوين مظهره.
3. أضف تعليقات التنقيح التوضيحية إلى صفحاتها واحفظ المستند.

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
