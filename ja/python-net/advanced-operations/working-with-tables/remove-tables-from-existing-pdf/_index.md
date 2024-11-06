---
title: 既存のPDFからテーブルを削除する
linktitle: テーブルを削除
type: docs
weight: 50
url: ja/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "既存のPDFからテーブルを削除する",
    "alternativeHeadline": "PDFからテーブルを削除する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, テーブル削除, テーブルを削除する",
    "wordcount": "302",
    "proficiencyLevel":"初級者",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF for Python via .NETは、PDFドキュメントが最初から生成される際に、ドキュメント内にテーブルを挿入または作成する機能を提供します。また、既存のPDFドキュメントにテーブルオブジェクトを追加することもできます。ただし、既存のテーブルセルの内容を更新できる[既存のPDF内のテーブルを操作する](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/)必要があるかもしれません。しかし、既存のPDFドキュメントからテーブルオブジェクトを削除する必要がある場合もあります。

{{% /alert %}}

テーブルを削除するためには、既存のPDF内のテーブルを取得するために[TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/)クラスを使用し、それから[remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods)を呼び出す必要があります。

## PDFドキュメントからテーブルを削除

新しい関数を追加しました。すなわち、
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) を既存の [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) クラスに追加して、PDF ドキュメントからテーブルを削除します。アブソーバーがページ上でテーブルを正常に検出すると、それらを削除できるようになります。以下のコードスニペットを確認して、PDF ドキュメントからテーブルを削除する方法を示します。

```python

    import aspose.pdf as ap

    # 既存のPDFドキュメントを読み込む
    pdf_document = ap.Document(input_file)
    # テーブルを見つけるためにTableAbsorberオブジェクトを作成する
    absorber = ap.text.TableAbsorber()
    # アブソーバーで最初のページを訪問する
    absorber.visit(pdf_document.pages[1])
    # ページ上の最初のテーブルを取得する
    table = absorber.table_list[0]
    # テーブルを削除する
    absorber.remove(table)
    # PDFを保存する
    pdf_document.save(output_file)
```

## PDF ドキュメントから複数のテーブルを削除する

時々、PDF ドキュメントには複数のテーブルが含まれていることがあり、それらを削除する必要が出てくることがあります。 複数のテーブルをPDFドキュメントから削除するためには、以下のコードスニペットを使用してください：

```python

    import aspose.pdf as ap

    # 既存のPDFドキュメントを読み込む
    pdf_document = ap.Document(input_file)
    # テーブルを見つけるためのTableAbsorberオブジェクトを作成
    absorber = ap.text.TableAbsorber()
    # アブソーバーで2ページ目を訪問
    absorber.visit(pdf_document.pages[1])
    # テーブルコレクションのコピーを取得
    tables = absorber.table_list
    # コレクションのコピーをループし、テーブルを削除
    for table in tables:
        absorber.remove(table)
    # ドキュメントを保存
    pdf_document.save(output_file)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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