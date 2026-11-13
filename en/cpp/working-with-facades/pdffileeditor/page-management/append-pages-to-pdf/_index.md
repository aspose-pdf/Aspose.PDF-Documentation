---
title: Append Pages to PDF in C++
linktitle: Append Pages to PDF
type: docs
weight: 10
url: /cpp/append-pages-to-pdf/
description: Append Pages to PDF in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Append Pages to PDF with the PdfFileEditor Facade
Abstract: Append page 1 from sampleFile to inputFile.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Append pages to PDF

Append page 1 from sampleFile to inputFile.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Append pages with [PdfFileEditor::Append()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/append/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AppendPagesToPdf(String inputFile, String sampleFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Append(inputFile, MakeArray<String>({sampleFile}), 1, 1, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
