---
title: التعليقات التوضيحية للعلامة المائية باستخدام Java
linktitle: التعليقات التوضيحية للعلامة المائية
type: docs
weight: 70
url: /java/watermark-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للعلامة المائية وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية للعلامة المائية في ملفات PDF باستخدام Java.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للعلامة المائية وفحصها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي إضافة تعليق توضيحي للعلامة المائية النصية مع حالة النص المخصصة والتعتيم، وقراءة مناطق التعليقات التوضيحية للعلامة المائية الموجودة، وحذف التعليقات التوضيحية للعلامة المائية.
---
تتيح لك التعليقات التوضيحية للعلامة المائية وضع محتوى متراكب قابل لإعادة الاستخدام على الصفحة مع الاستمرار في إدارته من خلال مجموعة التعليقات التوضيحية.

## إضافة تعليق توضيحي للعلامة المائية

استخدم هذا المثال عندما تحتاج إلى تعليق توضيحي للعلامة المائية النصية مع إعدادات الخط المخصصة والعتامة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [تعليقًا توضيحيًا للعلامة المائية](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) وأضفه إلى الصفحة.
1. قم بتكوين [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) ونص العلامة المائية والعتامة، ثم احفظ المستند.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## الحصول على التعليقات التوضيحية للعلامة المائية

يقوم هذا المثال بمسح مجموعة التعليقات التوضيحية وطباعة مستطيل كل تعليق توضيحي للعلامة المائية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. كرر من خلال التعليقات التوضيحية على الصفحة المستهدفة.
1. قم بتصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` واطبع مستطيلاتها.

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## حذف التعليقات التوضيحية للعلامة المائية

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية للعلامة المائية الموجودة من المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. احذف التعليقات التوضيحية المجمعة واحفظ ملف الإخراج.

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة بالتعليقات

- [التعليقات التوضيحية التفاعلية](/pdf/java/interactive-annotations/)
- [التعليقات التوضيحية الترميزية](/pdf/java/markup-annotations/)
- [التعليقات التوضيحية الأمنية](/pdf/java/security-annotations/)
- [التعليقات التوضيحية للشكل](/pdf/java/shape-annotations/)
- [التعليقات التوضيحية النصية](/pdf/java/text-based-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/java/import-export-annotations/)
