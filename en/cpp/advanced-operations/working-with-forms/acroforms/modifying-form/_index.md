---
title: Modify PDF form fields in C++
linktitle: Modify AcroForm
type: docs
weight: 50
url: /cpp/modifying-form/
description: Read and set text-field limits, change field appearance, delete a named field, and clear text in selected Form XObjects using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Update PDF Field Limits, Fonts, and Form Content in C++
Abstract: Learn how to change text-field settings and remove a named AcroForm field with Aspose.PDF for C++. A separate example clears text inside matching Typewriter Form XObjects on the first page.
---

Read and set text-field limits, change field appearance, delete a named field, and clear text in selected Form XObjects using Aspose.PDF for C++.

## Read the first field text limit

The form must contain at least one field. Only the first field is inspected; outputFile is unused.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select index 0 from the form Fields array.
1. Cast the field to [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/).
1. Print MaxLen when the cast succeeds.

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TextBoxField.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Text;

void FormExamples::GetFieldLimit(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto field = document->get_Form()->get_Fields()->idx_get(0);
    if (auto textBoxField = field.dynamic_pointer_cast<TextBoxField>())
    {
        std::cout << (String::Format(u"Limit: {0}", textBoxField->get_MaxLen())) << std::endl;
    }
}
```

## Set a named field character limit

The input must contain the target field. This snippet retains the qualified base-class Save() call from the source.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) and bind the input PDF.
1. Call [SetFieldLimit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) for First Name with a limit of 15.
1. Save through the SaveableFacade base implementation.

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>

using namespace System;

void FormExamples::SetFieldLimit(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>();
    form->BindPdf(inputFile);
    form->SetFieldLimit(String(u"First Name"), 15);
    form->Aspose::Pdf::Facades::SaveableFacade::Save(outputFile);
}
```

## Change the first text field font

The form must have at least one field and Calibri must be available.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select form field index 0 and cast it to [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/).
1. Create a [DefaultAppearance](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/defaultappearance/) using Calibri from [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/), size 10, and black text.
1. Assign the appearance when the cast succeeds.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TextBoxField.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void FormExamples::SetFormFieldFont(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto field = document->get_Form()->get_Fields()->idx_get(0);
    if (auto textBoxField = field.dynamic_pointer_cast<TextBoxField>())
    {
        textBoxField->set_DefaultAppearance(MakeObject<DefaultAppearance>(
            FontRepository::FindFont(String(u"Calibri")), 10, Color::get_Black()->ToRgb()));
    }

    document->Save(outputFile);
}
```

## Delete a named AcroForm field

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call Delete() on [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) for the field named First Name.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void FormExamples::DeleteFormField(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Form()->Delete(String(u"First Name"));
    document->Save(outputFile);
}
```

## Clear text in matching Typewriter XObjects

This modifies selected Form XObjects, not the values of all AcroForm fields.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Enumerate [XForm](https://reference.aspose.com/pdf/cpp/aspose.pdf/xform/) resources on page 1.
1. Select resources whose IT is Typewriter and Subtype is Form.
1. Visit each selected resource with [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Set every detected fragment text to an empty string.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>

#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/FormType.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Text;

void FormExamples::ClearTextInForm(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& form : document->get_Pages()->idx_get(1)->get_Resources()->get_Forms())
    {
        if (String(u"Typewriter") == form->get_IT() && String(u"Form") == form->get_Subtype())
        {
            auto absorber = MakeObject<TextFragmentAbsorber>();
            absorber->Visit(form);

            for (auto& fragment : absorber->get_TextFragments())
            {
                fragment->set_Text(String::Empty);
            }
        }
    }
    document->Save(outputFile);
}
```
