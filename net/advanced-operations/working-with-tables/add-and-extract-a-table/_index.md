---
title: Add and Extract a Table
type: docs
weight: 10
url: /net/add-and-extract-a-table/
description: Aspose.PDF for .NET makes it possible to carry out various manipulations with the tables contained in your pdf document. You may add and extract a table in the existing PDF document, render table on a new page and etc.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add table

Tables are important when working with PDF documents. They provide great features for displaying information in a systematic manner. The Aspose.PDF namespace contains classes named [Table](https://apireference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://apireference.aspose.com/pdf/net/aspose.pdf/cell), and [Row](https://apireference.aspose.com/pdf/net/aspose.pdf/row) which provides functionality for creating tables when generating PDF documents from scratch.

### Add Table in Existing PDF Document

To add a table to an existing PDF file with Aspose.PDF for .NET, take the following steps:

1. Load the source file.
1. Initialize a table and set its columns and rows.
1. Set table setting (we’ve set the borders).
1. Populate table.
1. Add the table to a page.
1. Save the file.

The following code snippets show how to add text in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Load source PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Initializes a new instance of the Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Set the table border color as LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Set the border for table cells
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Create a loop to add 10 rows
for (int row_count = 1; row_count < 10; row_count++)
{
    // Add row to table
    Aspose.Pdf.Row row = table.Rows.Add();
    // Add table cells
    row.Cells.Add("Column (" + row_count + ", 1)");
    row.Cells.Add("Column (" + row_count + ", 2)");
    row.Cells.Add("Column (" + row_count + ", 3)");
}
// Add table object to first page of input document
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// Save updated document containing table object
doc.Save(dataDir);
```

### AutoFitToWindow property in ColumnAdjustmentType enumeration

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instntiate the Pdf object by calling its empty constructor
Document doc = new Document();
// Create the section in the Pdf object
Page sec1 = doc.Pages.Add();

// Instantiate a table object
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Add the table in paragraphs collection of the desired section
sec1.Paragraphs.Add(tab1);

// Set with column widths of the table
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Set default cell border using BorderInfo object
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Set table border using another customized BorderInfo object
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Create MarginInfo object and set its left, bottom, right and top margins
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Set the default cell padding to the MarginInfo object
tab1.DefaultCellPadding = margin;

// Create rows in the table and then cells in the rows
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Save updated document containing table object
doc.Save(dataDir);
```

### Get Table Width

Sometimes, it is required to get table width dynamically. Aspose.PDF.Table class has a method [GetWidth](https://apireference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) for the purpose. For example, you have not set table columns width explicitly and set [ColumnAdjustment](https://apireference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) to AutoFitToContent. In this case you can get table width as following.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Create a new document
Document doc = new Document();
// Add page in document
Page page = doc.Pages.Add();
// Initialize new table
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Add row in table 
Row row = table.Rows.Add();
// Add cell in table
Cell cell = row.Cells.Add("Cell 1 text");
cell = row.Cells.Add("Cell 2 text");
// Get table width
Console.WriteLine(table.GetWidth());
```

## Add SVG Object to Table Cell

Aspose.PDF for .NET supports the feature to add a table cell into a PDF file. While creating a table, it is possible to add text or images into the cells. Furthermore, the API also offers the feature to convert SVG files to PDF format. Using a combination of these features, it is possible to load an SVG image and add it into a table cell.

The following code snippet shows the steps for creating a table instance and adding an SVG image inside a table cell.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instantiate Document object
Document doc = new Document();
// Create an image instance
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Set image type as SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Path for source file
img.File = dataDir + "SVGToPDF.svg";
// Set width for image instance
img.FixWidth = 50;
// Set height for image instance
img.FixHeight = 50;
// Create table instance
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Set width for table cells
table.ColumnWidths = "100 100";
// Create row object and add it to table instance
Aspose.Pdf.Row row = table.Rows.Add();
// Create cell object and add it to row instance
Aspose.Pdf.Cell cell = row.Cells.Add();
// Add textfragment to paragraphs collection of cell object
cell.Paragraphs.Add(new TextFragment("First cell"));
// Add another cell to row object
cell = row.Cells.Add();
// Add SVG image to paragraphs collection of recently added cell instance
cell.Paragraphs.Add(img);
// Create page object and add it to pages collection of document instance
Page page = doc.Pages.Add();
// Add table to paragraphs collection of page object
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Save PDF file
doc.Save(dataDir);
```

## Add HTML Tags inside Table

Sometimes you can come up with a requirement to import database contents that have some HTML tags and then import the content to the Table object. When importing the content, it should be rendered the HTML tags accordingly inside PDF document. We have enhanced ImprotDataTable() method, in order to achieve such requirement as follows:

{{% alert color="primary" %}}

Please take into account that using of HTML Tags inside table element increases document generation time, as API needs to process HTML Tags accordingly and render them in the output PDF document.

{{% /alert %}}

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Initializes a new instance of the Table
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
//Set column widths of the table
tableProvider.ColumnWidths = "400 50 ";
// Set the table border color as LightGray
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Set the border for table cells
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```

## Insert a Page Break between rows of table

As a default behavior, when creating a table inside a PDF file, the table flows to subsequent pages when it reaches tables Bottom margin. However, we may have a requirement to forcefully insert page break when a certain number of rows are added for table. The following code snippet shows the steps to insert page break when 10 rows are added for the table.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instantiate Document instance
Document doc = new Document();
// Add page to pages collection of PDF file
doc.Pages.Add();
// Create table instance
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Set border style for table
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Set default border style for table with border color as Red
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Specify table columsn widht
tab.ColumnWidths = "100 100";
// Create a loop to add 200 rows for table
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Cell " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Cell " + counter + ", 1"));
    row.Cells.Add(cell2);
    // When 10 rows are added, render new row in new page
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Add table to paragraphs collection of PDF file
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Save the PDF document
doc.Save(dataDir);
```

## Extract table border as Image

The page borders are path drawing operations. Therefore the Pdf->Html processing logic just performs drawing instructions and places the background behind the text. So, to repeat the logic, you have to process contents operators manually and draw the graphics yourself. Also please note that following code snippet might not work accurately for various PDF files but if you encounter any issue, please feel free to contact. This code was developed for specific PDF files. The following code snippet shows the steps to extract the table border as Image from PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document(dataDir + "input.pdf");

Stack graphicsState = new Stack();
System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap((int)doc.Pages[1].PageInfo.Width, (int)doc.Pages[1].PageInfo.Height);
System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
// Default ctm matrix value is 1,0,0,1,0,0
System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
// System.Drawing coordinate system is top left based, while pdf coordinate system is low left based, so we have to apply the inversion matrix
System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)doc.Pages[1].PageInfo.Height);
System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
{
    gr.SmoothingMode = SmoothingMode.HighQuality;
    graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

    // Process all the contents commands
    foreach (Operator op in doc.Pages[1].Contents)
    {
        Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
        Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
        Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
        Aspose.Pdf.Operators.MoveTo opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
        Aspose.Pdf.Operators.LineTo opLineTo = op as Aspose.Pdf.Operators.LineTo;
        Aspose.Pdf.Operators.Re opRe = op as Aspose.Pdf.Operators.Re;
        Aspose.Pdf.Operators.EndPath opEndPath = op as Aspose.Pdf.Operators.EndPath;
        Aspose.Pdf.Operators.Stroke opStroke = op as Aspose.Pdf.Operators.Stroke;
        Aspose.Pdf.Operators.Fill opFill = op as Aspose.Pdf.Operators.Fill;
        Aspose.Pdf.Operators.EOFill opEOFill = op as Aspose.Pdf.Operators.EOFill;
        Aspose.Pdf.Operators.SetRGBColor opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
        Aspose.Pdf.Operators.SetRGBColorStroke opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

        if (opSaveState != null)
        {
            // Save previous state and push current state to the top of the stack
            graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opRestoreState != null)
        {
            // Throw away current state and restore previous one
            graphicsState.Pop();
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opCtm != null)
        {
            System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
                (float)opCtm.Matrix.A,
                (float)opCtm.Matrix.B,
                (float)opCtm.Matrix.C,
                (float)opCtm.Matrix.D,
                (float)opCtm.Matrix.E,
                (float)opCtm.Matrix.F);

            // Multiply current matrix with the state matrix
            ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opMoveTo != null)
        {
            lastPoint = new System.Drawing.PointF((float)opMoveTo.X, (float)opMoveTo.Y);
        }
        else if (opLineTo != null)
        {
            System.Drawing.PointF linePoint = new System.Drawing.PointF((float)opLineTo.X, (float)opLineTo.Y);
            graphicsPath.AddLine(lastPoint, linePoint);

            lastPoint = linePoint;
        }
        else if (opRe != null)
        {
            System.Drawing.RectangleF re = new System.Drawing.RectangleF((float)opRe.X, (float)opRe.Y, (float)opRe.Width, (float)opRe.Height);
            graphicsPath.AddRectangle(re);
        }
        else if (opEndPath != null)
        {
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opRGBFillColor != null)
        {
            fillColor = opRGBFillColor.getColor();
        }
        else if (opRGBStrokeColor != null)
        {
            strokeColor = opRGBStrokeColor.getColor();
        }
        else if (opStroke != null)
        {
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.DrawPath(new System.Drawing.Pen(strokeColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opFill != null)
        {
            graphicsPath.FillMode = FillMode.Winding;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opEOFill != null)
        {
            graphicsPath.FillMode = FillMode.Alternate;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
    }
}
dataDir = dataDir + "ExtractBorder_out.png";
bitmap.Save(dataDir, ImageFormat.Png);
```

## Render Table on New Page

By default, paragraphs are added to a Page object’s Paragraphs collection. However, it is possible to render a table on a new page instead of directly after the previously added paragraph level object on the page.

### Adding a Table

To render table on a new page, use the [IsInNewPage](https://apireference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) property in the BaseParagraph class. The following code snippet shows how.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Added page.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// I want to keep table 1 to next page please...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```
