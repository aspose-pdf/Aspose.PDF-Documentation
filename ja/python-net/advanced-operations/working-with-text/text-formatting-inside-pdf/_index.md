---
title: PDF内のテキストフォーマットをPythonで実施
linktitle: PDF内のテキストフォーマット
type: docs
weight: 30
url: ja/python-net/text-formatting-inside-pdf/
description: このページでは、PDFファイル内のテキストをフォーマットする方法について説明します。行のインデントを追加する、テキストの境界線を追加する、下線付きテキストを追加するなどがあります。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストフォーマットをPythonで実施",
    "alternativeHeadline": "PDFファイル内のテキストをフォーマットする方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, format text in pdf",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "このページでは、PDFファイル内のテキストをフォーマットする方法について説明します。行のインデントを追加する、テキストの境界線を追加する、下線付きテキストを追加するなどがあります。"
}
</script>


## PDFに行インデントを追加する方法

Aspose.PDF for .NETは、[TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions)クラスにSubsequentLinesIndentプロパティを提供しています。これを使用して、TextFragmentやParagraphsコレクションを使用したPDF生成シナリオで行インデントを指定することができます。

以下のコードスニペットを使用してこのプロパティを使用してください:

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NETをご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 新しいドキュメントオブジェクトを作成
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// テキストフラグメントのTextFormattingOptionsを初期化し、SubsequentLinesIndentの値を指定
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

以下のコードスニペットは、TextBuilderを使用してテキストにボーダーを追加し、TextStateのDrawTextRectangleBorderプロパティを設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 新しいドキュメントオブジェクトの作成
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントの作成
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// テキストプロパティの設定
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// テキスト矩形の周りにボーダー（ストローク）を描画するためのStrokingColorプロパティを設定
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// DrawTextRectangleBorderプロパティの値をtrueに設定
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// ドキュメントを保存
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```


## 下線付きテキストを追加する方法

次のコードスニペットは、新しいPDFファイルを作成する際に下線付きテキストを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントオブジェクトを作成
Document pdfDocument = new Document();
// PDFドキュメントにページを追加
pdfDocument.Pages.Add();
// 最初のページのためのTextBuilderを作成
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// サンプルテキストを含むTextFragment
TextFragment fragment = new TextFragment("Test message");
// TextFragmentのフォントを設定
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// テキストの書式を下線付きに設定
fragment.TextState.Underline = true;
// TextFragmentを配置する位置を指定
fragment.Position = new Position(10, 800);
// PDFファイルにTextFragmentを追加
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// 結果のPDFドキュメントを保存。
pdfDocument.Save(dataDir);
```


## 追加したテキストの周りに境界線を追加する方法

追加したテキストの外観を自由に調整できます。以下の例は、追加したテキストの周りに四角形を描いて境界線を追加する方法を示しています。[PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor) クラスについてさらに詳しく知ることができます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// 結果のPDFドキュメントを保存します。
editor.Save(dataDir);
```

## 改行フィードを追加する方法

TextFragmentはテキスト内の改行をサポートしていません。しかし、改行を含むテキストを追加するには、TextParagraphを使用したTextFragmentを使用してください：

- TextFragment内で単一の"\n"の代わりに"\r\n"またはEnvironment.NewLineを使用します;
- TextParagraphオブジェクトを作成します。それにより、テキストが分割されて追加されます;
- TextParagraph.AppendLineでTextFragmentを追加します;
- TextBuilder.AppendParagraphでTextParagraphを追加します。
以下のコードスニペットを使用してください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NETをご覧ください
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

// 新しいTextFragmentを段落に追加
par.AppendLine(textFragment);

// 段落の位置を設定
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilderを使用してTextParagraphを追加
textBuilder.AppendParagraph(par);

dataDir = dataDir + "AddNewLineFeed_out.pdf";

// 結果のPDFドキュメントを保存
pdfApplicationDoc.Save(dataDir);
```


## StrikeOutテキストを追加する方法

TextStateクラスは、PDFドキュメント内に配置されるTextFragmentsのフォーマットを設定する機能を提供します。このクラスを使用して、太字、斜体、下線などのテキストフォーマットを設定でき、今回のリリースからテキストフォーマットを打ち消し線としてマークする機能が追加されました。以下のコードスニペットを使用して、打ち消し線のフォーマットを持つTextFragmentを追加してみてください。

完全なコードスニペットを使用してください：

```csharp
// 完全なサンプルとデータファイルは、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
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
// 打ち消し線プロパティを設定
textFragment.TextState.StrikeOut = true;
// テキストを太字としてマーク
textFragment.TextState.FontStyle = FontStyles.Bold;

// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// テキストフラグメントをPDFページに追加
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// 結果として得られるPDFドキュメントを保存
pdfDocument.Save(dataDir);
```


## テキストにグラデーションシェーディングを適用する

テキスト編集シナリオのためにAPIでのテキストフォーマットがさらに強化され、PDFドキュメント内でパターンカラースペースを使用してテキストを追加できるようになりました。Aspose.Pdf.Colorクラスは新しいプロパティPatternColorSpaceを導入し、テキストのシェーディングカラーを指定するために使用できます。この新しいプロパティは、以下のコードスニペットに示すように、軸方向シェーディング、放射状（タイプ3）シェーディングなど、異なるグラデーションシェーディングをテキストに追加します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // パターンカラースペースを使用して新しい色を作成
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```


>放射状グラデーションを適用するには、上記のコードスニペットで 'PatternColorSpace' プロパティを 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' に設定します。

## テキストを浮動コンテンツに合わせる方法

Aspose.PDFは、Floating Box要素内のコンテンツのテキスト配置を設定することをサポートしています。以下のコードサンプルに示すように、Aspose.Pdf.FloatingBoxインスタンスの配置プロパティを使用してこれを実現できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
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
    "applicationCategory": "PDF操作ライブラリ for .NET",
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