---
title: PDF内の画像を取得および検索する
linktitle: 画像を検索して取得する
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: このセクションでは、Aspose.PDFライブラリを使用してPDFドキュメントから画像を検索および取得する方法について説明します。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内の画像を取得および検索する",
    "alternativeHeadline": "PDFファイルから画像を取得および検索する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, .net, 画像を取得, 画像を検索",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、Aspose.PDFライブラリを使用してPDFドキュメントから画像を検索および取得する方法について説明します。"
}
</script>
ImagePlacementAbsorberを使用して、PDFドキュメントのすべてのページにある画像を検索できます。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

ドキュメント全体で画像を検索するには：

1. PagesコレクションのAcceptメソッドを呼び出します。AcceptメソッドはImagePlacementAbsorberオブジェクトをパラメータとして取ります。これにより、ImagePlacementオブジェクトのコレクションが返されます。
1. ImagePlacementsオブジェクトをループして、そのプロパティ（画像、寸法、解像度など）を取得します。

次のコードスニペットは、ドキュメントのすべての画像を検索する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// ドキュメントを開く
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf");

// 画像配置検索を実行するImagePlacementAbsorberオブジェクトを作成
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// すべてのページで吸収器を受け入れる
doc.Pages.Accept(abs);

// すべてのImagePlacementsをループし、画像とImagePlacementプロパティを取得
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // ImagePlacementオブジェクトを使用して画像を取得
    XImage image = imagePlacement.Image;

    // すべての配置の画像配置プロパティを表示
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);
}
```
個別のページから画像を取得するには、次のコードを使用します：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
doc.Pages[1].Accept(abs);
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
    "applicationCategory": "PDF操作ライブラリ for .NET",
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


