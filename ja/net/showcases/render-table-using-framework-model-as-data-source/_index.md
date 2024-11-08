---
title: エンティティフレームワークでテーブルをレンダリングする
linktitle: エンティティフレームワークでテーブルをレンダリングする
type: docs
weight: 40
url: /ja/net/render-table-using-entity-framework-model-as-data-source/
description: この記事では、Aspose.PDF for .NETを使用して、エンティティフレームワークモデルをデータソースとしてテーブルをレンダリングする方法を示します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

データベースからPDFドキュメントにデータをエクスポートする際には、最近人気のHTMLからPDFへの変換スキームを使用しない方が便利な場合があります。

この記事では、Aspose.PDF for .NETを使用してPDFドキュメントを生成する方法を示します。

## Aspose.PDFを使用したPDF生成の基本

Aspose.PDFの最も重要なクラスの一つは[Document class](https://reference.aspose.com/pdf/net/aspose.pdf/document)です。このクラスはPDFレンダリングエンジンです。PDF構造を提示するために、Aspose.PDFライブラリはドキュメント-ページモデルを使用しています。ここで、

* Document - PDFドキュメントのプロパティを含むページコレクションを含んでいます。
* ドキュメント - PDFドキュメントのプロパティを含み、ページコレクションを含んでいます。
* ページ - 特定のページのプロパティと、このページに関連付けられたさまざまな要素のコレクションを含んでいます。

したがって、Aspose.PDFでPDFドキュメントを作成するには、次の手順に従う必要があります：

1. Documentオブジェクトを作成する;
1. Documentオブジェクトのためにページ（Pageオブジェクト）を追加する;
1. ページに配置されるオブジェクトを作成する（例：テキストフラグメント、テーブルなど）
1. 作成したアイテムをページ上の対応するコレクションに追加する（この場合は段落コレクションになります）;
1. ドキュメントをPDFファイルとして保存する。

```csharp
// ステップ 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// ステップ 2
var pdfPage = document.Pages.Add();

// ステップ 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// ステップ 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// ステップ 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
最も一般的な問題は、データを表形式で出力することです。[Tableクラス](https://reference.aspose.com/pdf/net/aspose.pdf/table)は、表を処理するために使用されます。このクラスを使用すると、表を作成し、[Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows)と[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell)を使用してドキュメントに配置できます。したがって、表を作成するには、必要な数の行を追加し、適切な数のセルでそれらを埋める必要があります。

次の例では、4x10の表を作成します。

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
Tableオブジェクトを初期化する際、最小限のスキン設定が使用されました：

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 列の幅（デフォルト）;
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - テーブルセルのデフォルトのフィールド;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - テーブルフレームの属性（スタイル、厚さ、色）;
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - セルフレームの属性（スタイル、厚さ、色）。

その結果、幅が等しい列を持つ4x10のテーブルが得られます。

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## ADO.NETオブジェクトからデータをエクスポートする

TableクラスはADO.NETデータソースとのやり取りのためのメソッドを提供しています - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) および [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Table クラスは、ADO.NET データソースと対話するためのメソッドを提供します - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) および [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview)。
これらのオブジェクトが MVC テンプレートでの作業にあまり適していないという前提で、簡単な例に限定します。この例（行 50）では、ImportDataTable メソッドが呼び出され、パラメータとして DataTable インスタンスとヘッダーフラグ、データ出力の初期位置（行/列）などの追加設定を受け取ります。

```csharp
// 新しい PDF ドキュメントを作成
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// レポートのタイトル用の新しい TextFragment インスタンスを初期化
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // テーブルの列幅を設定
    ColumnWidths = "25% 25% 25% 25%",
    // セルのパディングを設定
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 左 下 右 上
    // テーブルの境界線の色を緑に設定
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // テーブルセルの境界線を黒に設定
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("config.json に接続文字列がありません");

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
## エンティティフレームワークからのデータエクスポート

現代の.NETでは、ORMフレームワークからのデータのインポートがより関連性があります。この場合、単純なリストまたはグループ化されたデータからデータをインポートするためにTableクラスを拡張メソッドで拡張するとよいでしょう。最も人気のあるORMの一つであるエンティティフレームワークの例を示しましょう。

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
                // テーブルに行を追加
                var row = table.Rows.Add();
                // テーブルのセルを追加
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
                // グループ行をテーブルに追加
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // データ行をテーブルに追加
                    var dataRow = table.Rows.Add();
                    // セルを追加
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
Data Annotations 属性は、モデルを記述し、テーブル作成を支援するためによく使用されます。そのため、ImportEntityListのテーブル生成アルゴリズムは次のように選ばれました：

* 12-18行目：ヘッダー行を構築し、ルール「DisplayAttributeが存在する場合はその値を取る、そうでなければプロパティ名を取る」に従ってヘッダーセルを追加する
* 50-53行目：データ行を構築し、ルール「DataTypeAttribute属性が定義されている場合は、それに対して追加のデザイン設定が必要かどうかを確認し、そうでなければデータを文字列に変換してセルに追加する」に従って行セルを追加する

この例では、DataType.Currency（32-34行目）および DataType.Date（35-43行目）に対して追加のカスタマイズが行われましたが、必要に応じて他のものを追加することができます。
ImportGroupedDataメソッドのアルゴリズムは前述のものとほぼ同じです。追加された GroupViewModel クラスを使用して、グループ化されたデータを保存します。

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```
グループを処理するため、最初にキー値のための行を生成します（66-71行目）。その後、このグループの行を生成します。
