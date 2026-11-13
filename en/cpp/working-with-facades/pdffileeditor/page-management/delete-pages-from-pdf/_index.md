---
title: Delete Pages from PDF in C++
linktitle: Delete Pages from PDF
type: docs
weight: 20
url: /cpp/delete-pages-from-pdf/
description: Delete Pages from PDF in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Pages from PDF with the PdfFileEditor Facade
Abstract: Delete pages 2 and 4.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Delete pages from PDF

Delete pages 2 and 4.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Delete the selected pages with [PdfFileEditor::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/delete/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeletePagesFromPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Delete(inputFile, MakeArray<int32_t>({2, 4}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
