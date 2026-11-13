---
title: Add Document Action in C++
linktitle: Add Document Action
type: docs
weight: 20
url: /cpp/add-document-action/
description: Add Document Action in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Document Action with the PdfContentEditor Facade
Abstract: Assign an alert script to the document-open additional action.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add document action

Assign an alert script to the document-open additional action.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the document action with [PdfContentEditor::AddDocumentAdditionalAction()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/adddocumentadditionalaction/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddDocumentAction(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->AddDocumentAdditionalAction(PdfContentEditor::DocumentOpen,
                                        u"app.alert('Document opened with PdfContentEditor action');");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
