---
title: Replace Text in PDF with C++
linktitle: Replace Text
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: Replace PDF text and fonts, adjust replacement layout, and remove text from documents, pages, or regions using C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Find, replace, resize, and remove PDF text in C++
Abstract: Modify existing PDF content with TextFragmentAbsorber and TextReplaceOptions. The examples cover document-wide and regional replacement, font changes, replacement fitting, and removal of visible or invisible text.
---

Use TextFragmentAbsorber to locate existing PDF text and update matching fragments. Configure replacement options when the new text needs to fit a different rectangle. These examples operate on text content rather than text embedded in scanned images.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the existing PDF path as `inputFile`. Examples that access page 2 require at least two pages. Pass the destination PDF path as `outputFile`.

The main APIs used here are [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/), [TextReplaceOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textreplaceoptions/), [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/), [TextEditOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/texteditoptions/), [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/).

## Replace text

### Replace text on all pages

Search every page for the literal phrase PDF and replace each match with pdf, then save the modified document.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) for the literal phrase `PDF`.
1. Visit all pages and set the text of each match to `pdf`.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages(String inputFile, String outputFile)
{
    String searchPhrase = String(u"PDF");
    String replacePhrase = String(u"pdf");

    {
        auto document = MakeObject<Document>(inputFile);
        auto absorber = MakeObject<TextFragmentAbsorber>(searchPhrase);
        document->get_Pages()->Accept(absorber);

        for (auto fragment : absorber->get_TextFragments())
        {
            fragment->set_Text(replacePhrase);
        }

        document->Save(outputFile);
    }
}
```

### Replace text in a page region

On page 1 only, limit the search for doc to the rectangle (300, 442, 500, 742) and replace matches with DOC.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) for `doc`.
1. Use [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/) to limit the search to (300, 442, 500, 742) on page 1.
1. Set each matched fragment’s text to `DOC`.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextInParticularPageRegion(String inputFile, String outputFile)
{
    String searchPhrase = String(u"doc");
    String replacePhrase = String(u"DOC");

    {
        auto document = MakeObject<Document>(inputFile);
        auto absorber = MakeObject<TextFragmentAbsorber>(searchPhrase);
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(
            MakeObject<Aspose::Pdf::Rectangle>(300, 442, 500, 742, true));
        document->get_Pages()->idx_get(1)->Accept(absorber);

        for (auto fragment : absorber->get_TextFragments())
        {
            fragment->set_Text(replacePhrase);
        }

        document->Save(outputFile);
    }
}
```

### Adjust replacement width without setting font size

Take the first fragment on page 1, move the left rectangle edge inward by 50 points and the right edge inward by 50 points, and duplicate its text. The example uses AdjustSpaceWidth and does not explicitly change the font size.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and use [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) to get the first text fragment on page 1.
1. Move both horizontal edges of its rectangle inward by 50 points.
1. Set the rectangle and [AdjustSpaceWidth](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textreplaceoptions/) in the replacement options, then replace the fragment text with two copies of itself.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndResizeAndShiftWithoutChangingFontSize(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    auto rectangle = fragment->get_Rectangle();
    rectangle->set_LLX(rectangle->get_LLX() + 50);
    rectangle->set_URX(rectangle->get_URX() - 50);
    fragment->get_ReplaceOptions()->set_Rectangle(rectangle);
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

### Use a page-based replacement rectangle

Take the first fragment on page 1 and set a replacement rectangle derived from the page MediaBox with 20-point left, right, and top insets. Duplicate the fragment text and use AdjustSpaceWidth.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select the first text fragment on page 1.
1. Build a rectangle from the page [MediaBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) with 20-point insets on the left, right, and top.
1. Set the rectangle and [AdjustSpaceWidth](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textreplaceoptions/) in the replacement options, then double the fragment text.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndResizeAndShiftParagraph(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    auto mediaBox = document->get_Pages()->idx_get(1)->get_MediaBox();
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(
        mediaBox->get_LLX() + 20, mediaBox->get_LLY(),
        mediaBox->get_URX() - 20, mediaBox->get_URY() - 20);
    fragment->get_ReplaceOptions()->set_Rectangle(rectangle);
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

### Scale replacement text to fill a rectangle

Take the first fragment on page 1, set the replacement rectangle to (100, 300, 512, 692), and duplicate the text. Use ScaleToFill together with AdjustSpaceWidth.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select the first text fragment on page 1.
1. Set the replacement bounds to (100, 300, 512, 692) and select [AdjustSpaceWidth](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textreplaceoptions/) and `ScaleToFill`.
1. Replace the fragment text with two copies of itself.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndResizeAndExpandFont(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    fragment->get_ReplaceOptions()->set_Rectangle(
        MakeObject<Aspose::Pdf::Rectangle>(100, 300, 512, 692, true));
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->get_ReplaceOptions()->set_FontSizeAdjustmentAction(
        TextReplaceOptions::FontSizeAdjustment::ScaleToFill);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

### Shrink replacement text to fit

Take the first fragment on page 1 and retain its original rectangle as the replacement bounds. Duplicate its text and combine ShrinkToFit with AdjustSpaceWidth. Each first-fragment example throws an exception if the page has no text fragments.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select the first text fragment on page 1.
1. Use the fragment’s original rectangle as the replacement bounds and select [ShrinkToFit](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textreplaceoptions/) and `AdjustSpaceWidth`.
1. Replace the fragment text with two copies of itself.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <stdexcept>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextAndFitTextIntoRectangle(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);
    String text = fragment->get_Text();
    fragment->get_ReplaceOptions()->set_Rectangle(fragment->get_Rectangle());
    fragment->get_ReplaceOptions()->set_FontSizeAdjustmentAction(
        TextReplaceOptions::FontSizeAdjustment::ShrinkToFit);
    fragment->get_ReplaceOptions()->set_ReplaceAdjustmentAction(
        TextReplaceOptions::ReplaceAdjustment::AdjustSpaceWidth);
    fragment->set_Text(text + String(u" ") + text);

    document->Save(outputFile);
}
```

### Replace a placeholder and set its style

Search all pages for the literal placeholder [Long_placeholder_Long_placeholder] and replace it with John Smith, South Development Studio. Set Calibri, 12-point size, and navy text. The supplied implementation does not explicitly configure paragraph reflow or replacement adjustment.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and search all pages for the literal placeholder `[Long_placeholder_Long_placeholder]`.
1. Replace each match with John Smith, South Development Studio.
1. Set the replacement text to 12-point Calibri in navy.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AutomaticallyRearrangePageContents(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(String(u"[Long_placeholder_Long_placeholder]"));
    document->get_Pages()->Accept(absorber);

    for (auto textFragment : absorber->get_TextFragments())
    {
        textFragment->set_Text(String(u"John Smith, South Development Studio"));
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Calibri")));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Navy());
    }

    document->Save(outputFile);
}
```

### Replace matches of a regular expression

On page 1, find values matching four digits, a hyphen, and four digits. Replace them with ABC1-2XZY and apply Verdana, blue foreground, and a light green background.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and enable regular-expression searching for four digits, a hyphen, and four more digits.
1. Visit page 1 and replace each match with `ABC1-2XZY`.
1. Apply Verdana, a blue foreground, and a light green background to each replacement.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <system/text/regularexpressions/regex.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextBasedOnRegex(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<System::Text::RegularExpressions::Regex>(String(u"\\d{4}-\\d{4}")));
    absorber->set_TextSearchOptions(MakeObject<TextSearchOptions>(true));
    document->get_Pages()->idx_get(1)->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        fragment->set_Text(String(u"ABC1-2XZY"));
        fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Verdana")));
        fragment->get_TextState()->set_FontSize(12);
        fragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        fragment->get_TextState()->set_BackgroundColor(Color::get_LightGreen());
    }

    document->Save(outputFile);
}
```

## Replace fonts and remove unused fonts

### Replace a specific font

Search all pages and change only fragments whose font name equals Arial-BoldMT to Verdana.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and collect text fragments from all pages.
1. Check each fragment’s font name and assign Verdana to fragments using `Arial-BoldMT`.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceFonts(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    document->get_Pages()->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        if (String(u"Arial-BoldMT") == fragment->get_TextState()->get_Font()->get_FontName())
        {
            fragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Verdana")));
        }
    }

    document->Save(outputFile);
}
```

