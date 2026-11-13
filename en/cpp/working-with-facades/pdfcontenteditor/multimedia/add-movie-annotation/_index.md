---
title: Add Movie Annotation in C++
linktitle: Add Movie Annotation
type: docs
weight: 10
url: /cpp/add-movie-annotation/
description: Add Movie Annotation in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Movie Annotation with the PdfContentEditor Facade
Abstract: Create a movie annotation on page 1 using movieFile and the supplied display rectangle.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add movie annotation

Create a movie annotation on page 1 using movieFile and the supplied display rectangle.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the movie annotation with [PdfContentEditor::CreateMovie()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createmovie/).
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

void AddMovieAnnotation(String inputFile, String movieFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateMovie(Rectangle(80, 500, 220, 120), movieFile, 1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
