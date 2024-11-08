---
title: PDFに画像スタンプを追加するC#の使用
linktitle: PDFファイルの画像スタンプ
type: docs
weight: 10
url: /ja/net/image-stamps-in-pdf-page/
description: Aspose.PDFライブラリを使用してPDFドキュメントに画像スタンプを追加します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFに画像スタンプを追加するC#の使用",
    "alternativeHeadline": "PDFに画像スタンプを追加するC#の使用",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, ドキュメント生成",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDFライブラリを使用してPDFドキュメントに画像スタンプを追加します。"
}
</script>
## PDFファイルにイメージスタンプを追加

ImageStampクラスを使用して、PDFファイルにイメージスタンプを追加できます。ImageStampクラスは、高さ、幅、透明度など、イメージベースのスタンプを作成するために必要なプロパティを提供します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリとも動作します。

イメージスタンプを追加するには：

1. 必要なプロパティを使用してDocumentオブジェクトとImageStampオブジェクトを作成します。
1. PDFにスタンプを追加するためにPageクラスのAddStampメソッドを呼び出します。

次のコードスニペットは、PDFファイルにイメージスタンプを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// イメージスタンプを作成
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// 特定のページにスタンプを追加
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
## スタンプとしての画像品質の制御

スタンプオブジェクトとして画像を追加する際、画像の品質を制御することができます。ImageStampクラスのQualityプロパティを使用してこの目的に利用されます。これは画像の品質をパーセントで示します（有効な値は0..100です）。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// 画像スタンプを作成する
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## フローティングボックスでの背景としての画像スタンプ

Aspose.PDF APIは、フローティングボックスで背景として画像スタンプを追加することを可能にします。
Aspose.PDF APIを使用すると、フローティングボックス内の背景に画像スタンプを追加できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Documentオブジェクトをインスタンス化します
Document doc = new Document();
// PDFドキュメントにページを追加します
Page page = doc.Pages.Add();
// FloatingBoxオブジェクトを作成します
FloatingBox aBox = new FloatingBox(200, 100);
// FloatingBoxの左位置を設定します
aBox.Left = 40;
// FloatingBoxの上位置を設定します
aBox.Top = 80;
// FloatingBoxの水平方向の配置を設定します
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// FloatingBoxの段落コレクションにテキストフラグメントを追加します
aBox.Paragraphs.Add(new TextFragment("main text"));
// FloatingBoxに境界を設定します
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// 背景画像を追加します
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// FloatingBoxの背景色を設定します
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// ページオブジェクトの段落コレクションにFloatingBoxを追加します
page.Paragraphs.Add(aBox);
// PDFドキュメントを保存します
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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

