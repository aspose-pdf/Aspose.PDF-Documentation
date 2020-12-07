---
title: Manipulate and Integrate Table
type: docs
weight: 20
url: /net/manipulate-and-integrate-table/
description: This article shows how to manipulate and integrate tables. You can read about set border style, margins, and padding of the table,  integrating table with the database, manipulating tables in existing PDF.
---

## Set Border Style, Margins and Padding of the Table (MergedAPI)

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) allows developers to create tables in PDF documents. Moreover, they can apply effects like border style, margins and cell padding, to the tables.

## Borders

To set the borders of Table, [Row](https://apireference.aspose.com/pdf/net/aspose.pdf/row) and [Cell](https://apireference.aspose.com/pdf/net/aspose.pdf/cell) objects, use the Table.Border, Row.Border and Cell.Border properties. Cell borders can also be set using the [Table](https://apireference.aspose.com/pdf/net/aspose.pdf/table) or Row class’ DefaultCellBorder property. All border related properties discussed above are assigned an instance of the Row class, which is created by calling its constructor. The Row class has many overloads that take almost all the parameters required to customize the border.

## Margins or Padding

Cell padding can be managed using the Table class’ [DefaultCellPadding](https://apireference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) property . All padding related properties are assigned an instance of the [MarginInfo](https://apireference.aspose.com/pdf/net/aspose.pdf/margininfo) class that takes information about the Left, Right, Top and Bottom parameters to create custom margins.

In the following example, the width of the cell border is set to 0.1 point, the width of the table border is set to 1 point and cell padding is set to 5 points.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
            
// Instntiate the Document object by calling its empty constructor
Document doc = new Document();
Page page = doc.Pages.Add();
// Instantiate a table object
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Add the table in paragraphs collection of the desired section
page.Paragraphs.Add(tab1);
// Set with column widths of the table
tab1.ColumnWidths = "50 50 50";
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
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 with large text string");
// Row1.Cells.Add("col3 with large text string to be placed inside cell");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Save the Pdf
doc.Save(dataDir);
```

To create table with rounded corner, use the BorderInfo class’ RoundedBorderRadius value and set the table corner style to round.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Create a blank BorderInfo object
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Set the border a rounder border where radius of round is 15
bInfo.RoundedBorderRadius = 15;
// Set the table Corner style as Round.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Set the table border information
tab1.Border = bInfo;
```
## Double Border

As stated above, the border can be added to Table or Cell objects. Our users have requested that we add a feature that allows them to add a double border around Table and Cell objects. This feature was added with Aspose.PDF for .NET 8.8.0. The code snippet below shows how to accomplish this requirement.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
           
// Instantiate Document object
Document doc = new Document();
// Add page to PDF document
Page page = doc.Pages.Add();
// Create BorderInfo object
Aspose.Pdf.BorderInfo border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All);
// Specify that Top border will be double
border.Top.IsDoubled = true;
// Specify that bottom border will be double
border.Bottom.IsDoubled = true;
// Instantiate Table object
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Specify Columns width information
table.ColumnWidths = "100";
// Create Row object
Aspose.Pdf.Row row = table.Rows.Add();
// Add a Table cell to cells collection of row
Aspose.Pdf.Cell cell = row.Cells.Add("some text");
// Set the border for cell object (double border)
cell.Border = border;
// Add table to paragraphs collection of Page
page.Paragraphs.Add(table);
dataDir = dataDir + "TableBorderTest_out.pdf";
// Save the PDF document
doc.Save(dataDir);
```
## Integrate Table with Database (DOM)

Databases are built to store and manage data. It’s common practice for programmers to populate different objects with data from databases. This article discusses adding data from a database into a table. It is possible to populate a [Table](https://apireference.aspose.com/pdf/net/aspose.pdf/table) object with data from any data source using Aspose.PDF for .NET. And it’s not only possible but it’s very easy.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) allows developers to import data from:

- Object Array
- DataTable
- DataView

This topic provides information about fetching data from a DataTable or DataView.

All developers working under .NET platform must be familiar with the basic ADO.NET concepts introduced by .NET Framework. It is possible to connect to almost all kinds of data sources using ADO.NET. We can retrieve data from databases and save it to a DataSet, DataTable or DataView. Aspose.PDF for .NET provides support for importing data from these too. This gives more freedom to developers to populate tables in PDF documents from any data source.

The ImportDataTable(..) and ImportDataView(..) methods of the Table class are used to import data from databases.

The example below demonstrates the use of the ImportDataTable method. In this example, the DataTable object is created from scratch and records are added programmatically instead of filling the DataTable with data from databases. Developers can populate DataTable from the database too according to their desire.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// Add 2 rows into the DataTable object programmatically
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// Create Document instance
Document doc = new Document();
doc.Pages.Add();
// Initializes a new instance of the Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Set column widths of the table
table.ColumnWidths = "40 100 100 100";
// Set the table border color as LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Set the border for table cells
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Add table object to first page of input document
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Save updated document containing table object
doc.Save(dataDir);
```

## How to determine if table will break in the current page

Tables are by default added from top-left position and if the table reaches the end of the page, it automatically breaks. You can programmatically get the information that either the Table will be accommodated in the current page or it will break at the bottom of the page. For that reason, first, you need to get the document size information, then you need to get the page Top and page Bottom margin information, Table top margin information and table height. If you add page Top Margin + page Bottom Margin + table Top Margin + table Height and deduct it from the document height, you can get the amount of space remaining over the document. Depending upon the particular height of row (which you have specified), you can calculate that if all the rows of a table can be accommodated within the remaining space over a page or not. Please take a look over the following code snippet. In the following code, the average row height is 23.002 Points.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instantiate an object PDF class
Document pdf = new Document();
// Add the section to PDF document sections collection
Aspose.Pdf.Page page = pdf.Pages.Add();
// Instantiate a table object
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Add the table in paragraphs collection of the desired section
page.Paragraphs.Add(table1);
// Set with column widths of the table
table1.ColumnWidths = "100 100 100";
// Set default cell border using BorderInfo object
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Set table border using another customized BorderInfo object
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Create MarginInfo object and set its left, bottom, right and top margins
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Set the default cell padding to the MarginInfo object
table1.DefaultCellPadding = margin;
// If you increase the counter to 17, table will break 
// Because it cannot be accommodated any more over this page
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Create rows in the table and then cells in the rows
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// Get the Page Height information
float PageHeight = (float)pdf.PageInfo.Height;
// Get the total height information of Page Top & Bottom margin,
// Table Top margin and table height.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Display Page Height, Table Height, table Top margin and Page Top 
// And Bottom margin information
Console.WriteLine("PDF document Height = " + pdf.PageInfo.Height.ToString() + "\nTop Margin Info = " + page.PageInfo.Margin.Top.ToString() + "\nBottom Margin Info = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nTable-Top Margin Info = " + table1.Margin.Top.ToString() + "\nAverage Row Height = " + table1.Rows[0].MinRowHeight.ToString() + " \nTable height " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTotal Page Height =" + PageHeight.ToString() + "\nCummulative height including Table =" + TotalObjectsHeight.ToString());

// Check if we deduct the sume of Page top margin + Page Bottom margin
// + Table Top margin and table height from Page height and its less
// Than 10 (an average row can be greater than 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // If the value is less than 10, then display the message. 
    // Which shows that another row can not be placed and if we add new 
    // Row, table will break. It depends upon the row height value.
    Console.WriteLine("Page Height - Objects Height < 10, so table will break");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Save the pdf document
pdf.Save(dataDir);
```
## Add Repeating Column in Table

In the Aspose.Pdf.Table class, you can set a RepeatingRowsCount that will repeat rows if the table is too long vertically and overflows to the next page. However, in some cases, tables are too wide to fit on a single page and needs to be continued to the next page. In order to serve the purpose, we have implemented RepeatingColumnsCount property in Aspose.Pdf.Table class. Setting this property will cause the table to break to next page column-wise and repeat given column count in the start of the next page. Following code snippet shows the usage of RepeatingColumnsCount property:
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Create a new document
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Instantiate an outer table that takes up the entire page
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Instantiate a table object that will be nested inside outerTable that will break inside the same page
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Add the outerTable to the page paragraphs
// Add mytable to outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Add header Row
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("header 1");
row.Cells.Add("header 2");
row.Cells.Add("header 3");
row.Cells.Add("header 4");
row.Cells.Add("header 5");
row.Cells.Add("header 6");
row.Cells.Add("header 7");
row.Cells.Add("header 11");
row.Cells.Add("header 12");
row.Cells.Add("header 13");
row.Cells.Add("header 14");
row.Cells.Add("header 15");
row.Cells.Add("header 16");
row.Cells.Add("header 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Create rows in the table and then cells in the rows 
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## Manipulate tables in existing PDF

One of the earliest features supported by Aspose.PDF for .NET is its capabilities of Working with Tables and it provides great support for adding tables in PDF files being generated from scratch or any existing PDF files. You also get the capability to Integrate Table with Database (DOM) to create dynamic tables based on database contents. In this new release, we have implemented new feature of searching and parsing simple tables that already exist on page of PDF document. A new class named **Aspose.PDF.Text.TableAbsorber** provides these capabilities. The usage of TableAbsorber is very much similar to existing TextFragmentAbsorber class. The following code snippet shows the steps to update contents in particular table cell.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Load existing PDF file
Document pdfDocument = new Document(dataDir + "input.pdf");
// Create TableAbsorber object to find tables
TableAbsorber absorber = new TableAbsorber();

// Visit first page with absorber
absorber.Visit(pdfDocument.Pages[1]);

// Get access to first table on page, their first cell and text fragments in it
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Change text of the first text fragment in the cell
fragment.Text = "hi world";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Remove Table from PDF document

We have added new function i.e. Remove() to the existing TableAbsorber Class in order to remove table from PDF document. Once the absorber successfully finds tables on the page, it becomes capable to remove them. Please check following code snippet showing how to remove a table from PDF document:
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Load existing PDF document
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Create TableAbsorber object to find tables
TableAbsorber absorber = new TableAbsorber();

// Visit first page with absorber
absorber.Visit(pdfDocument.Pages[1]);

// Get first table on the page
AbsorbedTable table = absorber.TableList[0];

// Remove the table
absorber.Remove(table);

// Save PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```
## Remove Multiple Tables from PDF document

Sometimes a PDF document may contain more than one table and you may come up with a requirement to remove multiple tables from it. In order to remove multiple tables from PDF document, please use the following code snippet:
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Load existing PDF document
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Create TableAbsorber object to find tables
TableAbsorber absorber = new TableAbsorber();

// Visit second page with absorber
absorber.Visit(pdfDocument.Pages[1]);

// Get copy of table collection
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Loop through the copy of collection and removing tables
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Save document
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Please take into account that removing or replacing of a table changes TableList collection. Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

{{% /alert %}}

## Replace old Table with a new one in PDF document

In case you need to find a particular table and replace it with the desired one, you can use Replace() the method of [TableAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) Class in order to do that. Following example demonstrate the functionality to replace the table inside PDF document:
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Load existing PDF document
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Create TableAbsorber object to find tables
TableAbsorber absorber = new TableAbsorber();

// Visit first page with absorber
absorber.Visit(pdfDocument.Pages[1]);

// Get first table on the page
AbsorbedTable table = absorber.TableList[0];

// Create new table
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// Replace the table with new one
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Save document
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
```
