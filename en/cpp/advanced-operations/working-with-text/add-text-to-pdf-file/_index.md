---
title: Add Text to PDF in C++
linktitle: Add Text
type: docs
weight: 10
url: /cpp/add-text-to-pdf-file/
description: Add text, paragraphs, hyperlinks, LaTeX fragments to PDF documents, and load custom fonts using C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insert and style PDF text with C++ examples
Abstract: Create PDF text with TextFragment, TextParagraph, and TextBuilder. The examples cover font styling, transparency, gradients, LaTeX content, hyperlinks, and custom fonts.
---

Use Aspose.PDF for C++ to create text fragments and add them to page paragraphs or place them with TextBuilder. The examples on this page create new documents; they do not append text to input PDF files.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the destination PDF path as `outputFile`. Most functions create their own text and do not use `inputFile`; exceptions that read text, images, or fonts are described below. Ensure the fonts named by each example are available.

The main APIs used here are [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/), [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/), [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/), [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/), [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/),  [TeXFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/), [WebHyperlink](https://reference.aspose.com/pdf/cpp/aspose.pdf/webhyperlink/).

## Basic text insertion

### Add a text fragment

Create a page, position a TextFragment at (100, 600), add it to the page paragraphs, and save the PDF.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) and set its position to (100, 600).
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextSimpleCase(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"Hello, Aspose!"));
    textFragment->set_Position(MakeObject<Position>(100, 600));

    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

### Add a paragraph

Read lorem.txt from the input directory, or use the fallback text if it is missing. Set a first-line indent of 20 points, a paragraph rectangle, and discretionary hyphenation before appending the paragraph with TextBuilder.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and read `lorem.txt` or use the fallback text.
1. Set the paragraph rectangle, 20-point first-line indent, and discretionary hyphenation.
1. Append the styled text as a line and add the paragraph with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextFormattingOptions.h>
#include <Aspose.PDF.Cpp/Text/TextParagraph.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddParagraph(String inputFile, String outputFile)
{
    auto loremPath = System::IO::Path::Combine(inputFile, u"lorem.txt");

    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();

        String text = System::IO::File::Exists(loremPath) ? System::IO::File::ReadAllText(loremPath)
                                                          : String(u"Lorem ipsum sample text not found.");

        auto builder = MakeObject<TextBuilder>(page);
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_FirstLineIndent(20);
        paragraph->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(80, 800, 400, 200, true));
        paragraph->get_FormattingOptions()->set_WrapMode(
            TextFormattingOptions::WordWrapMode::DiscretionaryHyphenation);

        auto fragment = MakeObject<TextFragment>(text);
        fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
        fragment->get_TextState()->set_FontSize(12);

        paragraph->AppendLine(fragment);
        builder->AppendParagraph(paragraph);

        document->Save(outputFile);
    }
}
```

### Set paragraph indents

Read the text file supplied as inputFile, with fallback text when it does not exist. Compare a 20-point first-line indent with a 20-point subsequent-lines indent in two separate paragraph rectangles.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and load the input text or use the fallback text.
1. Create two paragraphs in separate rectangles and append the same styled text to each.
1. Set a 20-point first-line indent on the first paragraph and a 20-point subsequent-lines indent on the second before adding them with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextFormattingOptions.h>
#include <Aspose.PDF.Cpp/Text/TextParagraph.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddParagraphsIndents(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    String text = System::IO::File::Exists(inputFile) ? System::IO::File::ReadAllText(inputFile)
        : String(u"Lorem ipsum sample text not found.");

    auto fragment = MakeObject<TextFragment>(text);
    fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    fragment->get_TextState()->set_FontSize(12);

    auto builder = MakeObject<TextBuilder>(page);
    auto paragraph1 = MakeObject<TextParagraph>();
    paragraph1->set_FirstLineIndent(20);
    paragraph1->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(80, 800, 300, 50, true));
    paragraph1->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);
    paragraph1->AppendLine(fragment);
    builder->AppendParagraph(paragraph1);

    auto paragraph2 = MakeObject<TextParagraph>();
    paragraph2->set_SubsequentLinesIndent(20);
    paragraph2->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(320, 800, 500, 50, true));
    paragraph2->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);
    paragraph2->AppendLine(fragment);
    builder->AppendParagraph(paragraph2);

    document->Save(outputFile);
}
```

