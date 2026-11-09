---
title: Set Submit Url in C++
linktitle: Set Submit Url
type: docs
weight: 40
url: /cpp/set-submit-url/
description: Set Submit Url in C++ with the FormEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set Submit Url with the FormEditor Facade
Abstract: Configure Script_Demo_Button to submit XFDF to the sample HTTPS endpoint.
---

Use [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Set submit url

Configure Script_Demo_Button to submit XFDF to the sample HTTPS endpoint.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the submission endpoint with [FormEditor::SetSubmitUrl()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setsubmiturl/).
1. Set the submission format with [FormEditor::SetSubmitFlag()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/setsubmitflag/).
1. Save the resulting PDF with [SaveableFacade::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/saveablefacade/save/).

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>
#include <Aspose.PDF.Cpp/Facades/SubmitFormFlag.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FormEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetSubmitUrl(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>();

    editor->BindPdf(inputFile);
    editor->SetSubmitUrl(u"Script_Demo_Button", u"https://www.example.com/submit");
    editor->SetSubmitFlag(u"Script_Demo_Button", SubmitFormFlag::Xfdf);
    editor->SaveableFacade::Save(outputFile);
}
} // namespace Facades::Examples::PDF_FormEditor
```
