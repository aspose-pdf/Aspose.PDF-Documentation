---
title: Format PDF Text in C++
linktitle: Text Formatting
type: docs
weight: 70
url: /cpp/text-formatting-inside-pdf/
description: Control PDF text spacing, create lists, add footnotes and endnotes, and configure page layout and tabs using C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format PDF spacing, lists, notes, and page layouts in C++
Abstract: Format text with TextState, TextParagraph, and related layout APIs. The examples demonstrate line and character spacing, text and markup lists, footnotes and endnotes, inline content, columns, and custom tab stops.
---

Use Aspose.PDF for C++ to control text spacing and create structured page content. These examples create new documents with lists, notes, and layout settings. For font styling, colors, and borders, see the text insertion guide.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the destination PDF path as `outputFile`. Most functions create their own text and do not use `inputFile`; exceptions that read text, images, or fonts are described below. Ensure the fonts named by each example are available.

The main APIs used here are [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/), [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textformattingoptions/), [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/), [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/), [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/), [TabStops](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tabstops/).

## Line and character spacing

### Set line spacing

Read lorem.txt from the input directory, with fallback text when it is absent. Set a 12-point font size and a line spacing value of 16 on the fragment.

1. Create a page and load `lorem.txt` or use the fallback text.
1. Set the fragment’s font size to 12 points and its [LineSpacing](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) to 16.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SpecifyLineSpacingSimpleCase(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto loremPath = System::IO::Path::Combine(inputFile, String(u"lorem.txt"));
    String text = System::IO::File::Exists(loremPath) ? System::IO::File::ReadAllText(loremPath)
                                                      : String(u"Lorem ipsum text not found.");

    auto textFragment = MakeObject<TextFragment>(text);
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_LineSpacing(16);
    page->get_Paragraphs()->Add(textFragment);

    document->Save(outputFile);
}
```

### Compare font-based line spacing modes

Read HPSimplified.ttf and lorem.txt from inputDir. Use FontSize and FullSize line spacing modes on two fragments; lorem.txt has fallback text, but the font file is required.

1. Create a page, open `HPSimplified.ttf`, and read `lorem.txt` or use the fallback text.
1. Create two fragments with the loaded font and configure one with `FontSize` mode and the other with [FullSize](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textformattingoptions/) mode.
1. Add both fragments to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontTypes.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextFormattingOptions.h>
#include <system/io/file_stream.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SpecifyLineSpacingSpecificCase(String inputDir, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto fontFile = System::IO::Path::Combine(inputDir, String(u"HPSimplified.ttf"));
    auto loremPath = System::IO::Path::Combine(inputDir, String(u"lorem.txt"));
    String text = System::IO::File::Exists(loremPath) ? System::IO::File::ReadAllText(loremPath)
                                                      : String(u"Lorem ipsum text not found.");

    {
        auto fontStream = System::IO::File::OpenRead(fontFile);
        auto font = FontRepository::OpenFont(fontStream, FontTypes::TTF);

        auto fragment1 = MakeObject<TextFragment>(text);
        fragment1->get_TextState()->set_Font(font);
        fragment1->get_TextState()->set_FormattingOptions(MakeObject<TextFormattingOptions>());
        fragment1->get_TextState()->get_FormattingOptions()->set_LineSpacing(
            TextFormattingOptions::LineSpacingMode::FontSize);
        page->get_Paragraphs()->Add(fragment1);

        auto fragment2 = MakeObject<TextFragment>(text);
        fragment2->get_TextState()->set_Font(font);
        fragment2->get_TextState()->set_FormattingOptions(MakeObject<TextFormattingOptions>());
        fragment2->get_TextState()->get_FormattingOptions()->set_LineSpacing(
            TextFormattingOptions::LineSpacingMode::FullSize);
        page->get_Paragraphs()->Add(fragment2);
    }

    document->Save(outputFile);
}
```

