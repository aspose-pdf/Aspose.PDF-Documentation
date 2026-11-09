---
title: Text annotations in C++
linktitle: Text annotations
type: docs
weight: 10
url: /cpp/text-based-annotations/
description: Create, inspect, and delete free text, highlight, strikeout, squiggly, and underline annotations in PDF files using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Extract PDF Text Markup in C++
Abstract: Create, inspect, and delete free text, highlight, strikeout, squiggly, and underline annotations with Aspose.PDF for C++. Additional examples set underline quad points, extract marked text and fragments, filter underlines by title, and flatten an underline into page content.
---

The examples cover free text and text markup on the first PDF page, including underline quadrilaterals, marked text extraction, filtering by author title, and flattening.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add free text annotations

Create a free text annotation on page 1, configure its title, color, and save the updated PDF. This sample configures the annotation appearance and title but does not set Contents.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/freetextannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/FreeTextAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

    void FreeTextAnnotationAdd(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(299, 713, 308, 720, true),
            MakeObject<DefaultAppearance>());
        freeTextAnnotation->set_Title(u"Aspose User");
        freeTextAnnotation->set_Color(Color::get_LightGreen());

        document->get_Pages()->idx_get(1)->get_Annotations()->Add(freeTextAnnotation);
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Text
```

## Get free text annotations

Find free text annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Text {

void FreeTextAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::FreeText) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Delete free text annotations

Collect free text annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Text {

void FreeTextAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::FreeText) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Add highlight annotations

Create a highlight annotation on page 1, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/highlightannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/HighlightAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextHighlightAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto highlightAnnotation = MakeObject<HighlightAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(300, 750, 320, 770, true));

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(highlightAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Get highlight annotations

Find highlight annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextHighlightAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Highlight) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Delete highlight annotations

Collect highlight annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextHighlightAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Highlight) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Add squiggly annotations

Create a squiggly annotation on page 1, configure its title, color, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [SquigglyAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/squigglyannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/SquigglyAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextSquigglyAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto squigglyAnnotation = MakeObject<SquigglyAnnotation>(
            page,
            MakeObject<Rectangle>(67, 317, 261, 459, true));
    squigglyAnnotation->set_Title(u"John Smith");
    squigglyAnnotation->set_Color(Color::get_Blue());

    page->get_Annotations()->Add(squigglyAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Get squiggly annotations

Find squiggly annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextSquigglyAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Squiggly) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Delete squiggly annotations

Collect squiggly annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextSquigglyAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Squiggly) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Add strikeout annotations

Create a strike out annotation on page 1, configure its title, subject, flags, color, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/strikeoutannotation/) with the supplied coordinates.
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
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/StrikeOutAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextStrikeoutAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto strikeoutAnnotation = MakeObject<StrikeOutAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769, true));
    strikeoutAnnotation->set_Title(u"Aspose User");
    strikeoutAnnotation->set_Subject(u"Inserted text 1");
    strikeoutAnnotation->set_Flags(AnnotationFlags::Print);
    strikeoutAnnotation->set_Color(Color::get_Blue());

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeoutAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Get strikeout annotations

Find strikeout annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextStrikeoutAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::StrikeOut) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Delete strikeout annotations

Collect strikeout annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextStrikeoutAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::StrikeOut) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Add underline annotations

Create a underline annotation on page 1, configure its title, subject, flags, color, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/) with the supplied coordinates.
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
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto underlineAnnotation = MakeObject<UnderlineAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769, true));
    underlineAnnotation->set_Title(u"Aspose User");
    underlineAnnotation->set_Subject(u"Inserted Underline 1");
    underlineAnnotation->set_Flags(AnnotationFlags::Print);
    underlineAnnotation->set_Color(Color::get_Blue());

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Get underline annotations

Find underline annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Underline) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Delete underline annotations

Collect underline annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Underline) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Delete underlines by title

Collect and delete only underline annotations whose Title equals "Aspose User".

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/) and cast matches to [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/).
1. Check the [MarkupAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/markupannotation/) Title and collect matching underlines.
1. Remove collected annotations with [AnnotationCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/delete/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <vector>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineByTitleDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<UnderlineAnnotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Underline) {
            auto ua = DynamicCast<UnderlineAnnotation>(annotation);
            if (ua->get_Title() == u"Aspose User") {
                toDelete.push_back(ua);
            }
        }
    }
    for (auto ua : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ua);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Add and flatten an underline

Create a blue underline and flatten it into the page content. After flattening, it is no longer an editable underline annotation.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create and configure an [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/).
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Call [Annotation::Flatten()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/flatten/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineFlattenAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto underlineAnnotation = MakeObject<UnderlineAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769, true));
    underlineAnnotation->set_Title(u"Aspose User");
    underlineAnnotation->set_Subject(u"Inserted Underline to Flatten");
    underlineAnnotation->set_Flags(AnnotationFlags::Print);
    underlineAnnotation->set_Color(Color::get_Blue());

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
    underlineAnnotation->Flatten();

    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```

## Get underlined text fragments

Retrieve the text fragments covered by underline annotations on page 1 and print each fragment text.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Cast matching annotations to [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/).
1. Call [GetMarkedTextFragments()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/textmarkupannotation/getmarkedtextfragments/) and read each [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

    void TextUnderlineMarkedFragmentsGet(System::String inputFile)
    {
        auto document = MakeObject<Document>(inputFile);
        for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
            if (annotation->get_AnnotationType() == AnnotationType::Underline) {
                auto ua = DynamicCast<UnderlineAnnotation>(annotation);
                for (auto fragment : ua->GetMarkedTextFragments()) {
                    std::cout << "Fragment text: " << fragment->get_Text() << std::endl;
                }
            }
        }
    }

} // namespace WorkingWithAnnotations::Text
```

## Get underlined text

Filter underline annotations on page 1 and print the text covered by each annotation.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/) and cast each match to [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/).
1. Call [GetMarkedText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/textmarkupannotation/getmarkedtext/) and print the returned text.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineMarkedTextGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Underline) {
            auto ua = DynamicCast<UnderlineAnnotation>(annotation);
            std::cout << "Marked text: " << ua->GetMarkedText() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Text
```

## Add an underline with quad points

Create a blue printable underline and explicitly set four quad points from the annotation rectangle.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/underlineannotation/) and configure its title, subject, print flag, and color.
1. Set the quadrilateral through [TextMarkupAnnotation::set_QuadPoints()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/textmarkupannotation/set_quadpoints/).
1. Add the annotation objects with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/array.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/UnderlineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Text {

void TextUnderlineWithQuadPointsAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto rect = MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769, true);
    auto underlineAnnotation = MakeObject<UnderlineAnnotation>(
            document->get_Pages()->idx_get(1), rect);
    underlineAnnotation->set_Title(u"Aspose User");
    underlineAnnotation->set_Subject(u"Inserted Underline with Quad Points");
    underlineAnnotation->set_Flags(AnnotationFlags::Print);
    underlineAnnotation->set_Color(Color::get_Blue());
    underlineAnnotation->set_QuadPoints(MakeArray<SharedPtr<Point>>({
            MakeObject<Point>(rect->get_LLX(), rect->get_LLY()),
            MakeObject<Point>(rect->get_URX(), rect->get_LLY()),
            MakeObject<Point>(rect->get_URX(), rect->get_URY()),
            MakeObject<Point>(rect->get_LLX(), rect->get_URY())
    }));

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Text
```
