---
title: تعليقات توضيحية للعلامة المائية باستخدام Java
linktitle: تعليقات توضيحية للعلامة المائية
type: docs
weight: 70
url: /ar/java/watermark-annotations/
description: تعلم كيفية إضافة وفحص وحذف تعليقات توضيحية للعلامة المائية في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: العمل مع تعليقات توضيحية للعلامة المائية في ملفات PDF باستخدام Java.
Abstract: تشرح هذه المقالة كيفية إنشاء وفحص وإزالة تعليقات توضيحية للعلامة المائية في مستندات PDF باستخدام Aspose.PDF for Java. وتغطي إضافة تعليقة توضيحية للعلامة المائية نصية مع حالة نص مخصصة وتعتيم، قراءة مناطق التعليقات التوضيحية للعلامة المائية الحالية، وحذف تعليقات العلامة المائية.
---
تسمح لك تعليقات العلامة المائية بوضع محتوى متراكب قابل لإعادة الاستخدام على صفحة مع الاستمرار في إدارته عبر مجموعة التعليقات التوضيحية.

## إضافة تعليقة علامة مائية

استخدم هذا المثال عندما تحتاج إلى تعليقة علامة مائية نصية مع إعدادات Font مخصصة وتعتيم.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) وأضفه إلى الصفحة.
1. اضبط [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)، نص العلامة المائية، والعتامة، ثم احفظ المستند.

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

## احصل على تعليقات العلامة المائية

يمسح هذا المثال مجموعة التعليقات التوضيحية ويطبع المستطيل الخاص بكل تعليق توضيحي علامة مائية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على التعليقات التوضيحية في الصفحة المستهدفة.
1. صفِّ التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` واطبع مستطيلاتها.

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

## حذف تعليقات العلامة المائية

استخدم هذا الأسلوب عندما يجب إزالة تعليقات العلامة المائية الموجودة من المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
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

## المواضيع المتعلقة بالتعليقات التوضيحية

- [التعليقات التوضيحية التفاعلية](/pdf/ar/java/interactive-annotations/)
- [تعليقات توضيحية للعلامات](/pdf/ar/java/markup-annotations/)
- [تعليقات توضيحية للأمان](/pdf/ar/java/security-annotations/)
- [تعليقات توضيحية للأشكال](/pdf/ar/java/shape-annotations/)
- [التعليقات التوضيحية النصية](/pdf/ar/java/text-based-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/ar/java/import-export-annotations/)
