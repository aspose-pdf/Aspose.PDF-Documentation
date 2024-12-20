---
title: C#を使用してPDFに透かしを追加する
linktitle: 透かしを追加
type: docs
weight: 90
url: /ja/net/add-watermarks/
description: この記事は、C#をプログラムで使用してPDFで透かしを取得し、アーティファクトの操作の特徴について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFに透かしを追加する",
    "alternativeHeadline": "PDFに透かしを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, 透かしを追加",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事は、C#をプログラムで使用してPDFで透かしを取得し、アーティファクトの操作の特徴について説明します。"
}
</script>

**Aspose.PDF for .NET** は、Artifactsを使用してPDFドキュメントにウォーターマークを追加することができます。この記事をチェックして、タスクを解決してください。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも連携します。

Adobe Acrobatで作成されたウォーターマークはアーティファクトと呼ばれます（PDF仕様の14.8.2.2 実際の内容とアーティファクトに記載）。アーティファクトを扱うために、Aspose.PDFには [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) クラスと [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection) クラスがあります。

特定のページのすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスには Artifacts プロパティがあります。このトピックでは、PDFファイルでアーティファクトを扱う方法について説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) クラスには以下のプロパティが含まれています:

**Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType 列挙の値をサポートしており、値には Background, Layout, Page, Pagination, Undefined が含まれます）。
**Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType列挙型の値をサポートし、値にはBackground, Layout, Page, Pagination, Undefinedが含まれます）。
**Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype列挙型の値をサポートし、値にはBackground, Footer, Header, Undefined, Watermarkが含まれます）。

{{% alert color="primary" %}}

Adobe Acrobatで作成された透かしは、タイプがPaginationでサブタイプがWatermarkです。

{{% /alert %}}

**Artifact.Contents** – アーティファクトの内部オペレータのコレクションを取得します。サポートされるタイプはSystem.Collections.ICollectionです。
**Artifact.Form** – アーティファクトのXFormを取得します（XFormが使用されている場合）。透かし、ヘッダー、フッターのアーティファクトには、すべてのアーティファクト内容を示すXFormが含まれています。
**Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、それ以外の場合はnull）。
**Artifact.Text** – アーティファクトのテキストを取得します。
**Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。
**Artifact.Rotation** – アーティファクトの回転を取得します（度数で、正の値は反時計回りの回転を示します）。
 **Artifact.Rotation** – アーティファクトの回転を取得します（度数で、正の値は反時計回りの回転を示します）。
**Artifact.Opacity** – アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。

## プログラミングサンプル：PDFファイルにウォーターマークを追加する方法

次のコードスニペットは、C#を使用してPDFファイルの最初のページにある各ウォーターマークを取得する方法を示しています。

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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

