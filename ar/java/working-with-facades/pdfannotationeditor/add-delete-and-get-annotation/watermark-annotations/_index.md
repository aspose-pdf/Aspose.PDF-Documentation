---
title: التعليقات التوضيحية للعلامة المائية باستخدام Java
linktitle: التعليقات التوضيحية للعلامة المائية
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للعلامة المائية وفحصها وحذفها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية للعلامة المائية في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للعلامة المائية وفحصها وإزالتها في مستندات PDF باستخدام Java. ويغطي إضافة تعليق توضيحي للعلامة المائية النصية مع حالة النص المخصصة والتعتيم، وقراءة مناطق التعليقات التوضيحية للعلامة المائية الموجودة، وحذف التعليقات التوضيحية للعلامة المائية.
---
## إضافة تعليق توضيحي للعلامة المائية

1. افتح ملف PDF المُدخل وحدد المستطيل الذي سيتم وضع التعليق التوضيحي للعلامة المائية فيه.
2. أنشئ `WatermarkAnnotation` وأضفه إلى الصفحة وقم بتكوين حالة نص العلامة المائية والتعتيم.
3. قم بتطبيق خطوط نص العلامة المائية واحفظ ملف PDF المعدل.

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
