---
title: データソースからテーブルをレンダリングする
linktitle: データソースからテーブルをレンダリングする
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/render-table-from-the-data-source/
description: このページでは、Aspose.PDfライブラリを使用してデータソースからテーブルをレンダリングする方法を説明します。
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
    "abstract": "Aspose.PDF for .NETは、PdfLightTableクラスを使用して、DataSets、DataTables、配列などのさまざまなデータソースから直接テーブルをレンダリングする強力な機能を紹介します。この機能により、動的データをPDF文書に統合するプロセスが簡素化され、開発者は列幅、セルの余白、境界線などの柔軟な属性を使用してテーブルを簡単に作成およびカスタマイズできます。シームレスなデータ統合と正確なテーブルフォーマット機能で文書の自動化を強化します。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

Aspose.PDFは、PdfLightTableクラスを使用して、DataSet、Data Table、配列、IEnumerableオブジェクトからデータソースを持つテーブルを作成することを可能にします。

[Tableクラス](https://reference.aspose.com/pdf/net/aspose.pdf/table)は、テーブルを処理するために使用されます。このクラスは、テーブルを作成し、[Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows)や[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell)を使用して文書に配置する能力を提供します。したがって、テーブルを作成するには、必要な数の行を追加し、それらを適切な数のセルで埋める必要があります。

次の例では、4x10のテーブルを作成します。

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
        var page = document.Pages.Add();

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
        page.Paragraphs.Add(table);

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
    var page = document.Pages.Add();

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
    page.Paragraphs.Add(table);

    // Save PDF document
    document.Save(dataDir + "AddTable_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Tableオブジェクトを初期化する際には、最小限のスキン設定が使用されました：

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 列の幅（デフォルト）。
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - テーブルセルのデフォルトフィールド。
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - テーブルフレームの属性（スタイル、厚さ、色）。
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - セルフレームの属性（スタイル、厚さ、色）。

## オブジェクトの配列からデータをエクスポートする

Tableクラスは、ADO.NETデータソースと対話するためのメソッドを提供します - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1)および[ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview)。最初のメソッドはDataTableからデータをインポートし、2番目はDataViewからデータをインポートします。
これらのオブジェクトはMVCテンプレートで作業するにはあまり便利ではないため、簡単な例に制限します。この例（行50）では、ImportDataTableメソッドが呼び出され、DataTableインスタンスとヘッダーフラグ、データ出力の初期位置（行/列）などの追加設定をパラメータとして受け取ります。

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