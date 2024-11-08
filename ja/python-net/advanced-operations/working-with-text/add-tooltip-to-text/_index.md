---
title: PDF Tooltip using Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: /ja/python-net/pdf-tooltip/
description: PythonとAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学ぶ
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using Python",
    "alternativeHeadline": "Add PDF Tooltip to the Text",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf tooltip",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "PythonとAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学ぶ"
}
</script>


## 検索されたテキストにツールチップを追加するために不可視ボタンを追加

このコードは、Aspose.PDFを使用してPDFドキュメント内の特定のテキストフラグメントにツールチップを追加する方法を示しています。ツールチップは、対応するテキストの上にマウスカーソルを移動したときに表示されます。

以下のコードスニペットは、この機能を実現する方法を示します:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("ここにマウスカーソルを移動してツールチップを表示")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "ここにマウスカーソルを移動して非常に長いツールチップを表示"
        )
    )
    document.save(output_pdf)

    # テキストでドキュメントを開く
    document = ap.Document(output_pdf)
    # 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成
    absorber = ap.text.TextFragmentAbsorber(
        "ここにマウスカーソルを移動してツールチップを表示"
    )
    # ドキュメントページにアブソーバーを適用
    document.pages.accept(absorber)
    # 抽出されたテキストフラグメントを取得
    text_fragments = absorber.text_fragments

    # フラグメントをループ処理
    for fragment in text_fragments:
        # テキストフラグメントの位置に不可視ボタンを作成
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # alternate_nameの値はビューワーアプリケーションによってツールチップとして表示されます
        field.alternate_name = "テキストのツールチップ。"
        # フォームフィールドをドキュメントに追加
        document.form.add(field)

    # 次に非常に長いツールチップのサンプル
    absorber = ap.text.TextFragmentAbsorber(
        "ここにマウスカーソルを移動して非常に長いツールチップを表示"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # 非常に長いテキストを設定
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # ドキュメントを保存
    document.save(output_pdf)
```


## マウスオーバーで表示される隠しテキストブロックを作成する

このPythonコードスニペットは、特定のエリアにマウスカーソルを置いたときに表示されるフローティングテキストをPDFドキュメントに追加する方法を示しています。

まず、新しいPDFドキュメントが作成され、「ここにマウスカーソルを移動してフローティングテキストを表示」というテキストを含む段落が追加されます。その後、ドキュメントが保存されます。

次に、保存されたドキュメントが再度開かれ、以前に追加されたテキストフラグメントを見つけるためにTextAbsorberオブジェクトが作成されます。このテキストフラグメントは、フローティングテキストフィールドの位置と特性を定義するために使用されます。

TextBoxFieldオブジェクトが作成され、フローティングテキストフィールドを表し、その位置、値、読み取り専用状態、可視性などのプロパティが適切に設定されます。さらに、フィールドにはユニークな名前と外観の特性が割り当てられます。

フローティングテキストフィールドがドキュメントのフォームに追加され、元のテキストフラグメントの位置に見えないボタンフィールドが作成されます。
 HideActionイベントはボタンフィールドに割り当てられ、マウスカーソルがその近くに入ると浮動テキストフィールドが表示され、カーソルが出ると消えるように指定されています。

最後に、ボタンフィールドがドキュメントのフォームに追加され、修正されたドキュメントが保存されます。

このコードスニペットは、Aspose.PDF for Pythonを使用してPDFドキュメントにインタラクティブな浮動テキスト要素を作成する方法を提供します。

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("ここにマウスカーソルを移動して浮動テキストを表示")
    )
    document.save(output_pdf)

    # テキスト付きのドキュメントを開く
    document = ap.Document(output_pdf)
    # 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成
    absorber = ap.text.TextFragmentAbsorber(
        "ここにマウスカーソルを移動して浮動テキストを表示"
    )
    # ドキュメントページに対してアブソーバーを適用
    document.pages.accept(absorber)
    # 最初に抽出されたテキストフラグメントを取得
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # 指定されたページの矩形に浮動テキストのための隠しテキストフィールドを作成
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # フィールドの値として表示されるテキストを設定
    floating_field.value = 'これは「浮動テキストフィールド」です。'
    # このシナリオではフィールドを「読み取り専用」にすることをお勧めします
    floating_field.read_only = True
    # ドキュメントオープン時にフィールドを不可視にするために「隠し」フラグを設定
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # フィールド名を一意にすることは必要ありませんが、許可されています
    floating_field.partial_name = "FloatingField_1"

    # フィールドの外観の特性を設定することは必要ではありませんが、設定するとより良くなります
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # ドキュメントにテキストフィールドを追加
    document.form.add(floating_field)
    # テキストフラグメントの位置に見えないボタンを作成
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # 指定されたフィールド（注釈）と不可視フラグのための新しい隠しアクションを作成
    # （上で指定した名前で浮動フィールドを参照することもできます。）
    # 見えないボタンフィールドでマウスのエンター/エグジット時のアクションを追加

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # ドキュメントにボタンフィールドを追加
    document.form.add(button_field)

    # ドキュメントを保存
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
    "applicationCategory": "PDF操作ライブラリ for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>