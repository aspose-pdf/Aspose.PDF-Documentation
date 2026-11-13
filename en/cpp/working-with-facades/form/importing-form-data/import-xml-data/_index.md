---
title: Import XML Data in C++
linktitle: Import XML Data
type: docs
weight: 40
url: /cpp/import-xml-data/
description: Import XML Data in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Import XML Data with the Form Facade
Abstract: Read XML data from dataFile and import it into the bound form.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Import XML

Read XML data from dataFile and import it into the bound form.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import XML data with [Form::ImportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/importxml/).
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

void ImportXml(String inputFile, String dataFile, String outputFile)
{
    auto form = MakeObject<Form>();
    auto inputStream = System::IO::File::OpenRead(dataFile);

    form->Facade::BindPdf(inputFile);
    form->ImportXml(inputStream);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
