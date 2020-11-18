---
title: Working with Graphs
type: docs
weight: 160
url: /net/graphs/
---
# Working with Graphs

## What is Graph
Adding graphs to PDF documents is a very common task for developers while working with Adobe Acrobat Writer or other PDF processing applications. There are many types of graphs that can be used in PDF applications.
[Aspose.PDF for .NET](/pdf/net/) also supports adding graphs to PDF documents. For this purpose, the Graph class is provided. Graph is a paragraph level element and it can be added to the Paragraphs collection in a Page instance. A Graph instance contains a collection of Shapes.

The following types of shapes are supported by the Graph class:

- Arc
- Circle
- Curve
- Line
- Rectangle
- Ellipse

## Create Filled Rectangle Object
Aspose.PDF for .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. It also offers the feature to fill rectangle object with a certain color.

The following code snippet shows how to add a Rectangle object that is filled with color.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF file
Page page = doc.Pages.Add();
// Create Graph instance
Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(100, 400);
// Add graph object to paragraphs collection of page instance
page.Paragraphs.Add(graph);
// Create Rectangle instance
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120);
// Specify fill color for Graph object
rect.GraphInfo.FillColor = Aspose.Pdf.Color.Red;
// Add rectangle object to shapes collection of Graph object
graph.Shapes.Add(rect);
dataDir = dataDir + "CreateFilledRectangle_out.pdf";
// Save PDF file
doc.Save(dataDir);
```
## Add text inside Graph Object
Aspose.PDF for .NET supports to add text inside the Graph Object. Text property of Graph Object provides option to set text of the Graph Object. The following code snippet shows how to add text inside a Rectangle object.

C#
```
 // Open document

string outFile = "Graph.pdf";

Aspose.PDF.Document pdfDoc = new Aspose.PDF.Document();

Aspose.PDF.Page pdfPage = pdfDoc.Pages.Add();

Aspose.PDF.Drawing.Graph graph = new Aspose.PDF.Drawing.Graph(500, 100);

pdfPage.Paragraphs.Add(graph);

//Add rectangle with text

Aspose.PDF.Drawing.Rectangle rect = new Aspose.PDF.Drawing.Rectangle(0, 30, 50, 40);

rect.GraphInfo.LineWidth = 1f;

rect.GraphInfo.Color = Aspose.PDF.Color.Black;

rect.Text = new TextFragment("Rectangle");

graph.Shapes.Add(rect);

pdfDoc.Save(outFile);
```
## Add line object to PDF
Aspose.PDF for .NET supports to get the leverage to add Line object where you can also specify the dash pattern, color and other formatting for Line element. The following code snippet shows how to add a Rectangle object that is filled with color.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF file
Page page = doc.Pages.Add();
// Create Graph instance
Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(100, 400);
// Add graph object to paragraphs collection of page instance
page.Paragraphs.Add(graph);
// Create Rectangle instance
Aspose.Pdf.Drawing.Line line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });
// Specify fill color for Graph object
line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
line.GraphInfo.DashPhase = 1;
// Add rectangle object to shapes collection of Graph object
graph.Shapes.Add(line);
dataDir = dataDir + "AddLineObject_out.pdf";
// Save PDF file
doc.Save(dataDir);
```
## DashLengthInBlack and DashLengthInWhite properties for Line object
The legacy Aspose.PDF.Generator provides the feature to set DashLengthInBlack and DashLengthInWhite properties where dash pattern for line object can be defined. Similar features can be accomplished while using DOM approach.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Instantiate Document instance
Document doc = new Document();
// Add page to pages collection of Document object
Page page = doc.Pages.Add();
// Create Drawing object with certain dimensions
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Add drawing object to paragraphs collection of page instance
page.Paragraphs.Add(canvas);
// Create Line object
Aspose.Pdf.Drawing.Line line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });
// Set color for Line object
line.GraphInfo.Color = Aspose.Pdf.Color.Red;
// Specify dash array for line object
line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
// Set the dash phase for Line instance
line.GraphInfo.DashPhase = 1;
// Add line to shapes collection of drawing object
canvas.Shapes.Add(line);
dataDir = dataDir + "DashLength_out.pdf";
// Save PDF document
doc.Save(dataDir);
```
## Drawing Line across the page
Aspose.PDF for .NET supports line object to draw a cross starting from Left-Bottom to Right-Upper corner and Left-Top corner to Bottom-Right corner. Please take a look over following code snippet to accomplish this requirement.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Create Document instance
Document pDoc = new Document();
// Add page to pages collection of PDF document
Page pg = pDoc.Pages.Add();
// Set page margin on all sides as 0
pg.PageInfo.Margin.Left = pg.PageInfo.Margin.Right = pg.PageInfo.Margin.Bottom = pg.PageInfo.Margin.Top = 0;
// Create Graph object with Width and Height equal to page dimensions
Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph((float)pg.PageInfo.Width , (float)pg.PageInfo.Height);
// Create first line object starting from Lower-Left to Top-Right corner of page
Aspose.Pdf.Drawing.Line line = new Aspose.Pdf.Drawing.Line(new float[] { (float)pg.Rect.LLX, 0, (float)pg.PageInfo.Width, (float)pg.Rect.URY });
// Add line to shapes collection of Graph object
graph.Shapes.Add(line);
// Draw line from Top-Left corner of page to Bottom-Right corner of page
Aspose.Pdf.Drawing.Line line2 = new Aspose.Pdf.Drawing.Line(new float[] { 0, (float)pg.Rect.URY, (float)pg.PageInfo.Width, (float)pg.Rect.LLX });
// Add line to shapes collection of Graph object
graph.Shapes.Add(line2);
// Add Graph object to paragraphs collection of page
pg.Paragraphs.Add(graph);

dataDir = dataDir + "DrawingLine_out.pdf";
// Save PDF file
pDoc.Save(dataDir);
```
## Create Rectangle with Alpha color channel
Aspose.PDF for .NET supports to fill rectangle object with a certain color. A rectangle object can also have Alpha color channel to give transparent appearance. The following code snippet shows how to add a **Rectangle** object with Alpha color channel.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Instantiate Document instance
Document doc = new Document();
// Add page to pages collection of PDF file
Aspose.Pdf.Page page = doc.Pages.Add();
// Create Graph instance
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Create rectangle object with specific dimensions
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 100);
// Set graph fill color from System.Drawing.Color structure from a 32-bit ARGB value
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Add rectangle object to shapes collection of Graph instance
canvas.Shapes.Add(rect);

