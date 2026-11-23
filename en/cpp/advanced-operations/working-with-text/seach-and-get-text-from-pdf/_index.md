---
title: Search and Extract PDF Text in C++
linktitle: Search and Get Text
type: docs
weight: 60
url: /cpp/search-and-get-text-from-pdf/
description: Search and extract PDF text, inspect fragment properties, use regular expressions, and add links to matches using C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF text and inspect search results in C++
Abstract: Use TextAbsorber for extracted strings and TextFragmentAbsorber for text fragments and their properties. Examples cover page and region filters, regular expressions, multiple patterns, style inspection, hyperlinks, and page image output.
---

Use TextAbsorber when you need a text string and TextFragmentAbsorber when you need individual matches, positions, or font properties. The examples read existing PDF text; they do not perform OCR on scanned images. Page indexes in these C++ examples start at 1.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the existing PDF path as `inputFile`. Examples that access page 2 require at least two pages. Console-only examples do not use `outputFile`; the hyperlink example writes a PDF, and the page-rendering example writes PNG files.

The main APIs used here are [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/), [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/), [TextExtractionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textextractionoptions/), [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/), [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).

## Extract text and inspect fragments

### Extract text from a region on all pages

Use Pure text extraction and a search rectangle of (0, 0, 842, 250), then visit every page. Print the resulting extracted string; despite the console label, this is not a fragment count.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/) in [Pure](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textextractionoptions/) extraction mode.
1. Restrict extraction to the rectangle (0, 0, 842, 250) and visit every page.
1. Print the extracted text.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextExtractionOptions.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextAbsorberSearch(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto textExtractionOptions =
        MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);
    auto textSearchOptions =
        MakeObject<TextSearchOptions>(MakeObject<Aspose::Pdf::Rectangle>(0, 0, 842, 250, true));
    auto absorber = MakeObject<TextAbsorber>(textExtractionOptions, textSearchOptions);

    document->get_Pages()->Accept(absorber);
    std::cout << (String(u"Text fragments found: ") + absorber->get_Text()) << std::endl;
}
```

### Extract text from a region on page 2

Use the same extraction settings and rectangle, but visit only page 2. The input document must contain at least two pages.

1. Open a PDF containing at least two pages as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/) in [Pure](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textextractionoptions/) mode.
1. Restrict extraction to the rectangle (0, 0, 842, 250) and visit page 2.
1. Print the extracted text.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextExtractionOptions.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextAbsorberSearchPage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto textExtractionOptions =
        MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);
    auto textSearchOptions =
        MakeObject<TextSearchOptions>(MakeObject<Aspose::Pdf::Rectangle>(0, 0, 842, 250, true));
    auto absorber = MakeObject<TextAbsorber>(textExtractionOptions, textSearchOptions);

    document->get_Pages()->idx_get(2)->Accept(absorber);
    std::cout << (String(u"Text fragments found: ") + absorber->get_Text()) << std::endl;
}
```

### Inspect text fragment properties

Visit all pages and print each fragment text, position, X and Y indents, font name, font accessibility and embedding flags, subset status, size, and foreground color.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and visit all pages with a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Read each fragment’s text, position, font name and flags, font size, and foreground color.
1. Print the collected properties.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearch(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    document->get_Pages()->Accept(absorber);

	for (auto& fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
        std::cout << (String(u"XIndent: ") + fragment->get_Position()->get_XIndent()) << std::endl;
        std::cout << (String(u"YIndent: ") + fragment->get_Position()->get_YIndent()) << std::endl;
        std::cout << (String(u"Font - Name: ") + fragment->get_TextState()->get_Font()->get_FontName())
                  << std::endl;
        std::cout << (String(u"Font - IsAccessible: ") +
                      fragment->get_TextState()->get_Font()->get_IsAccessible())
                  << std::endl;
        std::cout << (String(u"Font - IsEmbedded: ") +
                      fragment->get_TextState()->get_Font()->get_IsEmbedded())
                  << std::endl;
        std::cout << (String(u"Font - IsSubset: ") +
                      fragment->get_TextState()->get_Font()->get_IsSubset())
                  << std::endl;
        std::cout << (String(u"Font Size: ") + fragment->get_TextState()->get_FontSize()) << std::endl;
        std::cout << (String(u"Foreground Color: ") + fragment->get_TextState()->get_ForegroundColor())
                  << std::endl;
    }
}
```

### Find a phrase on page 2

Search page 2 for whale and print the text and position of each result.

1. Open a PDF containing at least two pages as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) for `whale`.
1. Visit page 2 and print the text and position of each match.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchPage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(String(u"whale"));
    document->get_Pages()->idx_get(2)->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
    }
}
```

