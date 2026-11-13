---
title: Split PDF from Beginning in C++
linktitle: Split PDF from Beginning
type: docs
weight: 10
url: /cpp/split-pdf-from-beginning/
description: Split PDF from Beginning in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Split PDF from Beginning with the PdfFileEditor Facade
Abstract: Write the first three pages to a new PDF.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Split PDF from beginning

Write the first three pages to a new PDF.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write the first page range with [PdfFileEditor::SplitFromFirst()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splitfromfirst/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfFromBeginning(String inputFile, String outputFile)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitFromFirst(inputFile, 3, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
