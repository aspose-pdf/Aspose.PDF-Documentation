---
title: PDF C#でテキストスタンプを追加
linktitle: PDFファイルのテキストスタンプ
type: docs
weight: 20
url: /net/text-stamps-in-the-pdf-file/
description: TextStamp クラスと Aspose.PDF for .NET ライブラリを使用して PDF 文書にテキストスタンプを追加します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF C#でテキストスタンプを追加",
    "alternativeHeadline": "PDF C#でテキストスタンプを追加",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "TextStamp クラスと Aspose.PDF for .NET ライブラリを使用して PDF 文書にテキストスタンプを追加します。"
}
</script>
## C#でテキストスタンプを追加

[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) クラスを使用して、PDFファイルにテキストスタンプを追加できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。テキストスタンプを追加するためには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PDFにスタンプを追加するためにPageのAddStampメソッドを呼び出すことができます。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

次のコードスニペットは、PDFファイルにテキストスタンプを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// テキストスタンプを作成
TextStamp textStamp = new TextStamp("Sample Stamp");
// スタンプが背景かどうかを設定
textStamp.Background = true;
// 原点を設定
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// スタンプを回転
textStamp.Rotate = Rotation.on90;
// テキストプロパティを設定
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// 特定のページにスタンプを追加
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
## TextStamp オブジェクトの配置を定義する

PDFドキュメントにウォーターマークを追加することは、よく要求される機能の一つであり、Aspose.PDF for .NETは画像およびテキストのウォーターマークを追加することが完全に可能です。[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) というクラスがあり、PDFファイル上にテキストスタンプを追加する機能を提供しています。最近、TextStampオブジェクトを使用する際にテキストの配置を指定する機能のサポートが求められています。この要求を満たすために、TextStampクラスにTextAlignmentプロパティを導入しました。このプロパティを使用すると、水平テキストの配置を指定できます。

以下のコードスニペットは、既存のPDFドキュメントを読み込み、それにTextStampを追加する例を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 入力ファイルでDocumentオブジェクトをインスタンス化
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// サンプル文字列でFormattedTextオブジェクトをインスタンス化
FormattedText text = new FormattedText("This");
// FormattedTextに新しいテキスト行を追加
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// FormattedTextを使用してTextStampオブジェクトを作成
TextStamp stamp = new TextStamp(text);
// テキストスタンプの水平配置を中央揃えに指定
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// テキストスタンプの垂直配置を中央揃えに指定
stamp.VerticalAlignment = VerticalAlignment.Center;
// TextStampのテキスト水平配置を中央揃えに指定
stamp.TextAlignment = HorizontalAlignment.Center;
// スタンプオブジェクトの上マージンを設定
stamp.TopMargin = 20;
// ドキュメントの最初のページにスタンプオブジェクトを追加
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
```
## PDFファイルにフィルストロークテキストをスタンプとして使用

テキストの追加および編集シナリオにおいて、テキストのレンダリングモードの設定を実装しました。ストロークテキストをレンダリングするには、TextStateオブジェクトを作成し、RenderingModeをTextRenderingMode.StrokeTextに設定し、StrokingColorプロパティに色を選択してください。その後、BindTextState()メソッドを使用してTextStateをスタンプにバインドします。

以下のコードスニペットは、フィルストロークテキストを追加する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// 高度なプロパティを転送するためのTextStateオブジェクトを作成します
TextState ts = new TextState();
// ストロークの色を設定します
ts.StrokingColor = Color.Gray;
// テキストレンダリングモードを設定します
ts.RenderingMode = TextRenderingMode.StrokeText;
// 入力PDFドキュメントをロードします
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// TextStateをバインドします
stamp.BindTextState(ts);
// X,Y原点を設定します
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// スタンプを追加します
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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

