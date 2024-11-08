---
title: AcroFormを抽出 - PythonでPDFからフォームデータを抽出
linktitle: AcroFormを抽出
type: docs
weight: 30
url: /ja/python-net/extract-form/
keywords: extract form data from pdf python
description: Aspose.PDF for Pythonライブラリを使用して、PDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "AcroFormを抽出",
    "alternativeHeadline": "PythonでPDFからAcroFormを抽出する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, acroformを抽出",
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
            "https://www.youtube.com/@AsposePDF",
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
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Pythonライブラリを使用して、PDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。"
}
</script>


## フォームからデータを抽出する

### PDFドキュメントのすべてのフィールドから値を取得する

PDFドキュメントのすべてのフィールドから値を取得するには、すべてのフォームフィールドをナビゲートし、Valueプロパティを使用して値を取得する必要があります。フォームコレクションから各フィールドを取得し、[Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/)と呼ばれる基本フィールドタイプでその[value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties)プロパティにアクセスします。

以下のPythonコードスニペットは、PDFドキュメントからすべてのフィールドの値を取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    pdfDocument = ap.Document(input_file)

    # すべてのフィールドから値を取得する
    for formField in pdfDocument.form.fields:
        # 必要に応じて名前と値を分析する
        print("フィールド名 : " + formField.partial_name)
        print("値 : " + str(formField.value))
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
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