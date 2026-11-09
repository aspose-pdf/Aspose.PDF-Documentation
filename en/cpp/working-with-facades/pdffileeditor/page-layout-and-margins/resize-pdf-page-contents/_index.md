---
title: Resize PDF Page Contents in C++
linktitle: Resize PDF Page Contents
type: docs
weight: 30
url: /cpp/resize-pdf-page-contents/
description: Resize PDF Page Contents in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Resize PDF Page Contents with the PdfFileEditor Facade
Abstract: Resize content on pages 1 and 3 using dimensions 400 and 750. Throw an error if ResizeContents returns false. Resize content on pages 1 and 2 using percentage-based margins of 10 on each side.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Resize PDF page contents

Resize content on pages 1 and 3 using dimensions 400 and 750. Throw an error if ResizeContents returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Resize page content with [PdfFileEditor::ResizeContents()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/resizecontents/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <stdexcept>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ResizePdfPageContents(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    if (!pdfEditor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1, 3}), 400, 750))
    {
        throw std::runtime_error("Failed to resize PDF page contents.");
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Resize content with percentage margins

Resize content on pages 1 and 2 using percentage-based margins of 10 on each side.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Resize page content with [PdfFileEditor::ResizeContents()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/resizecontents/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ResizePdfPageContents2(String inputFile, String outputFile)
{
    auto fileEditor = MakeObject<PdfFileEditor>();

    auto parameters = MakeObject<PdfFileEditor::ContentsResizeParameters>(

        PdfFileEditor::ContentsResizeValue::Percents(10),

        nullptr,

        PdfFileEditor::ContentsResizeValue::Percents(10),

        PdfFileEditor::ContentsResizeValue::Percents(10),

        nullptr,

        PdfFileEditor::ContentsResizeValue::Percents(10));

    fileEditor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1, 2}), parameters);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
