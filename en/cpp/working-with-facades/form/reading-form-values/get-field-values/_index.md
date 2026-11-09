---
title: Get Field Values in C++
linktitle: Get Field Values
type: docs
weight: 50
url: /cpp/get-field-values/
description: Get Field Values in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get Field Values with the Form Facade
Abstract: Enumerate field names and print each field's current value.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Inspect form fields

Enumerate field names and print each field's current value.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read field names through [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Read each field value with [Form::GetField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/getfield/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_Form
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Form = Aspose::Pdf::Facades::Form;

void InspectFormFields(String inputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);

    for (auto fieldName : form->get_FieldNames())
    {
        std::cout << fieldName << " = " << form->GetField(fieldName) << std::endl;
    }
}
} // namespace Facades::Examples::PDF_Form
```
