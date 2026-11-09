---
title: Update PDF links in C++
linktitle: Update Links
type: docs
weight: 20
url: /cpp/update-links/
description: Change PDF link colors, recolor text in link regions, and update web destination URIs using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify PDF Link Appearance and URI Targets in C++
Abstract: Update link annotation color, text appearance, and web destinations on the first page with Aspose.PDF for C++. The text-color sample expands link rectangles and searches the resulting regions for text fragments.
---

These examples modify existing links on page 1. Use a PDF containing link annotations; the URI update applies only to links with GoToURIAction.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Change link annotation color

Set each link annotation on page 1 to red. Despite the filename, the sample changes Color only; it does not change border width or dash settings.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter page 1 annotations by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Cast matching objects to [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/).
1. Set the annotation [Color](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/set_color/) to red.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of links/UpdateExamples.linkAnnotationUpdateBorder.
void LinkAnnotationUpdateBorder(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (const auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link && System::DynamicCast_noexcept<LinkAnnotation>(annotation)) {
            auto linkAnnotation = System::DynamicCast<LinkAnnotation>(annotation);
            linkAnnotation->set_Color(Color::get_Red());
        }
    }

    document->Save(outputFile);
}
```

## Change text color in link regions

For each page 1 link, expand its rectangle by 2 units on every side and set matching text fragments to red. The code modifies the annotation rectangle itself and can include nearby text.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the rectangle of each Link annotation through [Annotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/).
1. Expand its coordinates through [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) properties.
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) and restrict it with [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/).
1. Visit page 1 and set each fragment's [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) foreground color to red.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

// Port of links/UpdateExamples.linkAnnotationUpdateTextColor.
void LinkAnnotationUpdateTextColor(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (const auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link) {
            auto absorber = MakeObject<TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 2);
            rect->set_LLY(rect->get_LLY() - 2);
            rect->set_URX(rect->get_URX() + 2);
            rect->set_URY(rect->get_URY() + 2);
            absorber->set_TextSearchOptions(MakeObject<TextSearchOptions>(rect));
            absorber->Visit(document->get_Pages()->idx_get(1));
            for (const auto& textFragment : absorber->get_TextFragments()) {
                textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }
    }

    document->Save(outputFile);
}
```

## Update web link destinations

Change existing GoToURIAction targets on page 1 to https://www.aspose.com. Other link action types are skipped.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter for [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) objects on page 1.
1. Check each action for [GoToURIAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/).
1. Set [URI](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/set_uri/) to the replacement URL.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToURIAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of links/UpdateExamples.linkAnnotationUpdateWebDestination.
void LinkAnnotationUpdateWebDestination(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (const auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link && System::DynamicCast_noexcept<LinkAnnotation>(annotation)) {
            auto linkAnnotation = System::DynamicCast<LinkAnnotation>(annotation);
            if (System::DynamicCast_noexcept<GoToURIAction>(linkAnnotation->get_Action())) {
                auto action = System::DynamicCast<GoToURIAction>(linkAnnotation->get_Action());
                action->set_URI(u"https://www.aspose.com");
            }
        }
    }
    document->Save(outputFile);
}
```
