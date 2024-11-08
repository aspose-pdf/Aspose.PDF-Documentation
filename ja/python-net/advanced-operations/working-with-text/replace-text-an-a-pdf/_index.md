---
title: PythonでPDF内のテキストを置換
linktitle: PDFのテキストを置換
type: docs
weight: 40
url: /ja/python-net/replace-text-in-pdf/
description: Aspose.PDF for Python via .NETライブラリを使用して、テキストを置換および削除するさまざまな方法について学びます。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFのテキストを置換",
    "alternativeHeadline": "PDFファイル内のテキストを置換および削除",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, テキスト置換, テキスト削除",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Aspose.PDF for Python via .NETライブラリを使用して、テキストを置換および削除するさまざまな方法について学びます。"
}
</script>


## PDFドキュメントのすべてのページでテキストを置換する

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索して置換し、この[リンク](https://products.aspose.app/pdf/redaction)でオンラインで結果を確認することができます。

{{% /alert %}}

PDFドキュメントのすべてのページでテキストを置換するには、まず[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)を使用して置換したい特定のフレーズを見つける必要があります。その後、すべてのTextFragmentを通過してテキストを置換し、その他の属性を変更します。それが完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントのすべてのページでテキストを置換する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 入力検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成
    absorber = ap.text.TextFragmentAbsorber("format")

    # すべてのページに対してアブソーバーを受け入れる
    document.pages.accept(absorber)

    # 抽出されたテキストフラグメントを取得
    collection = absorber.text_fragments

    # フラグメントをループする
    for text_fragment in collection:
        # テキストとその他のプロパティを更新
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # ドキュメントを保存
    document.save(output_pdf)
```


## 特定のページ領域でテキストを置き換える

特定のページ領域でテキストを置き換えるためには、まずTextFragmentAbsorberオブジェクトをインスタンス化し、TextSearchOptions.Rectangleプロパティを使用してページ領域を指定し、すべてのTextFragmentを繰り返し処理してテキストを置き換える必要があります。これらの操作が完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。以下のコードスニペットは、PDFドキュメントのすべてのページでテキストを置き換える方法を示しています。

```python
// PDFファイルをロードする
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// TextFragment Absorberオブジェクトをインスタンス化する
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// ページの境界内でテキストを検索する
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// TextSearch Optionsのページ領域を指定する
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// PDFファイルの最初のページからテキストを検索する
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// 個々のTextFragmentを繰り返し処理する
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // テキストを空白文字に更新する
    tf.Text = "";
}

// テキスト置換後に更新されたPDFファイルを保存する
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## 正規表現に基づいてテキストを置換する

正規表現に基づいていくつかのフレーズを置換したい場合は、まずその特定の正規表現に一致するすべてのフレーズをTextFragmentAbsorberを使用して見つける必要があります。正規表現をTextFragmentAbsorberコンストラクタのパラメータとして渡す必要があります。また、正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成する必要があります。TextFragmentsで一致するフレーズを取得したら、それらすべてをループして必要に応じて更新します。最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存する必要があります。次のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// 正規表現に一致するすべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例: 1999-2000

