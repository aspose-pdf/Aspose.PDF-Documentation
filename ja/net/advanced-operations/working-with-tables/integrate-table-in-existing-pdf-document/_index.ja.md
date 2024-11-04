---
title: データソースPDFとテーブルを統合する
linktitle: テーブル統合
type: docs
weight: 30
url: /net/integrate-table/
description: この記事では、PDFテーブルを統合する方法を示します。データベースとテーブルを統合し、テーブルが現在のページで分割されるかどうかを判断します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "データソースPDFとテーブルを統合する",
    "alternativeHeadline": "データソースPDFとテーブルをどのように統合するか",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, テーブル統合",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、PDFテーブルを統合する方法を示します。データベースとテーブルを統合し、テーブルが現在のページで分割されるかどうかを判断します。"
}
</script>
次のコードスニペットは [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携します。

## データベースとテーブルの統合

データベースはデータの保存と管理のために構築されます。プログラマーがデータベースからのデータでさまざまなオブジェクトをポピュレートするのは一般的な習慣です。この記事では、データベースからテーブルにデータを追加することについて説明します。任意のデータソースからデータを [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) オブジェクトにポピュレートすることが可能です。そして、それは非常に簡単です。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) は開発者が以下からデータをインポートすることを可能にします:

- オブジェクト配列
- DataTable
- DataView

このトピックでは、DataTableまたはDataViewからデータを取得する情報を提供します。

.NETプラットフォームの下で働くすべての開発者は、.NETフレームワークによって導入された基本的なADO.NETの概念を熟知している必要があります。
.NETプラットフォームの下で働くすべての開発者は、.NET Frameworkによって導入された基本的なADO.NETの概念を熟知している必要があります。

TableクラスのImportDataTable(..)メソッドとImportDataView(..)メソッドは、データベースからデータを取り込むために使用されます。

以下の例は、ImportDataTableメソッドの使用方法を示しています。この例では、DataTableオブジェクトはゼロから作成され、データベースからデータを取り込む代わりにプログラムでレコードが追加されます。開発者は、データベースからDataTableを自由に入力することもできます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// データテーブルオブジェクトにプログラムで2行を追加します
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// Documentインスタンスの作成
Document doc = new Document();
doc.Pages.Add();
// Tableの新しいインスタンスを初期化します
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// テーブルの列幅を設定します
table.ColumnWidths = "40 100 100 100";
// テーブルの境界色をライトグレーに設定します
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// テーブルセルの境界を設定します
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// テーブルオブジェクトを入力文書の最初のページに追加します
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// テーブルオブジェクトを含む更新された文書を保存します
doc.Save(dataDir);
```
## 現在のページでテーブルが分割されるかどうかを判断する方法

テーブルはデフォルトで左上の位置から追加され、ページの終わりに達すると自動的に分割されます。テーブルが現在のページに収まるか、またはページの下部で分割されるかどうかをプログラムで取得することができます。そのためには、最初にドキュメントのサイズ情報を取得し、次にページの上マージンと下マージンの情報、テーブルの上マージンの情報、そしてテーブルの高さを取得する必要があります。ページ上マージン + ページ下マージン + テーブル上マージン + テーブルの高さを加算し、それをドキュメントの高さから差し引くと、ドキュメント上に残っているスペースの量を得ることができます。特定の行の高さ（指定したもの）に基づいて、テーブルのすべての行がページ上の残りのスペース内に収容できるかどうかを計算できます。以下のコードスニペットをご覧ください。次のコードでは、平均行高は23.002ポイントです。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// PDFクラスのオブジェクトをインスタンス化する
Document pdf = new Document();
// セクションをPDFドキュメントセクションコレクションに追加する
Aspose.Pdf.Page page = pdf.Pages.Add();
// テーブルオブジェクトをインスタンス化する
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// 希望するセクションの段落コレクションにテーブルを追加する
page.Paragraphs.Add(table1);
// テーブルの列幅を設定する
table1.ColumnWidths = "100 100 100";
// BorderInfoオブジェクトを使用してデフォルトのセルボーダーを設定する
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// カスタマイズされた別のBorderInfoオブジェクトを使用してテーブルボーダーを設定する
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfoオブジェクトを作成し、その左、下、右、上のマージンを設定する
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// MarginInfoオブジェクトにデフォルトのセルパディングを設定する
table1.DefaultCellPadding = margin;
// カウンターを17に増やすと、テーブルが分割される
// これ以上このページに収容することはできないからである
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // テーブルに行を作成し、その行にセルを追加する
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// ページの高さ情報を取得する
float PageHeight = (float)pdf.PageInfo.Height;
// ページの上下マージン、テーブルの上マージン、テーブルの高さの合計高さ情報を取得する
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// ページの高さ、テーブルの高さ、テーブルの上マージン、ページの上下マージン情報を表示する
Console.WriteLine("PDFドキュメントの高さ = " + pdf.PageInfo.Height.ToString() + "\n上マージン情報 = " + page.PageInfo.Margin.Top.ToString() + "\n下マージン情報 = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nテーブル上マージン情報 = " + table1.Margin.Top.ToString() + "\n平均行の高さ = " + table1.Rows[0].MinRowHeight.ToString() + " \nテーブルの高さ " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nページの全高 =" + PageHeight.ToString() + "\nテーブルを含む累積高さ =" + TotalObjectsHeight.ToString());

// ページの高さからページの上マージン + ページの下マージン
// + テーブルの上マージンとテーブルの高さを差し引いた値が10未満の場合
//（平均行は10より大きい可能性がある）
if ((PageHeight - TotalObjectsHeight) <= 10)
    // 値が10未満の場合、新しい
    // 行を追加すると、テーブルが分割されるメッセージを表示する。これは行の高さの値に依存する。
    Console.WriteLine("ページの高さ - オブジェクトの高さ < 10、したがってテーブルは分割される");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// pdfドキュメントを保存する
pdf.Save(dataDir);
```
## テーブルに繰り返し列を追加する

