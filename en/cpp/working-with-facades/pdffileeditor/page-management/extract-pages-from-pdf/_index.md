---
title: Extract Pages from PDF in C++
linktitle: Extract Pages from PDF
type: docs
weight: 30
url: /cpp/extract-pages-from-pdf/
description: Extract Pages from PDF in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Pages from PDF with the PdfFileEditor Facade
Abstract: Extract pages in the order 1, 4, 3.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Extract pages from PDF

Extract pages in the order 1, 4, 3.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Extract the selected pages with [PdfFileEditor::Extract()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/extract/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractPagesFromPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Extract(inputFile, MakeArray<int32_t>({1, 4, 3}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
