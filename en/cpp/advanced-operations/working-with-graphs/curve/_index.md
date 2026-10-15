---
title: Draw PDF curve shapes in C++
linktitle: Add Curve
type: docs
weight: 30
url: /cpp/add-curve/
description: Draw stroked and filled curves from point arrays using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create Stroked and Filled PDF Curves with C++
Abstract: Learn how to construct a Curve from the supplied coordinate array in Aspose.PDF for C++. Separate examples apply an outline color or a fill color before saving the PDF.
---

## Draw a stroked curve

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-200 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Construct a [Curve](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/curve/) from the eight supplied coordinate values.
1. Set its stroke color through [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/) and add it to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Curve.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

// Port of GraphsCurveExamples.addCurve.
void GraphExamples::AddCurve(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 200.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto curve1 = MakeObject<Curve>(MakeArray<float>({10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```

## Draw a filled curve

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-200 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Construct a [Curve](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/curve/) from the supplied coordinate array.
1. Set FillColor to GreenYellow and add the curve to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Curve.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

// Port of GraphsCurveExamples.addCurveFilled.
void GraphExamples::AddCurveFilled(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 200.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto curve1 = MakeObject<Curve>(MakeArray<float>({10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```
