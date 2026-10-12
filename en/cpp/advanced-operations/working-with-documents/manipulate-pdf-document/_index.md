---
title: Manipulate PDF documents in C++
linktitle: Manipulate PDF documents
type: docs
weight: 30
url: /cpp/manipulate-pdf-document/
description: Validate PDF/A documents, create and format a table of contents, add an expiry alert, and flatten a PDF with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Validate PDF/A documents, create and format a table of contents, add an expiry alert, and flatten a PDF with Aspose.PDF for C++.

## Validate PDF/A-1a

The output path is a validation report, not a converted PDF. Validation does not convert the document.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Validate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/validate/) with the report output path and PdfFormat::PDF_A_1A.
1. Use the Boolean result to print the validation status.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>

using namespace System;
using namespace Aspose::Pdf;

void ValidatePdfaStandardA1a(String inputFile, String outputFile) {
    auto document = System::MakeObject<Document>(inputFile);
    if (document->Validate(outputFile, PdfFormat::PDF_A_1A)) {
        Console::WriteLine(u"Document is valid according to PDF/A-1a standard.");
    }
    else {
        Console::WriteLine(u"Document is not valid according to PDF/A-1a standard.");
    }
}
```

## Validate PDF/A-1b

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Validate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/validate/) with the report output path and PdfFormat::PDF_A_1B.
1. Use the Boolean result to print the validation status.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>

using namespace System;
using namespace Aspose::Pdf;

void ValidatePdfaStandardA1b(String inputFile, String outputFile) {
    auto document = System::MakeObject<Document>(inputFile);
    if (document->Validate(outputFile, PdfFormat::PDF_A_1B)) {
        Console::WriteLine(u"Document is valid according to PDF/A-1b standard.");
    }
    else {
        Console::WriteLine(u"Document is not valid according to PDF/A-1b standard.");
    }
}
```

## Add a table of contents

