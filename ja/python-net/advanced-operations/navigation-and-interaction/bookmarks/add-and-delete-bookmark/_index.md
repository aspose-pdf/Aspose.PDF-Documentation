---
title: Pythonを使用してブックマークを追加および削除する
linktitle: ブックマークを追加および削除する
type: docs
weight: 10
url: ja/python-net/add-and-delete-bookmark/
description: Pythonを使用してPDFドキュメントにブックマークを追加できます。PDFドキュメントからすべてまたは特定のブックマークを削除することができます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ブックマークを追加および削除する",
    "alternativeHeadline": "PDFからブックマークを追加および削除する方法",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, ブックマークを削除, ブックマークを追加",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Pythonを使用してPDFドキュメントにブックマークを追加できます。PDFドキュメントからすべてまたは特定のブックマークを削除することができます。"
}
</script>


## PDFドキュメントにブックマークを追加する

ブックマークは、[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)コレクション内のDocumentオブジェクトに保持されており、[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/)コレクションにも含まれています。

PDFにブックマークを追加するには:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトを使用してPDFドキュメントを開きます。
2. ブックマークを作成し、そのプロパティを定義します。
3. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)コレクションをアウトラインコレクションに追加します。

以下のコードスニペットは、PDFドキュメントにブックマークを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # ブックマークオブジェクトを作成
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "テストブックマーク"
    outline.italic = True
    outline.bold = True
    # 移動先のページ番号を設定
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # ドキュメントのアウトラインコレクションにブックマークを追加
    document.outlines.append(outline)

    # 出力を保存
    document.save(output_pdf)
```


## PDFドキュメントに子ブックマークを追加する

ブックマークは入れ子にでき、親ブックマークと子ブックマークの階層関係を示します。この記事では、PDFに子ブックマーク、つまり第2レベルのブックマークを追加する方法を説明します。

PDFファイルに子ブックマークを追加するには、まず親ブックマークを追加します。

1. ドキュメントを開く。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) にブックマークを追加し、そのプロパティを定義する。
1. Documentオブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションに OutlineItemCollection を追加する。

子ブックマークは上記で説明した親ブックマークと同様に作成されますが、親ブックマークのアウトラインコレクションに追加されます。

以下のコードスニペットは、PDFドキュメントに子ブックマークを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 親ブックマークオブジェクトを作成する
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # 子ブックマークオブジェクトを作成する
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # 親ブックマークのコレクションに子ブックマークを追加する
    outline.append(childOutline)
    # ドキュメントのアウトラインコレクションに親ブックマークを追加する。
    document.outlines.append(outline)

    # 出力を保存する
    document.save(output_pdf)
```


## PDFドキュメントからすべてのブックマークを削除

PDF内のすべてのブックマークは、[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションに保持されています。この記事では、PDFファイルからすべてのブックマークを削除する方法を説明します。

PDFファイルからすべてのブックマークを削除するには:

1. [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) コレクションの Delete メソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して、変更されたファイルを保存します。

次のコードスニペットは、PDFドキュメントからすべてのブックマークを削除する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # すべてのブックマークを削除
    document.outlines.delete()

    # 更新されたファイルを保存
    document.save(output_pdf)

```

## PDFドキュメントから特定のブックマークを削除

PDFファイルから特定のブックマークを削除するには:

1. ブックマークのタイトルをパラメータとして[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/)コレクションのDeleteメソッドに渡します。
1. その後、更新されたファイルをDocumentオブジェクトのSaveメソッドで保存します。

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスは[OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/)コレクションを提供します。[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods)メソッドは、メソッドに渡されたタイトルのブックマークを削除します。

次のコードスニペットは、PDFドキュメントから特定のブックマークを削除する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # タイトルで特定のアウトラインを削除
    document.outlines.delete("Child Outline")

    # 更新されたファイルを保存
    document.save(output_pdf)