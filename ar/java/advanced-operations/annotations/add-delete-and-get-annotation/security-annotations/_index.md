---
title: التعليقات التوضيحية الأمنية باستخدام Java
linktitle: التعليقات التوضيحية الأمنية
type: docs
weight: 75
url: /ar/java/security-annotations/
description: تعلم كيفية وضع علامة على النص للحجب، وتطبيق تعليقات الحجب، وحجب المناطق المختارة من الصفحات في ملفات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف محتوى PDF الحساس في Java باستخدام التعليقات التوضيحية الأمنية.
Abstract: تشرح هذه المقالة كيفية العمل مع تعليقات الحذف في مستندات PDF باستخدام Aspose.PDF for Java. تغطي وضع علامات على النص المطابق باستخدام تعليقات الحذف، تطبيق الحذف بشكل دائم، وحذف المناطق المحددة بناءً على مستطيلات وضع الصور المكتشفة.
---
سير عمل تعليقات الأمان في هذا القسم يركز على إعداد وتطبيق الحذف على محتوى PDF الحساس.

## تمييز النص باستخدام تعليقات الحذف

استخدم هذا المثال عندما يجب تغطية النص المطابق بتعليقات الحذف قبل تطبيق الحذف بشكل دائم.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن النص المستهدف وأنشئ كائنًا من الفئة [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) لكل تطابق.
1. اضبط مظهر الحجب واحفظ المستند.

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

## تطبيق الحجب الموجودة

هذا المثال يطبق بشكل دائم تعليقات الحجب التي موجودة بالفعل على الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع التعليقات من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. استدعِ `redact()` على كل ملاحظة تم جمعها واحفظ الملف المحدث.

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

## إخفاء منطقة مختارة من الصفحة

استخدم هذا النهج عندما يتم تحديد المحتوى المستهدف حسب الموقع بدلاً من مطابقة النص.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اكتشف المستطيل المستهدف على الصفحة، على سبيل المثال من موضع صورة.
1. أنشئ كائنًا من الفئة [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) لتلك المنطقة واحفظ المستند.

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

## مواضيع التعليقات التوضيحية ذات الصلة

- [التعليقات التفاعلية](/pdf/ar/java/interactive-annotations/)
- [تعليقات التوسيم](/pdf/ar/java/markup-annotations/)
- [تعليقات الأشكال](/pdf/ar/java/shape-annotations/)
- [ملاحظات النص](/pdf/ar/java/text-based-annotations/)
- [ملاحظات العلامة المائية](/pdf/ar/java/watermark-annotations/)
- [استيراد وتصدير الملاحظات](/pdf/ar/java/import-export-annotations/)
