---
title: Create N-Up PDF Document in C++
linktitle: Create N-Up PDF Document
type: docs
weight: 10
url: /cpp/create-n-up-pdf-document/
description: Create N-Up PDF Document in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create N-Up PDF Document with the PdfFileEditor Facade
Abstract: Create N-up output using a 2 by 2 layout. Create a 2 by 2 N-up document and print a failure message if MakeNUp returns false.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create N-up PDF document

Create N-up output using a 2 by 2 layout.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate N-up output with [PdfFileEditor::MakeNUp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makenup/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateNupPdfDocument(String inputFile, String outputFile)
{
    auto nupMaker = MakeObject<PdfFileEditor>();
    nupMaker->MakeNUp(inputFile, outputFile, 2, 2);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Try create N-up PDF document

Create a 2 by 2 N-up document and print a failure message if MakeNUp returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate N-up output with [PdfFileEditor::MakeNUp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makenup/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <iostream>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void TryCreateNupPdfDocument(String inputFile, String outputFile)
{
    auto nupMaker = MakeObject<PdfFileEditor>();
    if (!nupMaker->MakeNUp(inputFile, outputFile, 2, 2))
    {
        std::cout << "Failed to create N-Up PDF document." << std::endl;
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```
