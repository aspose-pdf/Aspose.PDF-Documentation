---
title: PDFファイルから画像を削除するPythonの使用
linktitle: 画像を削除
type: docs
weight: 20
url: ja/python-net/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for Python via .NETを使用してPDFファイルから画像を削除する方法を説明します。
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルから画像を削除するPythonの使用",
    "alternativeHeadline": "PDFから画像を削除する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, 削除, pdfから画像を削除",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "このセクションでは、Aspose.PDF for Python via .NETを使用してPDFファイルから画像を削除する方法を説明します。"
}
</script>


PDFからすべてまたは特定の画像を削除する理由はたくさんあります。

時には、PDFファイルに重要な画像が含まれており、それを削除することでプライバシーを保護したり、特定の情報への不正アクセスを防止したりする必要があります。

不要または冗長な画像を削除すると、ファイルサイズを削減でき、PDFの共有や保存が容易になります。

必要に応じて、ドキュメントからすべての画像を削除することで、ページ数を減らすことができます。
また、ドキュメントから画像を削除することで、PDFを圧縮したり、テキスト情報を抽出したりする準備をすることができます。

**Aspose.PDF for Python via .NET** はこの作業を支援します。

## PDFファイルから画像を削除する

PDFファイルから画像を削除するには：

1. 既存のPDFドキュメントを開きます。
1. 特定の画像を削除します。
1. 更新したPDFファイルを保存します。

以下のコードスニペットは、PDFファイルから画像を削除する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_file)

    # 特定の画像を削除
    document.pages[2].resources.images.delete(1)

    # 更新したPDFファイルを保存
    document.save(output_pdf)
```


## 入力PDFからすべての画像を削除

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_file)

    # すべてのページのすべての画像を削除
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # 更新されたPDFファイルを保存
    document.save(output_file)
```

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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>