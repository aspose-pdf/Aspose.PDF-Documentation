---
title: Add text stamps to PDF in C++
linktitle: Text Stamps
type: docs
weight: 110
url: /cpp/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF page and configure its font, color, position, and rotation using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Add a text stamp to a PDF page and configure its font, color, position, and rotation using Aspose.PDF for C++.

## Add a styled text stamp

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/textstamp/) containing Sample Stamp.
1. Set background mode, position, and 90-degree rotation.
1. Use [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/) to select Arial and configure the stamp text state.
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) on page 1.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-text-stamp.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rotation.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <Aspose.PDF.Cpp/TextStamp.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of StampingExamples.addTextStamp.
void AddTextStamp(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto textStamp = MakeObject<TextStamp>(u"Sample Stamp");
    textStamp->set_Background(true);
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    textStamp->set_Rotate(Rotation::on90);
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0f);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_DarkGreen());
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);
    document->Save(outputFile);
}
```
