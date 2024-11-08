---
title: تدوير النص داخل PDF
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /ar/java/rotate-text-inside-pdf/
description: تعلم طرق مختلفة لتدوير النص في PDF. يتيح لك Aspose.PDF تدوير النص بأي زاوية، تدوير جزء من النص أو فقرة كاملة.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تدوير النص داخل PDF باستخدام خاصية التدوير

باستخدام طريقة [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) لفئة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)، يمكنك تدوير النص بزوايا مختلفة. يمكن استخدام تدوير النص في سيناريوهات مختلفة لإنشاء المستندات. يمكنك تحديد زاوية الدوران بالدرجات لتدوير النص حسب متطلباتك. يرجى التحقق من السيناريوهات المختلفة التالية، التي يمكنك من خلالها تنفيذ تدوير النص.

## تنفيذ التدوير باستخدام TextFragment وTextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // تهيئة كائن المستند
        Document pdfDocument = new Document();
        // الحصول على الصفحة المحددة
        Page pdfPage = pdfDocument.getPages().add();
        // إنشاء جزء نصي
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // تعيين خصائص النص
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // إنشاء جزء نصي مدوّر
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // تعيين خصائص النص
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // إنشاء جزء نصي مدوّر
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // تعيين خصائص النص
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // إنشاء كائن TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // إلحاق الجزء النصي بصفحة PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // حفظ المستند
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## تنفيذ التدوير باستخدام TextParagraph و TextBuilder (القطع الدوارة)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // تهيئة كائن المستند
    Document pdfDocument = new Document();
    // الحصول على صفحة معينة
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // إنشاء جزء نصي
    TextFragment textFragment1 = new TextFragment("نص مدوّر");
    // تعيين خصائص النص
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // تعيين التدوير
    textFragment1.getTextState().setRotation(45);

    // إنشاء جزء نصي
    TextFragment textFragment2 = new TextFragment("النص الرئيسي");
    // تعيين خصائص النص
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // إنشاء جزء نصي
    TextFragment textFragment3 = new TextFragment("نص مدوّر آخر");
    // تعيين خصائص النص
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // تعيين التدوير
    textFragment3.getTextState().setRotation(-45);

    // إلحاق الأجزاء النصية بالفقرة
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // إلحاق الفقرة النصية بصفحة الـ PDF
    textBuilder.appendParagraph(paragraph);
    // حفظ المستند
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## تنفيذ التدوير باستخدام TextFragment و Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // تهيئة كائن الوثيقة
    Document pdfDocument = new Document();
    // الحصول على صفحة معينة
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // إنشاء جزء نصي
    TextFragment textFragment1 = new TextFragment("main text");
    // ضبط خصائص النص
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // إنشاء جزء نصي
    TextFragment textFragment2 = new TextFragment("rotated text");

    // ضبط خصائص النص
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // ضبط التدوير
    textFragment2.getTextState().setRotation(315);

    // إنشاء جزء نصي
    TextFragment textFragment3 = new TextFragment("rotated text");
    // ضبط خصائص النص
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // ضبط التدوير
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // حفظ الوثيقة
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## تنفيذ التدوير باستخدام TextParagraph و TextBuilder (تدوير الفقرة بالكامل)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // تهيئة كائن المستند
    Document pdfDocument = new Document();
    // الحصول على صفحة معينة
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // تحديد التدوير
        paragraph.setRotation(i * 90 + 45);
        // إنشاء جزء النص
        TextFragment textFragment1 = new TextFragment("نص الفقرة");
        // إنشاء جزء النص
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // إنشاء جزء النص
        TextFragment textFragment2 = new TextFragment("السطر الثاني من النص");
        // ضبط خصائص النص
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // إنشاء جزء النص
        TextFragment textFragment3 = new TextFragment("والمزيد من النص...");
        // ضبط خصائص النص
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // إنشاء كائن TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // إلحاق جزء النص بصفحة PDF
        textBuilder.appendParagraph(paragraph);
    }
    // حفظ المستند
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```