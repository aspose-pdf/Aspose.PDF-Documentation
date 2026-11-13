---
title: Replace Text Simple in C++
linktitle: Replace Text Simple
type: docs
weight: 40
url: /cpp/replace-text-simple/
description: Replace Text Simple in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text Simple with the PdfContentEditor Facade
Abstract: Set ReplaceAll scope and replace 33 with XXXIII followed by a space.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Replace text simple

Set ReplaceAll scope and replace 33 with XXXIII followed by a space.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace matching text with [PdfContentEditor::ReplaceText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replacetext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/ReplaceTextStrategy.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ReplaceTextSimple(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->get_ReplaceTextStrategy()->set_ReplaceScope(ReplaceTextStrategy::Scope::ReplaceAll);
    editor->ReplaceText(u"33", u"XXXIII ");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
