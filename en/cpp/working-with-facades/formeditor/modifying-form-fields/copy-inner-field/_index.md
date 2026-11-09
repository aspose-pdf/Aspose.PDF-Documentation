---
title: Copy Inner Field in C++
linktitle: Copy Inner Field
type: docs
weight: 20
url: /cpp/copy-inner-field/
description: Copy Inner Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copy Inner Field with the FormEditor Facade
Abstract: Copy First Name to First Name Copy on page 2 at the specified coordinates.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Copy inner field

Copy First Name to First Name Copy on page 2 at the specified coordinates.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Copy the field within the document with [FormEditor::CopyInnerField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/copyinnerfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CopyInnerField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->CopyInnerField(u"First Name", u"First Name Copy", 2, 200, 600);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
