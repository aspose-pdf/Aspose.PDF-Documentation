---
title: Fill Check Box Fields in C++
linktitle: Fill Check Box Fields
type: docs
weight: 20
url: /cpp/fill-check-box-fields/
description: Fill Check Box Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill Check Box Fields with the Form Facade
Abstract: Set subscribe_newsletter and accept_terms to the export value Yes.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Fill check box fields

Set subscribe_newsletter and accept_terms to the export value Yes.

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

void FillCheckBoxFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillField(u"subscribe_newsletter", String(u"Yes"));
    form->FillField(u"accept_terms", String(u"Yes"));
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
