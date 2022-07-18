---
title: Add Curve Object to PDF file
linktitle: Add Curve
type: docs
weight: 30
url: /cpp/add-curve/
description: This article explains how to create a curve object to your PDF using Aspose.PDF for C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Curve object

A graph [Curve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) is a connected union of projective lines, each line meeting three others in ordinary double points.

Bézier curves are widely used in computer graphics to model smooth curves. The curve is completely contained in the convex hull of its control points, the points may be graphically displayed and used to manipulate the curve intuitively.
The entire curve is contained in the quadrilateral whose corners are the four given points (their convex hull).

In this article, we will investigate  simply graph curves, and filled curves, that you can create in your PDF document.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) instance

1. Create [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) with certain dimensions

1. Set [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) for Drawing object

1. Add [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) object to paragraphs collection of page

1. Save our PDF file

```cpp
void ExampleCurve() {

    // Create Document instance
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Drawing object with certain dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Set border for Drawing object
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Add Graph object to paragraphs collection of page
    page->get_Paragraphs()->Add(graph);

    // Save PDF file
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```

The following picture shows the result executed with our code snippet:

![Drawing Curve](drawing_curve.png)

## Create Filled Curve Object

This example shows how to add a Curve object that is filled with color.

```cpp
void ExampleFilledCurve() {

    // Create Document instance
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Drawing object with certain dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Set border for Drawing object
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Add Graph object to paragraphs collection of page
    page->get_Paragraphs()->Add(graph);

    // Save PDF file
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)
