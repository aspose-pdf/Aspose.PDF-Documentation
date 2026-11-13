---
title: Add List Item in C++
linktitle: Add List Item
type: docs
weight: 10
url: /cpp/add-list-item/
description: Add List Item in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add List Item with the FormEditor Facade
Abstract: Add New Zealand as a choice in the Country field.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add list item

Add New Zealand as a choice in the Country field.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add choice items with [FormEditor::AddListItem()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/addlistitem/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FormEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;
	using FormEditor = Aspose::Pdf::Facades::FormEditor;

	void AddListItem(String inputFile, String outputFile)
	{
		auto editor = MakeObject<FormEditor>();

		editor->BindPdf(inputFile);
		editor->AddListItem(u"Country", MakeArray<String>({ u"New Zealand", u"New Zealand" }));
		editor->SaveableFacade::Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FormEditor
```
