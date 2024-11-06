---
title: PDF内のテキストフォーマットについて
linktitle: PDF内のテキストフォーマット
type: docs
weight: 30
url: ja/net/text-formatting-inside-pdf/
description: このページでは、PDFファイル内のテキストをフォーマットする方法について説明します。行インデントの追加、テキストボーダーの追加、下線テキストの追加などがあります。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストフォーマットについて",
    "alternativeHeadline": "PDFファイルでのテキストフォーマットの方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf内のテキストフォーマット",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "このページでは、PDFファイル内のテキストをフォーマットする方法について説明します。行インデントの追加、テキストボーダーの追加、下線テキストの追加などがあります。"
}
</script>
以下のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDFに行インデントを追加する方法

Aspose.PDF for .NETは[TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions)クラスにSubsequentLinesIndentプロパティを提供しています。これを使用して、TextFragmentおよびParagraphsコレクションを使用したPDF生成シナリオで行インデントを指定できます。

次のコードスニペットを使用してください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 新しいドキュメントオブジェクトを作成する
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// テキストフラグメントのTextFormattingOptionsを初期化し、SubsequentLinesIndent値を指定する
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## テキストボーダーの追加方法

次のコードスニペットは、TextBuilderを使用してテキストにボーダーを追加し、TextStateのDrawTextRectangleBorderプロパティを設定する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 新しいドキュメントオブジェクトを作成
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントを作成
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// テキストプロパティを設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// テキストの矩形周りにボーダー（ストローキング）を描くためのStrokingColorプロパティを設定
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// DrawTextRectangleBorderプロパティの値をtrueに設定
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// ドキュメントを保存
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## 下線テキストの追加方法

次のコードスニペットは、新しいPDFファイルを作成する際に下線テキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントオブジェクトを作成する
Document pdfDocument = new Document();
// PDFドキュメントにページを追加する
pdfDocument.Pages.Add();
// 最初のページに対してTextBuilderを作成する
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// サンプルテキストを含むTextFragment
TextFragment fragment = new TextFragment("Test message");
// TextFragmentのフォントを設定する
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// テキストのフォーマットを下線に設定する
fragment.TextState.Underline = true;
// TextFragmentを配置する位置を指定する
fragment.Position = new Position(10, 800);
// TextFragmentをPDFファイルに追加する
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// 結果のPDFドキュメントを保存する。
pdfDocument.Save(dataDir);
```
## テキストに枠を追加する方法

テキストの見た目を制御することができます。以下の例は、追加したテキストの周りに矩形を描画することで枠を追加する方法を示しています。[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスについてもっと知る。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// 結果のPDF文書を保存。
editor.Save(dataDir);
```

## 改行を追加する方法
## 新しいラインフィードを追加する方法

TextFragmentはテキスト内の改行をサポートしていません。しかし、改行付きのテキストを追加するためには、TextParagraphを使ったTextFragmentを使用してください：

- TextFragmentでは単一の"\n"の代わりに"\r\n"またはEnvironment.NewLineを使用します；
- TextParagraphオブジェクトを作成します。これにより、テキストが分割されて追加されます；
- TextParagraph.AppendLineでTextFragmentを追加します；
- TextBuilder.AppendParagraphでTextParagraphを追加します。
以下のコードスニペットを使用してください。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 必要な改行マーカーを含むテキストで新しいTextFragmentを初期化します
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 必要に応じてテキストフラグメントのプロパティを設定します
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraphオブジェクトを作成します
TextParagraph par = new TextParagraph();

// 段落に新しいTextFragmentを追加します
par.AppendLine(textFragment);

// 段落の位置を設定します
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilderオブジェクトを作成します
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilderを使用してTextParagraphを追加します
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// 結果のPDFドキュメントを保存します。
pdfApplicationDoc.Save(dataDir);
```
## 取り消し線テキストの追加方法

TextStateクラスは、PDFドキュメント内に配置されるTextFragmentsに対してフォーマット設定を行う機能を提供します。このクラスを使用して、テキストのフォーマット設定を太字、イタリック、下線、そしてこのリリースからは取り消し線としてマークする機能が追加されました。次のコードスニペットを使用して、取り消し線フォーマットでTextFragmentを追加してみてください。

完全なコードスニペットを使用してください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントを開く
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();

// テキストフラグメントを作成
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// テキストプロパティを設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// StrikeOutプロパティを設定
textFragment.TextState.StrikeOut = true;
// テキストを太字に設定
textFragment.TextState.FontStyle = FontStyles.Bold;

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDFページにテキストフラグメントを追加
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```
## テキストにグラデーションシェーディングを適用する

テキスト編集シナリオのAPIでテキストフォーマットがさらに強化され、PDFドキュメント内にパターンカラースペースを持つテキストを追加できるようになりました。Aspose.Pdf.Colorクラスは、PatternColorSpaceの新しいプロパティを導入することでさらに強化されています。この新しいプロパティは、テキストのシェーディングカラーを指定するために使用できます。この新しいプロパティは、次のコードスニペットに示すように、異なるグラデーションシェーディングをテキストに追加します。例えば、軸シェーディング、放射状（タイプ3）シェーディングです：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // パターンカラースペースで新しい色を作成します
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>放射状グラデーションを適用するには、上記のコードスニペットで 'PatternColorSpace' プロパティを 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' に設定します。

## フロートコンテンツにテキストを整列させる方法

Aspose.PDFは、Floating Box要素内のコンテンツのテキストアラインメントを設定することをサポートしています。次のコードサンプルに示されているように、Aspose.Pdf.FloatingBoxインスタンスのアラインメントプロパティを使用してこれを実現できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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

