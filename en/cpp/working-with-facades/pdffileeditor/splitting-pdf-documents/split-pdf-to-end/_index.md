---
title: Split PDF to End in C++
linktitle: Split PDF to End
type: docs
weight: 40
url: /cpp/split-pdf-to-end/
description: Split PDF to End in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Split PDF to End with the PdfFileEditor Facade
Abstract: Write pages from page 2 through the end to a new PDF.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Split PDF to end

Write pages from page 2 through the end to a new PDF.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write the ending page range with [PdfFileEditor::SplitToEnd()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splittoend/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfToEnd(String inputFile, String outputFile)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitToEnd(inputFile, 2, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
