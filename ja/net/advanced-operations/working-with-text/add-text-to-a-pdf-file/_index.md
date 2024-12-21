---
title: PDFにテキストを追加する方法 C#
linktitle: PDFにテキストを追加
type: docs
weight: 10
url: /ja/net/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでテキストを扱うさまざまな側面について説明します。PDFにテキストを追加したり、HTMLフラグメントを追加したり、カスタムOTFフォントを使用する方法を学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFにテキストを追加する方法 C#",
    "alternativeHeadline": "PDFにテキストを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdfにテキストを追加",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDFでテキストを扱うさまざまな側面について説明します。PDFにテキストを追加したり、HTMLフラグメントを追加したり、カスタムOTFフォントを使用する方法を学びます。"
}
</script>
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリで動作します。

既存のPDFファイルにテキストを追加するには：

1. Documentオブジェクトを使用して入力PDFを開きます。
2. テキストを追加したい特定のページを取得します。
3. 入力テキストとその他のテキストプロパティを含むTextFragmentオブジェクトを作成します。その特定のページから作成されたTextBuilderオブジェクトを使用して、AppendTextメソッドを使用してページにTextFragmentオブジェクトを追加できます。
4. DocumentオブジェクトのSaveメソッドを呼び出し、出力PDFファイルを保存します。

## テキストの追加

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 文書を開く
Document pdfDocument = new Document(dataDir + "input.pdf");

// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages[1];

// テキストフラグメントを作成
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// テキストプロパティを設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);

// PDFページにテキストフラグメントを追加
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```
## ストリームからフォントを読み込む

次のコードスニペットは、PDFドキュメントにテキストを追加する際にストリームオブジェクトからフォントを読み込む方法を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// 入力PDFファイルを読み込む
Document doc = new Document(dataDir + "input.pdf");
// ドキュメントの最初のページ用のテキストビルダーオブジェクトを作成する
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// サンプル文字列を持つテキストフラグメントを作成する
TextFragment textFragment = new TextFragment("こんにちは世界");

if (fontFile != "")
{
    // TrueTypeフォントをストリームオブジェクトに読み込む
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // テキスト文字列のフォント名を設定する
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // テキストフラグメントの位置を指定する
        textFragment.Position = new Position(10, 10);
        // PDFファイル上に配置するためにテキストをTextBuilderに追加する
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // 結果のPDFドキュメントを保存する。
    doc.Save(dataDir);
}
```
## TextParagraphを使用してテキストを追加する

以下のコードスニペットでは、[TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph) クラスを使用してPDFドキュメントにテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントを開く
Document doc = new Document();
// ドキュメントオブジェクトのページコレクションにページを追加
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// テキストパラグラフを作成
TextParagraph paragraph = new TextParagraph();
// 後続の行のインデントを設定
paragraph.SubsequentLinesIndent = 20;
// TextParagraphを追加する位置を指定
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// 単語によるワードラップモードを指定
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// テキストフラグメントを作成
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// フラグメントをパラグラフに追加
paragraph.AppendLine(fragment1);
// パラグラフを追加
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// 結果のPDFドキュメントを保存。
doc.Save(dataDir);
```
## TextSegmentにハイパーリンクを追加

PDFページは1つ以上のTextFragmentオブジェクトで構成されており、各TextFragmentオブジェクトは1つ以上のTextSegmentインスタンスを持つことができます。TextSegmentのハイパーリンクを設定するためには、[TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) クラスのHyperlinkプロパティを使用し、Aspose.Pdf.WebHyperlinkインスタンスのオブジェクトを提供します。以下のコードスニペットを使用してこの要件を実現してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントインスタンスを作成
Document doc = new Document();
// PDFファイルのページコレクションにページを追加
Page page1 = doc.Pages.Add();
// TextFragmentインスタンスを作成
TextFragment tf = new TextFragment("サンプルテキストフラグメント");
// TextFragmentの水平方向の配置を設定
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// サンプルテキストでテキストセグメントを作成
TextSegment segment = new TextSegment(" ... テキストセグメント1...");
// セグメントをTextFragmentのセグメントコレクションに追加
tf.Segments.Add(segment);
// 新しいTextSegmentを作成
segment = new TextSegment("Googleへのリンク");
// セグメントをTextFragmentのセグメントコレクションに追加
tf.Segments.Add(segment);
// TextSegmentのハイパーリンクを設定
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// テキストセグメントの前景色を設定
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// テキストの書式をイタリックに設定
segment.TextState.FontStyle = FontStyles.Italic;
// 別のTextSegmentオブジェクトを作成
segment = new TextSegment("ハイパーリンクのないテキストセグメント");
// セグメントをTextFragmentのセグメントコレクションに追加
tf.Segments.Add(segment);
// TextFragmentをページオブジェクトの段落コレクションに追加
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// 結果のPDFドキュメントを保存。
doc.Save(dataDir);
```
## OTFフォントを使用する