// 正規表現の使用を指定するためにテキスト検索オプションを設定
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 単一ページ用にアブソーバーを受け入れる
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループする
foreach (TextFragment textFragment in textFragmentCollection)
{
    // テキストおよびその他のプロパティを更新
    textFragment.Text = "New Phrase";
    // オブジェクトのインスタンスに設定
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## 既存のPDFファイルのフォントを置き換える

Aspose.PDF for Python via .NETは、PDFドキュメント内のテキストを置き換える機能をサポートしています。しかし、場合によってはPDFドキュメント内で使用されているフォントのみを置き換える必要があります。この場合、テキストを置き換えるのではなく、使用されているフォントのみを置き換えます。TextFragmentAbsorberコンストラクタのオーバーロードの1つは、TextEditOptionsオブジェクトを引数として受け取り、TextEditOptions.FontReplace列挙からRemoveUnusedFonts値を使用して、要件を達成できます。次のコードスニペットは、PDFドキュメント内のフォントを置き換える方法を示しています。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NETをご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルを読み込む
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// テキストフラグメントを検索し、未使用フォントを削除する編集オプションを設定する
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// 全ページに対して吸収器を適用する
pdfDocument.Pages.Accept(absorber);
// すべてのTextFragmentsを通過する
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


## テキスト置換はページ内容を自動的に再配置する必要があります

Aspose.PDF for Python via .NETは、PDFファイル内のテキストを検索して置換する機能をサポートしています。しかし最近、特定のTextFragmentがより小さな内容に置換されたときに、結果のPDFに余分なスペースが表示される、またはTextFragmentがより長い文字列に置換された場合、既存のページ内容と重なるという問題が発生しました。そのため、PDFドキュメント内のテキストが置換されたときに、内容が再配置されるメカニズムを導入する必要がありました。

上記のシナリオに対応するために、Aspose.PDF for Python via .NETは強化され、PDFファイル内のテキストを置換する際にそのような問題が発生しないようになりました。以下のコードスニペットは、PDFファイル内のテキストを置換し、ページ内容が自動的に再配置される方法を示しています。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルをロード
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// 正規表現を使用してTextFragment Absorberオブジェクトを作成
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
    // プレースホルダーより大きな文字列でテキストを置換
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// 結果のPDFを保存
doc.Save(dataDir);
```


## PDF作成中の置換可能なシンボルのレンダリング

置換可能なシンボルは、実行時に対応するコンテンツに置換できるテキスト文字列内の特別なシンボルです。現在、Aspose.PDF名前空間の新しいドキュメントオブジェクトモデルでサポートされている置換可能なシンボルは、`$P`、`$p`、`\n`、`\r`です。`$p`と`$P`は、実行時のページ番号を扱うために使用されます。`$p`は現在のParagraphクラスがあるページの番号に置換されます。`$P`はドキュメント内のページの総数に置換されます。PDFドキュメントの段落コレクションに`TextFragment`を追加する際、テキスト内の改行はサポートされません。しかし、改行を含むテキストを追加するためには、`TextFragment`を`TextParagraph`と共に使用してください：

- 単一の"\n"の代わりに、TextFragmentで"\r\n"またはEnvironment.NewLineを使用します;
- TextParagraphオブジェクトを作成します。これにより、テキストは分割されて追加されます;
- TextParagraph.AppendLineでTextFragmentを追加します;
- TextBuilder.AppendParagraphでTextParagraphを追加します。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 必要な改行マーカーを含むテキストで新しいTextFragmentを初期化
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 必要に応じてテキストフラグメントプロパティを設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraphオブジェクトを作成
TextParagraph par = new TextParagraph();

// 新しいTextFragmentを段落に追加
par.AppendLine(textFragment);

// 段落の位置を設定
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilderを使用してTextParagraphを追加
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## ヘッダー/フッター領域の置換可能なシンボル

置換可能なシンボルは、PDFファイルのヘッダー/フッターセクション内にも配置できます。フッターセクションに置換可能なシンボルを追加する方法については、次のコードスニペットを参照してください。

```python
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
// marginInfo インスタンスを sec1.PageInfo の Margin プロパティに割り当てる
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// ヘッダーとして表示するコンテンツを格納するテキスト段落をインスタンス化
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

// セクション用の HeaderFooter オブジェクトを作成
HeaderFooter hfFoot = new HeaderFooter();
// 奇数と偶数のフッターに HeaderFooter オブジェクトを設定
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// 現在のページ番号と総ページ数を含むテキスト段落を追加
TextFragment t3 = new TextFragment("テスト日付に生成");
TextFragment t4 = new TextFragment("レポート名 ");
TextFragment t5 = new TextFragment("ページ $p / $P");

// テーブルオブジェクトをインスタンス化
Table tab2 = new Table();

// 希望のセクションの段落コレクションにテーブルを追加
hfFoot.Paragraphs.Add(tab2);

// テーブルの列幅を設定
tab2.ColumnWidths = "165 172 165";

// テーブルに行を作成し、行にセルを作成
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// テキストの垂直方向の配置を中央に設定
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントをコンパイルしたものです。#$NL" + "最新バージョンが含まれるように、毎日コンパイルされます。 #$NL " + "Aspose.Total for Javaを使用して、開発者は多種多様なアプリケーションを作成できます。 #$NL #$NL #$NP" + "Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントをコンパイルしたものです。#$NL" + "最新バージョンが含まれるように、毎日コンパイルされます。 #$NL " + "Aspose.Total for Javaを使用して、開発者は多種多様なアプリケーションを作成できます。 #$NL #$NL #$NP" + "Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントをコンパイルしたものです。#$NL" + "最新バージョンが含まれるように、毎日コンパイルされます。 #$NL " + "Aspose.Total for Javaを使用して、開発者は多種多様なアプリケーションを作成できます。 #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// 希望のセクションの段落コレクションにテーブルを追加
page.Paragraphs.Add(table);

// BorderInfo オブジェクトを使用してデフォルトのセルボーダーを設定
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// 別のカスタマイズされた BorderInfo オブジェクトを使用してテーブルボーダーを設定
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// テーブルに行を作成し、行にセルを作成
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
            c1 = row.Cells.Add("Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントをコンパイルしたものです。" + CRLF + "最新バージョンが含まれるように、毎日コンパイルされます。 " + CRLF + "最新バージョンが含まれるように、毎日コンパイルされます。 " + CRLF + "Aspose.Total for Javaを使用して、開発者は多種多様なアプリケーションを作成できます。");
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


## PDFファイルから未使用フォントを削除する

Aspose.PDF for Python via .NETは、PDFドキュメントを作成する際にフォントを埋め込む機能をサポートしており、既存のPDFファイルにフォントを埋め込む能力も備えています。Aspose.PDF for Python via .NET 7.3.0からは、PDFドキュメントから重複または未使用のフォントを削除することもできます。

フォントを置き換えるには、次のアプローチを使用します：

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) クラスを呼び出します。
1. TextFragmentAbsorberクラスのTextEditOptions.FontReplace.RemoveUnusedFontsパラメータを呼び出します。（これにより、フォント置換中に使用されなくなったフォントが削除されます）。
1. 各テキストフラグメントに対して個別にフォントを設定します。

