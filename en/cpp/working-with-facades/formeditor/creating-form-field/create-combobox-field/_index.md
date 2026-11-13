---
title: Create ComboBox Field in C++
linktitle: Create ComboBox Field
type: docs
weight: 20
url: /cpp/create-combobox-field/
description: Create ComboBox Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create ComboBox Field with the FormEditor Facade
Abstract: Create combobox1 on page 1 and add Australia and New Zealand choices.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create combo box field

Create combobox1 on page 1 and add Australia and New Zealand choices.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the fields with [FormEditor::AddField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfield/).
1. Add choice items with [FormEditor::AddListItem()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addlistitem/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FieldType.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateComboBoxField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddField(FieldType::ComboBox, u"combobox1", u"Australia", 1, 230, 498, 350, 514);
    editor->AddListItem(u"combobox1", MakeArray<String>({u"Australia", u"Australia"}));
    editor->AddListItem(u"combobox1", MakeArray<String>({u"New Zealand", u"New Zealand"}));
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
