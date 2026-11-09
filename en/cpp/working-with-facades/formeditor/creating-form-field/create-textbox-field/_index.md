---
title: Create TextBox Field in C++
linktitle: Create TextBox Field
type: docs
weight: 60
url: /cpp/create-textbox-field/
description: Create TextBox Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create TextBox Field with the FormEditor Facade
Abstract: Add first_name and last_name text fields to page 1 with initial values Alexander and Smith.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create text box field

Add first_name and last_name text fields to page 1 with initial values Alexander and Smith.

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

	void CreateTextBoxField(String inputFile, String outputFile)
	{
		auto editor = MakeObject<FormEditor>();

		editor->BindPdf(inputFile);
		editor->AddField(FieldType::Text, u"first_name", u"Alexander", 1, 50, 570, 150, 590);
		editor->AddField(FieldType::Text, u"last_name", u"Smith", 1, 235, 570, 330, 590);
		editor->SaveableFacade::Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FormEditor
```
