---
title: C#を使用してPDFをマージする方法
linktitle: PDFファイルをマージする
type: docs
weight: 50
url: /net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
description: このページでは、C#またはVB.NETを使用してPDFドキュメントを単一のPDFファイルにマージする方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFをマージする方法",
    "alternativeHeadline": "PDFドキュメントを結合する",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメントの操作",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "このページでは、C#またはVB.NETを使用してPDFドキュメントを単一のPDFファイルにマージする方法について説明します。"
}
</script>
## C#で複数のPDFを単一のPDFに結合または結合する

C#でPDFを結合するのは、サードパーティのライブラリを使用しないと簡単な作業ではありません。
この記事では、Aspose.PDF for .NETを使用して複数のPDFファイルを単一のPDFドキュメントに結合する方法を示します。 例はC#で書かれていますが、APIはVB.NETなどの他の.NETプログラミング言語でも使用できます。 PDFファイルは、最初のものが他のドキュメントの最後に結合されるように結合されます。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで機能します。

## C#とDOMを使用してPDFファイルを結合する

2つのPDFファイルを連結するには：

1. 入力PDFファイルのそれぞれを含む2つの[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 次に、他のPDFファイルを追加したいDocumentオブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションのAddメソッドを呼び出します。
1.
1. 最終的に、[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) メソッドを使用して出力PDFファイルを保存します。

次のコードスニペットは、PDFファイルを連結する方法を示しています。

```csharp
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// 最初のドキュメントを開く
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// 二番目のドキュメントを開く
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// 二番目のドキュメントのページを最初のドキュメントに追加
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// 連結した出力ファイルを保存
pdfDocument1.Save(dataDir);
```

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) は、プレゼンテーションのマージ機能がどのように機能するかを調査できる無料のオンラインWebアプリケーションです。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## 参照

- [DOMを使用してPDFを分割する](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [DOMを使用してPDFを分割する](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Facadesを使用してPDFドキュメントを連結する](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Facadesを使用してPDFを分割する](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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

