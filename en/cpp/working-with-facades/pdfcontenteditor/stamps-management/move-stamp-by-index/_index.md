---
title: Move Stamp By Index in C++
linktitle: Move Stamp By Index
type: docs
weight: 90
url: /cpp/move-stamp-by-index/
description: Move Stamp By Index in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move Stamp By Index with the PdfContentEditor Facade
Abstract: Move stamp index 0 on page 1 to (200, 200).
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Change stamp position

Move stamp index 0 on page 1 to (200, 200).

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Move the stamp by index with [PdfContentEditor::MoveStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/movestamp/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ChangeStampPosition(String inputFile, String outputFile)
{
    auto pdfContentEditor = MakeObject<PdfContentEditor>();

    pdfContentEditor->BindPdf(inputFile);

    int pageId = 1;
    int stampIndex = 0;
    double x = 200;
    double y = 200;

    pdfContentEditor->MoveStamp(pageId, stampIndex, x, y);

    pdfContentEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