Aspose.PDF for .NETは、PDFファイルの内容を作成・操作する際にカスタム/TrueTypeフォントを使用する機能を提供しています。これにより、ファイルの内容がデフォルトのシステムフォント以外の内容で表示されます。Aspose.PDF for .NET 10.3.0のリリースから、Open Type Fontsのサポートを提供しました。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET へアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 新しいドキュメントインスタンスを作成
Document pdfDocument = new Document();
// PDFファイルのページコレクションにページを追加
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// サンプルテキストを持つTextFragmentインスタンスを作成
TextFragment fragment = new TextFragment("OTFフォントのサンプルテキスト");
// システムフォントディレクトリ内でフォントを検索
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// または、システムディレクトリ内のOTFフォントのパスを指定することもできます
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// PDFファイル内にフォントを埋め込むように指定し、特定のフォントが対象マシンにインストールされていない/存在しない場合でも、適切に表示されるようにします
fragment.TextState.Font.IsEmbedded = true;
// TextFragmentをPageインスタンスのパラグラフコレクションに追加
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```
## DOMを使用してHTML文字列を追加

Aspose.Pdf.Generator.Text クラスには IsHtmlTagSupported というプロパティが含まれており、HTMLタグ/コンテンツをPDFファイルに追加することができます。追加されたコンテンツは単純なテキスト文字列として表示されるのではなく、ネイティブのHTMLタグでレンダリングされます。Aspose.Pdf 名前空間の新しいドキュメントオブジェクトモデル（DOM）で同様の機能をサポートするために、HtmlFragment クラスが導入されました。

[HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) インスタンスは、PDFファイルの内部に配置する必要があるHTMLコンテンツを指定するために使用できます。TextFragmentと同様に、HtmlFragmentは段落レベルのオブジェクトであり、Pageオブジェクトの段落コレクションに追加することができます。次のコードスニペットは、DOMアプローチを使用してPDFファイル内にHTMLコンテンツを配置する手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentオブジェクトをインスタンス化
Document doc = new Document();
// PDFファイルのページコレクションにページを追加
Page page = doc.Pages.Add();
// HTMLコンテンツでHtmlFragmentをインスタンス化
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// 下マージン情報を設定
title.Margin.Bottom = 10;
// 上マージン情報を設定
title.Margin.Top = 200;
// ページの段落コレクションにHTMLフラグメントを追加
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// PDFファイルを保存
doc.Save(dataDir);
```
以下のコードスニペットは、ドキュメントにHTML順序付きリストを追加する手順を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 出力ドキュメントへのパス。
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Document オブジェクトをインスタンス化
Document doc = new Document();
// 対応するHTMLフラグメントを持つ HtmlFragment オブジェクトをインスタンス化
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
// ページをページコレクションに追加
Page page = doc.Pages.Add();
// ページ内に HtmlFragment を追加
page.Paragraphs.Add(t);
// 結果のPDFファイルを保存
doc.Save(outFile);
```

また、次のように TextState オブジェクトを使用してHTML文字列のフォーマットを設定することもできます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
HtmlFragment html = new HtmlFragment("some text");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
HTMLマークアップを介して一部のテキスト属性の値を設定し、次に同じ値をTextStateプロパティで提供する場合、HTMLパラメータはTextStateインスタンスのプロパティで上書きされます。次のコードスニペットは、説明された動作を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 文書ディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Documentオブジェクトをインスタンス化
Document doc = new Document();
// PDFファイルのページコレクションにページを追加
Page page = doc.Pages.Add();
// HTMLコンテンツを持つHtmlFragmentをインスタンス化
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>テキストが含まれるテーブル</i></b></p>");
// 'Verdana'からのフォントファミリーは'Arial'にリセットされます
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// 下マージン情報を設定
title.Margin.Bottom = 10;
// 上マージン情報を設定
title.Margin.Top = 400;
// HTMLフラグメントをページの段落コレクションに追加
page.Paragraphs.Add(title);
// PDFファイルを保存
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// PDFファイルを保存
doc.Save(dataDir);
```
## 脚注と文末脚注（DOM）

