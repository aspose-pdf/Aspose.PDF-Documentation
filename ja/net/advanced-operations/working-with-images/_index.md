---
title: C#を使用したPDF内の画像の操作
linktitle: 画像の操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/working-with-images/
description: このセクションでは、C#ライブラリを使用してPDFファイル内の画像を操作する機能について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/manipulate-images/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Images in PDF using C#",
    "alternativeHeadline": "Comprehensive Image Handling in PDF with C#",
    "abstract": "Aspose.PDF for .NETの新機能により、PDFドキュメント内の画像を管理する能力が向上し、画像のリサイズ、置換、抽出、詳細な画像プロパティの取得などの高度な機能が提供されます。この堅牢なライブラリは、PDFファイルにグラフィックスを追加および操作するプロセスを簡素化し、効率的に動的なデジタルドキュメントを作成しようとする開発者にとって不可欠なツールとなります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF manipulation, Aspose.PDF library, image extraction, add image to PDF, replace image in PDF, set image size, search images in PDF, DICOM image support",
    "wordcount": "578",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/working-with-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、C#ライブラリを使用してPDFファイル内の画像を操作する機能について説明します。"
}
</script>

PDF形式における画像は非常に複雑なトピックです。PDFドキュメントの作業に直面したとき、ユーザーは画像に対してさまざまな操作を行うことができます。私たちは、画像はファイルに追加または削除することしかできないと考えがちですが、Aspose.PDFライブラリを使用すると、画像のサイズを設定したり、画像を置換したり、画像を抽出したり、検索したり、PDFドキュメントから画像を取得したりすることも可能です。

**PDFに画像を追加するにはどうすればよいですか？** Aspose.PDFを使用してPDF内の画像に関する最も人気のある質問に対する答えを得ることができます。

**Aspose.PDF for .NET**は、デジタルドキュメントを操作するためのスマートで効率的なツールであり、既存のPDFに任意のグラフィックオブジェクトを迅速にインポートして配置できます。
C#ライブラリを使用することは、レポートにチャートを挿入したり、プロジェクトにフロアプランのオーバーレイを追加したり、単に履歴書に写真を含めたりする必要がある場合にも便利です。PDFドキュメントに画像を挿入および編集するための高度な方法を探している場合は、次の記事を学ぶことを強くお勧めします。

以下の操作が可能です：

- [既存のPDFファイルに画像を追加](/pdf/net/add-image-to-existing-pdf-file/) - PDFドキュメントに画像と単一の画像の参照を追加し、その後品質を制御します。
- [PDFファイルから画像を削除](/pdf/net/delete-images-from-pdf-file/) - PDFファイルから画像を削除するためのコードスニペットを確認してください。
- [PDFファイルから画像を抽出](/pdf/net/extract-images-from-pdf-file/) - 画像コレクションを使用してPDFファイルから画像を抽出します。
- [埋め込まれた画像の解像度と寸法を取得](/pdf/net/get-resolution-and-dimensions-of-embedded-images/) - 解像度と寸法情報を取得する機能を提供するAspose.PDF名前空間のオペレータークラスを使用します。
- [画像の配置を操作](/pdf/net/working-with-image-placement/) - PDFドキュメント内の画像の解像度と位置を取得できます。
- [PDFドキュメントから画像を検索して取得](/pdf/net/search-and-get-images-from-pdf-document/) - C#を使用して、個々のページから画像を取得し、すべてのページの画像を検索できます。
- [既存のPDFファイル内の画像を置換](/pdf/net/replace-image-in-existing-pdf-file/) - PDFファイル内の画像を置換する方法を示すコードスニペットを確認してください。
- [画像サイズを設定](/pdf/net/set-image-size/) - C#ライブラリを使用して画像のサイズを設定できます。
- [デフォルトフォント名を設定](/pdf/net/set-default-font-name/) - 変換プロセスのためのデフォルトフォント名を設定します。
- [PDFドキュメントからサムネイル画像を生成](/pdf/net/generate-thumbnail-images-from-pdf-documents/) - 次の記事では、最初にAcrobat SDKを使用し、その後Aspose.PDFを使用してPDFドキュメントからサムネイル画像を生成する方法を示します。
- DICOM画像のサポート - Aspose.PDF for .NETは、特別な医療グラフィック標準の画像をサポートしています。Aspose.PDF for .NETは、DICOMおよびSVG画像を変換することができます。詳細は[Convert DICOM to PDF](/pdf/net/convert-images-format-to-pdf/#convert-dicom-to-pdf)セクションを確認してください。
- [ベクターグラフィックスの操作](/pdf/net/working-with-vector-graphics) - このセクションでは、C#を使用したGraphicsAbsorberツールの操作機能について説明します。

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