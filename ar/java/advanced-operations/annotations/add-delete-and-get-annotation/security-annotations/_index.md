---
title: الشروح الأمنية باستخدام جافا
linktitle: الشروح الأمنية
type: docs
weight: 75
url: /java/security-annotations/
description: تعرف على كيفية وضع علامة على النص للتنقيح، وتطبيق التعليقات التوضيحية للتنقيح، وتنقيح مناطق الصفحة المحددة في ملفات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتنقيح محتوى PDF الحساس في Java باستخدام التعليقات التوضيحية الأمنية.
Abstract: تشرح هذه المقالة كيفية التعامل مع تعليقات التنقيح التوضيحية في مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي وضع علامات على النص المطابق باستخدام تعليقات التنقيح التوضيحية، وتطبيق التنقيح بشكل دائم، وتنقيح المناطق المحددة بناءً على مستطيلات موضع الصورة المكتشفة.
---
تركز عمليات سير عمل التعليقات التوضيحية للأمان في هذا القسم على إعداد التنقيح وتطبيقه على محتوى PDF الحساس.

## وضع علامة على النص مع التعليقات التوضيحية للتنقيح

استخدم هذا المثال عندما يجب تغطية النص المطابق بتعليقات التنقيح التوضيحية قبل تطبيق التنقيح نهائيًا.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن النص المستهدف وقم بإنشاء [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) لكل تطابق.
1. قم بتكوين مظهر التنقيح واحفظ المستند.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## تطبيق التنقيحات الموجودة

يطبق هذا المثال تعليقات التنقيح التوضيحية الموجودة بالفعل على الصفحة بشكل دائم.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. اتصل بـ `redact()` على كل تعليق توضيحي تم جمعه واحفظ الملف المحدث.

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## قم بتنقيح منطقة الصفحة المحددة

استخدم هذا الأسلوب عندما يتم تحديد المحتوى المستهدف حسب الموضع بدلاً من مطابقة النص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اكتشف المستطيل المستهدف في الصفحة، على سبيل المثال من موضع الصورة.
1. أنشئ [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) لتلك المنطقة واحفظ المستند.

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة بالتعليقات

- [التعليقات التوضيحية التفاعلية](/pdf/java/interactive-annotations/)
- [التعليقات التوضيحية الترميزية](/pdf/java/markup-annotations/)
- [التعليقات التوضيحية للشكل](/pdf/java/shape-annotations/)
- [التعليقات التوضيحية النصية](/pdf/java/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/pdf/java/watermark-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/java/import-export-annotations/)