脚注は、連続する上付き数字を使用して論文のテキスト内のメモを示します。実際のメモはインデントされ、ページの下部に脚注として発生します。

### 脚注の追加

脚注参照システムでは、次のように参照を示します：

- 出典資料の直後の行の上に小さな数字を入れます。この数字は注釈識別子と呼ばれ、テキスト行のわずかに上に位置します。
- 同じ番号を付けて、ページの下部に出典を引用します。脚注は数値的であり、時系列的でなければなりません：最初の参照は1、次は2、というように続きます。

脚注の利点は、読者が興味を持った参照の出典を知るためにページを見下ろすだけで済むことです。

脚注を作成するには、以下の手順に従ってください：

- Documentインスタンスを作成する
- Pageオブジェクトを作成する
- TextFragmentオブジェクトを作成する
- Noteインスタンスを作成し、その値をTextFragment.FootNoteプロパティに渡す
- ノートインスタンスを作成し、その値をTextFragment.FootNoteプロパティに渡します
- TextFragmentをページインスタンスの段落コレクションに追加します

### FootNoteのカスタムラインスタイル

以下の例は、Pdfページの底に脚注を追加し、カスタムラインスタイルを定義する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentインスタンスを作成
Document doc = new Document();
// PDFのページコレクションにページを追加
Page page = doc.Pages.Add();
// GraphInfoオブジェクトを作成
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// 線の幅を2に設定
graph.LineWidth = 2;
// グラフオブジェクトの色を設定
graph.Color = Aspose.Pdf.Color.Red;
// ダッシュ配列値を3に設定
graph.DashArray = new int[] { 3 };
// ダッシュフェーズ値を1に設定
graph.DashPhase = 1;
// ページの脚注ラインスタイルをグラフとして設定
page.NoteLineStyle = graph;
// TextFragmentインスタンスを作成
TextFragment text = new TextFragment("Hello World");
// TextFragmentのFootNote値を設定
text.FootNote = new Note("foot note for test text 1");
// ドキュメントの最初のページの段落コレクションにTextFragmentを追加
page.Paragraphs.Add(text);
// 2番目のTextFragmentを作成
text = new TextFragment("Aspose.Pdf for .NET");
// 2番目のテキストフラグメントのFootNoteを設定
text.FootNote = new Note("foot note for test text 2");
// PDFファイルの段落コレクションに2番目のテキストフラグメントを追加
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// 結果のPDFドキュメントを保存。
doc.Save(dataDir);
```
フットノートラベル（注釈識別子）の書式設定は、次のようにTextStateオブジェクトを使用して設定できます：

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### フットノートラベルのカスタマイズ

デフォルトでは、FootNote番号は1から始まるインクリメントとなっています。しかし、カスタムFootNoteラベルを設定する必要がある場合もあります。この要件を達成するためには、以下のコードスニペットを試してみてください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Documentインスタンスを作成
Document doc = new Document();
// PDFのページコレクションにページを追加
Page page = doc.Pages.Add();
// GraphInfoオブジェクトを作成
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// 線の幅を2に設定
graph.LineWidth = 2;
// グラフオブジェクトの色を設定
graph.Color = Aspose.Pdf.Color.Red;
// ダッシュ配列の値を3として設定
graph.DashArray = new int[] { 3 };
// ダッシュフェーズの値を1として設定
graph.DashPhase = 1;
// ページのフットノートラインスタイルをグラフとして設定
page.NoteLineStyle = graph;
// TextFragmentインスタンスを作成
TextFragment text = new TextFragment("Hello World");
// TextFragmentにFootNote値を設定
text.FootNote = new Note("foot note for test text 1");
// FootNoteにカスタムラベルを指定
text.FootNote.Text = " Aspose(2015)";
// ドキュメントの最初のページのパラグラフコレクションにTextFragmentを追加
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## フットノートに画像と表を追加する

以前のリリースバージョンでは、フットノートのサポートが提供されていましたが、TextFragmentオブジェクトにのみ適用されていました。しかし、Aspose.PDF for .NET 10.7.0のリリースからは、PDFドキュメント内の他のオブジェクト（例えば、テーブル、セルなど）にもフットノートを追加することができます。以下のコードスニペットは、TextFragmentオブジェクトにフットノートを追加し、次に画像と表オブジェクトをフットノートセクションの段落コレクションに追加する手順を示しています。

```csharp

// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("some text");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("footnote text");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Row 1 Cell 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// 結果のPDFドキュメントを保存します。
doc.Save(dataDir);
```
## エンドノートの作成方法

エンドノートは、読者が論文の最後にある特定の場所を参照して、論文中に引用または言及された情報や言葉の出典を確認できるようにするための出典引用です。エンドノートを使用する場合、引用またはパラフレーズされた文や要約された内容の後に上付きの数字が続きます。

以下の例は、PDFページにエンドノートを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Documentインスタンスを作成
Document doc = new Document();
// PDFのページコレクションにページを追加
Page page = doc.Pages.Add();
// TextFragmentインスタンスを作成
TextFragment text = new TextFragment("Hello World");
// TextFragmentに対してFootNote値を設定
text.EndNote = new Note("sample End note");
// FootNoteにカスタムラベルを指定
text.EndNote.Text = " Aspose(2015)";
// ドキュメントの最初のページの段落コレクションにTextFragmentを追加
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// 結果のPDFドキュメントを保存。
doc.Save(dataDir);
```
## テキストと画像をインライン段落として

PDFファイルのデフォルトのレイアウトはフローレイアウト（左上から右下へ）です。したがって、PDFファイルに新しい要素を追加すると、右下のフローに追加されます。しかし、画像とテキストを同じレベルで（一つの後に一つ）表示する必要があるかもしれません。一つのアプローチは、Tableインスタンスを作成し、個々のセルオブジェクトに両方の要素を追加することです。しかし、もう一つのアプローチはインライン段落です。画像とテキストのIsInLineParagraphプロパティをtrueに設定すると、これらの段落は他のページ要素とインラインで表示されます。

以下のコードスニペットは、PDFファイルにテキストと画像をインライン段落として追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Documentインスタンスをインスタンス化します
Document doc = new Document();
// Documentインスタンスのページコレクションにページを追加します
Page page = doc.Pages.Add();
// TextFragmnetを作成します
TextFragment text = new TextFragment("Hello World.. ");
// Pageオブジェクトの段落コレクションにテキストフラグメントを追加します
page.Paragraphs.Add(text);
// 画像インスタンスを作成します
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// 画像をインライン段落として設定し、直前の段落オブジェクト（TextFragment）の直後に表示されるようにします
image.IsInLineParagraph = true;
// 画像ファイルのパスを指定します
image.File = dataDir + "aspose-logo.jpg";
// 画像の高さを設定します（オプション）
image.FixHeight = 30;
// 画像の幅を設定します（オプション）
image.FixWidth = 100;
// 画像をページオブジェクトの段落コレクションに追加します
page.Paragraphs.Add(image);
// 異なる内容でTextFragmentオブジェクトを再初期化します
text = new TextFragment(" Hello Again..");
// TextFragmentをインライン段落として設定します
text.IsInLineParagraph = true;
// 新しく作成されたTextFragmentをページの段落コレクションに追加します
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## テキスト追加時の文字間隔の指定

PDFファイルの段落コレクション内にテキストを追加するには、TextFragmentインスタンスを使用するか、TextParagraphオブジェクトを使用します。また、TextStampクラスを使用してPDF内にテキストをスタンプすることもできます。テキストを追加する際には、テキストオブジェクトの文字間隔を指定する必要がある場合があります。この要件を満たすために、CharacterSpacingプロパティという新しいプロパティが導入されました。以下のアプローチを参考にしてください。

以下のアプローチは、PDFドキュメント内にテキストを追加する際に文字間隔を指定する手順を示しています。

