---
title: Draw PDF circle shapes in C++
linktitle: Add Circle
type: docs
weight: 20
url: /cpp/add-circle/
description: Add an outlined circle or a filled circle with text to a PDF graph using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw and Label Filled PDF Circles in C++
Abstract: Learn how to create circle shapes in a PDF Graph with Aspose.PDF for C++. The examples set outline and fill colors and attach a text label to a filled circle.
---

## Draw an outlined circle

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-200 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Create a [Circle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/circle/) centered at (100, 100) with radius 40.
1. Set its stroke color to GreenYellow and add it to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Circle.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::AddCircle(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 200.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto circle = MakeObject<Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```

## Draw a filled circle with text

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-200 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Create a [Circle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/circle/) and configure its stroke and fill through [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/).
1. Assign a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing Circle to the shape.
1. Add the circle to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Circle.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;
using namespace Aspose::Pdf::Text;

// Port of GraphsCircleExamples.addCircleFilled.
void GraphExamples::AddCircleFilled(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 200.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto circle = MakeObject<Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());
    circle->set_Text(MakeObject<TextFragment>(u"Circle"));
    graph->get_Shapes()->Add(circle);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```
