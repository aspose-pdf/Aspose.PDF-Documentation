---
title: Replace Images in PDF in C++
linktitle: Replace Images in PDF
type: docs
weight: 30
url: /cpp/replace-image/
description: Replace Images in PDF in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Images in PDF with the PdfContentEditor Facade
Abstract: Replace image index 1 on page 1 with imageFile.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Replace image

Replace image index 1 on page 1 with imageFile.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace the selected image with [PdfContentEditor::ReplaceImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replaceimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ReplaceImage(String inputFile, String imageFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->ReplaceImage(1, 1, imageFile);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
