---
title: Delete All Images from PDF in C++
linktitle: Delete All Images from PDF
type: docs
weight: 10
url: /cpp/delete-all-images/
description: Delete All Images from PDF in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete All Images from PDF with the PdfContentEditor Facade
Abstract: Call DeleteImage() without arguments to remove images from the bound PDF.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Delete images

Call DeleteImage() without arguments to remove images from the bound PDF.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the images with [PdfContentEditor::DeleteImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteImages(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteImage();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
