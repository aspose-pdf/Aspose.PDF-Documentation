---
title: Export to XFDF in C++
linktitle: Export to XFDF
type: docs
weight: 20
url: /cpp/export-to-xfdf/
description: Export to XFDF in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export to XFDF with the Form Facade
Abstract: Export the bound form data to an XFDF output stream.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Export XFDF

Export the bound form data to an XFDF output stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Write XFDF data with [Form::ExportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/exportxfdf/).
1. Use the output stream as the exported data file.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void ExportXfdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto outputStream = System::IO::File::Create(outputFile);

    form->Facade::BindPdf(inputFile);
    form->ExportXfdf(outputStream);
}
} // namespace Facades::Examples::PDF_Form
```
