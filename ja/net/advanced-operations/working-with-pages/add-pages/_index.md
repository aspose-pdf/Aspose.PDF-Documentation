---
title: PDFドキュメントにページを追加
linktitle: ページを追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-pages/
description: Aspose.PDFを使用して、.NETで既存のPDFにページを追加する方法を探ります。ドキュメントを強化し、拡張します。
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
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "Aspose.PDF for .NETの機能により、ユーザーは指定された場所にPDFドキュメントにページを簡単に挿入でき、ドキュメントの柔軟性と整理を向上させます。この機能はページの追加をサポートするだけでなく、C#を使用して既存のページを移動または削除するオプションも含まれています。この直感的な追加により、PDF管理を効率化し、開発ツールキットを強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "この記事では、PDFファイルの所定の位置にページを挿入（追加）する方法を説明します。C#を使用してPDFファイルからページを移動、削除（削除）する方法を学びます。"
}
</script>

Aspose.PDF for .NET APIは、C#または他の.NET言語を使用してPDFドキュメント内のページを操作するための完全な柔軟性を提供します。PDFドキュメントのすべてのページは、PDFページを操作するために使用できる[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)に保持されます。
Aspose.PDF for .NETを使用すると、ファイル内の任意の位置にPDFドキュメントにページを挿入したり、PDFファイルの最後にページを追加したりできます。
このセクションでは、C#を使用してPDFにページを追加する方法を示します。

## PDFファイルにページを追加または挿入

Aspose.PDF for .NETを使用すると、ファイル内の任意の位置にPDFドキュメントにページを挿入したり、PDFファイルの最後にページを追加したりできます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

### 所定の位置にPDFファイルに空白ページを挿入

PDFファイルに空白ページを挿入するには：

1. 入力PDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. 指定されたインデックスで[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションの[Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert)メソッドを呼び出します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

上記の例では、デフォルトのパラメータで空白ページを追加しました。ドキュメント内の他のページと同じサイズにする必要がある場合は、いくつかのコード行を追加する必要があります。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### PDFファイルの最後に空白ページを追加

時には、ドキュメントが空白ページで終了することを確認したい場合があります。このトピックでは、PDFドキュメントの最後に空白ページを挿入する方法を説明します。

PDFファイルの最後に空白ページを挿入するには：

1. 入力PDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. パラメータなしで[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションの[Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)メソッドを呼び出します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの最後に空白ページを挿入する方法を示しています。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }
}
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