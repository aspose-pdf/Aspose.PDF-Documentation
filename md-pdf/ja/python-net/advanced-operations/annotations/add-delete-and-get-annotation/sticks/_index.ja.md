---
title: PDF スティッキー注釈を Python で使用する
linktitle: スティッキー注釈
type: docs
weight: 50
url: /python-net/sticky-annotations/
description: このトピックはスティッキー注釈についてであり、例としてテキストにウォーターマーク注釈を示します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF スティッキー注釈を Python で使用する",
    "alternativeHeadline": "PDF にスティッキー注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf ドキュメント生成",
    "keywords": "pdf, python, スティッキー注釈, ウォーターマーク注釈",
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
    "url": "/python-net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/sticky-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "このトピックはスティッキー注釈についてであり、Python ライブラリを使用してテキストにウォーターマーク注釈を示します。"
}
</script>


## ウォーターマーク注釈を追加

最も目に見えて視覚化しやすく伝達しやすいのがウォーターマーク注釈です。これは、PDFドキュメントにロゴやその独自性を確認するための他のサインを配置するための最良の方法です。

ウォーターマーク注釈は、印刷されるページの寸法に関わらず、固定サイズおよび位置でページに印刷されるべきグラフィックスを表現するために使用されます。

[WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) を使用して、PDFページの特定の位置にウォーターマークテキストを追加できます。ウォーターマークの不透明度も [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) プロパティを使用して制御できます。

ウォーターマーク注釈を追加するには、次のコードスニペットを確認してください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # 注釈を作成
    # 注釈を追加するためにページオブジェクトを読み込む
    page = document.pages[1]

    # 注釈を作成
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # ページの注釈コレクションに注釈を追加
    page.annotations.append(wa)

    # フォント設定のためのTextStateを作成
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # 注釈テキストの不透明度レベルを設定
    wa.opacity = 0.5

    # 注釈にテキストを追加
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```


## ウォーターマーク注釈を取得する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## ウォーターマーク注釈を削除する

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
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