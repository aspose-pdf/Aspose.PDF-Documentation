---
title: データソースからテーブルをレンダリング
linktitle: データソースからテーブルをレンダリング
type: docs
weight: 30
url: ja/net/render-table-from-the-data-source/
description: このページでは、Aspose.PDfライブラリを使用してデータソースからテーブルをレンダリングする方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDFを使用すると、PdfLightTableクラスを使用してDataSet、DataTable、配列、およびIEnumerableオブジェクトからDataSourceを持つテーブルを作成できます。

[Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table)は、テーブルを処理するために使用されます。このクラスにより、テーブルを作成してドキュメントに配置することができます。これには、[Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows)と[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell)を使用します。したがって、テーブルを作成するには、必要な数の行を追加し、適切な数のセルで埋める必要があります。

次の例では、4x10のテーブルを作成します。

```csharp
var table = new Table
    {
        // テーブルの列の自動幅を設定
        ColumnWidths = "25% 25% 25% 25%",
        // セルのパディングを設定
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 左 下 右 上
        // テーブルのボーダーカラーを緑に設定
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // テーブルセルのボーダーを黒に設定
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // テーブルに行を追加
        var row = table.Rows.Add();
        // テーブルセルを追加
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // テーブルオブジェクトを入力ドキュメントの最初のページに追加
    document.Pages[1].Paragraphs.Add(table);
```
Tableオブジェクトを初期化する際には、最小限のスキン設定が使用されました：

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 列の幅（デフォルト）;
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - テーブルセルのデフォルトのフィールド;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - テーブル枠の属性（スタイル、厚さ、色）;
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - セル枠の属性（スタイル、厚さ、色）。

## オブジェクトの配列からのデータのエクスポート

Tableクラスは、ADO.NETデータソースとのやり取りを可能にするメソッドを提供しています - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) および [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview)。

これらのオブジェクトが MVC テンプレートでの作業にあまり適していないという前提で、簡単な例に限定します。この例（行 50）では、ImportDataTable メソッドが呼び出され、パラメータとして DataTable インスタンスと、ヘッダーフラグ、データ出力の初期位置（行/列）などの追加設定を受け取ります。

```csharp
// 新しいPDFドキュメントを作成
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// レポートのタイトル用の新しいTextFragmentインスタンスを初期化
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // テーブルの列幅を設定
    ColumnWidths = "25% 25% 25% 25%",
    // セルのパディングを設定
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 左 下 右 上
    // テーブルの境界線の色を緑に設定
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // テーブルのセルの境界線を黒に設定
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("config.jsonに接続文字列がありません");

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

// テーブルオブジェクトを入力ドキュメントの最初のページに追加
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