### Replace fonts and remove unused resources

Create TextEditOptions with RemoveUnusedFonts, visit all pages, and change every found fragment font to Times New Roman. This example also replaces fonts; it is not only a resource cleanup operation.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) with [TextEditOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/texteditoptions/) set to remove unused fonts.
1. Visit every page and set the font of each collected fragment to Times New Roman.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextEditOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveUnusedFonts(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts);
    auto absorber = MakeObject<TextFragmentAbsorber>(options);
    document->get_Pages()->Accept(absorber);

    for (auto textFragment : absorber->get_TextFragments())
    {
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(String(u"Times New Roman")));
    }

    document->Save(outputFile);
}
```

## Remove text

### Remove text from the document

Call RemoveAllText with the document to remove text content across all pages, then save the result.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Pass the document to [RemoveAllText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/removealltext/) to remove text from all pages.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveAllTextUsingAbsorber1(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->RemoveAllText(document);
    document->Save(outputFile);
}
```

### Remove text from one page

Call RemoveAllText for page 1 only. Other pages are not passed to the removal method.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and retrieve page 1.
1. Pass that page to [RemoveAllText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/removealltext/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveAllTextUsingAbsorber2(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->RemoveAllText(document->get_Pages()->idx_get(1));
    document->Save(outputFile);
}
```

### Remove text from a page region

Remove text from the rectangle (10, 200, 120, 600) on page 1. The example does not remove all page content or process other pages.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and retrieve page 1.
1. Pass page 1 and the rectangle (10, 200, 120, 600) to [RemoveAllText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/removealltext/).
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveAllTextUsingAbsorber3(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->RemoveAllText(document->get_Pages()->idx_get(1),
                            MakeObject<Aspose::Pdf::Rectangle>(10, 200, 120, 600, true));
    document->Save(outputFile);
}
```

### Remove invisible text fragments

Visit all pages with replacement adjustment set to None. Set a fragment text to String::Empty only when its TextState::Invisible flag is true. This does not target every possible form of hidden content.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and configure a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) with replacement adjustment set to `None`.
1. Visit every page and inspect each fragment’s [Invisible](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) flag.
1. Set the text of fragments marked invisible to `String::Empty`.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextReplaceOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveHiddenText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto textAbsorber = MakeObject<TextFragmentAbsorber>();
    textAbsorber->set_TextReplaceOptions(
        MakeObject<TextReplaceOptions>(TextReplaceOptions::ReplaceAdjustment::None));
    document->get_Pages()->Accept(textAbsorber);

    for (auto &fragment : textAbsorber->get_TextFragments())
    {
        if (fragment->get_TextState()->get_Invisible())
        {
            fragment->set_Text(String::Empty);
        }
    }

    document->Save(outputFile);
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
