---
title: مثال على Hello World باستخدام Java
linktitle: مرحبا العالم المثال
type: docs
weight: 20
url: /java/hello-world-example/
description: يوضح هذا النموذج كيفية إنشاء مستند PDF بسيط بنص Hello World المصمم باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مثال Hello World عبر Java
Abstract: توفر هذه المقالة مثال Hello World لـ Aspose.PDF لـ Java. يقوم المثال بإنشاء مستند PDF جديد، وإضافة صفحة، وإنشاء TextFragment بموضع وخط وألوان مخصصة، وإلحاق النص بالصفحة باستخدام TextBuilder، وحفظ النتيجة كملف PDF.
---
يعد مثال "Hello World" هو أقصر طريق لفهم سير العمل الأساسي لإنشاء ملف PDF. في هذه المقالة، يقوم المثال بإنشاء ملف PDF جديد، ووضع جزء من النص المصمم على الصفحة، وحفظ ملف الإخراج.

يتبع مثال Java الخطوات التالية:

1. قم بإنشاء كائن [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) بالنص `Hello, world!`.
1. قم بتعيين [الموضع](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/) والخط وحجم الخط ولون الخلفية ولون المقدمة من خلال الجزء [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. قم بإنشاء [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) للصفحة.
1. قم بإلحاق [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) بـ [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ ملف PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

يعتمد كود Java التالي على `GetStartedExamples.java`.

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
