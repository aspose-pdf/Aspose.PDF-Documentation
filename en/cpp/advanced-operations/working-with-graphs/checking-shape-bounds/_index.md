---
title: Inspect PDF shape bounds checking in C++
linktitle: Check Shape Bounds
type: docs
weight: 70
url: /cpp/checking-shape-bounds/
description: Review the supplied disabled example for checking whether a shape fits inside its PDF graph using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Review Graph Shape Bounds Validation in C++
Abstract: Inspect how the supplied source would enable bounds checking and catch an exception when adding a rectangle with Aspose.PDF for C++. The bounds-checking workflow is commented out and is not executed by the function as supplied.
---

## Bounds checking: disabled source example

Page creation, graph setup, and bounds checking are inside a block comment. The active function does not perform a bounds check or explicitly add a page.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Inspect the commented setup for a 100-by-100 [Graph](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/graph/).
1. Review the drawing [Aspose::Pdf::Drawing::Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf.drawing/rectangle/) positioned at x = -1.
1. Inspect the call to UpdateBoundsCheckMode() with ThrowExceptionIfDoesNotFit.
1. Review the shape addition and System::Exception handler.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckableList.h>
#include <Aspose.PDF.Cpp/Generator/BoundsCheckableList/BoundsCheckMode.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Graph.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Rectangle.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/exceptions.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Drawing;

void GraphExamples::CheckShapeBounds(String outputFile)
{
    auto document = MakeObject<Document>();
    /*auto page = document->get_Pages()->Add();
    auto graph = MakeObject<Graph>(100.0, 100.0);
    graph->set_Top(10);
    graph->set_Left(15);
    graph->set_Border(MakeObject<BorderInfo>(BorderSide::Box, 1, Color::get_Black()));
    page->get_Paragraphs()->Add(graph);

    auto rectangle = MakeObject<Aspose::Pdf::Drawing::Rectangle>(-1, 0, 50, 50);
    rectangle->get_GraphInfo()->set_FillColor(Color::get_Tomato());
    try
    {
        graph->get_Shapes()->UpdateBoundsCheckMode(BoundsCheckMode::ThrowExceptionIfDoesNotFit);
        graph->get_Shapes()->Add(rectangle);
    }
    catch (const System::Exception &ex)
    {
        std::cout << ex->get_Message() << std::endl;
    }*/

    document->Save(outputFile);
}
```
