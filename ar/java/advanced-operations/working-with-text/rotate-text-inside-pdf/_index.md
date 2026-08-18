---
title: تدوير نص PDF في جافا
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: تعرف على كيفية تدوير أجزاء النص والفقرات داخل مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتدوير أجزاء النص والفقرات في مستندات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية تدوير النص في مستندات PDF باستخدام Aspose.PDF لـ Java. فهو يوضح كيفية تدوير أجزاء النص الفردية، وإنشاء فقرات تحتوي على أسطر تم تدويرها، وتدوير فقرات النص الكاملة لسيناريوهات تخطيط مختلفة.
---
يتيح لك Aspose.PDF for Java تدوير أجزاء النص الفردية بالإضافة إلى فقرات النص بأكملها.

## تدوير أجزاء النص الفردية

استخدم هذا المثال عندما يجب أن تستخدم أجزاء النص المتعددة الموجودة على نفس السطر زوايا دوران مختلفة.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. قم بإنشاء أجزاء نصية بقيم التدوير المطلوبة.
1. ألحقها بـ `TextBuilder` واحفظ النتيجة.

```java
public static void rotateTextInsidePdf1(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           TextFragment textFragment1 = new TextFragment("main text");
           textFragment1.setPosition(new Position(100, 600));
           textFragment1.getTextState().setFontSize(12);
           textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

           TextFragment textFragment2 = new TextFragment("rotated text");
           textFragment2.setPosition(new Position(200, 600));
           textFragment2.getTextState().setFontSize(12);
           textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment2.getTextState().setRotation(45);

           TextFragment textFragment3 = new TextFragment("rotated text");
           textFragment3.setPosition(new Position(300, 600));
           textFragment3.getTextState().setFontSize(12);
           textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
           textFragment3.getTextState().setRotation(90);

           TextBuilder builder = new TextBuilder(page);
           builder.appendText(textFragment1);
           builder.appendText(textFragment2);
           builder.appendText(textFragment3);

           document.save(outputFile.toString());
       }
   }
```

## تدوير الأسطر داخل فقرة نصية

استخدم هذا المثال عندما يجب أن تحتوي الفقرة على خطوط عادية ومستديرة.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. أنشئ `TextParagraph` وألحق أجزاء النص بإعدادات تدوير مختلفة.
1. أضف الفقرة إلى الصفحة واحفظ المستند.

```java
public static void rotateTextInsidePdf2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));

        TextFragment textFragment1 = new TextFragment("rotated text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setRotation(45);

        TextFragment textFragment2 = new TextFragment("main text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment3 = new TextFragment("another rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(-45);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## تدوير أجزاء الفقرة بدون مواضع واضحة

استخدم هذا المثال عندما يجب إضافة نص تمت استدارته من خلال تدفق فقرة الصفحة العادي.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. قم بإنشاء عدة أجزاء نصية بقيم دوران مختلفة.
1. أضفها إلى مجموعة فقرات الصفحة واحفظ ملف PDF.

```java
public static void rotateTextInsidePdf3(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(315);

        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(270);

        page.getParagraphs().add(textFragment1);
        page.getParagraphs().add(textFragment2);
        page.getParagraphs().add(textFragment3);

        document.save(outputFile.toString());
    }
}
```

## تدوير الفقرات كاملة

استخدم هذا المثال عندما يجب تدوير كتلة الفقرة بأكملها بينما يحتفظ كل سطر بالتصميم المشترك.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. أنشئ عدة كائنات `TextParagraph` بالتدوير على مستوى الفقرة.
1. أنشئ الأسطر باستخدام أسلوب مساعد مشترك وألحقها واحفظ المستند.

```java
public static void rotateTextInsidePdf4(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        for (int i = 0; i < 4; i++) {
            TextParagraph paragraph = new TextParagraph();
            paragraph.setPosition(new Position(200, 600));
            paragraph.setRotation(i * 90 + 45);

            TextFragment textFragment1 = rotatedLine("Paragraph Text", false);
            TextFragment textFragment2 = rotatedLine("Second line of text", false);
            TextFragment textFragment3 = rotatedLine("And some more text...", true);

            paragraph.appendLine(textFragment1);
            paragraph.appendLine(textFragment2);
            paragraph.appendLine(textFragment3);

            TextBuilder builder = new TextBuilder(page);
            builder.appendParagraph(paragraph);
        }

        document.save(outputFile.toString());
    }
}

private static TextFragment rotatedLine(String text, boolean underline) {
    TextFragment fragment = new TextFragment(text);
    fragment.getTextState().setFontSize(12);
    fragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    fragment.getTextState().setBackgroundColor(Color.getLightGray());
    fragment.getTextState().setForegroundColor(Color.getBlue());
    fragment.getTextState().setUnderline(underline);
    return fragment;
}
```
