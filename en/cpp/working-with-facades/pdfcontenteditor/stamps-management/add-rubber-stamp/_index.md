---
title: Add Rubber Stamp in C++
linktitle: Add Rubber Stamp
type: docs
weight: 10
url: /cpp/add-rubber-stamp/
description: Add Rubber Stamp in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Rubber Stamp with the PdfContentEditor Facade
Abstract: Create a green Approved rubber-stamp annotation on page 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add rubber stamp

Create a green Approved rubber-stamp annotation on page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the rubber-stamp annotation with [PdfContentEditor::CreateRubberStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createrubberstamp/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/color.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;
using DrawingColor = System::Drawing::Color;

void AddRubberStamp(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateRubberStamp(1, Rectangle(120, 450, 180, 60), u"Approved", u"Approved by reviewer",
                              DrawingColor::get_Green());
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
