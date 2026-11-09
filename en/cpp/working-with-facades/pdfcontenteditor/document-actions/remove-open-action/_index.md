---
title: Remove Open Action in C++
linktitle: Remove Open Action
type: docs
weight: 30
url: /cpp/remove-open-action/
description: Remove Open Action in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Open Action with the PdfContentEditor Facade
Abstract: Remove the document-open action.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Remove open action

Remove the document-open action.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Remove the open action with [PdfContentEditor::RemoveDocumentOpenAction()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/removedocumentopenaction/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveOpenAction(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->RemoveDocumentOpenAction();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
