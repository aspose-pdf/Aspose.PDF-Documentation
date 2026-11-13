---
title: Set Field Script in C++
linktitle: Set Field Script
type: docs
weight: 30
url: /cpp/set-field-script/
description: Set Field Script in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set Field Script with the FormEditor Facade
Abstract: Add an alert script to Script_Demo_Button, then replace it with a second alert script.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Set field script

Add an alert script to Script_Demo_Button, then replace it with a second alert script.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add a field script with [FormEditor::AddFieldScript()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addfieldscript/).
1. Replace the field script with [FormEditor::SetFieldScript()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setfieldscript/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetFieldScript(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->AddFieldScript(u"Script_Demo_Button", u"app.alert('Script 1 has been executed');");
    editor->SetFieldScript(u"Script_Demo_Button", u"app.alert('Script 2 has been executed');");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
