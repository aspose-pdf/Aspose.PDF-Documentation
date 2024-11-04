---
title: Pythonを使用してPDFでポートフォリオを作成する
linktitle: ポートフォリオ
type: docs
weight: 20
url: /python-net/portfolio/
description: Pythonを使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Wordドキュメント、画像ファイルを使用してPDFポートフォリオを作成する必要があります。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFでポートフォリオを作成する",
    "alternativeHeadline": "PDFドキュメントでポートフォリオを作成",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, ポートフォリオ",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Pythonを使用してPDFポートフォリオを作成する方法。Microsoft Excelファイル、Wordドキュメント、画像ファイルを使用してPDFポートフォリオを作成する必要があります。"
}
</script>


PDFポートフォリオを作成することで、さまざまな種類のファイルを1つの一貫したドキュメントにまとめてアーカイブすることができます。このようなドキュメントには、テキストファイル、画像、スプレッドシート、プレゼンテーション、およびその他の資料が含まれる可能性があり、関連するすべての資料が1か所に保存され、整理されていることを保証します。

PDFポートフォリオは、どこで使用しても高品質な方法でプレゼンテーションを表示するのに役立ちます。一般的に、PDFポートフォリオを作成することは非常に現在的でモダンなタスクです。

## PDFポートフォリオの作成方法

Aspose.PDF for Python via .NETを使用すると、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスを使用してPDFポートフォリオドキュメントを作成できます。[FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/)クラスを使用して取得した後、ファイルをdocument.collectionオブジェクトに追加します。ファイルが追加されたら、Documentクラスの[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用してポートフォリオドキュメントを保存します。

以下の例では、Microsoft Excelファイル、Wordドキュメント、および画像ファイルを使用してPDFポートフォリオを作成します。

以下のコードは次のポートフォリオを生成します。

### Aspose.PDF for Pythonを使用して作成されたPDFポートフォリオ

![Aspose.PDF for Pythonを使用して作成されたPDFポートフォリオ](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # ドキュメントオブジェクトをインスタンス化
    document = ap.Document()

    # ドキュメントコレクションオブジェクトをインスタンス化
    document.collection = ap.Collection()

    # ポートフォリオに追加するファイルを取得
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # ファイルの説明を提供
    excel.description = "Excel ファイル"
    word.description = "Word ファイル"
    image.description = "画像ファイル"

    # ファイルをドキュメントコレクションに追加
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # ポートフォリオドキュメントを保存
    document.save(output_pdf)
```

## PDFポートフォリオからファイルを削除

PDFポートフォリオからファイルを削除するには、次のコード行を使用してみてください。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    document.collection.delete()

    # 更新されたファイルを保存
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