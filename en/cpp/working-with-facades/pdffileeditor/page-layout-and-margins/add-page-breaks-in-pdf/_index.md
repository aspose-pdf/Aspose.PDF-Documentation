---
title: Add Page Breaks in PDF in C++
linktitle: Add Page Breaks in PDF
type: docs
weight: 20
url: /cpp/add-page-breaks-in-pdf/
description: Add Page Breaks in PDF in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Page Breaks in PDF with the PdfFileEditor Facade
Abstract: Insert a page break on page 1 at the position specified by 400.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add page breaks in PDF

Insert a page break on page 1 at the position specified by 400.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Insert the page break with [PdfFileEditor::AddPageBreak()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/addpagebreak/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageBreaksInPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->AddPageBreak(
        inputFile, outputFile,
        MakeArray<SharedPtr<PdfFileEditor::PageBreak>>({MakeObject<PdfFileEditor::PageBreak>(1, 400)}));
}
} // namespace  Facades::Examples::PDF_FileEditor
```
