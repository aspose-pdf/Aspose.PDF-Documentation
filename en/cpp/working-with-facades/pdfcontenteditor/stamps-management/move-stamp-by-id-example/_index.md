---
title: Move Stamp By ID in C++
linktitle: Move Stamp By ID
type: docs
weight: 80
url: /cpp/move-stamp-by-id-example/
description: Move Stamp By ID in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move Stamp By ID with the PdfContentEditor Facade
Abstract: Move stamp ID 1 on page 1 to (200, 200).
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Move stamp by id

Move stamp ID 1 on page 1 to (200, 200).

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Move the stamp by identifier with [PdfContentEditor::MoveStampById()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/movestampbyid/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void MoveStampById(String inputFile, String outputFile)
{
    auto pdfContentEditor = MakeObject<PdfContentEditor>();

    pdfContentEditor->BindPdf(inputFile);

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    pdfContentEditor->MoveStampById(pageId, stampId, x, y);

    pdfContentEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
