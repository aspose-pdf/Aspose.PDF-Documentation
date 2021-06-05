---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /net/manipulate-tables-in-existing-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

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
