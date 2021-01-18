---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 50
url: /net/remove-tables-from-existing-pdf/
lastmod: "2021-01-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF for NET offers the capabilities to insert/create Table inside PDF document while its being generated from scratch or you can also add the table object in any existing PDF document. However you may have a requirement to [Manipulate Tables in existing PDF](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) where you can update the contents in existing table cells. However you may come across a requirement to remove table objects from existing PDF document.

{{% /alert %}}

In order to remove the tables, we need to use [TableAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) class to get hold of tables in existing PDF and then call [Remove](https://apireference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

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