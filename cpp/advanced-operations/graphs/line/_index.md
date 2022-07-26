---
title: Add Line Object to PDF file
linktitle: Add Line
type: docs
weight: 40
url: /cpp/add-line/
description: This article explains how to create a line object to your PDF using Aspose.PDF for C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Line object

Aspose.PDF for C++ supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) object where you can also specify the dash pattern, color and other formatting for Line element.

Follow the steps below:

1. Create a new PDF [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)

1. Add [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) to pages collection of PDF file

1. Create [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/) instance.

1. Add Graph object to paragraphs collection of page instance.

1. Create [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) instance.

1. Set line width.

1. Add [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) object to shapes collection of Graph object.

1. Save your PDF file.

The following code snippet shows how to add a [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) object that is filled with color.

```cpp
 
void AddLineObjectToPDF()
{
	String _dataDir("C:\\Samples\\");
	// Create Document instance
	auto document = MakeObject<Document>();

	// Add page to pages collection of PDF file
	auto page = document->get_Pages()->Add();

	// Create Graph instance
	auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

	// Add graph object to paragraphs collection of page instance
	page->get_Paragraphs()->Add(graph);

	// Create Rectangle instance
	auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });
	
	// Specify fill color for Graph object
	line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));
	line->get_GraphInfo()->set_DashPhase (1);
	
	// Add rectangle object to shapes collection of Graph object
	graph->get_Shapes()->Add(line);
	
	// Save PDF file
	document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```

![Add Line](add_line.png)

## How to add Dotted Dashed Line to your PDF document

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{
	String _dataDir("C:\\Samples\\");
	// Create Document instance
	auto document = MakeObject<Document>();

	// Add page to pages collection of PDF file
	auto page = document->get_Pages()->Add();

	// Create Drawing object with certain dimensions
	auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);
	// Add drawing object to paragraphs collection of page instance
	page->get_Paragraphs()->Add(canvas);
	
	// Create Line object
	auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));
	// Set color for Line object
	line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());
	// Specify dash array for line object
	line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));
	// Set the dash phase for Line instance
	line->get_GraphInfo()->set_DashPhase(1);
	// Add line to shapes collection of drawing object
	canvas->get_Shapes()->Add(line);	
	// Save PDF file
	document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Let's check the result:

![Dashed Line](dash_line.png)

## Draw Line Across the Page

We can also use line object to draw a cross starting from Left-Bottom to Right-Upper corner and Left-Top corner to Bottom-Right corner.

Please take a look over following code snippet to accomplish this requirement.

```cpp
void ExampleLineAcrossPage() {

    // Create Document instance
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>();
   
    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();
    // Set page margin on all sides as 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Create Graph object with Width and Height equal to page dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Create first line object starting from Lower-Left to Top-Right corner of page
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Add line to shapes collection of Graph object
    graph->get_Shapes()->Add(line);
    // Draw line from Top-Left corner of page to Bottom-Right corner of page
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Add line to shapes collection of Graph object
    graph->get_Shapes()->Add(line2);
    // Add Graph object to paragraphs collection of page
    page->get_Paragraphs()->Add(graph);

    // Save PDF file
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

![Drawing Line](draw_line.png)
