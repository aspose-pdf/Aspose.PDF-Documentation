---
title: Export to FDF in C++
linktitle: Export to FDF
type: docs
weight: 10
url: /cpp/export-to-fdf/
description: Export to FDF in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export to FDF with the Form Facade
Abstract: Export the bound form data to an FDF output stream.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Export FDF

Export the bound form data to an FDF output stream.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Write FDF data with [Form::ExportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/exportfdf/).
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

void ExportFdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto outputStream = System::IO::File::Create(outputFile);

    form->Facade::BindPdf(inputFile);
    form->ExportFdf(outputStream);
}
} // namespace Facades::Examples::PDF_Form
```