次のコードスニペットは、すべてのドキュメントページのすべてのテキストフラグメントのフォントを置き換え、未使用のフォントを削除します。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ソースPDFファイルを読み込む
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// すべてのTextFragmentを繰り返す
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// 更新されたドキュメントを保存する
doc.Save(dataDir);
```


## PDFドキュメントからすべてのテキストを削除する

### 演算子を使用してすべてのテキストを削除する

あるテキスト操作では、PDFドキュメントからすべてのテキストを削除する必要があり、そのためには通常、見つかったテキストを空の文字列値に設定する必要があります。ポイントは、多数のテキストフラグメントを変更することが、多くのチェックとテキスト位置調整操作を呼び起こすことです。これらはテキスト編集のシナリオにおいて重要です。難しいのは、ループで処理されるシナリオでどれだけのテキストフラグメントが削除されるかを判断できないことです。

したがって、PDFページからすべてのテキストを削除するシナリオでは、別のアプローチを使用することをお勧めします。非常に高速で動作する以下のコードスニペットを考慮してください。

```python
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// PDFドキュメントのすべてのページをループする
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // ページ上のすべてのテキストを選択
    page.Contents.Accept(operatorSelector);
    // すべてのテキストを削除
    page.Contents.Delete(operatorSelector.Selected);
}
// ドキュメントを保存
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Python用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>