### Set character spacing on fragments

Use the included makeCharacterSpacingFragment helper to add three fragments with character spacing values of 2.0, 1.0, and 0.75 points.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with one page.
1. Use `makeCharacterSpacingFragment()` to create three fragments with spacing values of 2.0, 1.0, and 0.75 points.
1. Add all three fragments to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

static SharedPtr<TextFragment> makeCharacterSpacingFragment(float spacing)
{
    auto fragment = MakeObject<TextFragment>(String(u"Sample Text with character spacing"));
    fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment->get_TextState()->set_FontSize(14);
    fragment->get_TextState()->set_CharacterSpacing(spacing);
    return fragment;
}

void CharacterSpacingUsingTextFragment(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    page->get_Paragraphs()->Add(makeCharacterSpacingFragment(2.0f));
    page->get_Paragraphs()->Add(makeCharacterSpacingFragment(1.0f));
    page->get_Paragraphs()->Add(makeCharacterSpacingFragment(0.75f));

    document->Save(outputFile);
}
```

### Set character spacing inside a paragraph

Apply a 2-point character spacing value to a fragment, append it to a word-wrapped paragraph rectangle, and render it with TextBuilder.

1. Create a page and configure a word-wrapped paragraph rectangle with [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/).
1. Set [CharacterSpacing](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/set_characterspacing/) to 2 points on a text fragment and append it to the paragraph as a line.
1. Add the paragraph with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
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

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CharacterSpacingUsingTextParagraph(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto builder = MakeObject<TextBuilder>(page);
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(100, 700, 500, 750, true));
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    auto fragment = MakeObject<TextFragment>(String(u"Sample Text with character spacing"));
    fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment->get_TextState()->set_FontSize(14);
    fragment->get_TextState()->set_CharacterSpacing(2.0f);

    paragraph->AppendLine(fragment);
    builder->AppendParagraph(paragraph);
    document->Save(outputFile);
}
```

## Create lists

### Create a numbered text list

Prefix four text items with their one-based numbers and append them as lines in a word-wrapped TextParagraph. The list markers are text, rather than semantic tagged-list elements.

1. Create a page and configure a word-wrapped [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/).
1. Prefix each of the four items with its one-based number and append it as a separate line.
1. Add the paragraph with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
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
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateNumberedList(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto items =
        MakeArray<String>({String(u"First item in the list"),
                           String(u"Second item with more text to demonstrate wrapping behavior."),
                           String(u"Third item"), String(u"Fourth item")});

    auto builder = MakeObject<TextBuilder>(page);
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(80, 200, 400, 800, true));
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    for (int i = 0; i < items->get_Length(); i++)
    {
        auto fragment =
            MakeObject<TextFragment>(String::Format(u"{0}", i + 1) + String(u". ") + items[i]);
        fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
        fragment->get_TextState()->set_FontSize(12);
        paragraph->AppendLine(fragment);
    }

    builder->AppendParagraph(paragraph);
    document->Save(outputFile);
}
```

### Create a bullet-style text list

Prefix four items with a hyphen and append them to a word-wrapped TextParagraph. The markers are literal text.

1. Create a page and configure a word-wrapped [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/).
1. Prefix each of the four items with a hyphen and append it as a separate line.
1. Add the paragraph with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
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
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateBulletList(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto items =
        MakeArray<String>({String(u"First item in the list"),
                           String(u"Second item with more text to demonstrate wrapping behavior."),
                           String(u"Third item"), String(u"Fourth item")});

    auto builder = MakeObject<TextBuilder>(page);
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Rectangle(MakeObject<Aspose::Pdf::Rectangle>(80, 200, 400, 800, true));
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    for (auto item : items)
    {
        auto fragment = MakeObject<TextFragment>(String(u"- ") + item);
        fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
        fragment->get_TextState()->set_FontSize(12);
        paragraph->AppendLine(fragment);
    }

    builder->AppendParagraph(paragraph);
    document->Save(outputFile);
}
```

