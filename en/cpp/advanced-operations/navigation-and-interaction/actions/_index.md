---
title: Work with PDF actions in C++
linktitle: Actions
type: docs
weight: 20
url: /cpp/actions/
description: Add document and page actions, navigation buttons, print and hide buttons, and form submission actions using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure PDF Actions and Interactive Buttons in C++
Abstract: Create PDF document and page actions with Aspose.PDF for C++. The examples also add navigation controls and buttons for printing, hiding checkboxes, and submitting form data.
---

PDF actions are stored in the output file and run when triggered in a supporting viewer. The JavaScript and submit examples refer to a local service at http://localhost:3000. Adding or removing page actions requires at least three input pages.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Add document JavaScript actions

Set JavaScript actions for opening, saving, and printing the PDF. Despite the function name, this example creates JavascriptAction objects rather than LaunchAction objects. The URLs target a local service at http://localhost:3000.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [JavascriptAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/javascriptaction/) for each launchURL script.
1. Set the document [OpenAction](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/set_openaction/).
1. Set BeforeSaving and BeforePrinting through [DocumentActionCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/documentactioncollection/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DocumentActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/JavascriptAction.h>
#include <Aspose.PDF.Cpp/PageActionCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of ActionsExamples.addLaunchActions.
void AddLaunchActions(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->set_OpenAction(MakeObject<JavascriptAction>(u"app.launchURL('http://localhost:3000/open');"));
    document->get_Actions()->set_BeforeSaving(
    MakeObject<JavascriptAction>(u"app.launchURL('http://localhost:3000/save');"));
    document->get_Actions()->set_BeforePrinting(
    MakeObject<JavascriptAction>(u"app.launchURL('http://localhost:3000/print');"));

    document->Save(outputFile);
}
```

## Add page open and close actions

Require at least three pages and configure actions on page 3. Opening that page uses a GoToAction with an XYZ destination; closing it invokes a local URL through JavaScript.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check the [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) count and return if it is less than three.
1. Select page 3 and create a [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/) with an [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/xyzexplicitdestination/) at zoom 1.
1. Assign OnOpen and OnClose through [PageActionCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pageactioncollection/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DocumentActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/JavascriptAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/XYZExplicitDestination.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageActionCollection.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of ActionsExamples.addPageActions.
void AddPageActions(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() < 3) {
        std::cout << "Error: The document does not have at least 3 pages." << std::endl;
        return;
    }

    auto page = document->get_Pages()->idx_get(3);
    auto action = MakeObject<GoToAction>(page);
    action->set_Destination(MakeObject<XYZExplicitDestination>(page, 0, page->get_PageInfo()->get_Height(), 1));
    page->get_Actions()->set_OnOpen(action);
    page->get_Actions()->set_OnClose(
    MakeObject<JavascriptAction>(u"app.launchURL('http://localhost:3000/page/3');"));

    document->Save(outputFile);
}
```

## Remove page actions

Remove the actions attached to page 3. If the PDF contains fewer than three pages, print a message and return without saving.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check the [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) count.
1. Select page 3 and call [PageActionCollection::RemoveActions()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pageactioncollection/removeactions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DocumentActionCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageActionCollection.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of ActionsExamples.removePageActions.
void RemovePageActions(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() < 3) {
        std::cout << "Error: The document does not have at least 3 pages." << std::endl;
        return;
    }

    auto page = document->get_Pages()->idx_get(3);
    page->get_Actions()->RemoveActions();

    document->Save(outputFile);
}
```

## Add page navigation buttons

Add First Page, Previous Page, Next Page, and Last Page buttons to every page. First and previous buttons are read-only on the first page; next and last buttons are read-only on the last page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the document [Pages](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_pages/).
1. Create four [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) objects on each page and configure their labels and appearance.
1. Set ReadOnly at the document boundaries through [Field](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/field/) properties.
1. Assign [NamedAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/namedaction/) objects for the corresponding [PredefinedAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/predefinedaction/) values.
1. Add the fields with [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/NamedAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/PredefinedAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;

// Port of ActionsExamples.addNavigationButtons.
void AddNavigationButtons(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    int totalPages = document->get_Pages()->get_Count();

    for (const auto& page : document->get_Pages()) {
        auto firstPageButton = MakeObject<ButtonField>(page, MakeObject<Rectangle>(10, 10, 110, 40, true));
        firstPageButton->set_PartialName(u"First Page");
        firstPageButton->set_Value(u"First Page");
        firstPageButton->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
        firstPageButton->get_Characteristics()->set_Background(Color::get_Orange()->ToRgb());
        firstPageButton->set_ReadOnly(document->get_Pages()->IndexOf(page) == 1);
        firstPageButton->get_Actions()->set_OnReleaseMouseBtn(
        MakeObject<NamedAction>(PredefinedAction::FirstPage));
        document->get_Form()->Add(System::StaticCast<Field>(firstPageButton));

        auto previousPageButton = MakeObject<ButtonField>(page, MakeObject<Rectangle>(120, 10, 220, 40, true));
        previousPageButton->set_PartialName(u"Previous Page");
        previousPageButton->set_Value(u"Previous Page");
        previousPageButton->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
        previousPageButton->get_Characteristics()->set_Background(Color::get_Orange()->ToRgb());
        previousPageButton->set_ReadOnly(document->get_Pages()->IndexOf(page) == 1);
        previousPageButton->get_Actions()->set_OnReleaseMouseBtn(
        MakeObject<NamedAction>(PredefinedAction::PrevPage));
        document->get_Form()->Add(System::StaticCast<Field>(previousPageButton));

        auto nextPageButton = MakeObject<ButtonField>(page, MakeObject<Rectangle>(230, 10, 330, 40, true));
        nextPageButton->set_PartialName(u"Next Page");
        nextPageButton->set_Value(u"Next Page");
        nextPageButton->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
        nextPageButton->get_Characteristics()->set_Background(Color::get_Orange()->ToRgb());
        nextPageButton->set_ReadOnly(document->get_Pages()->IndexOf(page) == totalPages);
        nextPageButton->get_Actions()->set_OnReleaseMouseBtn(
        MakeObject<NamedAction>(PredefinedAction::NextPage));
        document->get_Form()->Add(System::StaticCast<Field>(nextPageButton));

        auto lastPageButton = MakeObject<ButtonField>(page, MakeObject<Rectangle>(340, 10, 440, 40, true));
        lastPageButton->set_PartialName(u"Last Page");
        lastPageButton->set_Value(u"Last Page");
        lastPageButton->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
        lastPageButton->get_Characteristics()->set_Background(Color::get_Orange()->ToRgb());
        lastPageButton->set_ReadOnly(document->get_Pages()->IndexOf(page) == totalPages);
        lastPageButton->get_Actions()->set_OnReleaseMouseBtn(
        MakeObject<NamedAction>(PredefinedAction::LastPage));
        document->get_Form()->Add(System::StaticCast<Field>(lastPageButton));
    }

    document->Save(outputFile);
}
```

## Add a print button

Create a Print button on page 1 with a one-unit border and a File_Print named action.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) on page 1.
1. Assign a [NamedAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/namedaction/) with File_Print to the release-mouse-button event.
1. Configure a [Border](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/border/) and add the field through [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/NamedAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/PredefinedAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;

// Port of ActionsExamples.addNamedActionPrint.
void AddNamedActionPrint(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(10, 10, 100, 40, true);
    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_PartialName(u"printButton");
    printButton->set_Value(u"Print");
    printButton->get_Actions()->set_OnReleaseMouseBtn(
    MakeObject<NamedAction>(PredefinedAction::File_Print));

    auto border = MakeObject<Border>(printButton);
    border->set_Width(1);
    printButton->set_Border(border);

    document->get_Form()->Add(printButton, 1);
    document->Save(outputFile);
}
```

## Add a button to hide checkboxes

Collect checkbox fields and create a Hide Checkboxes button on page 1. The button uses HideAction, even though the source function name includes NamedAction.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Collect the [CheckboxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/checkboxfield/) objects from the form.
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) on page 1.
1. Assign a [HideAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/hideaction/) targeting the collected annotations with the hide flag set to true.
1. Add the button with [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/collections/list.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/CheckboxField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/HideAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;

// Port of ActionsExamples.addNamedActionHide.
void AddNamedActionHide(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto checkboxes = MakeObject<System::Collections::Generic::List<SharedPtr<WidgetAnnotation>>>();
    for (const auto& field : document->get_Form()) {
        if (System::DynamicCast_noexcept<CheckboxField>(field)) {
            checkboxes->Add(System::DynamicCast<WidgetAnnotation>(field));
        }
    }

    auto rect = MakeObject<Rectangle>(10, 410, 140, 440, true);
    auto hideButton = MakeObject<ButtonField>(document->get_Pages()->idx_get(1), rect);
    hideButton->set_PartialName(u"HideButton");
    hideButton->set_Value(u"Hide Checkboxes");
    hideButton->get_Actions()->set_OnReleaseMouseBtn(
    MakeObject<HideAction>(checkboxes->ToArray(), true));

    document->get_Form()->Add(hideButton, 1);
    document->Save(outputFile);
}
```

## Add a form submission button

Add a Submit button targeting http://localhost:3000/submit. The action combines ExportFormat and SubmitCoordinates flags. Creating this PDF does not submit any data.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [SubmitFormAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/submitformaction/).
1. Configure a URL [FileSpecification](https://reference.aspose.com/pdf/cpp/aspose.pdf/filespecification/) and assign it to the action.
1. Set the flags on [SubmitFormAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/submitformaction/).
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/), assign the action to its release event, and register it with [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/SubmitFormAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Forms;

// Port of ActionsExamples.addSubmitAction.
void AddSubmitAction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto submitAction = MakeObject<SubmitFormAction>();
    auto submitUrl = MakeObject<FileSpecification>();
    submitUrl->set_FileSystem(u"URL");
    submitUrl->set_Name(u"http://localhost:3000/submit");
    submitAction->set_Url(submitUrl);
    submitAction->set_Flags(SubmitFormAction::ExportFormat | SubmitFormAction::SubmitCoordinates);

    auto rect = MakeObject<Rectangle>(10, 10, 100, 40, true);
    auto submitButton = MakeObject<ButtonField>(document->get_Pages()->idx_get(1), rect);
    submitButton->set_PartialName(u"SubmitButton");
    submitButton->set_Value(u"Submit");
    submitButton->get_Actions()->set_OnReleaseMouseBtn(submitAction);

    document->get_Form()->Add(submitButton, 1);
    document->Save(outputFile);
}
```
