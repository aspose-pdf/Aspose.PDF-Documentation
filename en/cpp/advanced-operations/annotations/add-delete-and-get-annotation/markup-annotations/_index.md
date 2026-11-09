---
title: Markup annotations in C++
linktitle: Markup annotations
type: docs
weight: 30
url: /cpp/markup-annotations/
description: Add, inspect, and delete sticky notes, caret markers, and grouped replacement annotations in PDF files using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Review Notes and Replacement Markup to PDFs in C++
Abstract: Use Aspose.PDF for C++ to add, inspect, and delete sticky notes, caret markers, and grouped replacement markup. The examples show how to associate a strikeout with a caret through reply properties without changing the underlying page text.
---

Use sticky notes and caret markers to review a PDF. A replacement annotation combines a caret with a grouped strikeout; it records review markup without replacing the underlying page text.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add caret annotations

Create a caret annotation on page 1, configure its title, subject, flags, color, popup, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [CaretAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/caretannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/CaretAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Markup {

    void CaretAnnotationsAdd(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto page = document->get_Pages()->idx_get(1);

        auto caretAnnotation = MakeObject<CaretAnnotation>(
            page,
            MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation->set_Title(u"Aspose User");
        caretAnnotation->set_Subject(u"Inserted text 1");
        caretAnnotation->set_Flags(AnnotationFlags::Print);
        caretAnnotation->set_Color(Color::get_Blue());
        caretAnnotation->set_Popup(MakeObject<PopupAnnotation>(
            page,
            MakeObject<Rectangle>(310, 713, 410, 730, true)));
        page->get_Annotations()->Add(caretAnnotation);

        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Markup
```

## Get caret annotations

Find caret annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Markup {

void CaretAnnotationsGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    for (auto& annot : page->get_Annotations()) {
        if (annot->get_AnnotationType() == AnnotationType::Caret) {
            std::cout << annot->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Markup
```

## Delete caret annotations

Collect caret annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Markup {

    void CaretAnnotationsDelete(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto page = document->get_Pages()->idx_get(1);

        std::vector<SharedPtr<Annotation>> caretAnnotations;
        for (auto& annot : page->get_Annotations()) {
            if (annot->get_AnnotationType() == AnnotationType::Caret) {
                caretAnnotations.push_back(annot);
            }
        }
        for (auto& annot : caretAnnotations) {
            page->get_Annotations()->Delete(annot);
        }
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Markup
```

## Add grouped replacement markup

Create a blue caret and strikeout, then link the strikeout to the caret as a grouped reply. This records a suggested replacement without changing the page text.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [CaretAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/caretannotation/) with a popup.
1. Create a [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/strikeoutannotation/) and set its quad points.
1. Set [InReplyTo](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/markupannotation/set_inreplyto/) to the caret and use the Group reply type.
1. Add the annotation objects with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/array.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/CaretAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/ReplyType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/StrikeOutAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Markup {

    void ReplaceAnnotationsAdd(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto page = document->get_Pages()->idx_get(1);

        auto caretAnnotation = MakeObject<CaretAnnotation>(
            page,
            MakeObject<Rectangle>(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation->set_Flags(AnnotationFlags::Print);
        caretAnnotation->set_Subject(u"Inserted text 2");
        caretAnnotation->set_Title(u"Aspose User");
        caretAnnotation->set_Color(Color::get_Blue());
        caretAnnotation->set_Popup(MakeObject<PopupAnnotation>(
            page,
            MakeObject<Rectangle>(310, 713, 410, 730, true)));

        auto strikeoutAnnotation = MakeObject<StrikeOutAnnotation>(
            page,
            MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation->set_Color(Color::get_Blue());
        strikeoutAnnotation->set_QuadPoints(MakeArray<SharedPtr<Point>>({
                MakeObject<Point>(321.66, 739.416),
                MakeObject<Point>(365.664, 739.416),
                MakeObject<Point>(321.66, 728.508),
                MakeObject<Point>(365.664, 728.508)
            }));
        strikeoutAnnotation->set_Subject(u"Cross-out");
        strikeoutAnnotation->set_InReplyTo(caretAnnotation);
        strikeoutAnnotation->set_ReplyType(ReplyType::Group);

        page->get_Annotations()->Add(caretAnnotation);
        page->get_Annotations()->Add(strikeoutAnnotation);

        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Markup
```

## Get grouped replacement markup

Inspect strikeout annotations on the first page and print the rectangle only when the annotation has an InReplyTo target and the Group reply type.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter annotations by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/) and cast strikeouts to [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/strikeoutannotation/).
1. Check [MarkupAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/markupannotation/) reply properties and print matching rectangles.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/ReplyType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/StrikeOutAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Markup {

void ReplaceAnnotationsGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    for (auto& annot : page->get_Annotations()) {
        if (annot->get_AnnotationType() == AnnotationType::StrikeOut) {
            auto sa = DynamicCast<StrikeOutAnnotation>(annot);
            if (sa->get_InReplyTo() != nullptr && sa->get_ReplyType() == ReplyType::Group) {
                std::cout << "Replace annotation rect: " << sa->get_Rect()->ToString() << std::endl;
            }
        }
    }
}

} // namespace WorkingWithAnnotations::Markup
```

## Delete strikeout annotations

Collect and delete all strikeout annotations on the first page. This function does not restrict deletion to grouped replacement markup and does not explicitly remove the caret.

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
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/StrikeOutAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Markup {

    void ReplaceAnnotationsDelete(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto page = document->get_Pages()->idx_get(1);

        std::vector<SharedPtr<StrikeOutAnnotation>> replaceAnnotations;
        for (auto& annot : page->get_Annotations()) {
            if (annot->get_AnnotationType() == AnnotationType::StrikeOut) {
                replaceAnnotations.push_back(DynamicCast<StrikeOutAnnotation>(annot));
            }
        }
        for (auto& annot : replaceAnnotations) {
            page->get_Annotations()->Delete(annot);
        }
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Markup
```

## Add text annotations

Create a text annotation on page 1, configure its title, subject, contents, flags, color, icon, open, popup, and save the updated PDF. The note text is preserved verbatim from the supplied example.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [TextAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/textannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/TextAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/TextIcon.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Markup {

void TextAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto textAnnotation = MakeObject<TextAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(299.988, 613.664, 428.708, 680.769, true));
    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sticky Note");
    textAnnotation->set_Contents(u"This is a text annotation added by Aspose.PDF for C++");
    textAnnotation->set_Flags(AnnotationFlags::Print);
    textAnnotation->set_Color(Color::get_Blue());
    textAnnotation->set_Icon(TextIcon::Help);

    auto popup = MakeObject<PopupAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(428.708, 613.664, 528.708, 713.664, true));
    popup->set_Open(true);
    textAnnotation->set_Popup(popup);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(textAnnotation, false);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Markup
```

## Get text annotations

Find text annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Markup {

    void TextAnnotationGet(System::String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
            if (annotation->get_AnnotationType() == AnnotationType::Text) {
                std::cout << annotation->get_Rect()->ToString() << std::endl;
            }
        }
    }

} // namespace WorkingWithAnnotations::Markup
```

## Delete text annotations

Collect text annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Markup {

void TextAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Text) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Markup
```