### Create a numbered HTML list

Render an ordered list containing four items using HtmlFragment.

1. Create a page and build an [HtmlFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlfragment/) containing an ordered list with four items.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void CreateNumberedListHtmlVersion(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    String htmlList = String(u"<ol><li>First item in the list</li>") +
                      String(u"<li>Second item with more text to demonstrate wrapping behavior.</li>") +
                      String(u"<li>Third item</li><li>Fourth item</li></ol>");
    page->get_Paragraphs()->Add(MakeObject<HtmlFragment>(htmlList));
    document->Save(outputFile);
}
```

### Create a LaTeX bullet list

Render four items in a LaTeX itemize environment with TeXFragment.

1. Create a page and build a [TeXFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/) with four items in an `itemize` environment.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TeXFragment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateBulletListLatexVersion(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    String texList =
        String(u"Lists are easy to create: \\begin{itemize}") + String(u"\\item First item") +
        String(u"\\item Second item with more text to demonstrate wrapping behavior.") +
        String(u"\\item Third item") + String(u"\\item Fourth item") + String(u"\\end{itemize}");
    page->get_Paragraphs()->Add(MakeObject<TeXFragment>(texList));
    document->Save(outputFile);
}
```

### Create a numbered LaTeX list

Render four items in a LaTeX enumerate environment with TeXFragment.

1. Create a page and build a [TeXFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/) with four items in an `enumerate` environment.
1. Add the fragment to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TeXFragment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateNumberedListLatexVersion(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    String texList =
        String(u"Lists are easy to create: \\begin{enumerate}") + String(u"\\item First item") +
        String(u"\\item Second item with more text to demonstrate wrapping behavior.") +
        String(u"\\item Third item") + String(u"\\item Fourth item") + String(u"\\end{enumerate}");
    page->get_Paragraphs()->Add(MakeObject<TeXFragment>(texList));
    document->Save(outputFile);
}
```

## Footnotes and endnotes

### Add a footnote

Attach a Note to a TextFragment through FootNote, then add another fragment with IsInLineParagraph enabled.

1. Create a page and attach a [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/) to a text fragment through [FootNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Add the fragment to the page, then add the continuation fragment with [IsInLineParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf/baseparagraph/) enabled.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddFootnote(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is a sample text with a footnote."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->set_FootNote(MakeObject<Note>(String(u"This is the footnote content.")));
    page->get_Paragraphs()->Add(textFragment);

    auto inlineText =
        MakeObject<TextFragment>(String(u" This is another text after footnote in the same paragraph."));
    inlineText->set_IsInLineParagraph(true);
    inlineText->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    inlineText->get_TextState()->set_FontSize(14);
    page->get_Paragraphs()->Add(inlineText);

    document->Save(outputFile);
}
```

### Style a footnote

Give the Note its own TextState with Times New Roman, 10-point size, red foreground, and italic style before attaching it to the main fragment.

1. Create a page and a text fragment for the main text.
1. Set the note’s [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) to 10-point Times New Roman with red italic text.
1. Assign the note to [FootNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) and add the fragment to the page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddFootnoteCustomTextStyle(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is a sample text with a footnote."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);

    auto note = MakeObject<Note>(String(u"This is the footnote content with custom text style."));
    auto noteTextState = MakeObject<TextState>();
    noteTextState->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    noteTextState->set_FontSize(10);
    noteTextState->set_ForegroundColor(Color::get_Red());
    noteTextState->set_FontStyle(FontStyles::Italic);
    note->set_TextState(noteTextState);
    textFragment->set_FootNote(note);

    page->get_Paragraphs()->Add(textFragment);
    document->Save(outputFile);
}
```

### Set a custom footnote marker

Create a footnote and set its Text marker to three asterisks.

1. Create a page and attach a [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/) to the main fragment through [FootNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Set the note’s `Text` marker to three asterisks and add the text fragments to the page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddFootnoteCustomText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is a sample text with a footnote."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->set_FootNote(MakeObject<Note>(String(u"This is the footnote content.")));
    textFragment->get_FootNote()->set_Text(String(u"***"));
    page->get_Paragraphs()->Add(textFragment);

    auto anotherText = MakeObject<TextFragment>(String(u" This is another text without footnote."));
    anotherText->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    anotherText->get_TextState()->set_FontSize(14);
    page->get_Paragraphs()->Add(anotherText);

    document->Save(outputFile);
}
```

