---
title: C#を使用したPDFドキュメントの操作
linktitle: ドキュメントの操作
type: docs
weight: 10
url: /ja/net/working-with-documents/
description: この記事では、Aspose.PDFライブラリを使用してドキュメントで行うことができる操作について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用したPDFドキュメントの操作",
    "alternativeHeadline": "PDFドキュメントの操作",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, pdfドキュメント",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/working-with-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDFライブラリを使用してドキュメントで行うことができる操作について説明します。"
}
</script>

PDFは、ソフトウェア、ハードウェア、またはそれが表示されているオペレーティングシステムに依存しない電子形式でドキュメントを表示するために使用されるポータブルドキュメントフォーマットを指します。

PDFはオープンスタンダードであり、現在は国際標準化機構（ISO）によって維持されています。

元々の目的は、どのプラットフォームやコンピュータプログラムで見られても、ドキュメントの内容とレイアウトを保存し保護することでした。これが、PDFが編集しにくく、時には情報を抽出することさえ困難な理由です。

しかし、**Aspose.PDF for .NET**はPDFドキュメントを扱う際に発生するほとんどのタスクを処理するのに役立ちます。

以下のことができます：

- [PDFドキュメントのフォーマット](/pdf/ja/net/formatting-pdf-document/) - ドキュメントの作成、ドキュメントのプロパティの取得と設定、フォントの埋め込み、およびPDFファイルのその他の操作。
- [PDFドキュメントの操作](/pdf/ja/net/manipulate-pdf-document/) - PDFドキュメントをPDF A規格に対応させる、目次の作業、PDFの有効期限の設定など。
- [PDFの最適化](/pdf/ja/net/optimize-pdf/) - ページ内容の最適化、ファイルサイズの最適化、使用されていないオブジェクトの削除、すべての画像を圧縮してドキュメントの最適化を成功させる。
- [PDFの最適化](/pdf/ja/net/optimize-pdf/) - ページコンテンツの最適化、ファイルサイズの最適化、使用されていないオブジェクトの削除、すべての画像の圧縮によるドキュメントの成功的な最適化。
- [PDFの結合](/pdf/ja/net/merge-pdf-documents/) - 複数のPDFファイルをC#を使用して単一のPDFドキュメントに結合します。
- [PDFの分割](/pdf/ja/net/split-document/) - .NETアプリケーションでPDFページを個々のPDFファイルに分割します。
- [フォルダ内のPDFファイルの連結](/pdf/ja/net/concatenating-all-pdf-files-in-particular-folder/) - PdfFileEditorクラスを使用して特定のフォルダ内のすべてのPDFファイルを連結します。
- [MemoryStreamsを使用した複数のPDFファイルの連結](/pdf/ja/net/concatenate-pdf-documents/) - C#を使用してMemoryStreamsで複数のPDFファイルを連結する方法を学びます。
- [見出しの操作](/pdf/ja/net/working-with-headings/) - C#を使用してPDFドキュメントの見出しに番号を付けることができます。

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

