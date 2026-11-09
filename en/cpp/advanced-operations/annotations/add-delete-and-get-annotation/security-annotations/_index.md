---
title: Security annotations in C++
linktitle: Security annotations
type: docs
weight: 75
url: /cpp/security-annotations/
description: Mark text and image areas for redaction and apply existing redaction annotations in PDF files using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mark PDF Content and Apply Redactions in C++
Abstract: Learn how to mark matching text and a selected image area for redaction with Aspose.PDF for C++. Separate examples distinguish saving redaction markers from calling Redact() to apply existing redactions on the first page.
---

Redaction has two stages: marking content and applying the redaction. MarkTextRedaction and RedactArea save redaction annotations without calling Redact(). ApplyRedaction applies existing redactions on the first page.

MarkTextRedaction searches all pages, while ApplyRedaction processes only the first page. Applying redactions on other pages requires extending that iteration.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Apply existing redactions

Collect redaction annotations on page 1 and apply each one before saving. Marked content is removed when Redact() is called.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter the first page annotations by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Collect the matches as [RedactionAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/redactionannotation/) objects.
1. Call [Redact()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/redactionannotation/redact/) on each collected annotation.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <vector>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RedactionAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Security {

void ApplyRedaction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<RedactionAnnotation>> redactionAnnotations;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Redaction) {
            redactionAnnotations.push_back(DynamicCast<RedactionAnnotation>(annotation));
        }
    }
    for (auto redactionAnnotation : redactionAnnotations) {
        redactionAnnotation->Redact();
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Security
```

## Mark matching text for redaction

Search all pages with a regular expression supplied as searchTerm. Add redaction annotations with a repeated REDACTED overlay; this function does not apply them.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) with searchTerm and enable regular expressions with [TextSearchOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textsearchoptions/).
1. Search the document pages and get the matching text rectangles.
1. Create a [RedactionAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/redactionannotation/) for each match and configure its overlay and colors.
1. Add the annotations with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RedactionAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextSearchOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Security {

void MarkTextRedaction(System::String inputFile, System::String outputFile, System::String searchTerm)
{
    auto document = MakeObject<Document>(inputFile);
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(searchTerm);
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);
    document->get_Pages()->Accept(textFragmentAbsorber);

    for (auto textFragment : textFragmentAbsorber->get_TextFragments()) {
        auto page = textFragment->get_Page();
        auto redactionAnnotation = MakeObject<RedactionAnnotation>(page, textFragment->get_Rectangle());
        redactionAnnotation->set_FillColor(Color::get_Gray());
        redactionAnnotation->set_BorderColor(Color::get_Red());
        redactionAnnotation->set_Color(Color::get_White());
        redactionAnnotation->set_OverlayText(u"REDACTED");
        redactionAnnotation->set_TextAlignment(HorizontalAlignment::Center);
        redactionAnnotation->set_Repeat(true);
        page->get_Annotations()->Add(redactionAnnotation, true);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Security
```

## Mark an image area for redaction

Locate the second image placement on page 1 and mark its rectangle for redaction. At least two image placements must exist. Despite its name, this function does not call Redact().

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit the first page with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. Get the second [ImagePlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/) rectangle.
1. Create and configure a [RedactionAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/redactionannotation/).
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RedactionAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Security {

void RedactArea(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto imagePlacementAbsorber = MakeObject<ImagePlacementAbsorber>();
    auto page = document->get_Pages()->idx_get(1);
    page->Accept(imagePlacementAbsorber);

    auto targetRect = imagePlacementAbsorber->get_ImagePlacements()->idx_get(2)->get_Rectangle();
    auto redactionAnnotation = MakeObject<RedactionAnnotation>(page, targetRect);
    redactionAnnotation->set_FillColor(Color::get_Gray());
    redactionAnnotation->set_BorderColor(Color::get_Red());
    redactionAnnotation->set_Color(Color::get_White());
    redactionAnnotation->set_OverlayText(u"REDACTED");
    redactionAnnotation->set_TextAlignment(HorizontalAlignment::Center);
    redactionAnnotation->set_Repeat(true);

    page->get_Annotations()->Add(redactionAnnotation, true);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Security
```
