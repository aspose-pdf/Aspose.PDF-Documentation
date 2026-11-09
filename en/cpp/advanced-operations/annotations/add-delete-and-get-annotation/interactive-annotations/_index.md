---
title: Interactive annotations in C++
linktitle: Interactive annotations
type: docs
weight: 60
url: /cpp/interactive-annotations/
description: Add, inspect, and delete PDF links and create line annotations, navigation buttons, and a print button using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF Links and Navigation Buttons in C++
Abstract: Learn how to create URI links, inspect link rectangles, and remove link annotations with Aspose.PDF for C++. The examples also add a line with a popup, previous and next page buttons, and a print button using named actions.
---

These examples create URI links, a line with a popup, page navigation buttons, and a print button. Activating links and button actions requires a PDF viewer that supports the corresponding actions.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add line annotations

Create a line annotation on page 1, configure its title, color, starting style, ending style, width, border, popup, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [LineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/lineannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LineAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LineEnding.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Interactive {

    void LineAnnotationAdd(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto lineAnnotation = MakeObject<LineAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(550, 93, 562, 439, true),
            MakeObject<Point>(556, 99),
            MakeObject<Point>(556, 443));

        lineAnnotation->set_Title(u"John Smith");
        lineAnnotation->set_Color(Color::get_Red());
        lineAnnotation->set_StartingStyle(LineEnding::OpenArrow);
        lineAnnotation->set_EndingStyle(LineEnding::OpenArrow);

        auto border = MakeObject<Border>(lineAnnotation);
        border->set_Width(3);
        lineAnnotation->set_Border(border);

        auto popup = MakeObject<PopupAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(842, 124, 1021, 266, true));
        lineAnnotation->set_Popup(popup);

        document->get_Pages()->idx_get(1)->get_Annotations()->Add(lineAnnotation);
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotationsExamples::Interactive
```

## Add a URI link

Search for the first occurrence of "file" on page 1 and place a link to https://www.aspose.com over its rectangle. The source page must contain that text.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Find text with [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) over the first matching fragment.
1. Assign a [GoToURIAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/) to the link.
1. Add the annotation objects with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToURIAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Interactive {

    void LinkAdd(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"file");
        document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

        auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);
        auto linkAnnotation = MakeObject<LinkAnnotation>(
            document->get_Pages()->idx_get(1),
            phoneNumberFragment->get_Rectangle());
        linkAnnotation->set_Action(MakeObject<GoToURIAction>(u"https://www.aspose.com"));

        document->get_Pages()->idx_get(1)->get_Annotations()->Add(linkAnnotation);
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Interactive
```

## Get link annotations

Find link annotations on the first page and print their bounding rectangles.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) collection.
1. Filter the annotations using [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Read the matching [Annotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/) rectangles and print them.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Interactive {

void LinkGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Interactive
```

## Delete link annotations

Collect link annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) collection and filter by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Collect the matching annotations before modifying the collection.
1. Delete each collected annotation with [AnnotationCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/delete/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <vector>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Interactive {

    void LinkDelete(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        std::vector<SharedPtr<Annotation>> toDelete;
        for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
            if (annotation->get_AnnotationType() == AnnotationType::Link) {
                toDelete.push_back(annotation);
            }
        }
        for (auto& annotation : toDelete) {
            document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
        }
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Interactive
```

## Add page navigation buttons

Append a page, then add Previous Page and Next Page buttons to every page. Each button runs a predefined named action.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a page through [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create each [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) with its rectangle, label, and appearance.
1. Assign a [NamedAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/namedaction/) for previous or next page navigation.
1. Register the buttons with [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
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
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Forms;

namespace WorkingWithAnnotationsExamples::Interactive {

void NavigationButtonsAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Pages()->Add();

    struct ButtonConfig { String name; double xPos; PredefinedAction action; };
    const ButtonConfig buttonConfigs[] = {
        {u"Previous Page", 120.0, PredefinedAction::PrevPage},
        {u"Next Page", 230.0, PredefinedAction::NextPage}
    };
    for (auto& page : document->get_Pages()) {
        for (const auto& config : buttonConfigs) {
            auto rect = MakeObject<Rectangle>(config.xPos, 10.0, config.xPos + 100, 40.0, true);
            auto button = MakeObject<ButtonField>(page, rect);
            button->set_PartialName(config.name);
            button->set_Value(config.name);
            button->get_Characteristics()->set_Border(Color::get_Red()->ToRgb());
            button->get_Characteristics()->set_Background(Color::get_Orange()->ToRgb());
            button->get_Actions()->set_OnReleaseMouseBtn(MakeObject<NamedAction>(config.action));
            document->get_Form()->Add(StaticCast<Field>(button));
        }
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Interactive
```

## Add a print button

Create a new one-page PDF with a button that requests the viewer print action when released.

1. Create a PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a page through [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) and set its label and border.
1. Assign a [NamedAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/namedaction/) using File_Print.
1. Add the field with [Form::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/form/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/BorderStyle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
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
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Forms;

namespace WorkingWithAnnotationsExamples::Interactive {

    void PrintButtonAdd(System::String outputFile)
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();

        auto rect = MakeObject<Rectangle>(72, 748, 164, 768, true);
        auto printButton = MakeObject<ButtonField>(page, rect);
        printButton->set_AlternateName(u"Print current document");
        printButton->set_Color(Color::get_Black());
        printButton->set_PartialName(u"printBtn1");
        printButton->set_Value(u"Print Document");
        printButton->get_Actions()->set_OnReleaseMouseBtn(
            MakeObject<NamedAction>(PredefinedAction::File_Print));

        auto border = MakeObject<Border>(printButton);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        printButton->set_Border(border);

        printButton->get_Characteristics()->set_Border(Color::get_Blue()->ToRgb());
        printButton->get_Characteristics()->set_Background(Color::get_LightBlue()->ToRgb());

        document->get_Form()->Add(StaticCast<Field>(printButton));
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Interactive
```
