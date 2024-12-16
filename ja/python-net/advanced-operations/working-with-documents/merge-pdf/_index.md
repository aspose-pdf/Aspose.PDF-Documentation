---
title: Pythonを使用してPDFをマージする方法
linktitle: PDFファイルをマージ
type: docs
weight: 50
url: /ja/python-net/merge-pdf-documents/
description: このページでは、Pythonを使用してPDFドキュメントを単一のPDFファイルにマージする方法を説明します。
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFをマージする方法",
    "alternativeHeadline": "Pythonを介してPDFドキュメントを結合",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document manipulation",
    "keywords": "pdf, python, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "このページでは、.NETを介してPythonでPDFドキュメントを単一のPDFファイルにマージする方法を説明します。"
}
</script>


## 複数のPDFをPythonで単一のPDFに結合または統合する

PDFファイルを結合することは、ユーザーの間で非常に人気のあるクエリです。これは、共有したいまたは一緒に保存したい複数のPDFファイルがある場合に便利です。

PDFファイルを結合することで、文書を整理し、PC上の保存スペースを確保し、複数のPDFファイルを1つの文書に結合して他の人と共有することができます。

.NET経由でPythonでPDFを結合することは、サードパーティライブラリを使用せずに行うのは簡単ではありません。この記事では、Aspose.PDF for Python via .NETを使用して複数のPDFファイルを単一のPDF文書に結合する方法を示します。

## PythonとDOMを使用してPDFファイルを結合

2つのPDFファイルを連結するには：

1. 各入力PDFファイルを含む2つの[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトを作成します。

1. 次に、他のPDFファイルを追加したいDocumentオブジェクトの[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションの[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)メソッドを呼び出します。
1. 2つ目のDocumentオブジェクトのPageCollectionコレクションを、最初のPageCollectionコレクションの[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)メソッドに渡します。
1. 最後に、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用して出力PDFファイルを保存します。

次のコードスニペットは、PDFファイルを連結する方法を示しています。

```python

    import aspose.pdf as ap

    # 最初のドキュメントを開く
    document1 = ap.Document(input_pdf_1)
    # 2番目のドキュメントを開く
    document2 = ap.Document(input_pdf_2)

    # 2番目のドキュメントのページを最初に追加
    document1.pages.add(document2.pages)

    # 連結された出力ファイルを保存
    document1.save(output_pdf)
```

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) は、プレゼンテーションのマージ機能がどのように機能するかを調査することができるオンラインの無料ウェブアプリケーションです。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

<script type="application/ld+json">
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
    "applicationCategory": "PDF 操作ライブラリ for Python",
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
</script>