Aspose.Pdf.Table クラスでは、RepeatingRowsCount を設定して、テーブルが縦に長すぎて次のページにオーバーフローする場合に行を繰り返すことができます。しかし、場合によってはテーブルが横に広すぎて1ページに収まらず、次のページに続く必要があります。この目的を果たすために、Aspose.Pdf.Table クラスに RepeatingColumnsCount プロパティを実装しました。このプロパティを設定すると、テーブルが次のページに列ごとに分割され、次のページの開始時に指定した列数が繰り返されます。次のコードスニペットは、RepeatingColumnsCount プロパティの使用方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// 新しいドキュメントを作成する
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// ページ全体を占める外側のテーブルをインスタンス化する
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// outerTable 内にネストされるテーブルオブジェクトをインスタンス化する。このテーブルは同じページ内で分割される
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// outerTable をページの段落に追加する
// mytable を outerTable に追加する
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// ヘッダー行を追加する
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("header 1");
row.Cells.Add("header 2");
row.Cells.Add("header 3");
row.Cells.Add("header 4");
row.Cells.Add("header 5");
row.Cells.Add("header 6");
row.Cells.Add("header 7");
row.Cells.Add("header 11");
row.Cells.Add("header 12");
row.Cells.Add("header 13");
row.Cells.Add("header 14");
row.Cells.Add("header 15");
row.Cells.Add("header 16");
row.Cells.Add("header 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // テーブルに行を作成し、その行にセルを追加する
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## Entity Framework ソースとテーブルの統合

現代の .NET にとってより関連性の高いのは、ORM フレームワークからのデータのインポートです。この場合、シンプルなリストまたはグループ化されたデータからデータをインポートするための拡張メソッドで Table クラスを拡張することが良いアイデアです。最も人気のある ORM の一つである Entity Framework の例を示しましょう。

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
                // テーブルセルを追加
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
                // テーブルにグループ行を追加
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
Data Annotations 属性はモデルの記述によく使用され、テーブル作成を支援します。したがって、ImportEntityListのために以下のテーブル生成アルゴリズムが選ばれました：

- 行 12-18: ヘッダー行を構築し、ルール「DisplayAttributeが存在する場合はその値を取り、そうでなければプロパティ名を取る」に従ってヘッダーセルを追加します。
- 行 50-53: データ行を構築し、ルール「DataTypeAttribute属性が定義されている場合、それに対して追加のデザイン設定が必要かどうかをチェックし、そうでなければデータを文字列に変換してセルに追加します；」に従って行セルを追加します。

この例では、DataType.Currency（行 32-34）とDataType.Date（行 35-43）に対して追加のカスタマイズが行われましたが、必要に応じて他のカスタマイズを追加することができます。
ImportGroupedDataメソッドのアルゴリズムは前述のものとほぼ同じです。追加でGroupViewModelクラスが使用され、グループ化されたデータを格納します。

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```
グループを処理しているため、最初にキー値のための行を生成し（66-71行目）、その後にこのグループの行を生成します。

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET ライブラリ",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "セールス",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "セールス",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "セールス",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

