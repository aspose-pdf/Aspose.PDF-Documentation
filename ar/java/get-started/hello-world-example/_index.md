---
title: مثال على Hello World باستخدام Java
linktitle: مثال Hello World
type: docs
weight: 20
url: /ar/java/hello-world-example/
description: هذا المثال يوضح كيفية إنشاء مستند PDF بسيط بنص Hello World مُنسق باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مثال Hello World عبر Java
Abstract: هذه المقالة توفر مثال Hello World لبرنامج Aspose.PDF for Java. يقوم المثال بإنشاء مستند PDF جديد، ويضيف صفحة، وينشئ TextFragment بموقع مخصص، وخط، وألوان، ويضيف النص إلى الصفحة باستخدام TextBuilder، ويحفظ النتيجة كملف PDF.
---
مثال \"Hello World\" هو أقصر طريق لفهم سير عمل إنشاء PDF الأساسي. في هذه المقالة، يقوم المثال بإنشاء PDF جديد، ويضع قطعة نصية منسقة على الصفحة، ويحفظ ملف الإخراج.

مثال Java يتبع الخطوات التالية:

1. إنشاء [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كائن.
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) مع النص `Hello, world!`.
1. تعيين [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), الخط، حجم الخط، لون الخلفية، ولون المقدمة عبر القطعة [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. إنشاء [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) للصفحة.
1. إلحاق الـ [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) إلى الـ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ ملف PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

الكود الجافا التالي مبني على `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
