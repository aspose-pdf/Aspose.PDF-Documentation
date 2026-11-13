---
title: Add Margins to PDF Pages in C++
linktitle: Add Margins to PDF Pages
type: docs
weight: 10
url: /cpp/add-margins-to-pdf-pages/
description: Add Margins to PDF Pages in C++ with the PdfFileEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Margins to PDF Pages with the PdfFileEditor Facade
Abstract: Apply margins of 36 points on each side of pages 1 and 3.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add margins to PDF pages

Apply margins of 36 points on each side of pages 1 and 3.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Apply page margins with [PdfFileEditor::AddMargins()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/addmargins/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void AddMarginsToPdfPages(String inputFile, String outputFile)
	{
		auto pdfEditor = MakeObject<PdfFileEditor>();
		pdfEditor->AddMargins(inputFile, outputFile, MakeArray<int32_t>({ 1, 3 }), 36, 36, 36, 36);
	}
} // namespace  Facades::Examples::PDF_FileEditor
```
