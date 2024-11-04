---
title: تنسيق النص داخل PDF باستخدام C++
linktitle: تنسيق النص داخل PDF
type: docs
weight: 30
url: /cpp/text-formatting-inside-pdf/
description: تشرح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حدود للنص، إضافة نص مسطر، إضافة حدود حول النص المضاف، محاذاة النص لمحتويات الصندوق العائم وما إلى ذلك.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إضافة مسافة بادئة للسطر إلى PDF

لإضافة مسافة بادئة للسطر إلى PDF، يستخدم Aspose.PDF لـ C++ خاصية [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) في فئة [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) وأيضًا يساعد مجموعات [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) و[Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).

الرجاء استخدام مقطع الشفرة التالي لاستخدام الخاصية:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("SubsequentIndent_out.pdf");


    // Create new document object
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول. قفز الثعلب البني السريع فوق الكلب الكسول.");

    // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"السطر2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"السطر3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"السطر4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"السطر5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## كيفية إضافة حدود للنص

يوضح مقطع الشيفرة التالي كيفية إضافة حدود لنص باستخدام TextBuilder وتعيين خاصية DrawTextRectangleBorder لـ [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Create new document object
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();

    // Create text fragment
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Set text properties
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Set StrokingColor property for drawing border (stroking) around text
    // rectangle
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Set DrawTextRectangleBorder property value to true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Save the document
    document->Save(_dataDir + outputFileName);
}
```

## كيفية إضافة نص مسطر

يظهر لك مقتطف الشيفرة التالي كيفية إضافة نص مسطر أثناء إنشاء ملف PDF جديد.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddUnderlineText_out.pdf");

    // Create new document object
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();

    // TextFragment with sample text
    auto fragment = MakeObject<TextFragment>("نص مع زخرفة المسطرة");
    // Set the font for TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Set the formatting of text as Underline
    fragment->get_TextState()->set_Underline(true);

    // Specify the position where TextFragment needs to be placed
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Append TextFragment to PDF file
    tb->AppendText(fragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## كيفية إضافة حدود حول النص المضاف

لديك التحكم في مظهر النص الذي تضيفه. يوضح المثال أدناه كيفية إضافة حدود حول قطعة من النص الذي قمت بإضافته عن طريق رسم مستطيل حوله. اكتشف المزيد عن فئة [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Save resulting PDF document.
    editor->Save(_dataDir + outputFileName);
}
```

## كيفية إضافة تغذية سطر جديد

لإضافة نص مع تغذية سطر جديد، يرجى استخدام [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) مع [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

يوضح لك مقتطف الشيفرة التالي كيفية إضافة تغذية سطر جديد في ملف PDF الخاص بك:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddNewLineFeed_out.pdf");

    // Create new document object
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();

    // Initialize new TextFragment with text containing required newline markers
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Set text fragment properties if necessary
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Create TextParagraph object
    auto par = MakeObject<TextParagraph>();

    // Add new TextFragment to paragraph
    par->AppendLine(textFragment);

    // Set paragraph position
    par->set_Position(MakeObject<Position>(100, 600));

    // Create TextBuilder object
    auto textBuilder = new TextBuilder(page);
    // Add the TextParagraph using TextBuilder
    textBuilder->AppendParagraph(par);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## كيفية إضافة نص مشطوب

يمكنك استخدام فئة [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) لضبط تنسيق النص مثل العريض والمائل والتسطير، وأيضًا، توفر API إمكانيات لتحديد تنسيق النص كالشطب.

يرجى محاولة استخدام مقتطف الشيفرة التالي لإضافة TextFragment مع تنسيق الشطب.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddStrikeOutText_out.pdf");

    // Open document
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();

    // Create text fragment
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Set text properties
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Set StrikeOut property
    textFragment->get_TextState()->set_StrikeOut(true);
    // Mark text as Bold
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## تطبيق تظليل التدرج على النص

تم تحسين فئة [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) بشكل أكبر عن طريق إدخال خاصية جديدة لـ [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54)، والتي يمكن استخدامها لتحديد ألوان التظليل للنص. تضيف هذه الخاصية الجديدة تظليل التدرج المختلف للنص مثل التظليل المحوري، التظليل الشعاعي (النوع 3) كما هو موضح في مقطع الكود التالي:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("ApplyGradientShading_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Create new color with pattern colorspace
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

> لتطبيق تدرج شعاعي، يمكنك تعيين الخاصية 'PatternColorSpace' لتكون مساوية لـ 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' في مقتطف الكود أعلاه.

## كيفية محاذاة النص مع محتوى عائم

يدعم Aspose.PDF تعيين محاذاة النص للمحتويات داخل عنصر صندوق عائم. يمكن استخدام خصائص المحاذاة لـ [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) لتحقيق ذلك كما هو موضح في عينة الكود التالية.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Create new color with pattern colorspace
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```