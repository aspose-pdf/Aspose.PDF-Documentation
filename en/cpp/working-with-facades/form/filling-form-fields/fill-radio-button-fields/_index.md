---
title: Fill Radio Button Fields in C++
linktitle: Fill Radio Button Fields
type: docs
weight: 30
url: /cpp/fill-radio-button-fields/
description: Fill Radio Button Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill Radio Button Fields with the Form Facade
Abstract: Select option index 0 in the gender field.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Fill radio button fields

Select option index 0 in the gender field.

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

void FillRadioButtonFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"gender", 0);
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
