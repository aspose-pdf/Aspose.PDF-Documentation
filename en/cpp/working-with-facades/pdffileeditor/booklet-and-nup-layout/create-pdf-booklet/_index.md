---
title: Create PDF Booklet in C++
linktitle: Create PDF Booklet
type: docs
weight: 20
url: /cpp/create-pdf-booklet/
description: Create PDF Booklet in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF Booklet with the PdfFileEditor Facade
Abstract: Create booklet output with the default MakeBooklet overload. Create a booklet and print a failure message if MakeBooklet returns false.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create PDF booklet

Create booklet output with the default MakeBooklet overload.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate booklet output with [PdfFileEditor::MakeBooklet()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makebooklet/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreatePdfBooklet(String inputFile, String outputFile)
{
    auto bookletMaker = MakeObject<PdfFileEditor>();
    bookletMaker->MakeBooklet(inputFile, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Try create PDF booklet

Create a booklet and print a failure message if MakeBooklet returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate booklet output with [PdfFileEditor::MakeBooklet()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makebooklet/).
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

void TryCreatePdfBooklet(String inputFile, String outputFile)
{
    auto bookletMaker = MakeObject<PdfFileEditor>();
    if (!bookletMaker->MakeBooklet(inputFile, outputFile))
    {
        std::cout << "Failed to create booklet." << std::endl;
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```
