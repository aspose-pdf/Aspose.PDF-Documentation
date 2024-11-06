---
title: タグ付きPDFでのテーブルの操作
linktitle: タグ付きPDFでのテーブルの操作
type: docs
weight: 40
url: ja/net/working-with-table-in-tagged-pdfs/
description: この記事では、Aspose.PDF for .NETを使用してタグ付きPDFドキュメントでテーブルを操作する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "タグ付きPDFでのテーブルの操作",
    "alternativeHeadline": "タグ付きPDFでのテーブル操作",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "テーブル, PDF, スタイルテーブル要素, テーブル作成",
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
    "url": "/net/working-with-table-in-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-table-in-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してタグ付きPDFドキュメントでテーブルを操作する方法について説明します。"
}
</script>
## タグ付きPDFでのテーブル作成

Aspose.PDF for .NETは、タグ付きPDFドキュメントにテーブルを作成することができます。
Aspose.PDF for .NETは、タグ付きPDFドキュメントで表を作成することができます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

次のコードスニペットは、タグ付きPDFドキュメントで表を作成する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを作成
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("例の表");
taggedContent.SetLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.RootElement;


TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.Border = new BorderInfo(BorderSide.All, 1.2F, Color.DarkBlue);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "ヘッド行";

headTrElement.BackgroundColor = Color.LightGray;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("ヘッド {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("行 {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
{
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("セル [{0}, {1}]", rowIndex, colIndex));


        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "フット行";

footTrElement.BackgroundColor = Color.LightSeaGreen;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("フット {0}", colIndex));

    tdElement.Alignment = HorizontalAlignment.Center;
    tdElement.StructureTextState.FontSize = 7F;
    tdElement.StructureTextState.FontStyle = FontStyles.Bold;
}


StructureAttributes tableAttributes = tableElement.Attributes.GetAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.SetStringValue("表の概要テキスト");
tableAttributes.SetAttribute(summaryAttribute);


// タグ付きPDFドキュメントを保存
document.Save(dataDir + "CreateTableElement.pdf");

