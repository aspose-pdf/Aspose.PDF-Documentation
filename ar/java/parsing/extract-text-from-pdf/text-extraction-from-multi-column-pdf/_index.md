---
title: تحسين استخراج النص من ملفات PDF متعددة الأعمدة
linktitle: استخراج النص من ملفات PDF متعددة الأعمدة
type: docs
weight: 30
url: /ar/java/text-extraction-from-multi-column-pdf/
description: تعلم تقنيات تحسين استخراج النص من تخطيطات PDF متعددة الأعمدة باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
غالبًا ما تتطلب التخطيطات متعددة الأعمدة معالجة إضافية لتحسين ترتيب القراءة وجودة الاستخراج.

## استخراج النص بعد تقليل حجم الخط

تقوم هذه التقنية بتحديث أحجام خطوط Font لـ TextFragment، تحفظ المستند المعدل في الذاكرة، ثم تستخرج النص من النتيجة المحوَّلة.

1. افتح ملف PDF المصدر في [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) وزر جميع صفحات المستند لجمع الكائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. مرّ على المقاطع وتقليل حجم الخط لكل منها بنسبة النسبة المطلوبة بحيث يمكن تطبيع تخطيط الأعمدة الكثيفة قبل الاستخراج.
1. احفظ المعدل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) إلى تدفق بايتات في الذاكرة.
1. أعد فتح ثانية [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) من تلك الذاكرة المؤقتة.
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)، زُر جميع صفحات المستند المحول، واكتب النص المستخرج إلى ملف الإخراج.

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

## استخراج النص مع عامل مقياس

استخدم `TextExtractionOptions` في وضع التنسيق النقي وضبط عامل المقياس لتصاميم ذات أعمدة كثيفة.

1. افتح ملف PDF المصدر في [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) للاستخراج الكامل للمستند.
1. أنشئ كائنًا من الفئة [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) في وضع التنسيق النقي بحيث يتم استخدام سلوك الاستخراج الحساس للتنسيق.
1. عيّن عامل المقياس وتطبيق خيارات الاستخراج على absorber قبل زيارة الصفحات.
1. زُر جميع صفحات المستند واكتب النص المستخرج إلى ملف الإخراج.

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
