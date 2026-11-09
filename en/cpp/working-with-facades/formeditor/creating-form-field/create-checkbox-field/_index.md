---
title: Create CheckBox Field in C++
linktitle: Create CheckBox Field
type: docs
weight: 10
url: /cpp/create-checkbox-field/
description: Create CheckBox Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create CheckBox Field with the FormEditor Facade
Abstract: Add checkbox1 to page 1 with its name, caption, and rectangle.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create check box field

Add checkbox1 to page 1 with its name, caption, and rectangle.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the fields with [FormEditor::AddField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FieldType.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateCheckBoxField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddField(FieldType::CheckBox, u"checkbox1", u"Check Box 1", 1, 240, 498, 256, 514);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
