---
title: List Stamps in C++
linktitle: List Stamps
type: docs
weight: 70
url: /cpp/list-stamps/
description: List Stamps in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: List Stamps with the PdfContentEditor Facade
Abstract: Print the number of stamps returned for page 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## List stamps

Print the number of stamps returned for page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read page stamp information with [PdfContentEditor::GetStamps()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getstamps/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/StampInfo.h>
#include <drawing/image.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ListStamps(String inputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto stamps = editor->GetStamps(1);
    std::cout << "Stamps on page 1: " << stamps->get_Length() << std::endl;
}
} // namespace Facades::Examples::PDF_ContentEditor
```
