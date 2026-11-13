---
title: Bind a PDF Stream and Save in C++
linktitle: Bind a PDF Stream and Save
type: docs
weight: 10
url: /cpp/bind-from-stream-and-save/
description: Bind a PDF Stream and Save in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bind a PDF Stream and Save with the PdfContentEditor Facade
Abstract: Bind the editor to a PDF input stream and save it to outputFile.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Bind from stream and save

Bind the editor to a PDF input stream and save it to outputFile.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void BindFromStreamAndSave(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();
    auto inputStream = System::IO::File::OpenRead(inputFile);

    editor->BindPdf(inputStream);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
