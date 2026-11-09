---
title: Import XFDF Data in C++
linktitle: Import XFDF Data
type: docs
weight: 20
url: /cpp/import-xfdf-data/
description: Import XFDF Data in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Import XFDF Data with the Form Facade
Abstract: Read XFDF data from dataFile and import it into the bound form.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Import XFDF

Read XFDF data from dataFile and import it into the bound form.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import XFDF data with [Form::ImportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/importxfdf/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

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

void ImportXfdf(String inputFile, String dataFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto inputStream = System::IO::File::OpenRead(dataFile);

    form->Facade::BindPdf(inputFile);
    form->ImportXfdf(inputStream);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
