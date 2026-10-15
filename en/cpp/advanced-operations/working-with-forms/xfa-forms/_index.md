---
title: Convert XFA forms to AcroForms in C++
linktitle: XFA Forms
type: docs
weight: 80
url: /cpp/xfa-forms/
description: Convert an XFA form to a standard AcroForm and optionally ignore the NeedsRendering flag using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Change XFA Form Type to Standard AcroForm in C++
Abstract: Learn how to set a PDF form type to Standard with Aspose.PDF for C++. A second example checks XFA rendering flags before enabling IgnoreNeedsRendering and saving the converted document.
---

## Convert a dynamic XFA form

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) and set its Type to [FormType](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/formtype/)::Standard.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/FormType.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::ConvertDynamicXfaToAcroform(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Form()->set_Type(FormType::Standard);
    document->Save(outputFile);
}
```

## Convert with an XFA rendering-flag check

Review the converted fields and appearance for your input, especially when ignoring a rendering requirement.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) and check that it is not null.
1. When HasXfa and NeedsRendering are true, set IgnoreNeedsRendering to true.
1. Set Type to [FormType](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/formtype/)::Standard.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/FormType.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void FormExamples::ConvertXfaFormWithIgnoreNeedsRendering(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto form = document->get_Form();

    if (form != nullptr)
    {
        if (form->get_HasXfa() && form->get_NeedsRendering())
        {
            form->set_IgnoreNeedsRendering(true);
        }
        form->set_Type(FormType::Standard);
    }

    document->Save(outputFile);
}
```
