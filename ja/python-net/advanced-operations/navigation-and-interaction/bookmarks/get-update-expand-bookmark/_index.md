---
title: Pythonを使用してブックマークを取得、更新、展開する
linktitle: ブックマークを取得、更新、展開する
type: docs
weight: 20
url: /ja/python-net/get-update-and-expand-bookmark/
description: この記事では、Aspose.PDF for Pythonライブラリを使用してPDFファイル内のブックマークを操作する方法について説明します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してブックマークを取得、更新、展開する",
    "alternativeHeadline": "PDFファイルからブックマークを取得する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, get bookmarks",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "この記事では、Aspose.PDF for Pythonライブラリを使用してPDFファイル内のブックマークを操作する方法について説明します。"
}
</script>


## ブックマークを取得する

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションには、PDF ファイルのすべてのブックマークが含まれています。この記事では、PDF ファイルからブックマークを取得する方法と、特定のブックマークがどのページにあるかを取得する方法について説明します。

ブックマークを取得するには、[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションをループして、OutlineItemCollection 内の各ブックマークを取得します。[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) は、すべてのブックマークの属性へのアクセスを提供します。次のコードスニペットは、PDF ファイルからブックマークを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # すべてのブックマークをループする
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## ブックマークのページ番号を取得する

ブックマークを追加したら、Bookmarkオブジェクトに関連付けられた宛先のPageNumberを取得することで、そのブックマークがどのページにあるかを確認できます。

```python

    import aspose.pdf as ap

    # PdfBookmarkEditorを作成
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # PDFファイルを開く
    bookmarkEditor.bind_pdf(input_pdf)
    # ブックマークを抽出
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "タイトル:", bookmark.title)
        print(str_level_seprator, "ページ番号:", bookmark.page_number)
        print(str_level_seprator, "ページアクション:", bookmark.action)
```

## PDFドキュメントから子ブックマークを取得する

ブックマークは、親と子を持つ階層構造で整理することができます。
 ドキュメント内のすべてのブックマークを取得するには、Document オブジェクトの Outlines コレクションをループします。ただし、子ブックマークも取得するには、最初のループで取得された各 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) オブジェクト内のすべてのブックマークもループします。以下のコードスニペットは、PDF ドキュメントから子ブックマークを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # すべてのブックマークをループする
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("子ブックマーク")
            # 子ブックマークがある場合はそれもループする
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDFドキュメントのブックマークを更新する

PDFファイルのブックマークを更新するには、まずブックマークのインデックスを指定して、DocumentオブジェクトのOutlineCollectionコレクションから特定のブックマークを取得します。[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)オブジェクトにブックマークを取得したら、そのプロパティを更新し、Saveメソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、PDFドキュメントのブックマークを更新する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ブックマークオブジェクトを取得
    outline = document.outlines[1]

    # 子ブックマークオブジェクトを取得
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # 保存する
    document.save(output_pdf)
```

## ドキュメントを表示する際に展開されたブックマーク

ブックマークは、Documentオブジェクトの[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)コレクションに保持されており、これは[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/)コレクション内にあります。
 しかし、PDFファイルを表示する際にすべてのブックマークを展開しておく必要がある場合があります。

この要件を達成するために、各アウトライン/ブックマーク項目のオープンステータスをOpenとして設定できます。次のコードスニペットは、PDFドキュメント内の各ブックマークを展開された状態に設定する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ページ表示モードを設定、サムネイル表示、フルスクリーン、添付ファイルパネルの表示など
    document.page_mode = ap.PageMode.USE_OUTLINES
    # PDFファイルのアウトラインコレクション内の各アウトライン項目を巡回
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # アウトライン項目のオープンステータスを設定
        item.open = True

    # 出力を保存
    document.save(output_pdf)
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