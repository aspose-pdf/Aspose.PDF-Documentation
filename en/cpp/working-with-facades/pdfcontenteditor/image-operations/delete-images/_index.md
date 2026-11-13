---
title: Delete Images from PDF in C++
linktitle: Delete Images from PDF
type: docs
weight: 20
url: /cpp/delete-images/
description: Delete Images from PDF in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Images from PDF with the PdfContentEditor Facade
Abstract: Delete image index 1 from page 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Delete image

Delete image index 1 from page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the images with [PdfContentEditor::DeleteImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteImage(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteImage(1, MakeArray<int32_t>({1}));

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
