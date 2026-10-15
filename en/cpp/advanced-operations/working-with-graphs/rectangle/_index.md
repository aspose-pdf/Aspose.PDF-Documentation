---
title: Draw PDF rectangles in C++
linktitle: Add Rectangle
type: docs
weight: 50
url: /cpp/add-rectangle/
description: Create filled rectangles, alpha colors, gradient fills, and graph stacking examples using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill PDF Rectangles and Control Transparency and Stacking in C++
Abstract: Learn how to style rectangle drawings with solid, alpha-channel, and axial-gradient colors in Aspose.PDF for C++. The examples also set Graph ZIndex values and retain a disabled outline-rectangle sample.
---

## Outline rectangle: disabled source example

The drawing and page-creation statements are commented out. As supplied, the function does not draw a rectangle or explicitly add a page.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Inspect the commented page, text, [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/), and [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/) statements.
1. Review the commented graph border and shape-addition calls.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;
using namespace Aspose::Pdf::Text;

void GraphExamples::AddRectangle(String outputFile)
{
    auto document = MakeObject<Document>();
    //auto page = document->get_Pages()->Add();
    //auto textFragment = MakeObject<TextFragment>(u"Rectangle");
    //page->get_Paragraphs()->Add(textFragment);

    //auto graph = MakeObject<Graph>(400.0, 300.0);
    //page->get_Paragraphs()->Add(graph);
    //graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    //auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(20, 20, 350, 250);
    //graph->get_Shapes()->Add(rectangle);
    //page->get_Paragraphs()->Add(textFragment);

    document->Save(outputFile);
}
```

## Draw a filled rectangle

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) and add it to the page.
1. Create a drawing [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/) at (100, 100) with width 200 and height 120.
1. Set its FillColor to red through [GraphInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/graphinfo/).
1. Add the rectangle to Shapes.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::CreateRectangleFilled(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    page->get_Paragraphs()->Add(graph);

    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 200, 120);
    rectangle->get_GraphInfo()->set_FillColor(Color::get_Red());
    graph->get_Shapes()->Add(rectangle);

    document->Save(outputFile);
}
```

## Use alpha-channel fill colors

The supplied rectangles extend beyond the graph's declared width. Keep that geometry in mind when evaluating the drawing or enabling bounds checks.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 100-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) and add it to the page.
1. Create two overlapping drawing [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/) objects.
1. Use [Color](https://reference.aspose.com/pdf/cpp/aspose.pdf/color/)::FromArgb() with alpha values 128 and 160 for their fills.
1. Add both rectangles to Shapes.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::CreateRectangleWithAlphaColorChannel(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(100.0, 400.0);
    page->get_Paragraphs()->Add(graph);

    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 200, 120);
    rectangle->get_GraphInfo()->set_FillColor(Color::FromArgb(128, 244, 180, 0));
    graph->get_Shapes()->Add(rectangle);

    auto rectangle1 = MakeObject<Aspose::Pdf::Drawing::Rectangle>(200, 150, 200, 100);
    rectangle1->get_GraphInfo()->set_FillColor(Color::FromArgb(160, 120, 0, 120));
    graph->get_Shapes()->Add(rectangle1);

    document->Save(outputFile);
}
```

## Use an axial gradient fill

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) and add it to the page.
1. Create a 300-by-300 drawing [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/).
1. Create [GradientAxialShading](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/gradientaxialshading/) from red to blue and set its start and end points.
1. Assign it to a [Color](https://reference.aspose.com/pdf/cpp/aspose.pdf/color/) PatternColorSpace and use that color as FillColor.
1. Add the rectangle to Shapes.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/GradientAxialShading.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

// Port of GraphsRectangleExamples.addDrawingWithGradientFill.
void GraphExamples::AddDrawingWithGradientFill(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    page->get_Paragraphs()->Add(graph);

    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(0, 0, 300, 300);
    auto gradientColor = MakeObject<Color>();
    auto gradientSettings = MakeObject<GradientAxialShading>(Color::get_Red(), Color::get_Blue());
    gradientSettings->set_Start(MakeObject<Point>(0, 0));
    gradientSettings->set_End(MakeObject<Point>(350, 350));
    gradientColor->set_PatternColorSpace(gradientSettings);
    rectangle->get_GraphInfo()->set_FillColor(gradientColor);
    graph->get_Shapes()->Add(rectangle);

    document->Save(outputFile);
}
```

## Control graph stacking order

ZIndex is set on the graph containing each rectangle, rather than on the rectangle itself.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Set the page size to 375 by 300 and set its left and top margins to zero.
1. Use addRectangleToPage() to create a separate [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) for each [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/).
1. Set IsChangePosition to false and position each graph with Left and Top.
1. Assign ZIndex values 2, 1, and 0 to the red, blue, and green graphs.
1. Add each graph to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

static void addRectangleToPage(SharedPtr<Page> page, float x, float y, float width, float height,
                               SharedPtr<Color> color, int zIndex)
{
    auto graph = MakeObject<Graph>(static_cast<double>(width), static_cast<double>(height));
    graph->set_IsChangePosition(false);
    graph->set_Left(x);
    graph->set_Top(y);
    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(0, 0, width, height);
    rectangle->get_GraphInfo()->set_FillColor(color);
    rectangle->get_GraphInfo()->set_Color(color);
    graph->get_Shapes()->Add(rectangle);
    graph->set_ZIndex(zIndex);
    page->get_Paragraphs()->Add(graph);
}

void GraphExamples::ControlZOrderOfRectangle(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->SetPageSize(375, 300);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    addRectangleToPage(page, 50, 40, 60, 40, Color::get_Red(), 2);
    addRectangleToPage(page, 20, 20, 30, 30, Color::get_Blue(), 1);
    addRectangleToPage(page, 40, 40, 60, 30, Color::get_Green(), 0);

    document->Save(outputFile);
}
```