### Insert a line break

Include a newline in a TextFragment, append it to a TextParagraph at (100, 600), and render it with TextBuilder.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and add a newline to the fragment text.
1. Style the fragment and append it to a [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/) positioned at (100, 600).
1. Add the paragraph to the page with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextParagraph.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddNewLine(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment =
        MakeObject<TextFragment>(String(u"Applicant Name: ") + String(u"\n") + String(u" Joe Smoe"));
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    auto paragraph = MakeObject<TextParagraph>();
    paragraph->AppendLine(textFragment);
    paragraph->set_Position(MakeObject<Position>(100, 600));

    auto textBuilder = MakeObject<TextBuilder>(page);
    textBuilder->AppendParagraph(paragraph);

    document->Save(outputFile);
}
```

### Inspect layout notifications

Enable notification logging, add four text fragments with explicit line breaks, and print the first page notifications before saving the PDF.

1. Enable notification logging on a new document and add a page.
1. Add four fragments containing explicit line breaks to the page paragraphs.
1. Call [GetNotifications()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/getnotifications/) for page 1 and print the result.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void DetermineLineBreak(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->set_EnableNotificationLogging(true);

    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++)
    {
        auto text = MakeObject<TextFragment>(
            String(u"Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, ") +
            String(u"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ") +
            String(u"Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris ") +
            String(u"nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in ") +
            String(u"reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla ") +
            String(u"pariatur. Excepteur sint occaecat cupidatat non proident, sunt in ") +
            String(u"culpa qui officia deserunt mollit anim id est laborum."));
        text->get_TextState()->set_FontSize(20);
        page->get_Paragraphs()->Add(text);
    }

    std::cout << (document->get_Pages()->idx_get(1)->GetNotifications()) << std::endl;
    document->Save(outputFile);
}
```

### Measure text width

Compare Font::MeasureString and TextState::MeasureString for characters from A through z at 14 points. This diagnostic writes messages only when measurements differ from the checks; it does not create a PDF, and neither file parameter is used. The fixed expected widths depend on the Arial font available on the system.

1. Find Arial with [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/) and configure a [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) at 14 points.
1. Measure the characters from A through z with [Font::MeasureString()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/font/measurestring/) and `TextState::MeasureString()`.
1. Compare the measurements with the example checks and print any discrepancies.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <cmath>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void GetTextWidthDynamically(String inputFile, String outputFile)
{
    auto font = FontRepository::FindFont(String(u"Arial"));
    auto textState = MakeObject<TextState>();
    textState->set_Font(font);
    textState->set_FontSize(14);

    if (std::abs(font->MeasureString(String(u"A"), 14) - 9.337) > 0.001)
    {
        std::cout << (String(u"Unexpected font string measure!")) << std::endl;
    }

    if (std::abs(textState->MeasureString(String(u"z")) - 7.0) > 0.001)
    {
        std::cout << (String(u"Unexpected font string measure!")) << std::endl;
    }

    for (char16_t c = u'A'; c <= u'z'; c++)
    {
        double fontMeasure = font->MeasureString(String(c, 1), 14);
        double textStateMeasure = textState->MeasureString(String(c, 1));
        if (std::abs(fontMeasure - textStateMeasure) > 0.001)
        {
            std::cout << (String(u"Font and state string measuring doesn't match!")) << std::endl;
        }
    }
}
```

### Add a text hyperlink

Build a fragment from several TextSegment objects and assign a WebHyperlink only to the segment labeled Link to Aspose. Style that segment in blue italic text.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and build a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) from multiple [TextSegment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsegment/) objects.
1. Assign a [WebHyperlink](https://reference.aspose.com/pdf/cpp/aspose.pdf/webhyperlink/) to the Link to Aspose segment and style it in blue italics.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/WebHyperlink.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextWithHyperlink(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>(String(u"Sample Text Fragment"));
    fragment->get_Segments()->Add(MakeObject<TextSegment>(String(u" ... Text Segment 1...")));

    auto segment = MakeObject<TextSegment>(String(u"Link to Aspose"));
    fragment->get_Segments()->Add(segment);
    segment->set_Hyperlink(MakeObject<WebHyperlink>(String(u"https://products.aspose.com/pdf")));
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    fragment->get_Segments()->Add(MakeObject<TextSegment>(String(u"TextSegment without hyperlink")));

    page->get_Paragraphs()->Add(fragment);
    document->Save(outputFile);
}
```

