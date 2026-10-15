---
title: Add PDF form submission actions in C++
linktitle: Posting Forms
type: docs
weight: 60
url: /cpp/posting-form/
description: Add a submit button or configure an explicit SubmitFormAction in a PDF using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure PDF Submit Buttons and Submission Targets in C++
Abstract: Learn how to add form submission controls with Aspose.PDF for C++. One example uses FormEditor, while another attaches a SubmitFormAction to a button field.
---

Add a submit button or configure an explicit SubmitFormAction in a PDF using Aspose.PDF for C++.

## Add a submit button with FormEditor

The localhost URL is a sample submission target. Creating the PDF does not send the form; submission depends on activation in a supporting PDF viewer and an available endpoint.

1. Create [FormEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) with the input and output paths.
1. Call [AddSubmitBtn()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formeditor/) with the button name, page 1, caption, target URL, and rectangle.
1. Save the edited PDF.

```cpp
#include <Aspose.PDF.Cpp/Facades/FormEditor.h>

using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::FormEditor;
void FormExamples::AddSubmitButton(String inputFile, String outputFile)
{
    auto editor = MakeObject<FormEditor>(inputFile, outputFile);
    editor->AddSubmitBtn(String(u"submitbutton"), 1, String(u"Submit"),
        String(u"http://localhost/testing/show"), 100, 450, 150, 475);
    editor->Save();
}
```

## Attach a submit action to a button

The example retains http://localhost:3000/submit as a local sample endpoint. Adapt it to the receiving application; the snippet does not start a server or perform a submission.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [SubmitFormAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/submitformaction/) and set its URL through [FileSpecification](https://reference.aspose.com/pdf/cpp/aspose.pdf/filespecification/).
1. Set the ExportFormat and SubmitCoordinates flags.
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) on page 1, set its name and caption, and assign OnActivated.
1. Add the button to [Aspose::Pdf::Forms::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/) on page 1.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/RadioButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/SubmitFormAction.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>

#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;


void FormExamples::AddSubmitAction(String inputFile, String outputFile)
{

    auto document = MakeObject<Document>(inputFile);
    auto submitAction = MakeObject<SubmitFormAction>();
    submitAction->set_Url(MakeObject<FileSpecification>(String(u"http://localhost:3000/submit")));
    submitAction->set_Flags(SubmitFormAction::ExportFormat | SubmitFormAction::SubmitCoordinates);

    auto submitButton = MakeObject<ButtonField>(document->get_Pages()->idx_get(1),
        MakeObject<Aspose::Pdf::Rectangle>(10, 10, 100, 40));
    submitButton->set_PartialName(String(u"SubmitButton"));
    submitButton->set_Value(String(u"Submit"));
    submitButton->set_OnActivated(submitAction);

    document->get_Form()->Add(submitButton, 1);
    document->Save(outputFile);
}
```