### Style the footnote separator

Set the page NoteLineStyle with a red 2-point dashed GraphInfo, then add two fragments with footnotes.

1. Create a page and configure a red, 2-point dashed [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/).
1. Assign the line settings to the page’s [NoteLineStyle](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Add two text fragments with footnotes to the page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddFootnoteWithCustomLineStyle(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto graphInfo = MakeObject<GraphInfo>();
    graphInfo->set_LineWidth(2);
    graphInfo->set_Color(Color::get_Red());
    graphInfo->set_DashArray(MakeArray<int>({3}));
    graphInfo->set_DashPhase(1);
    page->set_NoteLineStyle(graphInfo);

    auto text1 = MakeObject<TextFragment>(String(u"This is a sample text with a footnote."));
    text1->set_FootNote(MakeObject<Note>(String(u"foot note for text 1")));
    page->get_Paragraphs()->Add(text1);

    auto text2 = MakeObject<TextFragment>(String(u"This is yet another sample text with a footnote."));
    text2->set_FootNote(MakeObject<Note>(String(u"foot note for text 2")));
    page->get_Paragraphs()->Add(text2);

    document->Save(outputFile);
}
```

### Add an image and a table to a footnote

Read logo.jpg from the input directory. Build the note Paragraphs collection with a 20 by 20 point image, inline text, and a two-row table, then attach the note to a fragment.

1. Create a page with a body text fragment and prepare a [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/).
1. Add a 20-by-20-point image from `logo.jpg`, inline text, and a two-row table to the note’s paragraphs.
1. Attach the note to the body fragment through [FootNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddFootnoteWithImageAndTable(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>(String(u"This is a sample text with a footnote."));
    page->get_Paragraphs()->Add(text);

    auto note = MakeObject<Note>();

    auto imageNote = MakeObject<Image>();
    imageNote->set_File(System::IO::Path::Combine(inputFile, String(u"logo.jpg")));
    imageNote->set_FixHeight(20);
    imageNote->set_FixWidth(20);
    note->get_Paragraphs()->Add(imageNote);

    auto textNote = MakeObject<TextFragment>(String(u"This is the footnote content."));
    textNote->get_TextState()->set_FontSize(20);
    textNote->set_IsInLineParagraph(true);
    note->get_Paragraphs()->Add(textNote);

    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add(String(u"Cell 1,1"));
    table->get_Rows()->Add()->get_Cells()->Add(String(u"Cell 1,2"));
    note->get_Paragraphs()->Add(table);

    text->set_FootNote(note);
    document->Save(outputFile);
}
```

### Add an endnote

Attach a Note through EndNote and add five copies of lorem.txt from the input directory as body content. This example requires lorem.txt.

1. Create a page and attach a [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/) to the main fragment through [EndNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Read `lorem.txt` from the input directory and add five copies of it as body text.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddEndnote(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is a sample text with an endnote."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->set_EndNote(MakeObject<Note>(String(u"This is the EndNote content.")));
    page->get_Paragraphs()->Add(textFragment);

    String textContent =
        System::IO::File::ReadAllText(System::IO::Path::Combine(inputFile, u"lorem.txt"));
    for (int i = 0; i < 5; i++)
    {
        auto text = MakeObject<TextFragment>(textContent);
        text->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
        text->get_TextState()->set_FontSize(14);
        page->get_Paragraphs()->Add(text);
    }

    document->Save(outputFile);
}
```

### Set a custom endnote marker

Attach an endnote, set its Text marker to three asterisks, and add five copies of lorem.txt from the input directory.

1. Create a page and attach a [Note](https://reference.aspose.com/pdf/cpp/aspose.pdf/note/) to the main fragment through [EndNote](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Set the note’s `Text` marker to three asterisks.
1. Read `lorem.txt` and add five copies of it as body text.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddEndnoteCustomText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment = MakeObject<TextFragment>(String(u"This is a sample text with an endnote."));
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->set_EndNote(MakeObject<Note>(String(u"This is the EndNote content.")));
    textFragment->get_EndNote()->set_Text(String(u"***"));
    page->get_Paragraphs()->Add(textFragment);

    String textContent =
        System::IO::File::ReadAllText(System::IO::Path::Combine(inputFile, u"lorem.txt"));
    for (int i = 0; i < 5; i++)
    {
        auto text = MakeObject<TextFragment>(textContent);
        text->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
        text->get_TextState()->set_FontSize(14);
        page->get_Paragraphs()->Add(text);
    }

    document->Save(outputFile);
}
```

## Layout and page control

### Start a table on a new page

Create a five-row, three-column table and set IsInNewPage before adding it to page paragraphs.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with a page and configure a table with three columns and cell borders.
1. Populate five rows and enable [IsInNewPage](https://reference.aspose.com/pdf/cpp/aspose.pdf/baseparagraph/) on the table.
1. Add the table to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ForceNewPage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Table>();
    table->set_ColumnWidths(String(u"150 150 150"));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All));

    for (int i = 0; i < 5; i++)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add(String(u"Row ") + String::Format(u"{0}", i + 1) + String(u" - Col 1"));
        row->get_Cells()->Add(String(u"Row ") + String::Format(u"{0}", i + 1) + String(u" - Col 2"));
        row->get_Cells()->Add(String(u"Row ") + String::Format(u"{0}", i + 1) + String(u" - Col 3"));
    }

    table->set_IsInNewPage(true);
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Combine inline text and an image