### Add right-aligned Arabic text

Add the supplied Unicode Arabic string with Tahoma at 14 points and align the fragment to the right. Use a font containing the required Arabic glyphs.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and a fragment containing the Arabic text.
1. Set the font to Tahoma at 14 points and set the horizontal alignment to `Right`.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextWithRtlText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(
        String(u"\u064a\u0639\u062a\u0628\u0631 \u062e\u0648\u062c\u0627 \u0646\u0635\u0631 "
               u"\u0627\u0644\u062f\u064a\u0646 \u0634\u062e\u0635\u064a\u0629 "
               u"\u0641\u0648\u0644\u0643\u0644\u0648\u0631\u064a\u0629 \u0645\u0646 "
               u"\u0627\u0644\u0634\u0631\u0642 \u0627\u0644\u0625\u0633\u0644\u0627\u0645\u064a "
               u"\u0648\u0628\u0639\u0636 \u0634\u0639\u0648\u0628 \u0627\u0644\u0628\u062d\u0631 "
               u"\u0627\u0644\u0623\u0628\u064a\u0636 \u0627\u0644\u0645\u062a\u0648\u0633\u0637 "
               u"\u200b\u200b\u0648\u0627\u0644\u0628\u0644\u0642\u0627\u0646\u060c \u0648\u0647\u0648 "
               u"\u0628\u0637\u0644 \u0627\u0644\u0642\u0635\u0635 "
               u"\u0648\u0627\u0644\u062d\u0643\u0627\u064a\u0627\u062a "
               u"\u0627\u0644\u0642\u0635\u064a\u0631\u0629 \u0627\u0644\u0641\u0643\u0627\u0647\u064a\u0629 "
               u"\u0648\u0627\u0644\u0633\u0627\u062e\u0631\u0629\u060c "
               u"\u0648\u0623\u062d\u064a\u0627\u0646\u064b\u0627 "
               u"\u0627\u0644\u062d\u0643\u0627\u064a\u0627\u062a \u0627\u0644\u064a\u0648\u0645\u064a\u0629."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Tahoma")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->set_HorizontalAlignment(HorizontalAlignment::Right);

    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

## Text styling

### Style fragments and segments

Apply bold, italic, underline, size, and color settings to a greeting. Use the included addSegment helper to build a second fragment with individually styled subscript segments.

1. Create a [page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and set the greeting fragment’s font, size, color, and style.
1. Use `addSegment()` to assemble a second fragment with individually styled subscript segments.
1. Add both fragments to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

static void addSegment(SharedPtr<TextFragment> formula, String text, SharedPtr<TextState> state,
                       SharedPtr<Position> position)
{
    auto segment = MakeObject<TextSegment>(text);
    segment->set_TextState(state);
    segment->set_Position(position);
    formula->get_Segments()->Add(segment);
}

void AddTextWithFontStyling(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto formula = MakeObject<TextFragment>();
    auto textFragment = MakeObject<TextFragment>(String(u"Hello, Aspose!"));
    textFragment->set_Position(MakeObject<Position>(100, 600));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    textFragment->get_TextState()->set_Underline(true);
    textFragment->set_HorizontalAlignment(HorizontalAlignment::Left);

    auto textStateLetters = MakeObject<TextState>();
    textStateLetters->set_Font(FontRepository::FindFont(String(u"Arial")));
    textStateLetters->set_FontSize(14);
    textStateLetters->set_ForegroundColor(Color::get_Blue());
    textStateLetters->set_FontStyle(FontStyles::Bold);

    auto textStateIndex = MakeObject<TextState>();
    textStateIndex->set_Font(FontRepository::FindFont(String(u"Arial")));
    textStateIndex->set_FontSize(14);
    textStateIndex->set_ForegroundColor(Color::get_DarkRed());
    textStateIndex->set_Subscript(true);

    auto position = MakeObject<Position>(100, 500);
    addSegment(formula, String(u"S = a"), textStateLetters, position);
    addSegment(formula, String(u"2n"), textStateIndex, position);
    addSegment(formula, String(u" + a"), textStateLetters, position);
    addSegment(formula, String(u"2n+1"), textStateIndex, position);
    addSegment(formula, String(u" + a"), textStateLetters, position);
    addSegment(formula, String(u"2n+2"), textStateIndex, position);
    formula->set_HorizontalAlignment(HorizontalAlignment::Left);

    page->get_Paragraphs()->Add(textFragment);
    page->get_Paragraphs()->Add(formula);
    document->Save(outputFile);
}
```

### Underline text

Set Underline on an Arial text fragment, position it at (10, 800), and append it with TextBuilder.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page and an Arial text fragment.
1. Enable [Underline](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/set_underline/) on the fragment’s text state and position the fragment at (10, 800).
1. Append it with [TextBuilder::AppendText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/appendtext/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddUnderlineText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto textBuilder = MakeObject<TextBuilder>(page);

    auto fragment = MakeObject<TextFragment>(String(u"Hello, ASPOSE.PDF!"));
    fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment->get_TextState()->set_FontSize(10);
    fragment->get_TextState()->set_Underline(true);
    fragment->set_Position(MakeObject<Position>(10, 800));
    textBuilder->AppendText(fragment);

    document->Save(outputFile);
}
```

### Add transparent text

Draw a partially transparent filled rectangle and add green text with an alpha value of 30 using Color::FromArgb.

1. Create a page and add a graph containing a partially transparent filled rectangle.
1. Create a text fragment and set its foreground to green with an alpha value of 30 using [Color::FromArgb()](https://reference.aspose.com/pdf/cpp/aspose.pdf/color/fromargb/).
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextTransparent(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100.0, 400.0);
    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    rectangle->get_GraphInfo()->set_FillColor(Color::FromArgb(128, 0xC5, 0xB5, 0xFF));
    canvas->get_Shapes()->Add(rectangle);
    canvas->set_IsChangePosition(false);
    page->get_Paragraphs()->Add(canvas);

    auto text = MakeObject<TextFragment>(String(
        u"This is the transparent text. This is the transparent text. This is the transparent text."));
    text->get_TextState()->set_ForegroundColor(Color::FromArgb(30, 0, 255, 0));
    page->get_Paragraphs()->Add(text);

    document->Save(outputFile);
}
```

### Add invisible text

Add visible and invisible fragments to the same page. The second fragment has Invisible enabled; its text remains PDF content and can be found by text extraction.

1. Create a page and add a visible fragment to its paragraphs.
1. Set [Invisible](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) on a second fragment’s text state and add the fragment to the same page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextInvisible(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text1 = MakeObject<TextFragment>(
        String(u"This is the visible text. This is the visible text. This is the visible text."));
    page->get_Paragraphs()->Add(text1);

    auto text2 = MakeObject<TextFragment>(
        String(u"This is the invisible text. This is the invisible text. This is the invisible text."));
    text2->get_TextState()->set_Invisible(true);
    page->get_Paragraphs()->Add(text2);

    document->Save(outputFile);
}
```

### Draw a text border

Set the fragment background, foreground, and stroking colors, then enable DrawTextRectangleBorder to outline its text rectangle.

1. Create and position a text fragment on a new page.
1. Set its background, foreground, and stroking colors, then enable [DrawTextRectangleBorder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/).
1. Append the fragment with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextBorder(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is sample text with border."));
    textFragment->set_Position(MakeObject<Position>(10, 700));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);

    auto textBuilder = MakeObject<TextBuilder>(page);
    textBuilder->AppendText(textFragment);

    document->Save(outputFile);
}
```

### Strike out text

Enable StrikeOut on a bold text fragment with a light gray background and red foreground, then place it with TextBuilder.

1. Create a bold text fragment with a light gray background and red foreground.
1. Enable [StrikeOut](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) and set the fragment position.
1. Append the fragment to the new page with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddStrikeoutText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is sample strikeout text."));
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    textFragment->get_TextState()->set_StrikeOut(true);
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);
    textFragment->set_Position(MakeObject<Position>(100, 600));

    auto textBuilder = MakeObject<TextBuilder>(page);
    textBuilder->AppendText(textFragment);

    document->Save(outputFile);
}
```

## Advanced color effects

### Apply an axial gradient

Assign a red-to-blue GradientAxialShading pattern to the foreground color of a 36-point title.

1. Create and position a 36-point title on a new page.
1. Set the foreground color’s pattern color space to a red-to-blue [GradientAxialShading](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/gradientaxialshading/) and enable underlining.
1. Add the title to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/GradientAxialShading.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Drawing;

void ApplyGradientAxialShadingToText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"PDF TITLE"));
    textFragment->set_Position(MakeObject<Position>(100, 600));
    textFragment->get_TextState()->set_FontSize(36);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial Bold")));
    textFragment->get_TextState()->set_ForegroundColor(MakeObject<Color>());
    textFragment->get_TextState()->get_ForegroundColor()->set_PatternColorSpace(
        MakeObject<GradientAxialShading>(Color::get_Red(), Color::get_Blue()));
    textFragment->get_TextState()->set_Underline(true);

    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

