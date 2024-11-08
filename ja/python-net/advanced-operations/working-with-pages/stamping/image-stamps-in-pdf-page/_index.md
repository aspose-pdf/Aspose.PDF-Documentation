---
title: Pythonを使用してPDFに画像スタンプを追加する
linktitle: PDFファイルに画像スタンプ
type: docs
weight: 10
url: /ja/python-net/image-stamps-in-pdf-page/
description: ImageStampクラスを使用して、Aspose.PDF for PythonライブラリでPDFドキュメントに画像スタンプを追加します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFに画像スタンプを追加する",
    "alternativeHeadline": "Pythonを使用してPDFに画像スタンプを追加する",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "ImageStampクラスを使用して、Aspose.PDF for PythonライブラリでPDFドキュメントに画像スタンプを追加します。"
}
</script>


## PDFファイルに画像スタンプを追加する

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/)クラスを使用して、PDFファイルに画像スタンプを追加できます。[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/)クラスは、高さ、幅、不透明度など、画像ベースのスタンプを作成するために必要なプロパティを提供します。

画像スタンプを追加するには:

1. 必要なプロパティを使用して、DocumentオブジェクトとImageStampオブジェクトを作成します。
2. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)クラスの[add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)メソッドを呼び出して、スタンプをPDFに追加します。

以下のコードスニペットは、PDFファイルに画像スタンプを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 画像スタンプを作成
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # 特定のページにスタンプを追加
    document.pages[1].add_stamp(image_stamp)

    # 出力ドキュメントを保存
    document.save(output_pdf)
```


## スタンプを追加する際の画像品質の制御

画像をスタンプオブジェクトとして追加する際に、画像の品質を制御できます。[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスの [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) プロパティはこの目的で使用されます。これは画像の品質をパーセントで示します（有効な値は0..100）。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 画像スタンプを作成
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # 特定のページにスタンプを追加
    document.pages[1].add_stamp(image_stamp)

    # 出力ドキュメントを保存
    document.save(output_pdf)
```

## フローティングボックス内の背景としての画像スタンプ

Aspose.PDF for Python APIを使用すると、フローティングボックス内の背景として画像スタンプを追加できます。
 [背景](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties)プロパティは、以下のコードサンプルに示されているように、フローティングボックスの背景画像スタンプを設定するために使用できます。

```python

    import aspose.pdf as ap

    # Documentオブジェクトをインスタンス化
    document = ap.Document()
    # PDFドキュメントにページを追加
    page = document.pages.add()
    # FloatingBoxオブジェクトを作成
    box = ap.FloatingBox(200.0, 100.0)
    # FloatingBoxの左位置を設定
    box.left = 40
    # FloatingBoxの上位置を設定
    box.top = 80
    # FloatingBoxの水平配置を設定
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # FloatingBoxの段落コレクションにテキストフラグメントを追加
    box.paragraphs.add(ap.text.TextFragment("メインテキスト"))
    # FloatingBoxの境界線を設定
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # 背景画像を追加
    box.background_image = img
    # FloatingBoxの背景色を設定
    box.background_color = ap.Color.yellow
    # ページオブジェクトの段落コレクションにFloatingBoxを追加
    page.paragraphs.add(box)
    # PDFドキュメントを保存
    document.save(output_pdf)
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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
    "applicationCategory": "Python用PDF操作ライブラリ",
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