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
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render table from the data source",
    "alternativeHeadline": "Create Tables from Various Data Sources Easily",
    "abstract": "Aspose.PDF for .NET introduces a powerful feature to render tables directly from various data sources such as DataSets, DataTables, and arrays using the PdfLightTable class. This functionality simplifies the process of integrating dynamic data into PDF documents, allowing developers to easily create and customize tables with flexible attributes like column widths, cell padding, and borders. Enhance your document automation with seamless data integration and precise table formatting capabilities",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "670",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/render-table-from-the-data-source/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-table-from-the-data-source/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Aspose.PDF allows you to create the table with DataSource from DataSet, Data Table, arrays and IEnumerable objects using PdfLightTable class

The [Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table) is used to process tables. This class gives us the ability to create tables and place them in the document, using [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) and [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). So, to create the table, you need to add the required number of rows and fill them with the appropriate number of cells.

The following example creates the table 4x10.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            // Set column auto widths of the table
            ColumnWidths = "25% 25% 25% 25%",

            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        for (var rowCount = 0; rowCount < 10; rowCount++)
        {
            // Add row to table
            var row = table.Rows.Add();

            // Add table cells
            for (int i = 0; i < 4; i++)
            {
                row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
            }
        }

        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    document.Pages.Add();

    var table = new Aspose.Pdf.Table
    {
        // Set column auto widths of the table
        ColumnWidths = "25% 25% 25% 25%",

        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Add row to table
        var row = table.Rows.Add();

        // Add table cells
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
        }
    }

    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);

    // Save PDF document
    document.Save(dataDir + "AddTable_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

When initializing the Table object, the minimal skin settings were used:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - width of columns (by default).
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - the default fields for the table cell.
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - table frame attributes (style, thickness, color).
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - attributes of the cell frame (style, thickness, color).

## Exporting data from an array of objects

The Table class provides methods for interacting with ADO.NET data sources - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) and [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview). The first method imports data from the DataTable, the second from the DataView.
Premising that these objects are not very convenient for working in the MVC template, we will limit ourselves to a brief example. In this example (line 50), the ImportDataTable method is called and receives as parameters a DataTable instance and additional settings like the header flag and the initial position (rows/cols) for the data output.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    })
    {
        var table = new Aspose.Pdf.Table
        {
            // Set column widths of the table
            ColumnWidths = "25% 25% 25% 25%",
            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("config.json", false)
            .Build();

        var connectionString = configuration.GetSection("connectionString").Value;

        if (string.IsNullOrEmpty(connectionString))
        {
            throw new ArgumentException("No connection string in config.json");
        }

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

        table.ImportDataTable(resultTable, true, 1, 1);

        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "demotable2.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    var table = new Aspose.Pdf.Table
    {
        // Set column widths of the table
        ColumnWidths = "25% 25% 25% 25%",
        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    var configuration = new ConfigurationBuilder()
        .SetBasePath(Directory.GetCurrentDirectory())
        .AddJsonFile("config.json", false)
        .Build();

    var connectionString = configuration.GetSection("connectionString").Value;

    if (string.IsNullOrEmpty(connectionString))
    {
        throw new ArgumentException("No connection string in config.json");
    }

    var resultTable = new DataTable();

    using var conn = new SqlConnection(connectionString);

    const string sql = "SELECT * FROM Tennats";

    using var cmd = new SqlCommand(sql, conn);

    using var adapter = new SqlDataAdapter(cmd);
    
    adapter.Fill(resultTable);

    table.ImportDataTable(resultTable, true, 1, 1);

    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);

    using var streamOut = new MemoryStream();
    
    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };
}
```
{{< /tab >}}
{{< /tabs >}}
