---
title: Draw PDF arc shapes in C++
linktitle: Add Arc
type: docs
weight: 10
url: /cpp/add-arc/
description: Draw colored arcs and construct a filled arc example inside PDF graphs using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create Colored and Filled Arc Drawings in PDF with C++
Abstract: Learn how to add arc shapes to a Graph with Aspose.PDF for C++. The examples configure stroke colors and combine an arc with line segments for a filled drawing.
---

## Draw colored arcs

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) and give it a green [BorderInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/).
1. Create three [Arc](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/arc/) objects with the supplied centers, radii, and angles.
1. Set a different stroke color through each arc [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/).
1. Add the arcs to the graph Shapes collection.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Arc.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::AddArc(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto arc1 = MakeObject<Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```

## Create the filled arc drawing

The source combines an arc and line segments; the line is part of the supplied filled drawing.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Add an [Arc](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/arc/) centered at (100, 100) with radius 95 and angles 0 and 90.
1. Set its FillColor to GreenYellow.
1. Add a [Line](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/line/) through the supplied three points and set its FillColor.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Arc.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Line.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

// Port of GraphsArcExamples.addArcFilled.
void GraphExamples::AddArcFilled(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto arc = MakeObject<Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Line>(MakeArray<float>({195, 100, 100, 100, 100, 195}));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```
