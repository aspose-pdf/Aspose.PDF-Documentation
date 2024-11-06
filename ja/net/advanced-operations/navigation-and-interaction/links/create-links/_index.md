---
title: PDFファイルにC#でリンクを作成する
linktitle: リンクを作成
type: docs
weight: 10
url: ja/net/create-links/
description: このセクションでは、C#を使用してPDFドキュメントにリンクを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルにC#でリンクを作成する",
    "alternativeHeadline": "PDFにリンクを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdfにリンクを作成",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C#を使用してPDFドキュメントにリンクを作成する方法について説明します。"
}
</script>

以下のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## リンクを作成する

ドキュメントにアプリケーションへのリンクを追加することで、ドキュメントからアプリケーションにリンクすることができます。これは、例えばチュートリアルの特定のポイントで読者に特定のアクションを取らせたい場合や、機能豊かなドキュメントを作成する場合に便利です。アプリケーションリンクを作成するには：

1. [ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成します。
1. リンクを追加したい[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page)を取得します。
1. ページと[矩形](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle)オブジェクトを使用して[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを使用してリンク属性を設定します。
1. [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) オブジェクトを作成する際に、起動するアプリケーションを指定します。
1. リンクをページオブジェクトの [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) プロパティに追加します。
1. 最後に、ドキュメントオブジェクトの [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFを保存します。

以下のコードスニペットは、PDFファイルにアプリケーションへのリンクを作成する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// ドキュメントを開く
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// リンクを作成する
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// 更新されたドキュメントを保存する
document.Save(dataDir);
```
### PDFファイル内でPDFドキュメントリンクを作成

Aspose.PDF for .NETでは、外部のPDFファイルへのリンクを追加して、複数のドキュメントをリンクさせることができます。PDFドキュメントリンクを作成するには：

1. 最初に、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 次に、リンクを追加したい特定の[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を取得します。
1. Pageと[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle)オブジェクトを使用して、[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを使用してリンク属性を設定します。
1. Actionプロパティを[GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction)オブジェクトに設定します。
1. ページオブジェクトのアノテーションコレクションにリンクを追加します。
1. Documentオブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して、更新されたPDFを保存します。

以下のコードスニペットは、PDFファイル内にPDFドキュメントリンクを作成する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// ドキュメントを開く
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// リンクを作成する
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// 更新されたドキュメントを保存する
document.Save(dataDir);
```

<script type="application/ld+json">

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET ライブラリ",
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

