---
title: Concatenate Two PDF Files in C++
linktitle: Concatenate Two PDF Files
type: docs
weight: 60
url: /cpp/concatenate-two-files/
description: Concatenate Two PDF Files in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenate Two PDF Files with the PdfFileEditor Facade
Abstract: Concatenate firstInputFile and secondInputFile in that order.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Merge PDF documents

Concatenate firstInputFile and secondInputFile in that order.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Merge the input files with [PdfFileEditor::Concatenate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/concatenate/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void MergePdfDocuments(String firstInputFile, String secondInputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Concatenate(MakeArray<String>({firstInputFile, secondInputFile}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```
