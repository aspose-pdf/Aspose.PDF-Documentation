---
title: Get PDF Viewer Preferences in C++
linktitle: Get PDF Viewer Preferences
type: docs
weight: 20
url: /cpp/get-viewer-preferences/
description: Get PDF Viewer Preferences in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get PDF Viewer Preferences with the PdfContentEditor Facade
Abstract: Print the current viewer-preference flags.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get viewer preferences

Print the current viewer-preference flags.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read the viewer flags with [PdfContentEditor::GetViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getviewerpreference/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetViewerPreferences(String inputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    std::cout << "Current viewer preference: " << editor->GetViewerPreference() << std::endl;
}
} // namespace Facades::Examples::PDF_ContentEditor
```
