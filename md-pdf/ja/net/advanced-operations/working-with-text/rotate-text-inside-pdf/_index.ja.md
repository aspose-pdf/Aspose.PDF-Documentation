---
title: PDF内のテキストをC#を使用して回転する
linktitle: PDF内のテキストを回転する
type: docs
weight: 50
url: /net/rotate-text-inside-pdf/
description: PDFへのテキストの異なる回転方法を学びます。Aspose.PDFを使用して、任意の角度にテキストを回転させたり、テキストの断片または段落全体を回転させることができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストをC#を使用して回転する",
    "alternativeHeadline": "PDFファイルのテキストを回転する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, 文書生成",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "PDFへのテキストの異なる回転方法を学びます。Aspose.PDFを使用して、任意の角度にテキストを回転させたり、テキストの断片または段落全体を回転させることができます。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

## PDF内のテキストを回転プロパティを使用して回転する

[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) クラスの Rotation プロパティを使用することで、テキストをさまざまな角度で回転させることができます。テキストの回転は、ドキュメント生成の異なるシナリオで使用できます。テキストを必要に応じて回転する角度を度数で指定できます。テキストの回転を実装できる以下の異なるシナリオを確認してください。

## TextFragment と TextBuilder を使用した回転の実装

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントを作成
TextFragment textFragment1 = new TextFragment("メインテキスト");
textFragment1.Position = new Position(100, 600);
// テキストのプロパティを設定
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転したテキストフラグメントを作成
TextFragment textFragment2 = new TextFragment("回転テキスト");
textFragment2.Position = new Position(200, 600);
// テキストのプロパティを設定
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// 回転したテキストフラグメントを作成
TextFragment textFragment3 = new TextFragment("回転テキスト");
textFragment3.Position = new Position(300, 600);
// テキストのプロパティを設定
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// TextBuilder オブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDFページにテキストフラグメントを追加
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```
## TextParagraphとTextBuilderを使用した回転の実装（回転したフラグメント）

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// テキストフラグメントを作成
TextFragment textFragment1 = new TextFragment("回転したテキスト");
// テキストのプロパティを設定
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定
textFragment1.TextState.Rotation = 45;
// テキストフラグメントを作成
TextFragment textFragment2 = new TextFragment("メインテキスト");
// テキストのプロパティを設定
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// テキストフラグメントを作成
TextFragment textFragment3 = new TextFragment("別の回転したテキスト");
// テキストのプロパティを設定
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定
textFragment3.TextState.Rotation = -45;
// パラグラフにテキストフラグメントを追加
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDFページにテキストパラグラフを追加
textBuilder.AppendParagraph(paragraph);
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```
## TextFragmentとPage.Paragraphsを使用した回転の実装

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化します
Document pdfDocument = new Document();
// 特定のページを取得します
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントを作成します
TextFragment textFragment1 = new TextFragment("メインテキスト");
// テキストプロパティを設定します
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// テキストフラグメントを作成します
TextFragment textFragment2 = new TextFragment("回転テキスト");
// テキストプロパティを設定します
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定します
textFragment2.TextState.Rotation = 315;
// テキストフラグメントを作成します
TextFragment textFragment3 = new TextFragment("回転テキスト");
// テキストプロパティを設定します
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定します
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// ドキュメントを保存します
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```
## TextParagraphとTextBuilderを使用した回転の実装（全段落回転）

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトの初期化
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // 回転を指定
    paragraph.Rotation = i * 90 + 45;
    // テキストフラグメントを作成
    TextFragment textFragment1 = new TextFragment("段落テキスト");
    // テキストフラグメントを作成
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // テキストフラグメントを作成
    TextFragment textFragment2 = new TextFragment("テキストの2行目");
    // テキストのプロパティを設定
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // テキストフラグメントを作成
    TextFragment textFragment3 = new TextFragment("さらにテキスト...");
    // テキストのプロパティを設定
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // TextBuilderオブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // PDFページにテキストフラグメントを追加
    textBuilder.AppendParagraph(paragraph);
}
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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

