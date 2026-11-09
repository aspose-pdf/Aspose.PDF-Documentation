---
title: Split PDF into Single Pages in C++
linktitle: Split PDF into Single Pages
type: docs
weight: 30
url: /cpp/split-pdf-into-single-pages/
description: Split PDF into Single Pages in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Split PDF into Single Pages with the PdfFileEditor Facade
Abstract: Split the PDF into individual pages using outputFilePattern.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Split PDF into single pages

Split the PDF into individual pages using outputFilePattern.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write individual page files with [PdfFileEditor::SplitToPages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splittopages/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfIntoSinglePages(String inputFile, String outputFilePattern)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitToPages(inputFile, outputFilePattern);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
