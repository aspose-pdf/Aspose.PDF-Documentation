---
title: Rotate PDF Text in C++
linktitle: Rotate Text
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: Rotate individual PDF text fragments and entire paragraphs using TextBuilder and page paragraphs in C++.
lastmod: "2026-11-26"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Control PDF text fragment and paragraph rotation in C++
Abstract: Create rotated PDF text using TextFragmentState and TextParagraph. Compare positioned fragments, individually rotated paragraph lines, page paragraph flow, and rotation of complete multiline paragraphs.
---

Apply rotation to a fragment through its TextState or rotate a complete TextParagraph. These examples generate new documents with rotated text; they do not rotate existing text in an input PDF.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the destination PDF path as `outputFile`. Most functions create their own text and do not use `inputFile`; exceptions that read text, images, or fonts are described below. Ensure the fonts named by each example are available.

The main APIs used here are [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/), [TextFragmentState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/), [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/), [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).

## Rotate text fragments

### Rotate positioned fragments with TextBuilder

Create three fragments at different horizontal positions. Leave the first unrotated and rotate the next two by 45 and 90 degrees, then append each with TextBuilder.

1. Create a page and set the positions and fonts of three text fragments.
1. Keep the first fragment unrotated and set the other fragments’ rotations to 45 and 90 degrees.
1. Append each fragment with [TextBuilder::AppendText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/appendtext/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
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

void RotateTextInsidePdf1(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment1 = MakeObject<TextFragment>(String(u"main text"));
    textFragment1->set_Position(MakeObject<Position>(100, 600));
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));

    auto textFragment2 = MakeObject<TextFragment>(String(u"rotated text"));
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment2->get_TextState()->set_Rotation(45);

    auto textFragment3 = MakeObject<TextFragment>(String(u"rotated text"));
    textFragment3->set_Position(MakeObject<Position>(300, 600));
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment3->get_TextState()->set_Rotation(90);

    auto builder = MakeObject<TextBuilder>(page);
    builder->AppendText(textFragment1);
    builder->AppendText(textFragment2);
    builder->AppendText(textFragment3);

    document->Save(outputFile);
}
```

### Rotate individual paragraph lines

Append three fragments to a paragraph at (200, 600). Rotate the first fragment by 45 degrees and the third by -45 degrees while keeping the middle fragment unrotated.

1. Create a page and position a [TextParagraph](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textparagraph/) at (200, 600).
1. Rotate the first and third fragments by 45 and -45 degrees and leave the middle fragment unrotated.
1. Append the three fragments as lines and add the paragraph with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
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

void RotateTextInsidePdf2(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    auto textFragment1 = MakeObject<TextFragment>(String(u"rotated text"));
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment1->get_TextState()->set_Rotation(45);

    auto textFragment2 = MakeObject<TextFragment>(String(u"main text"));
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));

    auto textFragment3 = MakeObject<TextFragment>(String(u"another rotated text"));
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment3->get_TextState()->set_Rotation(-45);

    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);

    auto textBuilder = MakeObject<TextBuilder>(page);
    textBuilder->AppendParagraph(paragraph);

    document->Save(outputFile);
}
```

### Rotate fragments in page paragraph flow

Add three fragments directly to page paragraphs. Leave the first unrotated and set rotations of 315 and 270 degrees on the other two.

1. Create a [page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and style three text fragments.
1. Keep the first fragment unrotated and set the other rotations to 315 and 270 degrees.
1. Add the fragments directly to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
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

void RotateTextInsidePdf3(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto textFragment1 = MakeObject<TextFragment>(String(u"main text"));
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));

    auto textFragment2 = MakeObject<TextFragment>(String(u"rotated text"));
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment2->get_TextState()->set_Rotation(315);

    auto textFragment3 = MakeObject<TextFragment>(String(u"rotated text"));
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    textFragment3->get_TextState()->set_Rotation(270);

    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    document->Save(outputFile);
}
```

## Rotate entire paragraphs

### Rotate multiline paragraphs

Use the included rotatedLine helper to create three styled lines per paragraph. Draw four paragraphs at (200, 600), rotated by 45, 135, 225, and 315 degrees.

1. Create a page and use `rotatedLine()` to build styled text fragments.
1. Create four paragraphs at (200, 600) with rotations of 45, 135, 225, and 315 degrees.
1. Append three lines to each paragraph and add the paragraphs with [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
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

static SharedPtr<TextFragment> rotatedLine(String text, bool underline)
{
    auto fragment = MakeObject<TextFragment>(text);
    fragment->get_TextState()->set_FontSize(12);
    fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    fragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    fragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    fragment->get_TextState()->set_Underline(underline);
    return fragment;
}

void RotateTextInsidePdf4(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    for (int i = 0; i < 4; i++)
    {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        paragraph->set_Rotation(i * 90 + 45);

        auto textFragment1 = rotatedLine(String(u"Paragraph Text"), false);
        auto textFragment2 = rotatedLine(String(u"Second line of text"), false);
        auto textFragment3 = rotatedLine(String(u"And some more text..."), true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);

        auto builder = MakeObject<TextBuilder>(page);
        builder->AppendParagraph(paragraph);
    }

    document->Save(outputFile);
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
