---
title: Fill Barcode Fields in C++
linktitle: Fill Barcode Fields
type: docs
weight: 50
url: /cpp/fill-barcode-fields/
description: Fill Barcode Fields in C++ with the Form facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill Barcode Fields with the Form Facade
Abstract: Set product_barcode to 123456789012.
---

Use [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for this task. The examples below retain the original C++ code and API Reference steps.

## Fill barcode fields

Set product_barcode to 123456789012.

1. Create [Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the barcode field value with [Form::FillBarcodeField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/fillbarcodefield/).
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

void FillBarcodeFields(String inputFile, String outputFile)
{
    auto form = MakeObject<Form>();
    form->Facade::BindPdf(inputFile);
    form->FillBarcodeField(u"product_barcode", u"123456789012");
    form->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Form
```
