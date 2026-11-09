---
title: Shape annotations in C++
linktitle: Shape annotations
type: docs
weight: 20
url: /cpp/shape-annotations/
description: Add, inspect, and delete square, circle, polygon, polyline, and line annotations in PDF documents using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw and Manage PDF Shape Annotations in C++
Abstract: Add square, circle, polygon, polyline, and line annotations with Aspose.PDF for C++. The examples configure colors, fills, opacity, borders, and popups, then show how to inspect annotation geometry and delete annotations by type.
---

Shape annotations mark regions and draw review shapes on the first page. The examples create squares, circles, polygons, polylines, and lines and show how to inspect and delete each type.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add circle annotations

Create a circle annotation on page 1, configure its title, color, interior color, opacity, popup, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [CircleAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/circleannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/CircleAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Shape {

void CircleAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto circleAnnotation = MakeObject<CircleAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(270, 160, 483, 383, true));
    circleAnnotation->set_Title(u"John Smith");
    circleAnnotation->set_Color(Color::get_Red());
    circleAnnotation->set_InteriorColor(Color::get_MistyRose());
    circleAnnotation->set_Opacity(0.5);
    circleAnnotation->set_Popup(MakeObject<PopupAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(842, 316, 1021, 459, true)));

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(circleAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Get circle annotations

Find circle annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Shape {

void CircleAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Circle) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Shape
```

## Delete circle annotations

Collect circle annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Shape {

void CircleAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Circle) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

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

namespace WorkingWithAnnotationsExamples::Shape {

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

} // namespace WorkingWithAnnotations::Shape
```

## Get line annotations

Find line annotations on the first page and print their starting and ending coordinates.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) collection.
1. Filter the annotations using [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Cast each match to [LineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/lineannotation/) and print its start and end points.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LineAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Shape {

void LineAnnotationsGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Line) {
            auto la = DynamicCast<LineAnnotation>(annotation);
            std::cout << "[" << la->get_Starting()->get_X() << "," << la->get_Starting()->get_Y()
        << "]-[" << la->get_Ending()->get_X() << "," << la->get_Ending()->get_Y() << "]" << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Shape
```

## Delete line annotations

Collect line annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Shape {

void LineAnnotationsDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : page->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Line) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        page->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Add polygon annotations

Create a polygon annotation on page 1, configure its title, color, interior color, opacity, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [PolygonAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/polygonannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/array.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PolygonAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Shape {

void PolygonAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto polygonAnnotation = MakeObject<PolygonAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(200, 300, 400, 400, true),
            MakeArray<SharedPtr<Point>>({
                    MakeObject<Point>(200, 300),
                    MakeObject<Point>(220, 300),
                    MakeObject<Point>(250, 330),
                    MakeObject<Point>(300, 304),
                    MakeObject<Point>(300, 400)
            }));
    polygonAnnotation->set_Title(u"John Smith");
    polygonAnnotation->set_Color(Color::get_Blue());
    polygonAnnotation->set_InteriorColor(Color::get_BlueViolet());
    polygonAnnotation->set_Opacity(0.25);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(polygonAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Get polygon annotations

Find polygon annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Shape {

void PolygonAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Polygon) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Shape
```

## Delete polygon annotations

Collect polygon annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Shape {

void PolygonAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Polygon) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Add polyline annotations

Create a polyline annotation on page 1, configure its title, color, popup, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [PolylineAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/polylineannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/array.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PolylineAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Shape {

void PolylineAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto polylineAnnotation = MakeObject<PolylineAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(270, 193, 571, 383, true),
            MakeArray<SharedPtr<Point>>({
                    MakeObject<Point>(545, 150),
                    MakeObject<Point>(545, 190),
                    MakeObject<Point>(667, 190),
                    MakeObject<Point>(667, 110),
                    MakeObject<Point>(626, 111)
            }));
    polylineAnnotation->set_Title(u"John Smith");
    polylineAnnotation->set_Color(Color::get_Red());
    polylineAnnotation->set_Popup(MakeObject<PopupAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(842, 196, 1021, 338, true)));

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(polylineAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Get polyline annotations

Find polyline annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Shape {

void PolylineAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::PolyLine) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Shape
```

## Delete polyline annotations

Collect polyline annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Shape {

void PolylineAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::PolyLine) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Add square annotations

Create a square annotation on page 1, configure its title, color, interior color, opacity, and save the updated PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and create a [SquareAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/squareannotation/) with the supplied coordinates.
1. Configure the annotation properties shown in the example.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/SquareAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Shape {

void SquareAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto squareAnnotation = MakeObject<SquareAnnotation>(
            document->get_Pages()->idx_get(1),
            MakeObject<Rectangle>(60, 600, 250, 450, true));
    squareAnnotation->set_Title(u"John Smith");
    squareAnnotation->set_Color(Color::get_Blue());
    squareAnnotation->set_InteriorColor(Color::get_BlueViolet());
    squareAnnotation->set_Opacity(0.25);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(squareAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```

## Get square annotations

Find square annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Shape {

void SquareAnnotationGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Square) {
            std::cout << annotation->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Shape
```

## Delete square annotations

Collect square annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Shape {

void SquareAnnotationDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Square) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Shape
```
