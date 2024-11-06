---
title: PythonでPDFページサイズを変更する
linktitle: PDFページサイズの変更
type: docs
weight: 60
url: ja/python-net/change-page-size/
description: Aspose.PDF for Python via .NETライブラリを使用してPDFドキュメントのページサイズを変更します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PythonでPDFページサイズを変更する",
    "alternativeHeadline": "PythonでPDFページをリサイズする",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, change pdf size, resize pdf",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python via .NETライブラリを使用してPDFドキュメントのページサイズを変更します。"
}
</script>


## PDFページサイズの変更

Aspose.PDF for Python via .NETを使用すると、Pythonアプリケーションで簡単なコード行でPDFページサイズを変更できます。このトピックでは、既存のPDFファイルのページ寸法（サイズ）を更新/変更する方法を説明します。

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスには、ページサイズを設定するための [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) メソッドが含まれています。以下のコードスニペットは、いくつかの簡単なステップでページ寸法を更新します：

1. 元のPDFファイルを読み込みます。
1. ページを [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) オブジェクトに取得します。
1. 指定されたページを取得します。
1. set_page_size() メソッドを呼び出して寸法を更新します。
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出して、更新されたページ寸法でPDFファイルを生成します。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 特定のページを取得
    page = document.pages[1]

    # ページサイズをA4（11.7 x 8.3インチ）に設定し、Aspose.Pdfでは1インチ=72ポイント
    # したがって、A4の寸法はポイント単位で(842.4, 597.6)になります
    page.set_page_size(597.6, 842.4)

    # 更新されたドキュメントを保存
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "applicationCategory": "Python 用 PDF 操作ライブラリ",
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