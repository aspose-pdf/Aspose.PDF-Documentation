---
title: Entity Frameworkを使用してテーブルをレンダリング
linktitle: Entity Frameworkを使用してテーブルをレンダリング
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/render-table-using-entity-framework-model-as-data-source/
description: この記事では、Aspose.PDF for .NETを使用してEntity Frameworkモデルをデータソースとしてテーブルをレンダリングする方法を示します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render table with Entity Framework",
    "alternativeHeadline": "Render PDF from Entity Framework Data Easily",
    "abstract": "Entity FrameworkモデルからPDF文書に直接テーブルをシームレスにレンダリングする新機能を紹介します。Aspose.PDF for .NETを使用して、データの視覚化を簡素化し、ユーザーがORMフレームワークからデータを効率的にインポートできるようにし、カスタマイズ可能な属性とフォーマットオプションを持つ構造化されたテーブルを作成します。この強力な統合により、HTMLベースの変換を必要とせずに、クリーンでプロフェッショナルなPDF出力を提供し、レポート機能を強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1540",
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
    "url": "/net/render-table-using-entity-framework-model-as-data-source/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-table-using-entity-framework-model-as-data-source/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

データベースからPDF文書にデータをエクスポートする際、最近人気のHTMLからPDFへの変換スキームを使用せずに行う方が便利な場合がいくつかあります。

この記事では、Aspose.PDF for .NETを使用してPDF文書を生成する方法を示します。

## Aspose.PDFを使用したPDF生成の基本

Aspose.PDFで最も重要なクラスの1つは[Documentクラス](https://reference.aspose.com/pdf/net/aspose.pdf/document)です。このクラスはPDFレンダリングエンジンです。PDF構造を表現するために、Aspose.PDFライブラリはDocument-Pageモデルを使用します。ここで：

* Document - PDF文書のプロパティを含み、ページコレクションを持ちます。
* Page - 特定のページのプロパティと、このページに関連するさまざまな要素のコレクションを含みます。

したがって、Aspose.PDFを使用してPDF文書を作成するには、次の手順に従う必要があります。

1. Documentオブジェクトを作成します。
1. Documentオブジェクトにページ（Pageオブジェクト）を追加します。
1. ページに配置されるオブジェクトを作成します（例：テキストフラグメント、テーブルなど）。
1. 作成したアイテムをページの対応するコレクションに追加します（この場合は段落コレクションになります）。
1. 文書をPDFファイルとして保存します。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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
        // Add page
        var page = document.Pages.Add();

        var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

        var table = new Aspose.Pdf.Table
        {
            // .................................
        };

        page.Paragraphs.Add(textFragment);
        page.Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "tenants.pdf"
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

    // Add page
    var page = document.Pages.Add();

    var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

    var table = new Aspose.Pdf.Table
    {
        // .................................
    };

    page.Paragraphs.Add(textFragment);
    page.Paragraphs.Add(table);

    using var streamOut = new MemoryStream();

    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
{{< /tab >}}
{{< /tabs >}}

最も一般的な問題は、テーブル形式でデータを出力することです。[Tableクラス](https://reference.aspose.com/pdf/net/aspose.pdf/table)はテーブルを処理するために使用されます。このクラスは、テーブルを作成し、[Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows)と[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell)を使用して文書に配置する能力を提供します。したがって、テーブルを作成するには、必要な数の行を追加し、それらを適切な数のセルで埋める必要があります。

次の例では、4x10のテーブルを作成します。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

その結果、等幅の列を持つ4x10のテーブルが得られます。

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## ADO.NETオブジェクトからのデータのエクスポート

Tableクラスは、ADO.NETデータソースと対話するためのメソッドを提供します - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1)と[ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview)。最初のメソッドはDataTableからデータをインポートし、2番目はDataViewからデータをインポートします。
これらのオブジェクトはMVCテンプレートで作業するにはあまり便利ではないため、簡単な例に制限します。この例では（行50）、ImportDataTableメソッドが呼び出され、DataTableインスタンスとヘッダーフラグ、データ出力の初期位置（行/列）などの追加設定をパラメータとして受け取ります。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

## Entity Frameworkからのデータのエクスポート

現代の.NETにとってより関連性が高いのは、ORMフレームワークからのデータのインポートです。この場合、単純なリストまたはグループ化されたデータからデータをインポートするための拡張メソッドでTableクラスを拡張するのが良いアイデアです。最も人気のあるORMの1つであるEntity Frameworkの例を示しましょう。

```csharp
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Aspose.Pdf.Table table, IList<TSource> data)
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

    private static void ImportGroupedData<TKey, TValue>(this Aspose.Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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
            cell.BackgroundColor = Aspose.Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.White;

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

Data Annotations属性は、モデルを記述するためによく使用され、テーブルを作成するのに役立ちます。したがって、ImportEntityListのために次のテーブル生成アルゴリズムが選択されました：

* 行12-18：ヘッダ行を構築し、「DisplayAttributeが存在する場合はその値を取得し、そうでなければプロパティ名を取得する」というルールに従ってヘッダーセルを追加します。
* 行50-53：データ行を構築し、「DataTypeAttributeが定義されている場合は、追加のデザイン設定が必要かどうかを確認し、そうでなければデータを文字列に変換してセルに追加する」というルールに従って行セルを追加します。

この例では、DataType.Currency（行32-34）およびDataType.Date（行35-43）に対して追加のカスタマイズが行われましたが、必要に応じて他のカスタマイズを追加できます。
ImportGroupedDataメソッドのアルゴリズムは、前のものとほぼ同じです。グループ化されたデータを保存するために、追加のGroupViewModelクラスが使用されます。

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

グループを処理するため、最初にキー値の行を生成し（行66-71）、その後にこのグループの行を生成します。