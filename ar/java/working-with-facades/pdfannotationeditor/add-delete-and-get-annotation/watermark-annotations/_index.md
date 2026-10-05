---
title: تعليقات العلامة المائية باستخدام Java
linktitle: تعليقات العلامة المائية
type: docs
weight: 70
url: /ar/java/pdfannotationeditor-class/watermark-annotations/
description: تعلم كيفية إضافة، فحص، وحذف تعليقات العلامة المائية في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: التعامل مع تعليقات العلامة المائية في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء، فحص، وإزالة تعليقات العلامة المائية في مستندات PDF باستخدام Java. تغطي إضافة تعليق علامة مائية نصي مع حالة نص مخصصة وشفافية، قراءة مناطق تعليقات العلامة المائية الحالية، وحذف تعليقات العلامة المائية.
---
## إضافة تعليق علامة مائية

1. افتح ملف PDF الإدخال وحدد المستطيل الذي ستوضع فيه تعليقة العلامة المائية.
2. أنشئ `WatermarkAnnotation`، أضفه إلى الصفحة، واضبط حالة نص العلامة المائية والشفافية.
3. طبّق أسطر نص العلامة المائية واحفظ ملف PDF المعدل.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

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
