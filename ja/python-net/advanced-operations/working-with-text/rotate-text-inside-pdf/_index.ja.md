---
title: PDF内のテキストをPythonで回転させる
linktitle: PDF内のテキストを回転させる
type: docs
weight: 50
url: /python-net/rotate-text-inside-pdf/
description: PDFにテキストを回転させるさまざまな方法を学びます。Aspose.PDFを使用すると、任意の角度にテキストを回転させたり、テキストの断片や全文を回転させたりできます。
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストをPythonで回転させる",
    "alternativeHeadline": "PDFファイル内のテキストを回転させる方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "PDFにテキストを回転させるさまざまな方法を学びます。Aspose.PDFを使用すると、任意の角度にテキストを回転させたり、テキストの断片や全文を回転させたりできます。"
}
</script>


## 回転プロパティを使用してPDF内のテキストを回転

[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment) クラスの回転プロパティを使用することで、テキストをさまざまな角度で回転させることができます。テキストの回転は、ドキュメント生成のさまざまなシナリオで使用できます。必要に応じて、テキストを回転させるための角度を度数で指定できます。以下の異なるシナリオを確認して、テキストの回転を実装する方法を学んでください。

## TextFragmentとTextBuilderを使用した回転の実装

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントを作成
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// テキストプロパティを設定
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転されたテキストフラグメントを作成
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// テキストプロパティを設定
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// 回転されたテキストフラグメントを作成
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// テキストプロパティを設定
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// テキストフラグメントをPDFページに追加
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## TextParagraphとTextBuilderを使用した回転の実装（回転されたフラグメント）

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
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
// テキストフラグメントを段落に追加
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// TextBuilderオブジェクトを作成
TextBuilder textBuilder = new TextBuilder(pdfPage);
// テキスト段落をPDFページに追加
textBuilder.AppendParagraph(paragraph);
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## TextFragment と Page.Paragraphs を使用した回転の実装

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化
Document pdfDocument = new Document();
// 特定のページを取得
Page pdfPage = (Page)pdfDocument.Pages.Add();
// テキストフラグメントを作成
TextFragment textFragment1 = new TextFragment("main text");
// テキストプロパティを設定
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// テキストフラグメントを作成
TextFragment textFragment2 = new TextFragment("rotated text");
// テキストプロパティを設定
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定
textFragment2.TextState.Rotation = 315;
// テキストフラグメントを作成
TextFragment textFragment3 = new TextFragment("rotated text");
// テキストプロパティを設定
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 回転を設定
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// ドキュメントを保存
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## TextParagraph と TextBuilder を使用して回転を実装する（段落全体を回転）

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// ドキュメントオブジェクトを初期化する
Document pdfDocument = new Document();
// 特定のページを取得する
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // 回転を指定する
    paragraph.Rotation = i * 90 + 45;
    // テキストフラグメントを作成する
    TextFragment textFragment1 = new TextFragment("段落テキスト");
    // テキストフラグメントを作成する
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // テキストフラグメントを作成する
    TextFragment textFragment2 = new TextFragment("テキストの2行目");
    // テキストのプロパティを設定する
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // テキストフラグメントを作成する
    TextFragment textFragment3 = new TextFragment("そしてさらにいくつかのテキスト...");
    // テキストのプロパティを設定する
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // TextBuilder オブジェクトを作成する
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // テキストフラグメントを PDF ページに追加する
    textBuilder.AppendParagraph(paragraph);
}
// ドキュメントを保存する
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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