---
title: Pythonを使用してPDFにヘッダーとフッターを追加する
linktitle: PDFにヘッダーとフッターを追加
type: docs
weight: 50
url: /ja/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NETを使用して、TextStampクラスでPDFファイルにヘッダーとフッターを追加できます。
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFにヘッダーとフッターを追加する",
    "alternativeHeadline": "PDFファイルにヘッダーとフッターを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add header, add footer in pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NETを使用して、TextStampクラスでPDFファイルにヘッダーとフッターを追加できます。"
}
</script>


**Aspose.PDF for Python via .NET**は、既存のPDFファイルにヘッダーとフッターを追加することができます。PDFドキュメントに画像やテキストを追加することができます。また、Pythonを使用して1つのPDFファイルに異なるヘッダーを追加してみてください。

## PDFファイルのヘッダーにテキストを追加する

[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/)クラスを使用して、PDFファイルのヘッダーにテキストを追加することができます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するためには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、Pageの'add_stamp'メソッドを呼び出して、PDFのヘッダーにテキストを追加することができます。

PDFのヘッダーエリアにテキストを調整するように[top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)プロパティを設定する必要があります。また、'horizontal_alignment'をCenterに、'vertical_alignment'をTopに設定する必要があります。

以下のコードスニペットは、Pythonを使用してPDFファイルのヘッダーにテキストを追加する方法を示しています：

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ヘッダーを作成
    textStamp = ap.TextStamp("Header Text")
    # スタンプのプロパティを設定
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # すべてのページにヘッダーを追加
    for page in document.pages:
        page.add_stamp(textStamp)

    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

## PDFファイルのフッターにテキストを追加する

[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスを使用して、PDFファイルのフッターにテキストを追加できます。
 TextStamp クラスは、フォントサイズ、フォントスタイル、フォントカラーなどのテキストベースのスタンプを作成するために必要なプロパティを提供します。フッターにテキストを追加するためには、必要なプロパティを使用して Document オブジェクトと TextStamp オブジェクトを作成する必要があります。その後、PDF のフッターにテキストを追加するために、Page の 'add_stamp' メソッドを呼び出すことができます。

以下のコードスニペットは、Python を使用して PDF ファイルのフッターにテキストを追加する方法を示しています:

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # フッターを作成
    textStamp = ap.TextStamp("フッターテキスト")
    # スタンプのプロパティを設定
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # すべてのページにフッターを追加
    for page in document.pages:
        page.add_stamp(textStamp)

    # 更新されたPDFファイルを保存
    document.save(output_pdf)
```

## PDFファイルのヘッダーに画像を追加する

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスを使用して、PDF ファイルのヘッダーに画像を追加することができます。 Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなどの画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PDFのヘッダーに画像を追加するためにPageの'add_stamp'メソッドを呼び出すことができます。

次のコードスニペットは、PythonでPDFファイルのヘッダーに画像を追加する方法を示しています:

```python 

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ヘッダーを作成
    image_stamp = ap.ImageStamp(input_image)
    # スタンプのプロパティを設定
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # すべてのページにヘッダーを追加
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

## PDFファイルのフッターに画像を追加

[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/)クラスを使用してPDFファイルのフッターに画像を追加できます。 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) クラスは、フォントサイズ、フォントスタイル、フォントカラーなどの画像ベースのスタンプを作成するために必要なプロパティを提供します。フッターに画像を追加するためには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PDFのフッターに画像を追加するために、Pageの'add_stamp'メソッドを呼び出すことができます。

次のコードスニペットは、PythonでPDFファイルのフッターに画像を追加する方法を示しています:

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # フッターを作成
    image_stamp = ap.ImageStamp(input_image)
    # スタンプのプロパティを設定
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # すべてのページにフッターを追加
    for page in document.pages:
        page.add_stamp(image_stamp)

    # 更新されたPDFファイルを保存
    document.save(output_pdf)
```

## 1つのPDFファイルに異なるヘッダーを追加する

ドキュメントのヘッダー/フッターセクションにTextStampを追加できることは、[top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)または[bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)プロパティを使用することでわかっていますが、時には単一のPDFドキュメントに複数のヘッダー/フッターを追加する必要がある場合があります。**Aspose.PDF for Python via .NET**はその方法を説明しています。

この要件を達成するために、個々のTextStampオブジェクト（必要なヘッダー/フッターの数に応じたオブジェクトの数）を作成し、それらをPDFドキュメントに追加します。
 我々はまた、個々のスタンプオブジェクトに異なるフォーマット情報を指定することもできます。次の例では、Documentオブジェクトと3つのTextStampオブジェクトを作成し、ページの'add_stamp'メソッドを使用してPDFのヘッダーセクションにテキストを追加しました。以下のコードスニペットは、Aspose.PDF for Pythonを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```python

    import aspose.pdf as ap

    # 3つのスタンプを作成
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # スタンプの配置を設定（ページ上部に配置、水平中央揃え）
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # フォントスタイルをボールドに指定
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # テキストの前景色情報を赤に設定
    stamp1.text_state.foreground_color = ap.Color.red
    # フォントサイズを14に指定
    stamp1.text_state.font_size = 14

    # 次に、2番目のスタンプオブジェクトの垂直配置を上部に設定
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # スタンプの水平配置情報を中央揃えに設定
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # スタンプオブジェクトのズーム係数を設定
    stamp2.zoom = 10

    # 3番目のスタンプオブジェクトのフォーマットを設定
    # スタンプオブジェクトの垂直配置情報を上部に指定
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # スタンプオブジェクトの水平配置情報を中央揃えに設定
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # スタンプオブジェクトの回転角度を設定
    stamp3.rotate_angle = 35
    # スタンプの背景色をピンクに設定
    stamp3.text_state.background_color = ap.Color.pink
    # スタンプのフォントの種類をVerdanaに変更
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # 最初のスタンプは最初のページに追加されます
    document.pages[1].add_stamp(stamp1)
    # 2番目のスタンプは2ページ目に追加されます
    document.pages[2].add_stamp(stamp2)
    # 3番目のスタンプは3ページ目に追加されます
    document.pages[3].add_stamp(stamp3)

    # 更新されたドキュメントを保存
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