---
title: Render table from the data source
linktitle: Render table from the data source
type: docs
weight: 30
url: /net/render-table-from-the-data-source/
description: This page explain how possible render table from the data source using Aspose.PDf library.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF allows you to create the table with DataSource from DataSet, Data Table, arrays and IEnumerable objects using PdfLightTable class

The [Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table) is used to process tables. This class gives us the ability to create tables and place them in the document, using [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) and [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). So, to create the table, you need to add the required number of rows and fill them with the appropriate number of cells.

The following example creates the table 4x10.

```csharp
var table = new Table
    {
        // Set column auto widths of the table
        ColumnWidths = "25% 25% 25% 25%",
        // Set cell padding
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Set the table border color as Green
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Set the border for table cells as Black
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Add row to table
        var row = table.Rows.Add();
        // Add table cells
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);
```

When initializing the Table object, the minimal skin settings were used:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - width of columns (by default);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - the default fields for the table cell;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - table frame attributes (style, thickness, color);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - attributes of the cell frame (style, thickness, color).

## Exporting data from an array of objects

The Table class provides methods for interacting with ADO.NET data sources - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) and [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview). The first method imports data from the DataTable, the second from the DataView.
Premising that these objects are not very convenient for working in the MVC template, we will limit ourselves to a brief example. In this example (line 50), the ImportDataTable method is called and receives as parameters a DataTable instance and additional settings like the header flag and the initial position (rows/cols) for the data output.

```csharp
// Create new a PDF document
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Initializes a new instance of the TextFragment for report's title
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Set column widths of the table
    ColumnWidths = "25% 25% 25% 25%",
    // Set cell padding
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
    // Set the table border color as Green
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Set the border for table cells as Black
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("No connection string in config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// Add table object to first page of input document
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```
