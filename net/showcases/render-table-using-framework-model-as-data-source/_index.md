---
title: Render table with Entity Framework 
linktitle: Render table with Entity Framework
type: docs
weight: 40
url: /net/render-table-using-entity-framework-model-as-data-source/
description: This article will show you how to render table using Entity Framework model as data source using the Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

There are a number of tasks when for some reason it is more convenient to export data from databases to a PDF document without using the recently popular HTML to PDF conversion scheme.

This article will show you how to generate a PDF document using the Aspose.PDF for .NET.

## Basics of generation PDF with Aspose.PDF

One of the most important classes in Aspose.PDF is a [Document class](https://reference.aspose.com/pdf/net/aspose.pdf/document). This class is a PDF rendering engine. To present a PDF structure, the Aspose.PDF library uses the Document-Page model, where:

* Document - contains the properties of the PDF document including page collection;
* Page - contains the properties of a specific page and various collections of elements associated with this page.

Therefore, to create a PDF document with Aspose.PDF, you should follow these steps:

1. Create the Document object;
1. Add the page (the Page object) for the Document object;
1. Create objects that are placed on the page (e.g. text fragment, table, etc.)
1. Add created items to the corresponding collection on the page (in our case it will be a paragraph collection);
1. Save the document as PDF file.

```csharp
// Step 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Step 2
var pdfPage = document.Pages.Add();

// Step 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Step 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Step 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```

The most common problem is the output of data in a table format. The [Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table) is used to process tables. This class gives us the ability to create tables and place them in the document, using [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) and [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). So, to create the table, you need to add the required number of rows and fill them with the appropriate number of cells.

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

As a result, we get the table 4x10 with equal-width columns.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Exporting Data from ADO.NET Objects

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

## Exporting Data from the Entity Framework

More relevant for modern .NET is the import of data from ORM frameworks. In this case, it's a good idea to extend the Table class with extension methods for importing data from a simple list or from the grouped data. Let's give an example for one of the most popular ORMs - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Add row to table
                var row = table.Rows.Add();
                // Add table cells
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Add group row to table
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Add data row to table
                    var dataRow = table.Rows.Add();
                    // Add cells
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```

The Data Annotations attributes are often used to describe models and help us to create the table. Therefore, the following table generation algorithm was chosen for ImportEntityList:

* lines 12-18: build a header row and add header cells according to the rule "If the DisplayAttribute is present, then take its value otherwise take the property name"
* lines 50-53: build the data rows and add row cells according to the rule "If the attribute DataTypeAttribute is defined, then we check whether we need to make additional design settings for it, and otherwise just convert data to string and add to the cell;"

In this example, additional customizations were made for DataType.Currency (lines 32-34) and DataType.Date (lines 35-43), but you can add others if necessary.
The algorithm of the ImportGroupedData method is almost the same as the previous one. An additional GroupViewModel class is used, to store the grouped data.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```

Since we process groups, first we generate a line for the key value (lines 66-71), and after it - the lines of this group.
