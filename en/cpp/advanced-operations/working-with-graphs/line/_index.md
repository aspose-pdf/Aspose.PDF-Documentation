---
title: Draw PDF lines in C++
linktitle: Add Line
type: docs
weight: 40
url: /cpp/add-line/
description: Draw a dashed line and page-spanning diagonals, and inspect a disabled line example using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Style PDF Lines and Draw Diagonals across a Page in C++
Abstract: Learn how to configure a line dash pattern and draw diagonals across a PDF page with Aspose.PDF for C++. The supplied basic-line example is also included with its drawing statements left commented out.
---

## Basic line: disabled source example

Page creation and all drawing statements are commented out. The active code only creates a document and calls Save(); it does not draw a line or explicitly add a page.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Inspect the commented page, [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/), and [Line](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/line/) construction statements.
1. Review the commented dash settings and the addition to Shapes.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
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

// Port of GraphsLineExamples.addLine.
void GraphExamples::AddLine(String outputFile)
{
    auto document = MakeObject<Document>();
    //auto page = document->get_Pages()->Add();
    //auto graph = MakeObject<Graph>(400.0, 400.0);
    //page->get_Paragraphs()->Add(graph);

    //auto line = MakeObject<Line>(MakeArray<float>({100, 100, 200, 100}));
    //line->get_GraphInfo()->set_DashArray(MakeArray<int>({0, 1, 0}));
    //line->get_GraphInfo()->set_DashPhase(1);
    //graph->get_Shapes()->Add(line);

    document->Save(outputFile);
}
```

## Draw a line with a dash pattern

The source line coordinates extend beyond the declared graph width. Review graph dimensions and bounds behavior when adapting this example.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 100-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) and add it to the page paragraphs.
1. Create a [Line](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/line/) from (100, 100) to (200, 100).
1. Set the stroke color to red.
1. Set DashArray to {0, 1, 0} and DashPhase to 1 through [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/).
1. Add the line to Shapes.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
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

// Port of GraphsLineExamples.addDottedDashedLine.
void GraphExamples::AddDottedDashedLine(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(100.0, 400.0);
    page->get_Paragraphs()->Add(graph);

    auto line = MakeObject<Line>(MakeArray<float>({100, 100, 200, 100}));
    line->get_GraphInfo()->set_Color(Color::get_Red());
    line->get_GraphInfo()->set_DashArray(MakeArray<int>({0, 1, 0}));
    line->get_GraphInfo()->set_DashPhase(1);
    graph->get_Shapes()->Add(line);

    document->Save(outputFile);
}
```

## Draw two diagonals across a page

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Set all page margins to zero.
1. Create a [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with the page width and height.
1. Read the page rectangle corner coordinates.
1. Construct two [Line](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/line/) objects joining opposite corners.
1. Add both lines to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Line.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::DrawLineAcrossPage(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    auto graph = MakeObject<Graph>(page->get_PageInfo()->get_Width(), page->get_PageInfo()->get_Height());
    const float x1 = static_cast<float>(page->get_Rect()->get_LLX());
    const float x2 = static_cast<float>(page->get_Rect()->get_URX());
    const float y1 = static_cast<float>(page->get_Rect()->get_URY());
    const float y2 = static_cast<float>(page->get_Rect()->get_LLY());
    auto line = MakeObject<Line>(MakeArray<float>({x1, y1, x2, y2}));
    graph->get_Shapes()->Add(line);

    auto line2 = MakeObject<Line>(MakeArray<float>({x1, y2, x2, y1}));
    graph->get_Shapes()->Add(line2);
    page->get_Paragraphs()->Add(graph);

    document->Save(outputFile);
}
```
