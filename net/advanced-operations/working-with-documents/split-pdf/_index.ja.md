---
title: PDFをプログラムで分割
linktitle: PDFファイルを分割
type: docs
weight: 60
url: /net/split-pdf-document/
keywords: split pdf into multiple files, split pdf into separate pdfs, split pdf c#
description: このトピックでは、C#を使用して.NETアプリケーションでPDFページを個々のPDFファイルに分割する方法を示します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFをプログラムで分割",
    "alternativeHeadline": ".NETでPDFを分割する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, split pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "このトピックでは、C#を使用して.NETアプリケーションでPDFページを個々のPDFファイルに分割する方法を示します。"
}
</script>
## ライブ例

[Aspose.PDFスプリッター](https://products.aspose.app/pdf/splitter)はオンラインで無料のWebアプリケーションで、プレゼンテーションの分割機能の動作を調査できます。

[![Aspose PDFを分割](splitter.png)](https://products.aspose.app/pdf/splitter)

このトピックでは、.NETアプリケーションでPDFページを個々のPDFファイルに分割する方法について説明します。C#を使用してPDFページを単一ページのPDFファイルに分割するには、次の手順に従います：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションを通じてPDFドキュメントのページをループします
1. 各反復で、新しいDocumentオブジェクトを作成し、個々の[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトを空のドキュメントに追加します
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して新しいPDFを保存します

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。
[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでもこのコードスニペットは動作します。

## C#でPDFを複数のファイルまたは個別のPDFに分割する

以下のC#コードスニペットは、PDFページを個々のPDFファイルに分割する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// すべてのページをループする
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
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


