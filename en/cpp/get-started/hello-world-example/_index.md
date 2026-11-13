---
title: Create a Hello World PDF in C++
linktitle: Hello World Example
type: docs
weight: 20
url: /cpp/hello-world-example/
description: Create a PDF containing positioned Hello, world! text with font, size, foreground, and background styling using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Position and Style Text in Your First C++ PDF
Abstract: Create a PDF page and place a TextFragment at explicit coordinates with Aspose.PDF for C++. The example applies Times New Roman, a 12-point size, yellow text, and a blue background before saving the document.
---

The SimpleExample function creates a PDF containing Hello, world! at position (100, 600). It uses Times New Roman at 12 points with a blue background and yellow text.

Configure the Aspose.PDF for C++ SDK and ensure Times New Roman is available. Pass a writable PDF path as outputFile.

## Create and style the text

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing Hello, world!.
1. Set its location with a [Position](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/position/) at (100, 600).
1. Configure the [TextFragmentState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) with size 12 and Times New Roman from [FontRepository::FindFont()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/findfont/).
1. Set the text background to blue and foreground to yellow using [Color](https://reference.aspose.com/pdf/cpp/aspose.pdf/color/).
1. Create a [TextBuilder](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/) for the page and call [AppendText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textbuilder/appendtext/).
1. Save the PDF with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Text/Position.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextBuilder.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SimpleExample(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto text = MakeObject<TextFragment>(u"Hello, world!");
    text->set_Position(MakeObject<Position>(100, 600));
    text->get_TextState()->set_FontSize(12);
    text->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    text->get_TextState()->set_BackgroundColor(Color::get_Blue());
    text->get_TextState()->set_ForegroundColor(Color::get_Yellow());
    MakeObject<TextBuilder>(page)->AppendText(text);
    document->Save(outputFile);
}
```

After running SimpleExample(outputFile), open the saved PDF to inspect the text position and colors.