// Create second rectangle object
Aspose.Pdf.Drawing.Rectangle rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100);
rect1.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(16118015)));
canvas.Shapes.Add(rect1);
// Add graph instance to paragraph collection of page object
page.Paragraphs.Add(canvas);

dataDir = dataDir + "CreateRectangleWithAlphaColor_out.pdf";
// Save PDF file
doc.Save(dataDir);
```
## How to add drawing with transparent Color
While creating drawing objects such as Rectangle, Circle, Eclipse etc, we provide color information for border as well as fill color information. In order to have transparent fill impression, the **FromArgb(..)** method of Aspose.PDF.Color object can be used. Please take a look over following code snippet which demonstrates the feature to fill rectangle object with transparent color. Please try using following code snippet to accomplish this requirement.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

int alpha = 10;
int green = 0;
int red = 100;
int blue = 0;
// Create Color object using Alpha RGB 
Aspose.Pdf.Color alphaColor = Aspose.Pdf.Color.FromArgb(alpha, red, green, blue); // Provide alpha channel
// Instantiate Document object
Document document = new Document();
// Add page to pages collection of PDF file
Page page = document.Pages.Add();
// Create Graph object with certain dimensions
Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(300, 400);
// Set border for Drawing object
graph.Border = (new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Black));
// Add graph object to paragraphs collection of Page instance
page.Paragraphs.Add(graph);
// Create Rectangle object with certain dimensions
Aspose.Pdf.Drawing.Rectangle rectangle = new Aspose.Pdf.Drawing.Rectangle(0, 0, 100, 50);
// Create graphInfo object for Rectangle instance
Aspose.Pdf.GraphInfo graphInfo = rectangle.GraphInfo;
// Set color information for GraphInfo instance
graphInfo.Color = (Aspose.Pdf.Color.Red);
// Set fill color for GraphInfo
graphInfo.FillColor = (alphaColor);
// Add rectangle shape to shapes collection of graph object
graph.Shapes.Add(rectangle);
dataDir = dataDir + "AddDrawing_out.pdf";
// Save PDF file
document.Save(dataDir);
```
## Controlling Z-Order of Rectangle
When adding more than one instance of same object inside PDF file, we can control their rendering by specifying the Z-Order. Z-Order is also used when we need to render objects on top of each other. The following code snippet shows the steps to render Rectangle objects on top of each other.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

// Instantiate Document class object
Document doc1 = new Document();
/// Add page to pages collection of PDF file
Aspose.Pdf.Page page1 = doc1.Pages.Add();
// Set size of PDF page
page1.SetPageSize(375, 300);
// Set left margin for page object as 0
page1.PageInfo.Margin.Left = 0;
// Set top margin of page object as 0
page1.PageInfo.Margin.Top = 0;
// Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
AddRectangle(page1, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
// Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
AddRectangle(page1, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
// Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
AddRectangle(page1, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);
dataDir = dataDir + "ControlRectangleZOrder_out.pdf";
// Save resultant PDF file
doc1.Save(dataDir);
```
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zindex)
{
    // Create graph object with dimensions same as specified for Rectangle object
    Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height);
    // Can we change the position of graph instance
    graph.IsChangePosition = false;
    // Set Left coordinate position for Graph instance
    graph.Left = x;
    // Set Top coordinate position for Graph object
    graph.Top = y;
    // Add a rectangle inside the "graph"
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height);
    // Set rectangle fill color
    rect.GraphInfo.FillColor = color;
    // Color of graph object
    rect.GraphInfo.Color = color;
    // Add rectangle to shapes collection of graph instance
    graph.Shapes.Add(rect);
    // Set Z-Index for rectangle object
    graph.ZIndex = zindex;
    // Add graph to paragraphs collection of page object
    page.Paragraphs.Add(graph);
}
```
## Add Drawing with Gradient Fill
Aspose.PDF for .NET supports the ability to create a pure PDF document that has a single gradient transitioning from one Spot/Process color to another Spot/Process color. This is illustrated in the following code sample.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(300, 300);
page.Paragraphs.Add(graph);
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);
graph.Shapes.Add(rect);
rect.GraphInfo.FillColor = new Aspose.Pdf.Color
{
    PatternColorSpace = new GradientAxialShading(Color.Red, Color.Blue)
    {
        Start = new Point(0, 0),
        End = new Point(300, 300)
    }
};
doc.Save(dataDir + "AddDrawingWithGradientFill_out.pdf");
```
