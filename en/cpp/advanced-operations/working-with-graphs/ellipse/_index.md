---
title: Draw PDF ellipses in C++
linktitle: Add Ellipse
type: docs
weight: 60
url: /cpp/add-ellipse/
description: Create outlined and filled ellipses with a text label using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw, Fill, and Label Ellipse Shapes in PDF with C++
Abstract: Learn how to add ellipse shapes and configure their colors in Aspose.PDF for C++. The page includes a text-labeled outline example, overlapping filled ellipses, and a separate disabled text-formatting sample.
---

## Draw ellipses and label one shape

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Create two [Ellipse](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/ellipse/) objects using the supplied positions and dimensions.
1. Configure their stroke colors.
1. Assign a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing Ellipse to the first shape.
1. Add both shapes to the graph.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Ellipse.h>
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

// Port of GraphsEllipseExamples.addEllipse.
void GraphExamples::AddEllipse(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto ellipse1 = MakeObject<Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<TextFragment>(u"Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```

## Draw filled ellipses

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Create a 400-by-400 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) with a green border.
1. Create two [Ellipse](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/ellipse/) objects.
1. Set their FillColor values to GreenYellow and DarkRed.
1. Add the ellipses to Shapes.
1. Add the [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/) to the page paragraphs.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Ellipse.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::CreateEllipseFilled(String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(400.0, 400.0);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Green()));

    auto ellipse1 = MakeObject<Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    page->get_Paragraphs()->Add(graph);
    document->Save(outputFile);
}
```
