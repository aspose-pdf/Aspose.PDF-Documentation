---
title: C#を使用してPDFをマージする方法
linktitle: PDFファイルをマージする
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/merge-pdf-documents/
description: このページでは、C#またはVB.NETを使用してPDFドキュメントを単一のPDFファイルにマージする方法を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Aspose.PDFライブラリを使用して、複数のPDFドキュメントを単一のファイルに簡単にマージする強力な機能を発見してください。この機能により、開発者はPDFを効率的に結合することでワークフローを合理化し、プロセス全体で品質と構造を維持できます。ソフトウェア統合に最適で、この機能は文書管理タスクを簡素化することで生産性を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "このページでは、C#またはVB.NETを使用してPDFドキュメントを単一のPDFファイルにマージする方法を説明します。"
}
</script>

## C#で複数のPDFを単一のPDFにマージまたは結合する

C#でPDFをマージすることは、サードパーティライブラリを使用しないと簡単ではありません。
この記事では、Aspose.PDF for .NETを使用して複数のPDFファイルを単一のPDFドキュメントにマージする方法を示します。例はC#で書かれていますが、APIはVB.NETなどの他の.NETプログラミング言語でも使用できます。PDFファイルは、最初のファイルが他のドキュメントの最後に結合されるようにマージされます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## PDFファイルをマージする

2つのPDFファイルを連結するには：

1. 各入力PDFファイルを含む2つの[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 次に、他のPDFファイルを追加したいDocumentオブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションのAddメソッドを呼び出します。
1. 2番目のDocumentオブジェクトのPageCollectionコレクションを最初のPageCollectionコレクションのAddメソッドに渡します。
1. 最後に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFファイルを保存します。

以下のコードスニペットは、PDFファイルを連結する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)は、プレゼンテーションのマージ機能がどのように機能するかを調査できるオンラインの無料Webアプリケーションです。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## 参照

- [DOMを使用してPDFを分割する](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [ファサードを使用してPDFドキュメントを連結する](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [ファサードを使用してPDFを分割する](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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