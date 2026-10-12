---
title: Inspect fonts in PDF in C++
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /cpp/extract-fonts-from-pdf/
description: List the names of fonts used in a PDF document with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

List the names of fonts used in a PDF document with Aspose.PDF for C++.

## List document font names

Inspect the document font collection and print each name.

The example lists font names; it does not save embedded font files.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call GetAllFonts() through the document font utilities.
1. Iterate through the [Font](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/font/) objects and read FontName.
1. Print each font name.

Source example: `fonts.cpp`.

```cpp
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>

using namespace System;
using namespace Aspose::Pdf;
void ExtractFonts(System::String inputFile)
{

    // Open PDF document
    auto document = MakeObject<Document>(inputFile);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto& font : fonts)
    {
        Console::WriteLine(System::String(u"Font Name: {0}"), font->get_FontName());
    }
}
```
