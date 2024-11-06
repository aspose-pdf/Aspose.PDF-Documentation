---
title: PDF内のテキストを置換
linktitle: PDF内のテキストを置換
type: docs
weight: 40
url: ja/net/replace-text-in-pdf/
description: Aspose.PDF for .NETライブラリからテキストを置換または削除するさまざまな方法について学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストを置換",
    "alternativeHeadline": "PDFファイル内のテキストの置換および削除",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, テキストを置換, テキストを削除",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETライブラリからテキストを置換または削除するさまざまな方法について学びます。"
}
</script>

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## PDFドキュメントの全ページのテキストを置換

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを見つけて置換することができ、この[リンク](https://products.aspose.app/pdf/redaction)でオンラインで結果を得ることができます

{{% /alert %}}

PDFドキュメントの全ページのテキストを置換するには、まずTextFragmentAbsorberを使用して置換したい特定のフレーズを見つける必要があります。その後、すべてのTextFragmentsを通過してテキストを置換し、他の属性を変更する必要があります。それが完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントの全ページでテキストを置換する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// すべてのページでabsorberを受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループ
foreach (TextFragment textFragment in textFragmentCollection)
{
    // テキストと他のプロパティを更新
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```
## 特定のページ領域のテキストを置換する

特定のページ領域でテキストを置換するためには、まずTextFragmentAbsorberオブジェクトをインスタンス化し、TextSearchOptions.Rectangleプロパティを使用してページ領域を指定し、すべてのTextFragmentsを反復処理してテキストを置換します。これらの操作が完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントのすべてのページでテキストを置換する方法を示しています。

```csharp
// PDFファイルをロード
Aspose.PDF.Document pdf = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// TextFragment Absorberオブジェクトをインスタンス化
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// ページ境界内でテキストを検索
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// TextSearch Optionsのためのページ領域を指定
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// PDFファイルの最初のページからテキストを検索
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// 個々のTextFragmentを反復処理
foreach (Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // テキストを空白文字に更新
    tf.Text = "";
}

// テキスト置換後の更新されたPDFファイルを保存
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## 正規表現に基づいてテキストを置換する

正規表現に基づいてフレーズを置換したい場合、まずTextFragmentAbsorberを使用してその正規表現に一致するすべてのフレーズを見つける必要があります。正規表現をパラメータとしてTextFragmentAbsorberコンストラクタに渡す必要があります。また、正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成する必要があります。一致するフレーズがTextFragmentsで取得できたら、それらをすべてループ処理して必要に応じて更新する必要があります。最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存する必要があります。以下のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// 正規表現に一致するすべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成する
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例：1999-2000

// 正規表現の使用を指定するためのテキスト検索オプションを設定する
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 単一ページに対して吸収器を受け入れる
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得する
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループ処理する
foreach (TextFragment textFragment in textFragmentCollection)
{
    // テキストとその他のプロパティを更新する
    textFragment.Text = "New Phrase";
    // オブジェクトのインスタンスに設定する。
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## 既存のPDFファイル内のフォントを置き換える

Aspose.PDF for .NETは、PDFドキュメント内のテキストを置き換える機能をサポートしています。しかし、時々PDFドキュメント内に使用されているフォントのみを置き換える必要があります。テキストを置き換える代わりに、使用されているフォントのみが置き換えられます。TextFragmentAbsorberのコンストラクタのオーバーロードの一つは、TextEditOptionsオブジェクトを引数として受け入れ、TextEditOptions.FontReplace列挙型からRemoveUnusedFonts値を使用して要件を達成することができます。次のコードスニペットは、PDFドキュメント内のフォントを置き換える方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルを読み込む
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// テキストフラグメントを検索し、編集オプションとして未使用フォントを削除する
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// すべてのページでアブソーバを受け入れる
pdfDocument.Pages.Accept(absorber);
// すべてのテキストフラグメントを通過する
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // フォント名がArialMTの場合、フォント名をArialに置き換える
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// 更新されたドキュメントを保存する
pdfDocument.Save(dataDir);
```

## ページコンテンツは自動的に再配置されるべきです

Aspose.PDF for .NETは、PDFファイル内のテキストの検索と置換をサポートしています。しかし、最近、特定のTextFragmentがより小さなコンテンツに置換されたときに、結果のPDFに余分なスペースが表示される、またはTextFragmentがより長い文字列に置換された場合に、単語が既存のページコンテンツと重なる問題が発生していました。したがって、PDFドキュメント内のテキストを置換した後、コンテンツが再配置されるようなメカニズムを導入する要求がありました。

上記のシナリオに対応するために、Aspose.PDF for .NETは強化され、PDFファイル内のテキストを置換する際にこのような問題が発生しないようになりました。以下のコードスニペットは、PDFファイル内のテキストを置換し、ページコンテンツが自動的に再配置される方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルをロード
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// 正規表現を用いたTextFragment Absorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// 各TextFragmentを置換
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // 置換されるテキストフラグメントのフォントを設定
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // フォントサイズを設定
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // プレースホルダーよりも大きな文字列でテキストを置換
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// 結果のPDFを保存
doc.Save(dataDir);
```
## PDF作成時の置換可能なシンボルのレンダリング

置換可能なシンボルは、実行時に対応する内容に置き換えられる特別なシンボルです。現在、Aspose.PDFの新しいドキュメントオブジェクトモデルでサポートされている置換可能なシンボルは`$P`, `$p`, `\n`, `\r`です。`$p`および`$P`は実行時のページ番号処理に使用されます。`$p`は現在のParagraphクラスが存在するページの番号に置き換えられ、`$P`はドキュメントのページ総数に置き換えられます。PDFドキュメントのparagraphsコレクションに`TextFragment`を追加する際、テキスト内の改行はサポートされていません。しかし、改行を含むテキストを追加するためには、`TextFragment`を`TextParagraph`と共に使用してください：

- `TextFragment`で単一の"\n"の代わりに"\r\n"またはEnvironment.NewLineを使用する；
- `TextParagraph`オブジェクトを作成する。これにより、テキストが分割されて追加されます；
- `TextFragment`を`TextParagraph.AppendLine`で追加する；
- `TextBuilder.AppendParagraph`で`TextParagraph`を追加する。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 必要な改行マーカーを含むテキストで新しいTextFragmentを初期化
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 必要に応じてテキストフラグメントのプロパティを設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraphオブジェクトを作成
TextParagraph par = new TextParagraph();

// パラグラフに新しいTextFragmentを追加
par.AppendLine(textFragment);

// パラグラフの位置を設定
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilderを使用してTextParagraphを追加
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## ヘッダー/フッターエリアの置換可能なシンボル

置換可能なシンボルは、PDFファイルのヘッダー/フッターセクション内にも配置できます。フッターセクションに置換可能なシンボルを追加する方法の詳細については、次のコードスニペットをご覧ください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// MarginInfoインスタンスをsec1.PageInfoのMarginプロパティに割り当てます
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// ヘッダーとして表示する内容を保存するテキスト段落をインスタンス化します
TextFragment t1 = new TextFragment("レポートタイトル");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("レポート名");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// セクション用のHeaderFooterオブジェクトを作成します
HeaderFooter hfFoot = new HeaderFooter();
// 奇数および偶数のフッターにHeaderFooterオブジェクトを設定します
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// 現在のページ番号およびページの総数を含むテキスト段落を追加します
TextFragment t3 = new TextFragment("テスト日に生成");
TextFragment t4 = new TextFragment("レポート名");
TextFragment t5 = new TextFragment("ページ $p / $P");

// テーブルオブジェクトをインスタンス化します
Table tab2 = new Table();

// 希望のセクションの段落コレクションにテーブルを追加します
hfFoot.Paragraphs.Add(tab2);

// テーブルの列幅を設定します
tab2.ColumnWidths = "165 172 165";

// テーブルに行を作成し、その行にセルを作成します
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// テキストの垂直整列を中央揃えに設定します
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// 希望のセクションの段落コレクションにテーブルを追加します
page.Paragraphs.Add(table);

// BorderInfoオブジェクトを使用してデフォルトのセルボーダーを設定します
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブルボーダーを設定します
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// テーブルに行を作成し、その行にセルを作成します
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントのコンパイルです。これは、" + CRLF + "最新バージョンの各Javaコンポーネントを含むように毎日コンパイルされています。" + CRLF + "最新バージョンの各Javaコンポーネントを含むように毎日コンパイルされています。" + CRLF + "開発者は、Aspose.Total for Javaを使用して、幅広いアプリケーションを作成できます。");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## PDFファイルから未使用のフォントを削除する

Aspose.PDF for .NETは、PDFドキュメントの作成時にフォントを埋め込む機能をサポートするとともに、既存のPDFファイルにフォントを埋め込む機能も提供します。Aspose.PDF for .NET 7.3.0から、PDFドキュメントから重複または未使用のフォントを削除することも可能です。

フォントを置換するには、次のアプローチを使用します：

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) クラスを呼び出します。
1. TextFragmentAbsorberクラスのTextEditOptions.FontReplace.RemoveUnusedFontsパラメータを呼び出します（これにより、フォント置換中に未使用となったフォントが削除されます）。
1. 各テキストフラグメントに個別にフォントを設定します。

以下のコードスニペットは、すべてのドキュメントページのすべてのテキストフラグメントのフォントを置換し、未使用のフォントを削除します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルをロード
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// すべてのTextFragmentsを反復処理します
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
```
## PDFドキュメントからすべてのテキストを削除する

### 演算子を使用してすべてのテキストを削除する

テキスト操作でPDFドキュメントからすべてのテキストを削除する必要がある場合、通常、見つかったテキストを空の文字列値に設定する必要があります。テキストを複数のテキストフラグメントで変更することは、チェックとテキスト位置の調整操作を数多く引き起こします。これらはテキスト編集シナリオで不可欠です。問題は、ループで処理されるシナリオでは、削除されるテキストフラグメントの数を決定できないことです。

したがって、PDFページからすべてのテキストを削除するシナリオには別のアプローチを使用することをお勧めします。非常に高速に動作する次のコードスニペットを検討してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// PDFドキュメントのすべてのページをループする
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // ページ上のすべてのテキストを選択する
    page.Contents.Accept(operatorSelector);
    // すべてのテキストを削除する
    page.Contents.Delete(operatorSelector.Selected);
}
// ドキュメントを保存する
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NETライブラリ",
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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