### Reuse an absorber across visits

Search page 1 for whale and print the accumulated results. Then visit page 2 and the whole document with the same absorber before printing again. Repeated visits can accumulate repeated matches; this is not a deduplicated page-by-page report.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and set the absorber phrase to `whale`.
1. Visit page 1 and print its matches.
1. Reuse the same absorber to visit page 2 and then the entire document.
1. Print the accumulated matches, including any duplicates.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSequentialSearch(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->set_Phrase(String(u"whale"));

    document->get_Pages()->idx_get(1)->Accept(absorber);
    for (auto fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Page: ") + fragment->get_Page()->get_Number()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
    }

    std::cout << (String(u"--")) << std::endl;

    document->get_Pages()->idx_get(2)->Accept(absorber);
    absorber->Visit(document);

    for (auto fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Page: ") + fragment->get_Page()->get_Number()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
    }
}
```

## Search phrases and patterns

### Find a phrase in a page region

Search for elephant within (0, 0, 842, 250) on page 2 and print each match and its position.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and configure a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) for `elephant` within (0, 0, 842, 250).
1. Visit page 2 and print each match and its position.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchPhrase(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(
        String(u"elephant"),
        MakeObject<TextSearchOptions>(MakeObject<Aspose::Pdf::Rectangle>(0, 0, 842, 250, true)));

    document->get_Pages()->idx_get(2)->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
    }
}
```

### Search with a regular expression

Search page 2 for decimal numbers using the pattern \d+\.\d+ with regular-expression searching enabled.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and configure a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) with the decimal-number pattern `\d+\.\d+` and regular-expression searching.
1. Visit page 2 and print each match and its position.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>
#include <system/text/regularexpressions/regex.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchRegex(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<System::Text::RegularExpressions::Regex>(String(u"\\d+\\.\\d+")),
        MakeObject<TextSearchOptions>(true));

    document->get_Pages()->idx_get(2)->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
        std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
    }
}
```

### Search multiple patterns

Search every page using separate whale and elephant regular expressions. Read each pattern result collection from RegexResults and print fragment text and position.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and create an absorber with separate regular expressions for `whale` and `elephant`.
1. Visit all pages and retrieve each pattern’s matches from [RegexResults](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Print the text and position of each match.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>
#include <system/array.h>
#include <system/collections/dictionary.h>
#include <system/text/regularexpressions/regex.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchListOfPhrases(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto patterns = MakeArray<SharedPtr<System::Text::RegularExpressions::Regex>>(
        {MakeObject<System::Text::RegularExpressions::Regex>(String(u"whale")),
         MakeObject<System::Text::RegularExpressions::Regex>(String(u"elephant"))});
    auto absorber = MakeObject<TextFragmentAbsorber>(patterns, MakeObject<TextSearchOptions>(true));
    document->get_Pages()->Accept(absorber);

    for (auto fragments : absorber->get_RegexResults()->get_Values())
    {
        for (auto fragment : fragments)
        {
            std::cout << (String(u"Text: ") + fragment->get_Text()) << std::endl;
            std::cout << (String(u"Position: ") + fragment->get_Position()) << std::endl;
        }
    }
}
```

## Use and inspect search results

### Turn matched words into hyperlinks