### Apply a radial gradient

Assign a red-to-blue GradientRadialShading pattern to the foreground color of a 36-point title.

1. Create and position a 36-point title on a new page.
1. Set the foreground color’s pattern color space to a red-to-blue [GradientRadialShading](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/gradientradialshading/) and enable underlining.
1. Add the title to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/GradientRadialShading.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Drawing;

void ApplyGradientRadialShadingToText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"PDF TITLE"));
    textFragment->set_Position(MakeObject<Position>(100, 600));
    textFragment->get_TextState()->set_FontSize(36);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial Bold")));
    textFragment->get_TextState()->set_ForegroundColor(MakeObject<Color>());
    textFragment->get_TextState()->get_ForegroundColor()->set_PatternColorSpace(
        MakeObject<GradientRadialShading>(Color::get_Red(), Color::get_Blue()));
    textFragment->get_TextState()->set_Underline(true);

    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

## LaTeX fragments

### Add a LaTeX formula

Add a TeXFragment containing braces, annotations, and a formula to page paragraphs.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a [TeXFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/) containing the LaTeX formula and add it to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TeXFragment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextLatexFragment(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TeXFragment>(String(
        u"\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"));
    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

## Custom fonts

### Load a font from a file

Pass a font file path as inputFile. Open it with FontRepository::OpenFont and use it for a blue 24-point italic greeting.

1. Open the input font file with [FontRepository::OpenFont()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/openfont/).
1. Create a page and set the opened font on a positioned, blue, 24-point italic fragment.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void UseCustomFontFromFile(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>();
	auto page = document->get_Pages()->Add();

	auto fragment = MakeObject<TextFragment>(String(u"Hello, Aspose!"));
	fragment->set_Position(MakeObject<Position>(100, 600));
	fragment->get_TextState()->set_Font(FontRepository::OpenFont(inputFile));
	fragment->get_TextState()->set_FontSize(24);
	fragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
	fragment->get_TextState()->set_FontStyle(FontStyles::Italic);

	page->get_Paragraphs()->Add(fragment);
	document->Save(outputFile);
}
```

### Load a font from a stream

Pass an OpenType font path as inputFile. Open its stream with FontRepository::OpenFont using FontTypes::OTF, enable embedding, and use the font in a new PDF.

1. Open the input font as a stream and pass it to [FontRepository::OpenFont()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/openfont/) with [FontTypes::OTF](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fonttypes/).
1. Enable font embedding and apply the font to a positioned text fragment.
1. Add the fragment to the new page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/FontTypes.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/file_stream.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void UseCustomFontFromStream(String inputFile, String outputFile)
{

	auto fontStream = System::IO::File::OpenRead(inputFile);
	auto font = FontRepository::OpenFont(fontStream, FontTypes::OTF);
	font->set_IsEmbedded(true);

	auto document = MakeObject<Document>();
	auto page = document->get_Pages()->Add();

	auto fragment = MakeObject<TextFragment>(String(u"Hello, Aspose!"));
	fragment->set_Position(MakeObject<Position>(100, 600));
	fragment->get_TextState()->set_Font(font);
	fragment->get_TextState()->set_FontSize(14);
	fragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
	fragment->get_TextState()->set_FontStyle(FontStyles::Italic);

	page->get_Paragraphs()->Add(fragment);
	document->Save(outputFile);

}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
