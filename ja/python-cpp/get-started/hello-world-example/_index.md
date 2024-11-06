---
title: Python言語を使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
weight: 20
url: ja/python-cpp/hello-world-example/
description: このサンプルは、Aspose.PDF for Pythonを使用してシンプルなPDF「Hello, World!」ドキュメントを作成する方法を示しています。
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python言語を使用したHello Worldの例",
    "alternativeHeadline": "Aspose.PDF Python (via C++) の例",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf文書生成",
    "keywords": "pdf, Python, 文書生成",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "このサンプルは、Aspose.PDF for Pythonを使用してシンプルなPDFドキュメントを作成する方法を示しています。",
    "articleBody": "シンプルなユースケースは、プログラミング言語やソフトウェアの機能を示すのに役立ちます。これは通常、「Hello World」例で行われます。\n\nAspose.PDF for Python via C++は、開発者がPythonアプリケーションでPDFドキュメントを作成、操作、変換することを可能にする強力なPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX、画像ファイル形式など、さまざまなファイル形式の操作をサポートしています。この記事では、Aspose.PDF APIを使用して「Hello World!」というテキストを含むPDFドキュメントを作成する方法を示します。以下のコードサンプルを実行する前に、環境にAspose.PDF for Python via C++をインストールする必要があります。\n1. AsposePdfPythonモジュールをインポートします。\n2. document_create関数を使用して新しいPDFドキュメントオブジェクトを作成します。\n3. document_get_pages関数を使用してドキュメントのページコレクションを取得します。\n4. page_collection_add_page関数を使用してページコレクションに新しいページを追加します。\n5. page_get_paragraphs関数を使用してページの段落コレクションを取得します。\n6. image_create関数を使用して新しい画像オブジェクトを作成します。\n7. image_set_file関数を使用して画像オブジェクトのファイル名を「sample.jpg」に設定します。\n8. paragraphs_add_image関数を使用して段落コレクションに画像オブジェクトを追加します。\n9. document_save関数を使用してドキュメントを「document.pdf」という名前のファイルに保存します。\n10. close_handle関数を使用してドキュメントハンドルを閉じます。"
}
</script>


A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.

プログラミング言語やソフトウェアの機能を示すのに、簡単なユースケースが役立ちます。これは通常、「Hello World」の例で行われます。

Aspose.PDF for Python via C++ is a powerful PDF API that enables the developers to create, manipulate and convert PDF documents in their Python applications. It supports working with various file formats such as PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we will show you how to create a PDF document with the text "Hello World!" using Aspose.PDF API. You need to install Aspose.PDF for Python via C++ in your environment before running the following code sample.

Aspose.PDF for Python via C++ は、開発者がPythonアプリケーションでPDFドキュメントを作成、操作、および変換することを可能にする強力なPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX、および画像ファイル形式など、さまざまなファイル形式を扱うことをサポートしています。この記事では、Aspose.PDF API を使用して「Hello World!」というテキストを含むPDFドキュメントを作成する方法を紹介します。以下のコードサンプルを実行する前に、環境にAspose.PDF for Python via C++ をインストールする必要があります。

1. Import the `AsposePdfPython` module.
1. Create a new PDF document object using the `document_create` function.
1. Get the pages collection of the document using the `document_get_pages` function.
1. Add a new page to the pages collection using the `page_collection_add_page` function.

1. `AsposePdfPython` モジュールをインポートします。
1. `document_create` 関数を使用して、新しいPDFドキュメントオブジェクトを作成します。
1. `document_get_pages` 関数を使用して、ドキュメントのページコレクションを取得します。
1. `page_collection_add_page` 関数を使用して、ページコレクションに新しいページを追加します。

1. `page_get_paragraphs` 関数を使用してページの段落コレクションを取得します。
1. `image_create` 関数を使用して新しい画像オブジェクトを作成します。
1. `image_set_file` 関数を使用して画像オブジェクトのファイル名を "sample.jpg" に設定します。
1. `paragraphs_add_image` 関数を使用して画像オブジェクトを段落コレクションに追加します。
1. `document_save` 関数を使用してドキュメントを "document.pdf" という名前のファイルに保存します。
1. `close_handle` 関数を使用してドキュメントハンドルを閉じます。

次のコードスニペットは、Aspose.PDF for Python via C++ がどのように動作するかを示す Hello World プログラムです。

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```