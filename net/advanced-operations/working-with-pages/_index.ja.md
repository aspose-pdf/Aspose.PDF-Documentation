---
title: C#でPDFページを操作する
linktitle: ページの操作
type: docs
weight: 20
url: /net/working-with-pages/
description: このセクションでは、ページの追加、ヘッダーとフッターの追加、ウォーターマークの追加方法について説明します。Aspose.PDF for .NETがこのトピックに関するすべての詳細を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#でPDFページを操作する",
    "alternativeHeadline": "PDFページの操作方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, pdfページ, pdfページ追加, ページ番号追加, ページ回転, ページ削除",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、ページの追加、ヘッダーとフッターの追加、ウォーターマークの追加方法について説明します。Aspose.PDF for .NETがこのトピックに関するすべての詳細を説明します。"
}
</script>
**Aspose.PDF for .NET** は、ファイル内の任意の位置にPDFドキュメントにページを挿入するだけでなく、PDFファイルの最後にページを追加することができます。このセクションでは、Acrobat ReaderなしでPDFにページを追加する方法を示します。
PDFファイルのヘッダーとフッターにテキストまたは画像を追加し、AsposeによるC#ライブラリでドキュメントの異なるヘッダーを選択できます。
また、C#を使用してPDFドキュメントのページをプログラムでトリミングしてみてください。

このセクションでは、Artifactクラスを使用してPDFファイルに透かしを追加する方法を学びます。このタスクのプログラミングサンプルを確認します。
PageNumberStampクラスを使用してページ番号を追加します。ドキュメントにスタンプを追加するには、ImageStampクラスとTextStampクラスを使用します。**Aspose.PDF for .NET**を使用してPDFファイルに背景画像を作成するために透かしを追加してください。

以下の操作が可能です：

- [ページを追加する](/pdf/net/add-pages/) - 望ましい位置にページを追加するか、PDFファイルの最後にページを追加し、ドキュメントからページを削除します。
- [ページを移動する](/pdf/net/move-pages/) - 一つのドキュメントから別のドキュメントへページを移動します。
- [ページの移動](/pdf/net/move-pages/) - あるドキュメントから別のドキュメントへページを移動します。
- [ページの削除](/pdf/net/delete-pages/) - PageCollection コレクションを使用してPDFファイルからページを削除します。
- [ページサイズの変更](/pdf/net/change-page-size/) - Aspose.PDF ライブラリを使用したコードスニペットでPDFページのサイズを変更できます。
- [ページの回転](/pdf/net/rotate-pages/) - 既存のPDFファイルのページの向きを変更できます。
- [ページの分割](/pdf/net/split-document/) - PDFファイルを一つまたは複数のPDFに分割できます。
- [ヘッダーおよび/またはフッターの追加](/pdf/net/add-headers-and-footers-of-pdf-file/) - PDFファイルのヘッダーやフッターにテキストや画像を追加します。
- [ページのトリミング](/pdf/net/crop-pages/) - 異なるページプロパティを使用してPDFドキュメントのページをプログラムでトリミングできます。
- [ウォーターマークの追加](/pdf/net/add-watermarks/) - Artifact Class を使用してPDFファイルにウォーターマークを追加します。
- [PDFファイルにページ番号を追加](/pdf/net/add-page-number/) - PageNumberStampクラスを使用してPDFファイルにページ番号を追加します。
- [PDFファイルにページ番号を追加する](/pdf/net/add-page-number/) - PageNumberStampクラスを使用してPDFファイルにページ番号を追加できます。
- [背景を追加する](/pdf/net/add-backgrounds/) - 背景画像を使用して透かしを追加できます。
- [スタンピング](/pdf/net/stamping/) - ImageStampクラスを使用してPDFファイルに画像スタンプを追加し、TextStampクラスを使用してテキストを追加できます。

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

