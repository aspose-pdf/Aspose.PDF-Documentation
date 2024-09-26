---
title: PDF内に表を作成または追加する C#
linktitle: 表を作成または追加する
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET は、PDF テーブルを作成、読み取り、編集するためのライブラリです。このトピックで他の高度な機能を確認してください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内に表を作成または追加する C#",
    "alternativeHeadline": "PDFに表を追加する方法 .NETで",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内に表を作成, 表を追加",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET は、PDF テーブルを作成、読み取り、編集するためのライブラリです。このトピックで他の高度な機能を確認してください。"
}
</script>
## C\#を使用してテーブルを作成する

PDFドキュメントを扱う際、テーブルは重要です。テーブルは情報を体系的に表示するための優れた機能を提供します。Aspose.PDF名前空間には、PDFドキュメントを一から生成する際にテーブルを作成する機能を提供する[Table](https://reference.aspose.com/pdf/net/aspose.pdf/table)、[Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)、および[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)というクラスが含まれています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

Tableクラスのオブジェクトを作成することでテーブルを作成できます。

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### 既存のPDFドキュメントにテーブルを追加する

Aspose.PDF for .NETを使用して既存のPDFファイルにテーブルを追加するには、以下の手順を実行します：

1. ソースファイルを読み込む。
1. テーブルを初期化し、その列と行を設定する。
1. テーブルの設定を行う（境界線を設定しました）。
1. テーブルにデータを入力する。
1. テーブルをページに追加する。
1.

既存のPDFファイルにテキストを追加する方法を示すコードスニペットです。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// ソースPDFドキュメントをロードします
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Tableの新しいインスタンスを初期化します
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// テーブルのボーダーカラーをライトグレーに設定します
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// テーブルセルのボーダーを設定します
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// 10行を追加するループを作成します
for (int row_count = 1; row_count < 10; row_count++)
{
    // テーブルに行を追加します
    Aspose.Pdf.Row row = table.Rows.Add();
    // テーブルセルを追加します
    row.Cells.Add("Column (" + row_count + ", 1)");
    row.Cells.Add("Column (" + row_count + ", 2)");
    row.Cells.Add("Column (" + row_count + ", 3)");
}
// テーブルオブジェクトを入力ドキュメントの最初のページに追加します
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// テーブルオブジェクトを含む更新されたドキュメントを保存します
doc.Save(dataDir);
```
### テーブル内のColSpanとRowSpan

Aspose.PDF for .NETは、テーブル内の列をマージするための[ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan)プロパティと、行をマージするための[RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan)プロパティを提供しています。

テーブルセルを作成する`Cell`オブジェクトに`ColSpan`または`RowSpan`プロパティを使用します。必要なプロパティを適用した後、作成されたセルをテーブルに追加できます。

```csharp
public static void AddTable_RowColSpan()
{
    // Load source PDF document
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Initializes a new instance of the Table
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Set the table border color as LightGray
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Set the border for table cells
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Add 1st row to table
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Add table cells
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // Add 2nd row to table
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // Add 3rd row to table
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // Add 4th row to table
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // Add 5th row to table
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // Add table object to first page of input document
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Save updated document containing table object
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
以下のコードの実行結果は、次の画像に示されている表です：

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 境界線、マージン、パディングの操作

表の境界線スタイル、マージン、セルのパディングを設定する機能もサポートしていることに注意してください。より技術的な詳細に入る前に、以下の図に示されている境界線、マージン、およびパディングの概念を理解することが重要です：

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

上記の図では、表、行、およびセルの境界線が重なっていることがわかります。Aspose.PDFを使用すると、表にマージンを設定でき、セルにはパディングを設定できます。セルのマージンを設定するには、セルのパディングを設定する必要があります。

### 境界線

Table、[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)、および[Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)オブジェクトの境界線を設定するには、Table.Border、Row.Border、およびCell.Borderプロパティを使用します。
テーブル、[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)、および[Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)オブジェクトの境界線を設定するには、Table.Border、Row.Border、およびCell.Borderプロパティを使用します。

### 余白またはパディング

セルのパディングは、Tableクラスの[DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding)プロパティを使用して管理できます。すべてのパディング関連プロパティには、`Left`、`Right`、`Top`、および`Bottom`パラメータに関する情報を取得する[MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo)クラスのインスタンスが割り当てられます。

次の例では、セルの境界線の幅を0.1ポイント、テーブルの境界線の幅を1ポイントに設定し、セルのパディングを5ポイントに設定します。

![PDFテーブルの余白と境界線](margin-border.png)

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 空のコンストラクタを呼び出すことによってDocumentオブジェクトをインスタンス化します
Document doc = new Document();
Page page = doc.Pages.Add();
// テーブルオブジェクトをインスタンス化します
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// 希望するセクションの段落コレクションにテーブルを追加します
page.Paragraphs.Add(tab1);
// テーブルの列幅を設定します
tab1.ColumnWidths = "50 50 50";
// BorderInfoオブジェクトを使用してデフォルトのセル境界線を設定します
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブル境界線を設定します
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfoオブジェクトを作成し、その左、下、右、上のマージンを設定します
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// MarginInfoオブジェクトにデフォルトのセルパディングを設定します
tab1.DefaultCellPadding = margin;
// テーブルに行を作成し、その行にセルを作成します
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 with large text string");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Pdfを保存します
doc.Save(dataDir);
```
丸い角のあるテーブルを作成するには、`BorderInfo` クラスの `RoundedBorderRadius` 値を使用し、テーブルの角のスタイルを丸く設定します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// 空のBorderInfoオブジェクトを作成
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// 境界線に丸い境界線を設定し、丸の半径を15にします
bInfo.RoundedBorderRadius = 15;
// テーブルの角のスタイルを丸く設定。
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// テーブルの境界情報を設定
tab1.Border = bInfo;
```

## テーブルに異なる自動調整設定を適用する

Microsoft Wordなどの視覚的エージェントを使用してテーブルを作成する場合、自動的にテーブルを所望の幅にサイズ調整するためにAutoFitオプションのいずれかを使用することがよくあります。
Microsoft Word などの視覚エージェントを使用してテーブルを作成する際、しばしば自動的にテーブルを所望の幅にサイズ調整する AutoFit オプションのいずれかを使用することになります。

デフォルトでは Aspose.Pdf は `ColumnAdjustment` を `Customized` 値で新しいテーブルを挿入します。このテーブルはページ上で利用可能な幅にサイズ設定されます。このようなテーブル、または既存のテーブルのサイジング動作を変更するには、Table.autoFit(int) メソッドを呼び出すことができます。このメソッドは AutoFitBehavior 列挙型を受け入れ、テーブルに適用されるオートフィットのタイプを定義します。

Microsoft Word でのように、autofit メソッドは実際には異なるプロパティを一度にテーブルに適用するショートカットです。これらのプロパティは実際にテーブルが観察される動作を与えます。各 autofit オプションについてこれらのプロパティを議論します。以下のテーブルを使用して、異なるオートフィット設定をデモンストレーションとして適用します：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 空のコンストラクタを呼び出すことにより Pdf オブジェクトをインスタンス化します
Document doc = new Document();
// Pdf オブジェクトにセクションを作成します
Page sec1 = doc.Pages.Add();

// テーブルオブジェクトをインスタンス化します
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// 希望するセクションの段落コレクションにテーブルを追加します
sec1.Paragraphs.Add(tab1);

// テーブルの列幅を設定します
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// BorderInfoオブジェクトを使用してデフォルトのセルボーダーを設定します
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// カスタマイズされたBorderInfoオブジェクトを使用してテーブルボーダーを設定します
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfoオブジェクトを作成し、その左、下、右、上のマージンを設定します
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// MarginInfoオブジェクトにデフォルトのセルパディングを設定します
tab1.DefaultCellPadding = margin;

// テーブルに行を作成し、その行にセルを作成します
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// テーブルオブジェクトを含む更新されたドキュメントを保存します
doc.Save(dataDir);
```
### テーブルの幅を取得

時々、テーブルの幅を動的に取得する必要があります。Aspose.PDF.Table クラスにはその目的のための [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) メソッドがあります。例えば、テーブルの列の幅を明示的に設定せずに [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) を AutoFitToContent に設定した場合、以下のようにテーブルの幅を取得できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 新しいドキュメントを作成
Document doc = new Document();
// ドキュメントにページを追加
Page page = doc.Pages.Add();
// 新しいテーブルを初期化
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// テーブルに行を追加
Row row = table.Rows.Add();
// テーブルにセルを追加
Cell cell = row.Cells.Add("Cell 1 text");
cell = row.Cells.Add("Cell 2 text");
// テーブルの幅を取得
Console.WriteLine(table.GetWidth());
```

## テーブルセルにSVGイメージを追加する
## テーブルセルにSVG画像を追加

Aspose.PDF for .NETは、PDFファイルにテーブルセルを追加する機能をサポートしています。テーブルを作成する際に、セルにテキストや画像を追加することが可能です。さらに、APIはSVGファイルをPDF形式に変換する機能も提供しています。これらの機能を組み合わせることで、SVG画像を読み込み、テーブルセルに追加することができます。

次のコードスニペットは、テーブルインスタンスを作成し、テーブルセル内にSVG画像を追加する手順を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Documentオブジェクトのインスタンスを作成
Document doc = new Document();
// 画像インスタンスを作成
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// 画像タイプをSVGとして設定
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// ソースファイルのパス
img.File = dataDir + "SVGToPDF.svg";
// 画像インスタンスの幅を設定
img.FixWidth = 50;
// 画像インスタンスの高さを設定
img.FixHeight = 50;
// テーブルインスタンスを作成
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// テーブルセルの幅を設定
table.ColumnWidths = "100 100";
// 行オブジェクトを作成し、テーブルインスタンスに追加
Aspose.Pdf.Row row = table.Rows.Add();
// セルオブジェクトを作成し、行インスタンスに追加
Aspose.Pdf.Cell cell = row.Cells.Add();
// セルオブジェクトの段落コレクションにTextFragmentを追加
cell.Paragraphs.Add(new TextFragment("First cell"));
// 行オブジェクトに別のセルを追加
cell = row.Cells.Add();
// 最近追加されたセルインスタンスの段落コレクションにSVG画像を追加
cell.Paragraphs.Add(img);
// ページオブジェクトを作成し、ドキュメントインスタンスのページコレクションに追加
Page page = doc.Pages.Add();
// ページオブジェクトの段落コレクションにテーブルを追加
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// PDFファイルを保存
doc.Save(dataDir);
```
## テーブル内のHTMLタグの使用

データベースの内容をインポートする際にHTMLタグが含まれている場合があり、その内容をTableオブジェクトにインポートする必要があります。インポートする際には、PDFドキュメント内でHTMLタグが適切にレンダリングされるようにする必要があります。この要件を達成するために、ImprotDataTable()メソッドを強化しました。

{{% alert color="primary" %}}

テーブル要素内でHTMLタグを使用すると、ドキュメントの生成時間が増加することに注意してください。APIはHTMLタグを適切に処理して出力PDFドキュメントにレンダリングする必要があります。

{{% /alert %}}

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Tableの新しいインスタンスを初期化
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// テーブルの列幅を設定
tableProvider.ColumnWidths = "400 50 ";
// テーブルの境界線の色をLightGrayに設定
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// テーブルセルの境界線を設定
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## テーブルの行間に改ページを挿入する

PDFファイル内にテーブルを作成する際のデフォルトの動作では、テーブルが下部のマージンに達すると、テーブルは次のページに流れます。しかし、テーブルに特定の数の行が追加されたときに強制的に改ページを挿入する必要がある場合があります。以下のコードスニペットは、テーブルに10行追加されたときに改ページを挿入する手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Documentインスタンスをインスタンス化する
Document doc = new Document();
// PDFファイルのページコレクションにページを追加
doc.Pages.Add();
// テーブルインスタンスを作成
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// テーブルのボーダースタイルを設定
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// レッドのボーダーカラーでテーブルのデフォルトボーダースタイルを設定
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// テーブルの列幅を指定
tab.ColumnWidths = "100 100";
// テーブルに200行を追加するためのループを作成
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Cell " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Cell " + counter + ", 1"));
    row.Cells.Add(cell2);
    // 10行追加されたとき、新しいページに新しい行をレンダー
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// テーブルをPDFファイルのパラグラフコレクションに追加
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// PDFドキュメントを保存
doc.Save(dataDir);
```
## 新しいページにテーブルをレンダリング

デフォルトでは、段落はPageオブジェクトのParagraphsコレクションに追加されます。しかし、以前に追加された段落レベルのオブジェクトの直後ではなく、新しいページにテーブルをレンダリングすることも可能です。

### サンプル: C#を使用して新しいページにテーブルをレンダリングする方法

新しいページにテーブルをレンダリングするには、BaseParagraphクラスの[IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage)プロパティを使用します。以下のコードスニペットを参照してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// ページを追加しました。
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// 次のページにテーブル1を保持したいです...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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
```