Read logo.jpg from the input directory. Add an initial text fragment, an inline 30 by 30 point image, an inline continuation fragment, and a final fragment that starts a new paragraph.

1. Create a page and add the opening text fragment.
1. Load `logo.jpg` as a 30-by-30-point image and enable [IsInLineParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf/baseparagraph/) on the image and the continuation fragment.
1. Add the image and continuation, then add the final fragment as a new paragraph.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void UsingInlineParagraphProperty(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto fragment1 = MakeObject<TextFragment>(String(u"This is the first part of the paragraph. "));
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment1->get_TextState()->set_FontSize(14);
    page->get_Paragraphs()->Add(fragment1);

    auto image = MakeObject<Image>();
    image->set_IsInLineParagraph(true);
    image->set_File(System::IO::Path::Combine(inputFile, String(u"logo.jpg")));
    image->set_FixHeight(30);
    image->set_FixWidth(30);
    page->get_Paragraphs()->Add(image);

    auto fragment2 = MakeObject<TextFragment>(String(u"This is the second part of the same paragraph."));
    fragment2->set_IsInLineParagraph(true);
    fragment2->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment2->get_TextState()->set_FontSize(14);
    page->get_Paragraphs()->Add(fragment2);

    auto fragment3 = MakeObject<TextFragment>(String(u"This is a new paragraph."));
    fragment3->get_TextState()->set_Font(FontRepository::FindFont(String(u"Arial")));
    fragment3->get_TextState()->set_FontSize(14);
    page->get_Paragraphs()->Add(fragment3);

    document->Save(outputFile);
}
```

### Create a two-column PDF

Add a horizontal rule and heading, then place a caption and five copies of lorem.txt inside a two-column FloatingBox. Use 230-point column widths and a 5-point gap.

1. Set the page margins, add a page, and insert a horizontal rule and heading.
1. Configure a [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) with two 230-point columns and a 5-point gap.
1. Add the caption and five copies of `lorem.txt` to the box, then add it to the page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/ColumnInfo.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Line.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <system/array.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateMultiColumnPdf(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_PageInfo()->get_Margin()->set_Left(40);
    document->get_PageInfo()->get_Margin()->set_Right(40);
    auto page = document->get_Pages()->Add();
    auto rule = MakeObject<Aspose::Pdf::Drawing::Graph>(500.0, 2.0);
    rule->get_Shapes()->Add(MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({1, 2, 500, 2})));
    page->get_Paragraphs()->Add(rule);
    auto heading = MakeObject<TextFragment>(u"How to Steer Clear of Money Scams");
    heading->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    heading->get_TextState()->set_FontSize(18);
    page->get_Paragraphs()->Add(heading);
    auto box = MakeObject<FloatingBox>();
    box->get_ColumnInfo()->set_ColumnCount(2);
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");
    box->get_ColumnInfo()->set_ColumnWidths(u"230 230");
    auto caption = MakeObject<TextFragment>(u"By Example Author");
    caption->get_TextState()->set_FontSize(8);
    caption->get_TextState()->set_LineSpacing(2);
    box->get_Paragraphs()->Add(caption);
    auto text = System::IO::File::ReadAllText(System::IO::Path::Combine(inputFile, u"lorem.txt"));
    for (int i = 0; i < 5; ++i) box->get_Paragraphs()->Add(MakeObject<TextFragment>(text));
    page->get_Paragraphs()->Add(box);
    document->Save(outputFile);
}
```

