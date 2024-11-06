---
title: PythonでPDFにテキストスタンプを追加
linktitle: PDFファイルにおけるテキストスタンプ
type: docs
weight: 20
url: ja/python-net/text-stamps-in-the-pdf-file/
description: Aspose.PDF for Pythonライブラリを使用してTextStampクラスでPDFドキュメントにテキストスタンプを追加します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PythonでPDFにテキストスタンプを追加",
    "alternativeHeadline": "PythonでPDFにテキストスタンプを追加",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, ドキュメント生成",
    "wordcount": "302",
    "proficiencyLevel":"初級",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Pythonライブラリを使用してTextStampクラスでPDFドキュメントにテキストスタンプを追加します。"
}
</script>


## Pythonでテキストスタンプを追加

[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスを使用して、PDFファイルにテキストスタンプを追加できます。[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) クラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。テキストスタンプを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、[add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) メソッドをPageに呼び出して、PDFにスタンプを追加できます。以下のコードスニペットは、PDFファイルにテキストスタンプを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # テキストスタンプを作成
    text_stamp = ap.TextStamp("Sample Stamp")
    # スタンプが背景かどうかを設定
    text_stamp.background = True
    # 原点を設定
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # スタンプを回転
    text_stamp.rotate = ap.Rotation.ON90
    # テキストプロパティを設定
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # 特定のページにスタンプを追加
    document.pages[1].add_stamp(text_stamp)

    # 出力ドキュメントを保存
    document.save(output_pdf)
```


## TextStampオブジェクトの配置を定義する

PDFドキュメントに透かしを追加することは、頻繁に要求される機能の一つであり、Aspose.PDF for Pythonは、画像やテキストの透かしを追加するための完全な機能を備えています。[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/)というクラスがあり、PDFファイルにテキストスタンプを追加する機能を提供しています。最近、TextStampオブジェクトを使用する際にテキストの配置を指定する機能をサポートする必要が出てきました。この要件を満たすために、[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/)クラスに[text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)プロパティを導入しました。このプロパティを使用して、[horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties)テキスト配置を指定できます。

次のコードスニペットは、既存のPDFドキュメントを読み込み、それにTextStampを追加する方法の例を示しています。

```python

    import aspose.pdf as ap

    # 入力ファイルでDocumentオブジェクトをインスタンス化
    doc = ap.Document(input_pdf)
    # サンプル文字列でFormattedTextオブジェクトをインスタンス化
    text = ap.facades.FormattedText("This")
    # FormattedTextに新しいテキスト行を追加
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # FormattedTextを使用してTextStampオブジェクトを作成
    stamp = ap.TextStamp(text)
    # テキストスタンプの水平配置を中央揃えに指定
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # テキストスタンプの垂直配置を中央揃えに指定
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # TextStampのテキスト水平配置を中央揃えに指定
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # スタンプオブジェクトの上部マージンを設定
    stamp.top_margin = 20
    # ドキュメントの最初のページにスタンプオブジェクトを追加
    doc.pages[1].add_stamp(stamp)

    # 更新されたドキュメントを保存
    doc.save(output_pdf)
```


## PDFファイルにスタンプとしての塗りつぶしストロークテキスト

テキストの追加と編集のシナリオに対するレンダリングモードの設定を実装しました。ストロークテキストをレンダリングするには、TextStateオブジェクトを作成して高度なプロパティを転送します。ストロークの色を設定します。その後、テキストレンダリングモードを設定します。次のステップはTextStateをバインドし、スタンプを追加することです。

次のコードスニペットは、塗りつぶしストロークテキストの追加を示しています:

```python

    import aspose.pdf as ap

    # 高度なプロパティを転送するTextStateオブジェクトを作成
    ts = ap.text.TextState()
    # ストロークの色を設定
    ts.stroking_color = ap.Color.gray
    # テキストレンダリングモードを設定
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # 入力PDFドキュメントを読み込む
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # TextStateをバインド
    stamp.bind_text_state(ts)
    # X,Yの原点を設定
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # スタンプを追加
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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
                "contactType": "セールス",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "セールス",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "セールス",
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