---
title: Add and Extract a Table
linktitle: Add and Extract a Table
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET makes it possible to carry out various manipulations with the tables contained in your pdf document. You may add and extract a table in the existing PDF document, render table on a new page and etc.
lastmod: "2021-11-01"
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
1. Set table setting (we've set the borders).
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
