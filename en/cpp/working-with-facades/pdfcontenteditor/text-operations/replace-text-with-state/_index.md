---
title: Replace Text With State in C++
linktitle: Replace Text With State
type: docs
weight: 50
url: /cpp/replace-text-with-state/
description: Replace Text With State in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace Text With State with the PdfContentEditor Facade
Abstract: Replace software with SOFTWARE using blue, 14-point text and ReplaceAll scope.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Replace text with state

Replace software with SOFTWARE using blue, 14-point text and ReplaceAll scope.

1. Configure text appearance through [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/).
1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace matching text with [PdfContentEditor::ReplaceText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replacetext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/ReplaceTextStrategy.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using namespace Aspose::Pdf::Text;
using PdfColor = Aspose::Pdf::Color;

void ReplaceTextWithState(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto textState = MakeObject<TextState>();
    textState->set_ForegroundColor(PdfColor::get_Blue());
    textState->set_FontSize(14);
    editor->get_ReplaceTextStrategy()->set_ReplaceScope(ReplaceTextStrategy::Scope::ReplaceAll);
    editor->ReplaceText(u"software", u"SOFTWARE", textState);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
