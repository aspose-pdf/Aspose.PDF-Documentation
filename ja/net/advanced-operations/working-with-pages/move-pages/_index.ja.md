---
title: プログラムでPDFページを移動する C#
linktitle: PDFページを移動
type: docs
weight: 20
url: /net/move-pages/
description: Aspose.PDF for .NETを使用して、PDFファイルの望ましい位置またはファイルの末尾にページを移動します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "プログラムでPDFページを移動する C#",
    "alternativeHeadline": ".NETでPDFページを移動する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, PDFページを移動",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF ドキュメントチーム",
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
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用して、PDFファイルの望ましい位置またはファイルの末尾にページを移動します。"
}
</script>
## PDFドキュメント間でページを移動する方法

このトピックでは、C#を使用して一つのPDFドキュメントから別のドキュメントの最後にページを移動する方法について説明します。

次のコードスニペットは[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

ページを移動するには以下の手順を実行します：

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. 宛先PDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションからページを取得します。
1. 宛先ドキュメントにページを[Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。
1. ソースドキュメントでページを[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)します。
1.

以下のコードスニペットは、ページを移動する方法を示しています。

```csharp
var srcFileName = "<ファイル名を入力>";
var dstFileName = "<ファイル名を入力>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// 出力ファイルの保存
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## PDFドキュメントから別のPDFドキュメントへの複数ページの移動

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスオブジェクトを作成します。
1. 宛先PDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスオブジェクトを作成します。
1. 移動するページ番号の配列を定義します。
1. 配列をループ処理します:
    1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) コレクションからページを取得します。
    1.
1. [保存](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して、出力PDFを保存します。
1. 配列を使用してソースドキュメントの[削除](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2)ページ。
1. [保存](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して、ソースPDFを保存します。

以下のコードスニペットは、あるPDFドキュメントから別のPDFドキュメントにページの束を移動する方法を示しています。

```csharp
var srcFileName = "<ファイル名を入力>";
var dstFileName = "<ファイル名を入力>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// 出力ファイルを保存
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## 現在のPDFドキュメントでページを新しい位置に移動

1. 
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) コレクションからページを取得します。
1. 新しい位置にページを[追加](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)します（例えば最後に）。
1. 前の位置でページを[削除](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) メソッドを使用して出力PDFを保存します。

```csharp
var srcFileName = "<ファイル名を入力>";
var dstFileName = "<ファイル名を入力>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// 出力ファイルを保存
srcDocument.Save(dstFileName);
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

