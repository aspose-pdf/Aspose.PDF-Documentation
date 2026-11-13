---
title: Copy Outer Field in C++
linktitle: Copy Outer Field
type: docs
weight: 30
url: /cpp/copy-outer-field/
description: Copy Outer Field in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copy Outer Field with the FormEditor Facade
Abstract: Create a new one-page destination PDF and copy First Name from the source PDF onto it.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Copy outer field

Create a new one-page destination PDF and copy First Name from the source PDF onto it.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Copy the field from the other PDF with [FormEditor::CopyOuterField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/copyouterfield/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CopyOuterField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();

    document->get_Pages()->Add();
    document->Save(outputFile);

    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(outputFile);
    editor->CopyOuterField(inputFile, u"First Name", 1, 200, 600);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
