---
title: PythonでPDFにページを追加
linktitle: ページを追加
type: docs
weight: 10
url: /python-net/add-pages/
description: この記事では、PDFファイルの希望の場所にページを挿入（追加）する方法を教えます。C#を使用して、PDFファイルからページを移動、削除（削除）する方法を学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PythonでPDFにページを追加",
    "alternativeHeadline": "PDFドキュメントにページを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf page, insert pdf page",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、PDFファイルの希望の場所にページを挿入（追加）する方法を教えます。Pythonを使用して、PDFファイルからページを移動、削除（削除）する方法を学びます。"
}
</script>


Aspose.PDF for Python via .NET APIは、Pythonを使用してPDFドキュメント内のページを操作するための完全な柔軟性を提供します。PDFドキュメントのすべてのページを[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)で管理し、PDFページを操作するために使用できます。  
Aspose.PDF for Python via .NETを使用すると、ファイル内の任意の場所にページを挿入したり、PDFファイルの末尾にページを追加したりできます。このセクションでは、Pythonを使用してPDFにページを追加する方法を示します。

## PDFファイルにページを追加または挿入する

Aspose.PDF for Python via .NETを使用すると、ファイル内の任意の場所にページを挿入したり、PDFファイルの末尾にページを追加したりできます。

### 希望の場所に空のページをPDFファイルに挿入する

PDFファイルに空のページを挿入するには：

1. 入力PDFファイルを使用して[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスオブジェクトを作成します。

1. 指定されたインデックスで[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションの[insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert)メソッドを呼び出します。
1. [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # PDFに空白ページを挿入する
    document.pages.insert(2)
    # 出力ファイルを保存する
    document.save(output_pdf)
```

### PDFファイルの末尾に空白ページを追加する

時々、ドキュメントが空白ページで終わることを確認したいことがあります。このトピックでは、PDFドキュメントの末尾に空白ページを挿入する方法を説明します。

PDFファイルの末尾に空白ページを挿入するには:

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスオブジェクトを作成します。

1. パラメーターなしで[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションの[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)メソッドを呼び出します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの末尾に空のページを挿入する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # PDFファイルの末尾に空のページを挿入
    document.pages.add()

    # 出力ファイルを保存
    document.save(output_pdf)