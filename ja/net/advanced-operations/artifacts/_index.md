---
title: .NETでのアーティファクトの操作
linktitle: アーティファクトの操作
type: docs
weight: 110
url: ja/net/artifacts/
description: Aspose.PDF for .NETは、PDFページに背景画像を追加し、Artifactクラスを使用して各ウォーターマークを取得することができます。
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": ".NETでのアーティファクトの操作",
    "alternativeHeadline": "PDFドキュメントのアーティファクト",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdfのアーティファクト",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETは、PDFページに背景画像を追加し、Artifactクラスを使用して各ウォーターマークを取得することができます。"
}
</script>
PDFのアーティファクトは、ドキュメントの実際のコンテンツの一部ではないグラフィックオブジェクトやその他の要素です。通常、装飾、レイアウト、または背景目的で使用されます。アーティファクトの例には、ページヘッダー、フッター、セパレーター、または意味を伝えない画像が含まれます。

PDFのアーティファクトの目的は、コンテンツと非コンテンツ要素を区別することを可能にすることです。これはアクセシビリティにとって重要で、スクリーンリーダーやその他の支援技術がアーティファクトを無視して関連するコンテンツに焦点を当てることができます。また、アーティファクトは印刷、検索、またはコピーから省略されることで、PDFドキュメントのパフォーマンスと品質を向上させることもできます。

PDFで要素をアーティファクトとして作成するには、[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) クラスを使用する必要があります。
以下の便利なプロパティが含まれています：

- **Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType列挙の値をサポートし、値にはBackground、Layout、Page、Pagination、Undefinedが含まれます）。
- **Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType列挙体の値をサポートし、Background, Layout, Page, Pagination, Undefinedが含まれます）。
- **Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype列挙体の値をサポートし、Background, Footer, Header, Undefined, Watermarkが含まれます）。
- **Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合は画像を、そうでない場合はnullを返します）。
- **Artifact.Text** – アーティファクトのテキストを取得します。
- **Artifact.Contents** – アーティファクトの内部オペレータのコレクションを取得します。サポートされているタイプはSystem.Collections.ICollectionです。
- **Artifact.Form** – アーティファクトのXFormを取得します（XFormが使用されている場合）。ウォーターマーク、ヘッダー、フッターのアーティファクトには、すべてのアーティファクトの内容を示すXFormが含まれています。
- **Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。
- **Artifact.Rotation** – アーティファクトの回転を取得します（度数で、正の値は反時計回りの回転を示します）。
- **Artifact.Opacity** – アーティファクトの不透明度を取得します。
- **Artifact.Opacity** – アーティファクトの不透明度を取得します。

以下のクラスもアーティファクトの操作に役立つかもしれません：

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## 既存の透かしの操作

Adobe Acrobatで作成された透かしはアーティファクトと呼ばれます（PDF仕様の14.8.2.2 実際のコンテンツとアーティファクトに記述されています）。

特定のページにあるすべての透かしを取得するために、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスには Artifacts プロパティがあります。

以下のコードスニペットは、PDFファイルの最初のページのすべての透かしを取得する方法を示しています。

_注記:_ このコードは [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。
_Note:_ このコードは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## アーティファクトとしての背景の扱い

背景画像は、水印や他の控えめなデザインを文書に加えるために使用できます。Aspose.PDF for .NETでは、各PDF文書はページの集合であり、各ページはアーティファクトの集合を含んでいます。[BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) クラスを使用して、ページオブジェクトに背景画像を追加することができます。

以下のコードスニペットは、BackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
もし何かの理由で無地の背景を使用したい場合は、以下の方法で先のコードを変更してください：

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## 特定のタイプのアーティファクトのカウント

特定のタイプのアーティファクトの総数を計算するには（例えば、ウォーターマークの総数）、以下のコードを使用します：

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NETライブラリ",
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

