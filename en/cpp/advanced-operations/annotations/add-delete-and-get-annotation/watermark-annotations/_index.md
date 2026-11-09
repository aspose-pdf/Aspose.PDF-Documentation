---
title: Watermark annotations in C++
linktitle: Watermark annotations
type: docs
weight: 70
url: /cpp/watermark-annotations/
description: Add a text watermark annotation, inspect its rectangle, and delete watermark annotations from a PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Manage Text Watermark Annotations in C++
Abstract: Add a multiline text watermark annotation with Aspose.PDF for C++ and configure its font, size, color, and opacity. The examples also read watermark annotation rectangles and delete watermark annotations from the first page.
---

Create a watermark annotation containing three lines of text, inspect watermark rectangles, or remove watermark annotations from the first page. The creation example uses Arial at 25 points with blue text and 0.5 opacity.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add a watermark annotation

Place a three-line blue watermark on page 1 using Arial at 25 points and an opacity of 0.5.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/watermarkannotation/) with the target rectangle.
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Configure [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) with the font, size, and color.
1. Set opacity and supply the text lines with [SetTextAndState()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/watermarkannotation/settextandstate/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/array.h>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WatermarkAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Watermark {

void WatermarkAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto watermarkAnnotation = MakeObject<WatermarkAnnotation>(
            page,
            MakeObject<Rectangle>(100, 100, 400, 200, true));

    page->get_Annotations()->Add(watermarkAnnotation);

    auto textState = MakeObject<TextState>();
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_FontSize(25);
    textState->set_Font(FontRepository::FindFont(u"Arial"));

    watermarkAnnotation->set_Opacity(0.5);
    watermarkAnnotation->SetTextAndState(MakeArray<String>({u"HELLO", u"Line 1", u"Line 2"}), textState);

    document->Save(outputFile);
}

} // namespace WorkingWithAnnotationsExamples::Watermark
```

## Get watermark annotations

Find watermark annotations on the first page and print their bounding rectangles.

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

namespace WorkingWithAnnotationsExamples::Watermark {

void WatermarkGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto a : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (a->get_AnnotationType() == AnnotationType::Watermark) {
            std::cout << a->get_Rect()->ToString() << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Watermark
```

## Delete watermark annotations

Collect watermark annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

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

namespace WorkingWithAnnotationsExamples::Watermark {

void WatermarkDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto a : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (a->get_AnnotationType() == AnnotationType::Watermark) {
            toDelete.push_back(a);
        }
    }
    for (auto a : toDelete) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(a);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Watermark
```
