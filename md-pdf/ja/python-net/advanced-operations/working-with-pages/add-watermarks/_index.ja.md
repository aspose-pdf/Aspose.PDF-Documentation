---
title: Pythonを使用してPDFに透かしを追加する
linktitle: 透かしを追加
type: docs
weight: 40
url: /python-net/add-watermarks/
description: この記事では、Pythonを使用してプログラムでPDFのアーティファクトを操作し、透かしを取得する機能について説明します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFに透かしを追加する",
    "alternativeHeadline": "PDFに透かしを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf,python, 透かし追加",
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
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Pythonを使用してPDFのアーティファクトを操作し、透かしを取得する機能について説明します。"
}
</script>


**Aspose.PDF for Python via .NET**は、アーティファクトを使用してPDFドキュメントに透かしを追加することを可能にします。このタスクを解決するために、この記事を確認してください。

アーティファクトを操作するために、Aspose.PDFには2つのクラスがあります：[Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/)と[ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)です。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスにはArtifactsプロパティがあります。このトピックでは、PDFファイルでアーティファクトを操作する方法を説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) クラスには以下のプロパティがあります：

**contents** – アーティファクト内部オペレーターのコレクションを取得します。そのサポートされているタイプはSystem.Collections.ICollectionです。

**form** – アーティファクトのXFormを取得します（XFormが使用されている場合）。透かし、ヘッダー、フッターアーティファクトには、すべてのアーティファクトコンテンツを表示するXFormが含まれています。

**image** – アーティファクトの画像を取得します（画像が存在する場合、それ以外の場合はnull）。
**text** – アーティファクトのテキストを取得します。
**rectangle** – ページ上のアーティファクトの位置を取得します。
**rotation** – アーティファクトの回転を取得します（度単位、正の値は反時計回りの回転を示します）。
**opacity** – アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。

## プログラミングサンプル: PDFファイルに透かしを追加する方法

以下のコードスニペットは、Pythonを使用してPDFファイルの最初のページに各透かしを取得する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
```


{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "Python用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}