---
title: Flatten All Fields in C++
linktitle: Flatten All Fields
type: docs
weight: 10
url: /cpp/flatten-all-fields/
description: Flatten All Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Flatten All Fields with the Form Facade
Abstract: Flatten all form fields into page content before saving the PDF.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Flatten all fields

Flatten all form fields into page content before saving the PDF.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Flatten the fields with [Form::FlattenAllFields()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/flattenallfields/).
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

void FlattenAllFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FlattenAllFields();
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
