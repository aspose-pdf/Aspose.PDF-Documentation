---
title: .NETでのアーティファクトの操作
linktitle: アーティファクトの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /ja/net/artifacts/
description: Aspose.PDF for .NETはPDFページに背景画像を追加し、Artifactクラスを使用して各ウォーターマークを取得することを可能にします。
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NETはArtifactクラスを導入し、開発者がPDFドキュメント内で背景画像やウォーターマークなどの非コンテンツ要素を効率的に管理できるようにします。この機能は、アーティファクトが支援技術によって無視されることができるため、文書構造を強化し、アクセシビリティとパフォーマンスを向上させます。タイプとプロパティのカスタマイズ可能なオプションを使用して、ユーザーはこれらの要素を簡単に操作し、視覚的に魅力的なPDFを作成できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETはPDFページに背景画像を追加し、Artifactクラスを使用して各ウォーターマークを取得することを可能にします。"
}
</script>

PDFのアーティファクトは、文書の実際のコンテンツの一部ではないグラフィックオブジェクトやその他の要素です。通常、装飾、レイアウト、または背景の目的で使用されます。アーティファクトの例には、ページヘッダー、フッター、区切り線、または意味を伝えない画像が含まれます。

PDFにおけるアーティファクトの目的は、コンテンツと非コンテンツ要素の区別を可能にすることです。これはアクセシビリティにとって重要であり、スクリーンリーダーやその他の支援技術がアーティファクトを無視し、関連するコンテンツに焦点を合わせることができます。アーティファクトは、印刷、検索、またはコピーから省略できるため、PDFドキュメントのパフォーマンスと品質を向上させることもできます。

PDFで要素をアーティファクトとして作成するには、[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact)クラスを使用する必要があります。
以下の便利なプロパティが含まれています：

- **Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType列挙型の値をサポートし、値にはBackground、Layout、Page、Pagination、Undefinedが含まれます）。
- **Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype列挙型の値をサポートし、値にはBackground、Footer、Header、Undefined、Watermarkが含まれます）。
- **Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、そうでない場合はnull）。
- **Artifact.Text** – アーティファクトのテキストを取得します。
- **Artifact.Contents** – アーティファクト内部オペレーターのコレクションを取得します。サポートされているタイプはSystem.Collections.ICollectionです。
- **Artifact.Form** – アーティファクトのXFormを取得します（XFormが使用されている場合）。ウォーターマーク、ヘッダー、フッターアーティファクトには、すべてのアーティファクト内容を示すXFormが含まれています。
- **Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。
- **Artifact.Rotation** – アーティファクトの回転を取得します（度数で、正の値は反時計回りの回転を示します）。
- **Artifact.Opacity** – アーティファクトの不透明度を取得します。可能な値は0...1の範囲で、1は完全に不透明です。

アーティファクトの操作に役立つ以下のクラスもあります：

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## 既存のウォーターマークの操作

Adobe Acrobatで作成されたウォーターマークはアーティファクトと呼ばれます（PDF仕様の14.8.2.2 実際のコンテンツとアーティファクトに記載されています）。

特定のページ上のすべてのウォーターマークを取得するには、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)クラスのArtifactsプロパティを使用します。

以下のコードスニペットは、PDFファイルの最初のページにあるすべてのウォーターマークを取得する方法を示しています。

_注:_ このコードは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## アーティファクトとしての背景の操作

背景画像は、ドキュメントにウォーターマークやその他の微妙なデザインを追加するために使用できます。Aspose.PDF for .NETでは、各PDFドキュメントはページのコレクションであり、各ページにはアーティファクトのコレクションが含まれています。[BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact)クラスを使用して、ページオブジェクトに背景画像を追加できます。

以下のコードスニペットは、BackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

何らかの理由で、単色の背景を使用したい場合は、前のコードを次のように変更してください：

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## 特定のタイプのアーティファクトのカウント

特定のタイプのアーティファクトの総数を計算するには（例えば、ウォーターマークの総数）、以下のコードを使用します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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