The example uses two supplied titles rather than detecting headings from the input PDF.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Insert a new page at position 1.
1. Create [TocInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/tocinfo/) and set its title using a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Create [Heading](https://reference.aspose.com/pdf/cpp/aspose.pdf/heading/) entries for up to two original pages.
1. Set each destination page and top coordinate, and add each entry to the TOC page.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/TocInfo.h>
#include <Aspose.PDF.Cpp/Generator/Heading.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTableOfContents(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto tocPage = document->get_Pages()->Insert(1);
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>(u"Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    const int length = 2;
    String titles[length] = { u"First page", u"Second page" };
    for (int index = 0; index < length && index + 2 <= document->get_Pages()->get_Count(); index++)
    {
        auto heading = MakeObject<Heading>(1);
        auto segment = MakeObject<TextSegment>(titles[index]);
        heading->set_TocPage(tocPage);
        heading->get_Segments()->Add(segment);
        auto destinationPage = document->get_Pages()->idx_get(index + 2);
        heading->set_DestinationPage(destinationPage);
        heading->set_Top(destinationPage->get_Rect()->get_Height());
        tocPage->get_Paragraphs()->Add(heading);
    }
    document->Save(outputFile);
}
```

## Format table of contents levels

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a TOC page and assign [TocInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/tocinfo/).
1. Configure four level formats with margins, leaders, and text styles.
1. Append a content page with [Heading](https://reference.aspose.com/pdf/cpp/aspose.pdf/heading/) objects for levels 1 through 4.
1. Enable automatic sequence and inclusion in the TOC.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Heading.h>
#include <Aspose.PDF.Cpp/Generator/LevelFormat.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TocInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TabStop.h>
#include <Aspose.PDF.Cpp/Text/TabStops.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SetTocLevels(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();
    tocInfo->set_LineDash(TabLeaderType::Solid);
    auto title = MakeObject<TextFragment>(u"Table Of Contents");
    title->get_TextState()->set_FontSize(30);
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()[0]->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()[0]->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()[0]->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()[0]->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()[1]->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()[1]->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()[1]->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()[1]->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()[2]->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()[2]->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()[2]->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()[3]->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()[3]->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()[3]->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()[3]->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    for (int level = 1; level < 5; level++) {
        auto heading = MakeObject<Heading>(level);
        heading->set_IsAutoSequence(true);
        heading->set_TocPage(tocPage);
        heading->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        heading->get_Segments()->Add(MakeObject<TextSegment>(String::Format(u"Sample Heading {0}", level)));
        heading->set_IsInList(true);
        page->get_Paragraphs()->Add(heading);
    }

    document->Save(outputFile);
}
```

## Hide page numbers in the TOC

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a TOC page and configure [TocInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/tocinfo/).
1. Set IsShowPageNumbers to false.
1. Configure the level formats and add a sample [Heading](https://reference.aspose.com/pdf/cpp/aspose.pdf/heading/) to a new content page.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Heading.h>
#include <Aspose.PDF.Cpp/Generator/LevelFormat.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TocInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void HidePageNumbersInToc(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>(u"Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->set_Title(title);
    tocInfo->set_IsShowPageNumbers(false);
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()[0]->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()[0]->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()[1]->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()[1]->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()[1]->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()[2]->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()[3]->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    auto heading = MakeObject<Heading>(1);
    heading->set_TocPage(tocPage);

    heading->set_IsAutoSequence(true);
    heading->set_IsInList(true);
    heading->get_Segments()->Add(MakeObject<TextSegment>(u"this is heading of level 1"));
    page->get_Paragraphs()->Add(heading);

    document->Save(outputFile);
}
```

## Add a prefix to TOC page numbers

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Insert a TOC page at position 1 and assign [TocInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/tocinfo/).
1. Set PageNumbersPrefix to P.
1. Create [Heading](https://reference.aspose.com/pdf/cpp/aspose.pdf/heading/) entries for all remaining pages and assign their destinations.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Heading.h>
#include <Aspose.PDF.Cpp/Generator/LevelFormat.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TocInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CustomizePageNumbersInToc(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto tocPage = document->get_Pages()->Insert(1);
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>(u"Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->set_Title(title);
    tocInfo->set_PageNumbersPrefix(u"P");
    tocPage->set_TocInfo(tocInfo);

    for (int index = 2; index <= document->get_Pages()->get_Count(); index++) {
        auto page = document->get_Pages()->idx_get(index);
        auto heading = MakeObject<Heading>(1);
        heading->set_TocPage(tocPage);
        heading->set_DestinationPage(page);
        heading->set_Top(page->get_Rect()->get_Height());
        heading->get_Segments()->Add(MakeObject<TextSegment>(String::Format(u"Page {0}", index - 1)));
        tocPage->get_Paragraphs()->Add(heading);
    }

    document->Save(outputFile);
}
```

## Add an expiry-date alert

This displays an alert in viewers that support and enable PDF JavaScript. It does not prevent access to the file and replaces any existing open action.

1. Validate the supplied calendar date.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Build JavaScript using the expiry date with a zero-based month.
1. Assign a [JavascriptAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/javascriptaction/) to OpenAction.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/date_time.h>
#include <system/string.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/JavascriptAction.h>

using namespace System;
using namespace Aspose::Pdf;

void SetPdfExpiryDate(String inputFile, String outputFile, int year, int month, int day)
{
    // DateTime validates the calendar date; JavaScript months are zero-based.
    const DateTime expiry(year, month, day);
    auto document = MakeObject<Document>(inputFile);
    auto code = String::Format(
        u"var expiry = new Date({0}, {1}, {2});\n"
        u"if (new Date().getTime() >= expiry.getTime())\n"
        u"    app.alert('The file is expired. You need a new one.');",
        expiry.get_Year(), expiry.get_Month() - 1, expiry.get_Day());
    // This is a viewer alert, not access control or encryption.
    document->set_OpenAction(MakeObject<Annotations::JavascriptAction>(code));
    document->Save(outputFile);
}
```

## Flatten a PDF

Flattening turns interactive content into page content. Keep the original PDF if you need to retain editable fields or annotations.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Flatten()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/flatten/) on the document.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

void FlattenFillablePdf(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->Flatten();
    document->Save(outputFile);
}
```
