---
title: Pythonを使用してPDFを作成する方法
linktitle: PDFドキュメントの作成
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Aspose.PDF for Python via .NETを使用してPDFドキュメントを作成およびフォーマットします。
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFを作成する方法",
    "alternativeHeadline": "Pythonを使用してゼロからPDFドキュメントを作成する",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, dotnet, pdfドキュメントの作成",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NETを使用してPDFドキュメントを作成およびフォーマットします。"
}
</script>


**Aspose.PDF for Python via .NET** は、開発者がPython for .NETアプリケーションから直接PDFファイルを作成、読み込み、変更、変換するための数行のコードで操作できるPDF操作APIです。

## シンプルなPDFファイルの作成方法

Aspose.PDFを使用してPython経由で.NETでPDFを作成するには、次の手順に従います:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成する
1. Documentオブジェクトの [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) コレクションに [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトを追加する
1. ページの [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) コレクションに [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を追加する
1. 結果のPDFドキュメントを保存する

```python

    import aspose.pdf as ap

    # ドキュメントオブジェクトを初期化
    document = ap.Document()
    # ページを追加
    page = document.pages.add()
    # 新しいページにテキストを追加
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # 更新されたPDFを保存
    document.save(output_pdf)
```