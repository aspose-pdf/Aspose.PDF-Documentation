---
title: Add Text Annotations in C++
linktitle: Add Text Annotations
type: docs
weight: 50
url: /cpp/add-text-annotation/
description: Add Text Annotations in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Text Annotations with the PdfContentEditor Facade
Abstract: Create an open text annotation titled Text Annotation on page 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add text annotation

Create an open text annotation titled Text Annotation on page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the text annotation with [PdfContentEditor::CreateText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createtext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;

void AddTextAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateText(Rectangle(100, 400, 50, 50), u"Text Annotation", u"This is a text annotation", true, u"Insert",
                       1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
