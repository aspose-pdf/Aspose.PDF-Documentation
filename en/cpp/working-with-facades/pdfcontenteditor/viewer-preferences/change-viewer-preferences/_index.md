---
title: Change PDF Viewer Preferences in C++
linktitle: Change PDF Viewer Preferences
type: docs
weight: 10
url: /cpp/change-viewer-preferences/
description: Change PDF Viewer Preferences in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Change PDF Viewer Preferences with the PdfContentEditor Facade
Abstract: Read the existing viewer-preference flags and set the additional bit represented by 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Change viewer preferences

Read the existing viewer-preference flags and set the additional bit represented by 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the viewer flags with [PdfContentEditor::ChangeViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/changeviewerpreference/).
1. Read the viewer flags with [PdfContentEditor::GetViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getviewerpreference/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ChangeViewerPreferences(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->ChangeViewerPreference(editor->GetViewerPreference() | 1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