// PDF/UAコンプライアンスをチェック
document = new Document(dataDir + "CreateTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "table.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UAコンプライアンス: {0}", isPdfUaCompliance));
```
## スタイルテーブル要素

Aspose.PDF for .NET はタグ付きPDFドキュメントでテーブルをスタイリングすることができます。テーブルをスタイリングするために、[ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) インターフェースの [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) メソッドを使用してテーブルを作成し、[TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) クラスのプロパティを使用してスタイルを設定できます。以下は、テーブルをスタイルするために使用できるプロパティのリストです：

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/border)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/alignment)
- [CornerStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [CornerStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [Broken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/broken)
- [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnadjustment)
- [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnwidths)
- [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellborder)
- [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellpadding)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcelltextstate)
- [DefaultColumnWidth](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcolumnwidth)
- [IsBroken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)
- [IsBroken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)
- [IsBordersIncluded](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbordersincluded)
- [Left](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/left)
- [Top](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/top)

タグ付きPDFドキュメントのテーブルスタイルを設定するコードスニペットは以下の通りです:

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを作成
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("例のテーブルスタイル");
taggedContent.SetLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.RootElement;

// テーブル構造要素を作成
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.BackgroundColor = Color.Beige;
tableElement.Border = new BorderInfo(BorderSide.All, 0.80F, Color.Gray);
tableElement.Alignment = HorizontalAlignment.Center;
tableElement.Broken = TableBroken.Vertical;
tableElement.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;
tableElement.ColumnWidths = "80 80 80 80 80";
tableElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.DarkBlue);
tableElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
tableElement.DefaultCellTextState.ForegroundColor = Color.DarkCyan;
tableElement.DefaultCellTextState.FontSize = 8F;
tableElement.DefaultColumnWidth = "70";

tableElement.IsBroken = false;
tableElement.IsBordersIncluded = true;

tableElement.Left = 0F;
tableElement.Top = 40F;

tableElement.RepeatingColumnsCount = 2;
tableElement.RepeatingRowsCount = 3;
TextState rowStyle = new TextState();
rowStyle.BackgroundColor = Color.LightCoral;
tableElement.RepeatingRowsStyle = rowStyle;

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "ヘッド行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("ヘッド {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("行 {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("セル [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "フット行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("フット {0}", colIndex));
}

// タグ付きPDFドキュメントを保存
document.Save(dataDir + "StyleTableElement.pdf");

// PDF/UA準拠をチェック
document = new Document(dataDir + "StyleTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableElement.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA準拠: {0}", isPdfUaCompliance));
```
## スタイルテーブル行

Aspose.PDF for .NETは、タグ付きPDFドキュメントのテーブル行のスタイルを設定することができます。テーブル行をスタイルするために、[TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement)クラスのプロパティを使用できます。以下はテーブル行をスタイルするために使用できるプロパティのリストです：

- 背景色
- ボーダー
- デフォルトセルボーダー
- 最小行高
- 固定行高
- 新しいページにあるか
- 行が中断されたか
- デフォルトセルテキストステート
- デフォルトセルパディング
- 垂直配置

次のコードスニペットは、タグ付きPDFドキュメントでテーブル行をスタイルする方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを作成する
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("例のテーブル行スタイル");
taggedContent.SetLanguage("en-US");

// ルート構造要素を取得する
StructureElement rootElement = taggedContent.RootElement;

// テーブル構造要素を作成する
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "ヘッド行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("ヘッド {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("行 {0}", rowIndex);

    trElement.BackgroundColor = Color.LightGoldenrodYellow;
    trElement.Border = new BorderInfo(BorderSide.All, 0.75F, Color.DarkGray);

    trElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.Blue);
    trElement.MinRowHeight = 100.0;
    trElement.FixedRowHeight = 120.0;
    trElement.IsInNewPage = (rowIndex % 3 == 1);
    trElement.IsRowBroken = true;

    TextState cellTextState = new TextState();
    cellTextState.ForegroundColor = Color.Red;
    trElement.DefaultCellTextState = cellTextState;

    trElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
    trElement.VerticalAlignment = VerticalAlignment.Bottom;

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("セル [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "フット行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("フット {0}", colIndex));
}

// タグ付きPDFドキュメントを保存する
document.Save(dataDir + "StyleTableRow.pdf");

// PDF/UA準拠をチェックする
document = new Document(dataDir + "StyleTableRow.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableRow.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA準拠: {0}", isPdfUaCompliance));
```
## スタイルテーブルセル

Aspose.PDF for .NET では、タグ付きPDFドキュメントのテーブルセルをスタイリングすることができます。テーブルセルをスタイルするためには、[TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement) クラスのプロパティを使用できます。以下は、テーブルセルをスタイルするために使用できるプロパティのリストです：

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/border)
- [IsNoBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/isnoborder)
- [Margin](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/margin)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/alignment)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [IsWordWrapped](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/iswordwrapped)
- [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/verticalalignment)
- [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/colspan)
- [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/rowspan)

以下のコードスニペットは、タグ付きPDFドキュメントのテーブルセルにスタイルを適用する方法を示しています:

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// ドキュメントを作成
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("例：テーブルセルスタイル");
taggedContent.SetLanguage("en-US");

// ルート構造要素を取得
StructureElement rootElement = taggedContent.RootElement;

// テーブル構造要素を作成
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "ヘッド行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("ヘッド {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("行 {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("セル [{0}, {1}]", rowIndex, colIndex));


        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "フット行";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("フット {0}", colIndex));
}

// タグ付きPdfドキュメントを保存
document.Save(dataDir + "StyleTableCell.pdf");

// PDF/UAコンプライアンスの確認
document = new Document(dataDir + "StyleTableCell.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableCell.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UAコンプライアンス: {0}", isPdfUaCompliance));
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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "en"
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

