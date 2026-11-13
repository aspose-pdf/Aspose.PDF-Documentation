---
title: Rename Field in C++
linktitle: Rename Field
type: docs
weight: 70
url: /cpp/rename-field/
description: Rename Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rename Field with the FormEditor Facade
Abstract: Rename City to Town.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Rename field

Rename City to Town.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Rename the field with [FormEditor::RenameField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/renamefield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RenameField(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->RenameField(u"City", u"Town");
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
