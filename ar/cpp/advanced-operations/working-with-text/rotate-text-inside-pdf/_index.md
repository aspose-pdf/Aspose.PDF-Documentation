---
title: تدوير النص داخل PDF باستخدام C++
linktitle: تدوير النص داخل PDF
type: docs
weight: 50
url: /ar/cpp/rotate-text-inside-pdf/
description: تعرف على طرق مختلفة لتدوير النص إلى PDF. يتيح لك Aspose.PDF تدوير النص بأي زاوية، تدوير جزء من النص أو فقرة كاملة.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تدوير النص داخل PDF باستخدام خاصية الدوران

باستخدام خاصية Rotation لفئة [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)، يمكنك تدوير النص بزوايا مختلفة. يمكن استخدام تدوير النص في سيناريوهات مختلفة لإنشاء المستندات. يمكنك تحديد زاوية الدوران بالدرجات لتدوير النص حسب متطلباتك. يرجى التحقق من السيناريوهات المختلفة التالية، حيث يمكنك تنفيذ تدوير النص.

## تنفيذ الدوران باستخدام TextFragment وTextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Initialize document object
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();
    // Create text fragment
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Set text properties
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Create rotated text fragment
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Set text properties
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Create rotated text fragment
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Set text properties
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Append the text fragment to the PDF page
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Save document
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## تنفيذ الدوران باستخدام TextParagraph و TextBuilder (القطع الدوارة)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // تهيئة كائن المستند
    auto document = MakeObject<Document>();
    // الحصول على صفحة معينة
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // إنشاء جزء نصي
    auto textFragment1 = MakeObject<TextFragment>("نص دوار");
    // تعيين خصائص النص
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // تعيين الدوران
    textFragment1->get_TextState()->set_Rotation(45);

    // إنشاء جزء نصي
    auto textFragment2 = MakeObject<TextFragment>("النص الرئيسي");
    // تعيين خصائص النص
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // إنشاء جزء نصي
    auto textFragment3 = MakeObject<TextFragment>("نص دوار آخر");
    // تعيين خصائص النص
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // تعيين الدوران
    textFragment3->get_TextState()->set_Rotation(-45);

    // إلحاق الأجزاء النصية بالفقرة
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // إنشاء كائن TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // إلحاق الفقرة النصية بصفحة PDF
    textBuilder->AppendParagraph(paragraph);
    // حفظ المستند
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## تنفيذ التدوير باستخدام TextFragment وPage.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // تهيئة كائن المستند
    auto document = MakeObject<Document>();
    // الحصول على صفحة معينة
    auto page = document->get_Pages()->Add();
    // إنشاء جزء نصي
    auto textFragment1 = MakeObject<TextFragment>("النص الرئيسي");
    // تعيين خصائص النص
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // إنشاء جزء نصي
    auto textFragment2 = MakeObject<TextFragment>("نص مدور");

    // تعيين خصائص النص
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // تعيين التدوير
    textFragment2->get_TextState()->set_Rotation(315);

    // إنشاء جزء نصي
    auto textFragment3 = MakeObject<TextFragment>("نص مدور");
    // تعيين خصائص النص
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // تعيين التدوير
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // حفظ المستند
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## تنفيذ التدوير باستخدام TextParagraph و TextBuilder (تدوير الفقرة كاملة)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // تهيئة كائن الوثيقة
    auto document = MakeObject<Document>();
    // الحصول على الصفحة المعينة
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // تحديد التدوير
        paragraph->set_Rotation(i * 90 + 45);
        // إنشاء جزء نصي
        auto textFragment1 = MakeObject<TextFragment>("نص الفقرة");
        // إنشاء جزء نصي
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // إنشاء جزء نصي
        auto textFragment2 = MakeObject<TextFragment>("السطر الثاني من النص");
        // تعيين خصائص النص
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // إنشاء جزء نصي
        auto textFragment3 = MakeObject<TextFragment>("والمزيد من النص...");
        // تعيين خصائص النص
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // إنشاء كائن TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // إلحاق الجزء النصي بصفحة PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // حفظ الوثيقة
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```