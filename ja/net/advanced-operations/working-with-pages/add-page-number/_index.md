---
title: C#を使用してPDFにページ番号を追加
linktitle: ページ番号の追加
type: docs
weight: 100
url: /ja/net/add-page-number/
description: Aspose.PDF for .NETを使用して、PageNumber Stampクラスを使用してPDFファイルにページ番号スタンプを追加できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFにページ番号を追加",
    "alternativeHeadline": "PDFにページ番号スタンプを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文書生成",
    "keywords": "pdf, c#, ページ番号スタンプ",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用して、PageNumber Stampクラスを使用してPDFファイルにページ番号スタンプを追加できます。"
}
</script>
すべてのドキュメントにはページ番号が含まれている必要があります。ページ番号により、読者がドキュメントの異なる部分を簡単に見つけることができます。
**Aspose.PDF for .NET** では、PageNumberStamp を使用してページ番号を追加できます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも機能します。

[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) クラスを使用して、PDFファイルにページ番号スタンプを追加することができます。
[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) クラスを使用して、PDFファイルにページ番号のスタンプを追加できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// ページ番号スタンプを作成する
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// スタンプが背景かどうか
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// テキストプロパティを設定
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// 特定のページにスタンプを追加
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
## ライブ例

[PDFページ番号を追加する](https://products.aspose.app/pdf/page-number) は、ページ番号追加機能がどのように機能するかを調査できる無料のオンラインWebアプリケーションです。

[![PDFでページ番号を追加する方法（C#使用）](page_number.png)](https://products.aspose.app/pdf/page-number)

## Bates番号の追加/削除

**Bates番号**（Batesスタンピングとも呼ばれます）は、法律、医療、ビジネス分野で使用され、画像や文書に識別番号や日付/時刻マークを配置します。これらは、スキャンされるか処理される際、例えば裁判の準備の発見段階やビジネス領収書の識別時に使用されます。このプロセスは、画像や文書の識別、保護、および自動連番を提供します。

Aspose.PDFは現在、Bates番号のサポートが限定されています。この機能は顧客の要望に応じて更新されます。

### Bates番号を削除する方法

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
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
    "applicationCategory": ".NETのためのPDF操作ライブラリ",
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