### Align text with custom tab stops

Define stops at 100, 200, and 300 points using right, center, and left alignment with solid, dash, and dot leaders. Use the #$TAB placeholder to align header and data text.

1. Create a page and use [TabStops](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tabstops/) to define stops at 100, 200, and 300 points.
1. Set the stops to right, center, and left alignment with solid, dash, and dot leaders, respectively.
1. Build the header and data fragments with the tab stops and use `#$TAB` to align the text.
1. Add the fragments to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TabStop.h>
#include <Aspose.PDF.Cpp/Text/TabStops.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CustomTabStops(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto tabStops = MakeObject<TabStops>();
    auto tabStop1 = tabStops->Add(100);
    tabStop1->set_AlignmentType(TabAlignmentType::Right);
    tabStop1->set_LeaderType(TabLeaderType::Solid);

    auto tabStop2 = tabStops->Add(200);
    tabStop2->set_AlignmentType(TabAlignmentType::Center);
    tabStop2->set_LeaderType(TabLeaderType::Dash);

    auto tabStop3 = tabStops->Add(300);
    tabStop3->set_AlignmentType(TabAlignmentType::Left);
    tabStop3->set_LeaderType(TabLeaderType::Dot);

    auto header =
        MakeObject<TextFragment>(String(u"This is an example of forming table with TAB stops"), tabStops);
    auto text0 = MakeObject<TextFragment>(String(u"#$TABHead1 #$TABHead2 #$TABHead3"), tabStops);
    auto text1 = MakeObject<TextFragment>(String(u"#$TABdata11 #$TABdata12 #$TABdata13"), tabStops);

    auto text2 = MakeObject<TextFragment>(String(u"#$TABdata21 "), tabStops);
    text2->get_Segments()->Add(MakeObject<TextSegment>(String(u"#$TAB")));
    text2->get_Segments()->Add(MakeObject<TextSegment>(String(u"data22 ")));
    text2->get_Segments()->Add(MakeObject<TextSegment>(String(u"#$TAB")));
    text2->get_Segments()->Add(MakeObject<TextSegment>(String(u"data23")));

    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(outputFile);
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
