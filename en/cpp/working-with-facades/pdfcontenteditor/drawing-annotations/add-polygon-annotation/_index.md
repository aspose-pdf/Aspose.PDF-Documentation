---
title: Add Polygon Annotation in C++
linktitle: Add Polygon Annotation
type: docs
weight: 40
url: /cpp/add-polygon-annotation/
description: Add Polygon Annotation in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Polygon Annotation with the PdfContentEditor Facade
Abstract: Create a page 1 polygon annotation using the LineInfo vertex array.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add polygon annotation

Create a page 1 polygon annotation using the LineInfo vertex array.

1. Set the polygon vertices and border through [LineInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/lineinfo/).
1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the polygon annotation with [PdfContentEditor::CreatePolygon()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createpolygon/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/LineInfo.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/rectangle.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;

void AddPolygonAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto lineInfo = MakeObject<LineInfo>();
    lineInfo->set_BorderStyle(0);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({100, 200, 150, 260, 220, 220, 200, 160}));
    editor->CreatePolygon(lineInfo, 1, Rectangle(90, 150, 150, 120), u"This is polygon annotation");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