### TextBuilderとTextFragmentを使用する

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentインスタンスを作成
Document pdfDocument = new Document();
// ドキュメントのページコレクションにページを追加
Page page = pdfDocument.Pages.Add();
// TextBuilderインスタンスを作成
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// サンプル内容を持つテキストフラグメントインスタンスを作成
TextFragment wideFragment = new TextFragment("文字間隔を広げたテキスト");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// TextFragmentの文字間隔を指定
wideFragment.TextState.CharacterSpacing = 2.0f;
// TextFragmentの位置を指定
wideFragment.Position = new Position(100, 650);
// TextBuilderインスタンスにTextFragmentを追加
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```
### TextParagraphの使用

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentインスタンスを作成します
Document pdfDocument = new Document();
// Documentのページコレクションにページを追加します
Page page = pdfDocument.Pages.Add();
// TextBuilderインスタンスを作成します
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// TextParagraphインスタンスをインスタンス化します
TextParagraph paragraph = new TextParagraph();
// フォント名とサイズを指定するためのTextStateインスタンスを作成します
TextState state = new TextState("Arial", 12);
// 文字間隔を指定します
state.CharacterSpacing = 1.5f;
// TextParagraphオブジェクトにテキストを追加します
paragraph.AppendLine("これは文字間隔のある段落です", state);
// TextParagraphの位置を指定します
paragraph.Position = new Position(100, 550);
// TextParagraphをTextBuilderインスタンスに追加します
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// 結果のPDFドキュメントを保存します。
pdfDocument.Save(dataDir);
```
### TextStampの使用

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentインスタンスを作成します
Document pdfDocument = new Document();
// ドキュメントのページコレクションにページを追加します
Page page = pdfDocument.Pages.Add();
// サンプルテキストでTextStampインスタンスをインスタンス化します
TextStamp stamp = new TextStamp("これは文字間隔のあるテキストスタンプです");
// Stampオブジェクトのフォント名を指定します
stamp.TextState.Font = FontRepository.FindFont("Arial");
// TextStampのフォントサイズを指定します
stamp.TextState.FontSize = 12;
// 文字間隔を1fとして指定します
stamp.TextState.CharacterSpacing = 1f;
// StampのXIndentを設定します
stamp.XIndent = 100;
// StampのYIndentを設定します
stamp.YIndent = 500;
// ページインスタンスにテキストスタンプを追加します
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// 結果のPDFドキュメントを保存します。
pdfDocument.Save(dataDir);
```
## マルチカラムPDFドキュメントを作成する

雑誌や新聞では、本と異なり、ニュースが1ページに複数のカラムで表示されることが多く、テキストの段落は左から右に全ページに印刷されることが一般的です。Microsoft WordやAdobe Acrobat Writerなどのドキュメント処理アプリケーションは、単一のページに複数のカラムを作成し、そこにデータを追加する機能を提供しています。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) は、PDFドキュメントのページ内に複数のカラムを作成する機能も提供しています。
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) は、PDFドキュメントのページ内に複数の列を作成する機能も提供しています。

列間隔とは、列と列の間の空間を意味し、列間のデフォルトの間隔は1.25cmです。列の幅が指定されていない場合、[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) は、ページサイズと列間の間隔に応じて各列の幅を自動的に計算します。

以下に、グラフオブジェクト（ライン）を2列に作成し、それをFloatingBoxの段落コレクションに追加し、その後、ページインスタンスの段落コレクションに追加する例を示します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// PDFファイルの左マージン情報を指定
doc.PageInfo.Margin.Left = 40;
// PDFファイルの右マージン情報を指定
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// 線をセクションオブジェクトの段落コレクションに追加
page.Paragraphs.Add(graph1);

// 線の座標を指定
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// HTMLタグを含むテキストの文字列変数を作成

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> How to Steer Clear of money scams</<strong> "
+ "</font>";
// HTMLテキストを含むテキスト段落を作成

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// セクションに4列を追加
box.ColumnInfo.ColumnCount = 2;
// 列間の間隔を設定
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// 線を描くためのグラフオブジェクトを作成
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// 線の座標を指定
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// 線をセクションオブジェクトの段落コレクションに追加
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// PDFファイルを保存
doc.Save(dataDir);
```
## カスタムタブストップの使用

