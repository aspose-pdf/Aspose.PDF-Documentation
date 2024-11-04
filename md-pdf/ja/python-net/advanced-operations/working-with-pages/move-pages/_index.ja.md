---
title: Pythonを使用してPDFページをプログラムで移動
linktitle: PDFページの移動
type: docs
weight: 100
url: /python-net/move-pages/
description: Aspose.PDF for Python via .NETを使用して、PDFファイル内の任意の場所または末尾にページを移動してみてください。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFページをプログラムで移動",
    "alternativeHeadline": "PythonでPDFページを移動する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, move pdf page",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python via .NETを使用して、PDFファイル内の任意の場所または末尾にページを移動してみてください。"
}
</script>


## PDFドキュメントから別のPDFドキュメントへのページの移動

このトピックでは、Pythonを使用して、あるPDFドキュメントから別のドキュメントの末尾にページを移動する方法を説明します。
ページを移動するには、次の手順を実行します：

1. ソースPDFファイルを使用して[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスオブジェクトを作成します。
1. 目的のPDFファイルを使用して[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションからページを取得します。
1. 目的のドキュメントにページを[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用して出力PDFを保存します。
1. ソースドキュメントのページを[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します。

1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用してソースPDFを保存します。

次のコードスニペットは、1ページを移動する方法を示しています。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # 出力ファイルを保存
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## 複数のページをあるPDFドキュメントから別のドキュメントに移動

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスオブジェクトを作成します。
1. 宛先PDFファイルで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスオブジェクトを作成します。
1. 移動するページ番号を指定した配列を定義します。
1. 配列をループ処理します:

1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションからページを取得します。
1. 目的のドキュメントにページを[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して出力PDFを保存します。
1. 配列を使用してソース ドキュメント内のページを[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用してソースPDFを保存します。

次のコードスニペットは、PDFファイルの最後に空のページを挿入する方法を示しています。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # 出力ファイルを保存
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## 現在のPDFドキュメント内でページを新しい場所に移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)コレクションからページを取得します。
1. ページを新しい場所に[add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します（例えば、最後に追加）。
1. 以前の場所からページを[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用して出力PDFを保存します。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # 出力ファイルを保存
    srcDocument.save(output_pdf)
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
    "applicationCategory": "PDF Manipulation Library for Python",
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