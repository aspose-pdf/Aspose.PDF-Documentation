---
title: تحسين استخراج النص من ملفات PDF متعددة الأعمدة
linktitle: استخراج النص من ملفات PDF متعددة الأعمدة
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: تعرّف على تقنيات تحسين استخراج النص من تخطيطات PDF متعددة الأعمدة باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
غالبًا ما تتطلب التخطيطات متعددة الأعمدة معالجة إضافية لتحسين ترتيب القراءة وجودة الاستخراج.

## استخراج النص بعد تقليل حجم الخط

تقوم هذه التقنية بتحديث أحجام خطوط أجزاء النص، وحفظ المستند المعدل في الذاكرة، ثم استخراج النص من النتيجة المحولة.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextFragmentAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) وقم بزيارة كافة صفحات المستندات لتجميع كائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. قم بالتكرار عبر الأجزاء وتقليل حجم كل خط حسب النسبة المطلوبة حتى يمكن تطبيع تخطيط العمود الكثيف قبل الاستخراج.
1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المعدل في دفق بايت في الذاكرة.
1. أعد فتح [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ثانٍ من مخزن الذاكرة المؤقت هذا.
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)، وقم بزيارة جميع صفحات المستند المحول، واكتب النص المستخرج إلى ملف الإخراج.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## استخراج النص مع عامل الحجم

استخدم `TextExtractionOptions` في وضع التنسيق النقي وقم بضبط عامل القياس للتخطيطات ذات الأعمدة الثقيلة.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) لاستخراج المستند بالكامل.
1. قم بإنشاء [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) في وضع التنسيق النقي بحيث يتم استخدام سلوك الاستخراج الحساس للتخطيط.
1. اضبط عامل القياس وقم بتطبيق خيارات الاستخراج على الممتص قبل زيارة الصفحات.
1. قم بزيارة جميع صفحات المستند واكتب النص المستخرج إلى ملف الإخراج.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