タブストップは、タブキーを押すたびにカーソルや挿入ポイントがジャンプする停止点です。ワードプロセッサーでは、各行には定期的な間隔（例えば、半インチごと）でタブストップが配置されています。しかし、ほとんどのワードプロセッサーでは、任意の場所にタブストップを設定することができます。タブストップ自体は不可視ですが、テキストファイルには存在しませんが、ワードプロセッサーはタブキーに正しく反応できるようにこれらを追跡します。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) は、PDFドキュメントでカスタムタブストップを使用できるように開発者をサポートしています。Aspose.Pdf.Text.TabStopクラスは、[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)クラスでカスタムTABストップを設定するために使用されます。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) はまた、TabLeaderTypeという列挙型で事前に定義されたタブリーダータイプをいくつか提供しており、その事前に定義された値とその説明は以下の通りです：
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) では、TabLeaderType という列挙型でいくつかの事前定義されたタブリーダータイプも提供しています。事前定義された値とその説明は以下の通りです：

|**タブリーダータイプ**|**説明**|
| :- | :- |
|None|タブリーダーなし|
|Solid|実線のタブリーダー|
|Dash|破線のタブリーダー|
|Dot|点線のタブリーダー|

ここにカスタムTABストップを設定する例を示します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("これはTABストップで表を形成する例です", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## PDFに透明テキストを追加する方法

PDFファイルにはイメージ、テキスト、グラフ、添付ファイル、注釈オブジェクトが含まれており、TextFragmentを作成する際には、前景色、背景色情報およびテキストの書式設定を設定できます。Aspose.PDF for .NETは、アルファカラーチャネルを使用したテキストの追加機能をサポートしています。次のコードスニペットは、透明な色でテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Documentインスタンスを作成
Document doc = new Document();
// PDFファイルのページコレクションにページを作成
Aspose.Pdf.Page page = doc.Pages.Add();

// Graphオブジェクトを作成
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// 特定の寸法で矩形インスタンスを作成
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// アルファカラーチャネルから色オブジェクトを作成
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Graphオブジェクトのシェイプコレクションに矩形を追加
canvas.Shapes.Add(rect);
// ページオブジェクトの段落コレクションにグラフオブジェクトを追加
page.Paragraphs.Add(canvas);
// グラフオブジェクトの位置を変更しないように設定
canvas.IsChangePosition = false;

// サンプル値を持つTextFragmentインスタンスを作成
TextFragment text = new TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
// アルファチャネルから色オブジェクトを作成
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// テキストインスタンスに色情報を設定
text.TextState.ForegroundColor = color;
// ページインスタンスの段落コレクションにテキストを追加
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## フォントの行間を指定する

すべてのフォントには抽象的な正方形があり、その高さは同じタイプサイズのタイプ行間の意図された距離です。
すべてのフォントには抽象的な正方形があり、その高さは同じサイズのタイプの行間の距離として意図されています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// 入力PDFファイルをロード
Document doc = new Document();
// LineSpacingMode.FullSizeを使用してTextFormattingOptionsを作成
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// ドキュメントの最初のページに対してテキストビルダーオブジェクトを作成
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// サンプル文字列を持つテキストフラグメントを作成
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // TrueTypeフォントをストリームオブジェクトにロード
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // テキスト文字列のフォント名を設定
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Text Fragmentの位置を指定
        textFragment.Position = new Position(100, 600);
        // 現在のフラグメントのTextFormattingOptionsを事前定義されたものに設定（LineSpacingMode.FullSizeを指す）
        textFragment.TextState.FormattingOptions = formattingOptions;
        // PDFファイル上に配置できるようにテキストをTextBuilderに追加
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // 結果のPDFドキュメントを保存
    doc.Save(dataDir);
}
```
## 動的にテキスト幅を取得する

時々、テキストの幅を動的に取得する必要があります。Aspose.PDF for .NETは文字列の幅を測定するための2つの方法を含んでいます。Aspose.Pdf.Text.FontまたはAspose.Pdf.Text.TextStateクラス（またはその両方）の[MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring)メソッドを呼び出すことができます。以下のコードスニペットは、この機能を使用する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("予期しないフォント文字列の測定です！");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("予期しないフォント文字列の測定です！");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("フォントと状態の文字列測定が一致しません！");
}
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

