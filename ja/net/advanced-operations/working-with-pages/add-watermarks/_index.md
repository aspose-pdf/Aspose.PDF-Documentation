---
title: C#を使用してPDFに透かしを追加する
linktitle: 透かしを追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ja/net/add-watermarks/
description: この記事では、C#を使用してプログラム的にPDF内のアーティファクトを操作し、透かしを取得する機能について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "Aspose.PDF for .NETの新機能により、開発者はアーティファクト機能を使用してPDFドキュメントにカスタマイズ可能な透かしをプログラム的に追加できます。この機能は、タイプ、透明度、回転、テキストのカスタマイズなど、さまざまなアーティファクトプロパティをサポートすることで文書管理を強化し、ユーザーがプロフェッショナルで識別可能なPDFファイルを簡単に作成できるようにします。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "この記事では、C#を使用してプログラム的にPDF内のアーティファクトを操作し、透かしを取得する機能について説明します。"
}
</script>

**Aspose.PDF for .NET**は、アーティファクトを使用してPDFドキュメントに透かしを追加することを可能にします。このタスクを解決するためにこの記事を確認してください。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

Adobe Acrobatで作成された透かしはアーティファクトと呼ばれます（PDF仕様の14.8.2.2の実際のコンテンツとアーティファクトに記載されています）。アーティファクトを操作するために、Aspose.PDFには2つのクラスがあります：[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact)と[ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)。

特定のページ上のすべてのアーティファクトを取得するには、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)クラスのArtifactsプロパティを使用します。このトピックでは、PDFファイル内のアーティファクトの操作方法について説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact)クラスには次のプロパティがあります：

- **Artifact.Type**: アーティファクトのタイプを取得します（Artifact.ArtifactType列挙型の値をサポートし、値にはBackground、Layout、Page、Pagination、Undefinedが含まれます）。
- **Artifact.Subtype**: アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype列挙型の値をサポートし、値にはBackground、Footer、Header、Undefined、Watermarkが含まれます）。

{{% alert color="primary" %}}

Adobe Acrobatで作成された透かしは、タイプがPaginationでサブタイプがWatermarkであることに注意してください。

{{% /alert %}}

- **Artifact.Contents**: アーティファクト内部オペレーターのコレクションを取得します。サポートされているタイプはSystem.Collections.ICollectionです。
- **Artifact.Form**: アーティファクトのXFormを取得します（XFormが使用されている場合）。透かし、ヘッダー、フッターのアーティファクトには、すべてのアーティファクト内容を示すXFormが含まれています。
- **Artifact.Image**: アーティファクトの画像を取得します（画像が存在する場合、そうでない場合はnull）。
- **Artifact.Text**: アーティファクトのテキストを取得します。
- **Artifact.Rectangle**: ページ上のアーティファクトの位置を取得します。
- **Artifact.Rotation**: アーティファクトの回転を取得します（度数で、正の値は反時計回りの回転を示します）。
- **Artifact.Opacity**: アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。

## PDFファイルに透かしを追加する方法

次のコードスニペットは、C#を使用してPDFファイルの最初のページにある各透かしを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
    }
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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