---
title: Extract an Image from a Stamp in C++
linktitle: Extract an Image from a Stamp
type: docs
weight: 10
url: /cpp/extract-image-from-stamp/
description: Extract an Image from a Stamp in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract an Image from a Stamp with the PdfContentEditor Facade
Abstract: Read page 1 stamps and save the first stamp image as PNG. Throw an error if no stamps are found.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Extract image from stamp

Read page 1 stamps and save the first stamp image as PNG. Throw an error if no stamps are found.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read page stamp information with [PdfContentEditor::GetStamps()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getstamps/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/StampInfo.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/image.h>
#include <drawing/imaging/image_format.h>
#include <stdexcept>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImageFromStamp(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();
    editor->BindPdf(inputFile);
    auto infos = editor->GetStamps(1);
    if (infos->get_Length() == 0)
        throw std::runtime_error("No stamps found");
    infos->idx_get(0)->get_Image()->Save(outputFile, System::Drawing::Imaging::ImageFormat::get_Png());
}
} // namespace Facades::Examples::PDF_ContentEditor
```
