---
title: PDFドキュメントにページを追加する
linktitle: ページを追加
type: docs
weight: 10
url: ja/net/add-pages/
description: この記事では、PDFファイルの希望の位置にページを挿入（追加）する方法を学びます。C#を使用してPDFファイルからページを移動、削除（削除）する方法についても説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#でPDFにページを追加する",
    "alternativeHeadline": "PDFドキュメントにページを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, PDFページ追加, PDFページ挿入",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、PDFファイルの希望の位置にページを挿入（追加）する方法を学びます。C#を使用してPDFファイルからページを移動、削除（削除）する方法についても説明します。"
}
</script>

Aspose.PDF for .NET APIは、C#または他の.NET言語を使用してPDFドキュメントのページを操作するための完全な柔軟性を提供します。PDFドキュメントのすべてのページは[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)に保持されており、PDFページを操作するために使用できます。
Aspose.PDF for .NETでは、ファイルの任意の位置にPDFドキュメントにページを挿入したり、PDFファイルの末尾にページを追加することができます。
このセクションでは、C#を使用してPDFにページを追加する方法を示します。

## PDFファイルにページを追加または挿入する

Aspose.PDF for .NETでは、ファイルの任意の位置にPDFドキュメントにページを挿入したり、PDFファイルの末尾にページを追加することができます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

### PDFファイルの望ましい位置に空ページを挿入する

PDFファイルに空ページを挿入するには：

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスオブジェクトを作成します。
1.
1.
[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) メソッドを使用して出力PDFを保存します。

以下のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```cs
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// PDFに空のページを挿入
pdfDocument.Pages.Insert(2);
// 出力ファイルを保存
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

上記の例では、デフォルトパラメータを使用して空ページを追加しました。ドキュメントの別のページと同じページサイズにする必要がある場合は、いくつかのコード行を追加する必要があります：

```cs
var page = pdfDocument.Pages.Insert(2);
//ページ1からページパラメータをコピー
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### PDFファイルの最後に空白ページを追加する

時々、ドキュメントが空白のページで終わることを確認したい場合があります。このトピックでは、PDFドキュメントの最後に空白ページを挿入する方法について説明します。

PDFファイルの最後に空白ページを挿入するには：

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) コレクションの [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) メソッドをパラメータなしで呼び出します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの最後に空白ページを挿入する方法を示しています。

```cs
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// PDFファイルの最後に空白ページを挿入
pdfDocument.Pages.Add();

// 出力ファイルを保存
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

