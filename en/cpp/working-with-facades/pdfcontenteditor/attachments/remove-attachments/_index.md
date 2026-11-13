---
title: Remove Attachments in C++
linktitle: Remove Attachments
type: docs
weight: 50
url: /cpp/remove-attachments/
description: Remove Attachments in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Attachments with the PdfContentEditor Facade
Abstract: Delete document attachments.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Remove attachments

Delete document attachments.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Remove document attachments with [PdfContentEditor::DeleteAttachments()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteattachments/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveAttachments(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteAttachments();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
