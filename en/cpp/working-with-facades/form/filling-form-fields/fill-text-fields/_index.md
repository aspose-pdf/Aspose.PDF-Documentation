---
title: Fill Text Fields in C++
linktitle: Fill Text Fields
type: docs
weight: 10
url: /cpp/fill-text-fields/
description: Fill Text Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill Text Fields with the Form Facade
Abstract: Fill name, address, and email with the sample contact details.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Fill text fields

Fill name, address, and email with the sample contact details.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Fill the named fields with [Form::FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillfield/).
1. Save the resulting PDF with [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void FillTextFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"name", String(u"John Doe"));
    form->FillField(u"address", String(u"123 Main St, Anytown, USA"));
    form->FillField(u"email", String(u"john.doe@example.com"));
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
