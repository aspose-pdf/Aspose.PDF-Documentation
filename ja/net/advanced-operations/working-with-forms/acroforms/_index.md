---
title: AcroFormsの操作
linktitle: アクロフォーム
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/acroforms/
description: Aspose.PDF for .NETを使用すると、ゼロからフォームを作成し、PDFドキュメントのフォームフィールドに入力し、フォームからデータを抽出することができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NETは、AcroFormsを操作するための強化された機能を提供し、ユーザーがゼロからフォームを効率的に作成し、PDFフィールドに入力し、シームレスにデータを抽出できるようにします。この強力な機能は、複数のデータベースレコードの統合をサポートし、動的なフォーム管理とスムーズなユーザー体験を実現します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## AcroFormsの基本

**AcroForms**は、元々のPDFフォーム技術です。AcroFormsはページ指向のフォームです。1998年に初めて導入されました。これらは、Forms Data FormatまたはFDFおよびXML Forms Data FormatまたはxFDFで入力を受け付けます。サードパーティのベンダーはAcroFormsをサポートしています。AdobeがAcroFormsを導入した際、彼らはそれを「Adobe Acrobat Pro/Standardで作成されたPDFフォームであり、特別な静的または動的XFAフォームではない」と呼びました。AcroFormsはポータブルであり、すべてのプラットフォームで動作します。

AcroFormsを使用して、PDFフォームドキュメントに追加のページを追加できます。テンプレートの概念のおかげで、AcroFormsを使用して複数のデータベースレコードでフォームを埋めることをサポートできます。

PDF 1.7は、データとPDFフォームを統合するための2つの異なる方法をサポートしています。

*AcroForms（Acrobatフォームとも呼ばれる）*は、PDF 1.2形式仕様で導入され、含まれています。

*Adobe XML Forms Architecture（XFA）フォーム*は、PDF 1.5形式仕様でオプション機能として導入されました（XFA仕様はPDF仕様に含まれておらず、参照のみです）。

**Acroforms**と**XFA**フォームを理解するためには、まず基本を理解する必要があります。まず、両者は使用できるPDFフォームです。Acroformsは1998年に作成された古いもので、今でもクラシックPDFフォームと呼ばれています。XFAフォームは、PDFとして保存できるウェブページで、2003年に登場しました。PDFがXFAフォームを受け入れるようになるまでには時間がかかりました。

AcroFormsにはXFAにはない機能があり、逆にXFAにはAcroFormsにはない機能があります。例えば：

- AcroFormsは「テンプレート」の概念をサポートしており、複数のデータベースレコードでフォームを埋めるためにPDFフォームドキュメントに追加のページを追加できます。
- XFAは、データを収容するために必要に応じてフィールドのサイズを変更できるドキュメントリフローの概念をサポートしています。

Javaライブラリの機能について詳しく学ぶには、以下の記事を参照してください：

- [AcroFormの作成](/pdf/ja/net/create-form) - C#でゼロからフォームを作成します。
- [AcroFormの入力](/pdf/ja/net/fill-form) - PDFドキュメントのフォームフィールドに入力します。
- [AcroFormの抽出](/pdf/ja/net/extract-form) - PDFドキュメントのすべてまたは個々のフィールドから値を取得します。
- [AcroFormの修正](/pdf/ja/net/modifing-form) - FieldLimitを取得または設定し、フォームフィールドのフォントを設定します。
- [AcroFormデータの投稿](/pdf/ja/net/posting-acroform-data/) - フォームデータをXMLファイルにインポートおよびエクスポートします。
- [データのインポートとエクスポート](/pdf/ja/net/import-and-export-data/) - フォームクラスを使用してデータをインポートおよびエクスポートします。
- [PDFからフォームを削除](/pdf/ja/net/remove-form/) - サブタイプ/フォームに基づいてテキストを削除し、すべてのフォームを削除します。
- [JSONでのデータのインポートとエクスポート](/pdf/ja/net/import-export-json/) - JSONを使用してデータをインポートおよびエクスポートします。

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