---
title: Rename Form Fields in C++
linktitle: Rename Form Fields
type: docs
weight: 30
url: /cpp/rename-form-fields/
description: Rename Form Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rename Form Fields with the Form Facade
Abstract: Rename First Name and Last Name to NewFirstName and NewLastName.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Rename form fields

Rename First Name and Last Name to NewFirstName and NewLastName.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Rename the field with [Form::RenameField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/renamefield/).
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

void RenameFormFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->RenameField(u"First Name", u"NewFirstName");
    form->RenameField(u"Last Name", u"NewLastName");
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
