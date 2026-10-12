---
title: Region-based text extraction in C++
linktitle: Region-Based Extraction
type: docs
weight: 20
url: /cpp/region-based-extraction/
description: Extract text from a page rectangle and inspect the supplied paragraph geometry example using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Extract text from a page rectangle and inspect the supplied paragraph geometry example using Aspose.PDF for C++.

## Extract text from a rectangle

Limit extraction to a supplied region on a selected page.

Supply a valid page number and rectangle in the page coordinate system.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/) and [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/) using the supplied [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/).
1. Enable LimitToPageBounds and assign the search options.
1. Select pageNumber and call Accept() with the absorber.
1. Write the extracted text to the output file.

Source example: `region-based.cpp`.

```cpp
#include <system/io/file.h>
#include <system/io/memory_stream.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void ExtractTextFromRegion(
    System::String inputFile,
    System::String outputFile,
    int pageNumber,
    System::SharedPtr<Rectangle> rectangle)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextAbsorber>();
    auto options = MakeObject<TextSearchOptions>(rectangle);
    options->set_LimitToPageBounds(true);
    absorber->set_TextSearchOptions(options);
    document->get_Pages()->idx_get(pageNumber)->Accept(absorber);
    System::IO::File::WriteAllText(outputFile, absorber->get_Text());
}
```

