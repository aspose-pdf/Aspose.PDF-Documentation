---
title: Add page numbers to PDF in C++
linktitle: Page Number Stamps
type: docs
weight: 120
url: /cpp/add-page-number/
description: Add a page-number stamp to the first PDF page or use Roman-number stamps on all pages with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Add a page-number stamp to the first PDF page or use Roman-number stamps on all pages with Aspose.PDF for C++.

## Number the first page

Only the first page is stamped. The total page count is inserted into the format string.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PageNumberStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagenumberstamp/) and set Format using # as the current-page placeholder.
1. Set bottom margin, alignment, and StartingNumber to 1.
1. Configure the text state with Arial from [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/).
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) on page 1.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-page-num-stamp.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PageNumberStamp.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of StampingExamples.addPageNumStamp.
void AddPageNumStamp(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    pageNumberStamp->set_Background(false);
    pageNumberStamp->set_Format(String::Format(u"Page # of {0}", document->get_Pages()->get_Count()));
    pageNumberStamp->set_BottomMargin(10);
    pageNumberStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    pageNumberStamp->set_StartingNumber(1);
    pageNumberStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    pageNumberStamp->get_TextState()->set_FontSize(14.0f);
    pageNumberStamp->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    pageNumberStamp->get_TextState()->set_ForegroundColor(Color::get_BlueViolet());

    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);
    document->Save(outputFile);
}
```

## Number all pages using Roman numerals

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PageNumberStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagenumberstamp/) with StartingNumber set to 42.
1. Set [NumberingStyle](https://reference.aspose.com/pdf/cpp/aspose.pdf/numberingstyle/) to NumeralsRomanUppercase.
1. Configure alignment, margin, and text state.
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) for every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-page-num-stamp-roman.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/NumberingStyle.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PageNumberStamp.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of StampingExamples.addPageNumStampRoman.
void AddPageNumStampRoman(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    pageNumberStamp->set_Background(false);
    pageNumberStamp->set_BottomMargin(10);
    pageNumberStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    pageNumberStamp->set_StartingNumber(42);
    pageNumberStamp->set_NumberingStyle(NumberingStyle::NumeralsRomanUppercase);
    pageNumberStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    pageNumberStamp->get_TextState()->set_FontSize(14.0f);
    pageNumberStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    pageNumberStamp->get_TextState()->set_ForegroundColor(Color::get_BlueViolet());

    for (const auto& page : document->get_Pages()) {
        page->AddStamp(pageNumberStamp);
    }
    document->Save(outputFile);
}
```
