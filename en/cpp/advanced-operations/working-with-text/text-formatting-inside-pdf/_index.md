---
title: Text Formatting inside PDF using C++
linktitle: Text Formatting inside PDF
type: docs
weight: 30
url: /cpp/text-formatting-inside-pdf/
description: Learn how to apply text formatting within PDFs in C++ using Aspose.PDF to control text appearance.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to add Line Indent to PDF

To add line indentation to PDF Aspose.PDF for C ++ uses the [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) property in the [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) class  and also help the [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) and [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) collections.

Please use the following code snippet to use the property:

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

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## How to add Text Border

The following code snippet shows, how to add a border to a text using TextBuilder and setting DrawTextRectangleBorder property of [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

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

## How to add Underline Text

The following code snippet shows you how to add Underline text while creating a new PDF file.

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
    auto fragment = MakeObject<TextFragment>("Text with underline decoration");
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

## How to add Border Around Added Text

You have control over the look and feel of the text you add. The example below shows how to add a border around a piece of text that you have added by drawing a rectangle around it. Find out more about the [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/) class.

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

## How to add NewLine feed

For adding text with line feed, please use [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) with [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

The following code snippet shows you how to add NewLine feed in your PDF file:

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

## How to add StrikeOut Text

You can use [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) class to set text formatting like Bold, Italic, Underline, and also, the API has provided the capabilities to mark text formatting as Strikeout.

Please try using the following code snippet to add TextFragment with Strikeout formatting.

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

## Apply Gradient Shading to the Text

[Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) Class has further been enhanced by introducing new property of [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), which can be used to specify shading colors for the text. This new property adds different Gradient Shading to the text e.g. Axial Shading, Radial (Type 3) Shading as shown in the following code snippet:

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

>In order to apply a Radial Gradient, you can set ‘PatternColorSpace’ property equal to ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ in the above code snippet.

## How to align text to float content

Aspose.PDF supports setting text alignment for contents inside a Floating Box element. The alignment properties of [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) instance can be used to achieve this as shown in the following code sample.

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
