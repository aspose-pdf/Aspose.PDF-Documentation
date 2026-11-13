---
title: Add Line Annotation in C++
linktitle: Add Line Annotation
type: docs
weight: 30
url: /cpp/add-line-annotation/
description: Add Line Annotation in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Line Annotation with the PdfContentEditor Facade
Abstract: Create a red line annotation on page 1 with the specified endpoints, border, and line-ending settings.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add line annotation

Create a red line annotation on page 1 with the specified endpoints, border, and line-ending settings.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the line annotation with [PdfContentEditor::CreateLine()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createline/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/color.h>
#include <drawing/rectangle.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;
using DrawingColor = System::Drawing::Color;

void AddLineAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateLine(Rectangle(100, 100, 200, 200), u"This is line annotation", 100, 100, 200, 200, 1, 1,
                       DrawingColor::get_Red(), u"Solid", MakeArray<int32_t>({3, 2}), MakeArray<String>({u"Square"}));
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
