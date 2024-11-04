---
title: PythonでPDFページを操作する
linktitle: ページの操作
type: docs
weight: 20
url: /python-net/working-with-pages/
description: ページを追加したり、ヘッダーとフッターを追加したり、ウォーターマークを追加したりする方法をこのセクションで知ることができます。Aspose.PDF for Python via .NETがこのトピックに関するすべての詳細を説明します。
lastmod: "2023-04-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PythonでPDFページを操作する",
    "alternativeHeadline": "PDFページを操作する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf ドキュメント生成",
    "keywords": "pdf, python, pdfページ, pdfページを追加, ページ番号を追加, ページを回転, ページを削除",
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
    "url": "/python-net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-pages/"
    },
    "dateModified": "2023-02-04",
    "description": "ページを追加したり、ヘッダーとフッターを追加したり、ウォーターマークを追加したりする方法をこのセクションで知ることができます。Aspose.PDF for Python via .NETがこのトピックに関するすべての詳細を説明します。"
}
</script>


**Aspose.PDF for Python via .NET**を使用すると、PDFドキュメントにページをファイル内の任意の場所に挿入したり、PDFファイルの末尾にページを追加したりできます。このセクションでは、Acrobat Readerを使用せずにPDFにページを追加する方法を示します。AsposeのPythonライブラリを使用して、PDFファイルのヘッダーとフッターにテキストや画像を追加し、ドキュメント内で異なるヘッダーを選択できます。また、Pythonを使用してプログラム的にPDFドキュメントのページをトリミングしてみてください。

このセクションでは、Artifactクラスを使用してPDFファイルに透かしを追加する方法を学びます。このタスクのプログラミングサンプルを確認します。[PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)クラスを使用してページ番号を追加します。ドキュメントにスタンプを追加するには、[ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/)および[TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/)クラスを使用します。**Aspose.PDF for Python via .NET**を使用して、PDFファイルに背景画像を作成するための透かしを追加します。


You are able to do the following:

- [ページを追加する](/pdf/python-net/add-pages/) - PDFファイルの任意の場所または末尾にページを追加し、ドキュメントからページを削除します。
- [ページを移動する](/pdf/python-net/move-pages/) - ページを他のドキュメントに移動します。
- [ページを削除する](/pdf/python-net/delete-pages/) - PageCollectionコレクションを使用してPDFファイルからページを削除します。
- [ページサイズを変更する](/pdf/python-net/change-page-size/) - Aspose.PDFライブラリを使用してコードスニペットでPDFページのサイズを変更できます。
- [ページを回転する](/pdf/python-net/rotate-pages/) - 既存のPDFファイルのページの向きを変更できます。
- [ページを分割する](/pdf/python-net/split-document/) - PDFファイルを1つまたは複数のPDFに分割できます。
- [ヘッダーやフッターを追加する](/pdf/python-net/add-headers-and-footers-of-pdf-file/) - PDFファイルのヘッダーとフッターにテキストや画像を追加します。
- [ページをトリミングする](/pdf/python-net/crop-pages/) - 異なるページプロパティを使用して、プログラムでPDFドキュメントのページをトリミングできます。

- [透かしを追加する](/pdf/python-net/add-watermarks/) - Artifactクラスを使用してPDFファイルに透かしを追加します。
- [PDFファイルにページ番号を追加する](/pdf/python-net/add-page-number/) - PageNumberStampクラスはPDFファイルにページ番号を追加するのに役立ちます。
- [背景を追加する](/pdf/python-net/add-backgrounds/) - 背景画像を使用して透かしを追加できます。
- [スタンプ](/pdf/python-net/stamping/) - ImageStampクラスを使用して、PDFファイルに画像スタンプを追加し、TextStampクラスを使用してテキストを追加できます。
- [ページプロパティの取得と設定](/pdf/python-net/get-and-set-page-properties/) - このセクションでは、PDFファイルのページ数を取得したり、色などのPDFページプロパティの情報を取得したり、ページプロパティを設定したりする方法を示します。

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