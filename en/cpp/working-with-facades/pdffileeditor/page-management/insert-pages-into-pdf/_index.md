---
title: Insert Pages into PDF in C++
linktitle: Insert Pages into PDF
type: docs
weight: 40
url: /cpp/insert-pages-into-pdf/
description: Insert Pages into PDF in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insert Pages into PDF with the PdfFileEditor Facade
Abstract: Insert pages 1 and 2 from sampleFile after page 2 of the input document.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Insert pages into PDF

Insert pages 1 and 2 from sampleFile after page 2 of the input document.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Insert source pages with [PdfFileEditor::Insert()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/insert/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void InsertPagesIntoPdf(String inputFile, String sampleFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Insert(inputFile, 2, sampleFile, MakeArray<int32_t>({1, 2}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
