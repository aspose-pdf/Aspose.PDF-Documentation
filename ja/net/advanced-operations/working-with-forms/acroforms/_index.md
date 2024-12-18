---
title: AcroFormsとの作業
linktitle: AcroForms
type: docs
weight: 10
url: /ja/net/acroforms/
description: Aspose.PDF for .NETを使用して、ゼロからフォームを作成したり、PDFドキュメントのフォームフィールドに記入したり、フォームからデータを抽出したりすることができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "AcroFormsとの作業",
    "alternativeHeadline": "PDFのAcroFormsで作業するオプション",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, pdfのacroforms",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用して、ゼロからフォームを作成したり、PDFドキュメントのフォームフィールドに記入したり、フォームからデータを抽出したりすることができます。"
}
</script>
## AcroFormsの基礎

**AcroForms**は、元々のPDFフォーム技術です。AcroFormsはページ指向のフォームです。1998年に初めて導入されました。Forms Data FormatまたはFDF、そしてXML Forms Data FormatまたはxFDFで入力を受け付けます。サードパーティのベンダーがAcroFormsをサポートしています。AdobeがAcroFormsを導入したとき、それを「Adobe Acrobat Pro/Standardで作成されたPDFフォームで、静的または動的なXFAフォームの特別なタイプではない」と表現しました。Acroformsはポータブルで、すべてのプラットフォームで機能します。

PDFフォームドキュメントに追加ページを加えるためにAcroFormsを使用することができます。テンプレートの概念のおかげで、複数のデータベースレコードでフォームを埋めるためにAcroFormsをサポートすることができます。

PDF 1.7は、データとPDFフォームを統合するための2つの異なる方法をサポートしています。

*AcroForms（別名アクロバットフォーム）*、PDF 1.2形式仕様に導入され、含まれています。

*Adobe XML Forms Architecture (XFA) フォーム*、PDF 1.5形式仕様でオプション機能として導入されました（XFA仕様はPDF仕様には含まれておらず、参照のみです。
*Adobe XML Forms Architecture（XFA）フォーム* は、PDF 1.5形式の仕様でオプション機能として導入されました（XFA仕様はPDF仕様には含まれておらず、参照のみです。

**Acroforms** と **XFA** フォームを理解するためには、まず基本を理解する必要があります。初めに、どちらも使用できるPDFフォームです。Acroformsは1998年に作成された古いもので、今でも古典的なPDFフォームとして言及されています。XFAフォームは、2003年に登場したPDFとして保存できるWebページです。PDFがXFAフォームを受け入れ始めるまでには時間がかかりました。

AcroFormsにはXFAにはない機能があり、逆もまた同様です。例えば：

- AcroFormsは「テンプレート」という概念をサポートしており、複数のデータベースレコードでフォームを埋めるためにPDFフォームドキュメントに追加ページを追加することができます。
- XFAはドキュメントのリフローの概念をサポートしており、データを収容するために必要な場合にフィールドのサイズを変更できます。

Javaライブラリの機能について詳しく学ぶには、次の記事を参照してください：
Javaライブラリの機能を詳しく学ぶために、以下の記事を参照してください：

- [Create AcroForm](/pdf/ja/net/create-form) - C#を使って最初からフォームを作成します。
- [Fill AcroForm](/pdf/ja/net/fill-form) - PDFドキュメントのフォームフィールドを入力します。
- [Extract AcroForm](/pdf/ja/net/extract-form) - PDFドキュメントのすべてまたは個々のフィールドから値を取得します。
- [Modifing AcroForm](/pdf/ja/net/modifing-form) - FieldLimitを取得または設定し、フォームフィールドのフォント等を設定します。
- [Posting AcroForm Data](/pdf/ja/net/posting-acroform-data/) - フォームデータをXMLファイルにインポートおよびエクスポートします。
- [Import and Export Data](/pdf/ja/net/import-and-export-data/) - Form Classを使用してデータをインポートおよびエクスポートします。

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

