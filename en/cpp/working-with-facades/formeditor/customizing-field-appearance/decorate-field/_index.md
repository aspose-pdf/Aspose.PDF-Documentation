---
title: Decorate Field in C++
linktitle: Decorate Field
type: docs
weight: 10
url: /cpp/decorate-field/
description: Decorate Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decorate Field with the FormEditor Facade
Abstract: Apply a red background, blue text, green border, and centered alignment to First Name.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Decorate field

Apply a red background, blue text, green border, and centered alignment to First Name.

1. Configure the field colors and alignment with [FormFieldFacade](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formfieldfacade/).
1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set facade through [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) using the example values.
1. Apply the configured appearance with [FormEditor::DecorateField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/decoratefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Facades/FormFieldFacade.h>
#include <drawing/color.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using DrawingColor = System::Drawing::Color;

void DecorateField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    auto facade = MakeObject<FormFieldFacade>();
    facade->set_BackgroundColor(DrawingColor::get_Red());
    facade->set_TextColor(DrawingColor::get_Blue());
    facade->set_BorderColor(DrawingColor::get_Green());
    facade->set_Alignment(FormFieldFacade::AlignCenter);
    editor->set_Facade(facade);
    editor->DecorateField(u"First Name");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