On page 1, search for whale or elephant, style each match in blue with an underline, and assign a Wikipedia WebHyperlink based on the matched word. Save the modified PDF.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and search page 1 for `whale` or `elephant` using a regular expression.
1. Style each matching fragment in blue with an underline.
1. Assign a [WebHyperlink](https://reference.aspose.com/pdf/cpp/aspose.pdf/webhyperlink/) to the Wikipedia article for the matched word.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/WebHyperlink.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchAndAddHyperlink(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>(String(u"whale|elephant"));
    absorber->set_TextSearchOptions(MakeObject<TextSearchOptions>(true));
    absorber->Visit(document->get_Pages()->idx_get(1));

    for (auto fragment : absorber->get_TextFragments())
    {
        fragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        fragment->get_TextState()->set_Underline(true);
        fragment->set_Hyperlink(
            MakeObject<WebHyperlink>(String(u"https://en.wikipedia.org/wiki/") + fragment->get_Text()));
    }

    document->Save(outputFile);
}
```

### Inspect bold and invisible fragments

Visit page 1 and print fragments whose FontStyle equals Bold, and fragments with Invisible enabled. The equality check targets the exact Bold value rather than every combination containing the bold flag.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and collect text fragments from page 1.
1. Print the text of fragments whose font style equals `Bold`.
1. Check the [Invisible](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) flag independently and print the text of fragments marked invisible.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextFragmentAbsorberSearchStyledText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    absorber->set_TextSearchOptions(MakeObject<TextSearchOptions>(true));
    absorber->Visit(document->get_Pages()->idx_get(1));

    for (auto fragment : absorber->get_TextFragments())
    {
        if (fragment->get_TextState()->get_FontStyle() == FontStyles::Bold)
        {
            std::cout << (String(u"Bold: ") + fragment->get_Text()) << std::endl;
        }
        if (fragment->get_TextState()->get_Invisible())
        {
            std::cout << (String(u"Invisible: ") + fragment->get_Text()) << std::endl;
        }
    }
}
```

### Render pages and report text coordinates

Search non-whitespace runs on every page, render each page to PNG at 150 DPI, and print fragment and page upper Y coordinates. Pass an outputFile ending in .png so the page number can be inserted into each output name. The supplied implementation does not draw highlight annotations or save a highlighted PDF.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and configure a regular-expression absorber to match non-whitespace runs.
1. Visit each page and render it to a numbered PNG at 150 DPI with [PngDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/pngdevice/).
1. Print each matched fragment’s upper Y coordinate alongside the page’s upper Y coordinate.

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <iostream>
#include <system/io/file.h>
#include <system/io/memory_stream.h>
#include <system/text/regularexpressions/regex.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Devices;

void TextFragmentAbsorberSearchAndHighlight(String inputFile, String outputFile)
{
    int resolution = 150;
    auto pngDevice = MakeObject<PngDevice>(MakeObject<Resolution>(resolution, resolution));

    {
        auto document = MakeObject<Document>(inputFile);
        auto absorber = MakeObject<TextFragmentAbsorber>(
            MakeObject<System::Text::RegularExpressions::Regex>(String(u"[\\S]+")));
        absorber->set_TextSearchOptions(MakeObject<TextSearchOptions>(true));

        for (int pageNumber = 1; pageNumber <= document->get_Pages()->get_Count(); pageNumber++)
        {
            auto page = document->get_Pages()->idx_get(pageNumber);
            page->Accept(absorber);

            {
                auto stream = MakeObject<System::IO::MemoryStream>();
                pngDevice->Process(page, stream);
                auto output = outputFile.Replace(u".png", String::Format(u"_{0}.png", page->get_Number()));
                System::IO::File::WriteAllBytes(output, stream->ToArray());
            }

            for (auto textFragment : absorber->get_TextFragments())
            {
                auto pageRect = page->GetPageRect(true);
                std::cout << (String(u"TextFragment = ") + textFragment->get_Text() +
                              String(u" Page URY = ") + pageRect->get_URY() +
                              String(u" TextFragment URY = ") + textFragment->get_Rectangle()->get_URY())
                          << std::endl;
            }
        }
    }
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
