---
title: C#でPDFページサイズを変更する
linktitle: PDFページサイズの変更
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/change-page-size/
description: Aspose.PDF for .NETライブラリを使用してPDFドキュメントのページサイズを変更します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change PDF Page Size with C#",
    "alternativeHeadline": "Effortlessly Resize PDF Pages in C#",
    "abstract": "Aspose.PDF for .NETの新機能により、開発者はプログラムでPDFドキュメントのページサイズを簡単に変更できます。数行のコードで、ユーザーは既存のPDFの寸法を変更し、ドキュメント管理機能を向上させ、さまざまなレイアウト要件との互換性を確保できます。この機能は、.NETアプリケーション内でA4などの希望する形式にPDFページをリサイズするプロセスを簡素化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "300",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETライブラリを使用してPDFドキュメントのページサイズを変更します。"
}
</script>

## C#でPDFページサイズを変更する

Aspose.PDF for .NETを使用すると、.NETアプリケーション内で簡単なコード行でPDFページサイズを変更できます。このトピックでは、既存のPDFファイルのページ寸法（サイズ）を更新/変更する方法を説明します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)クラスには、ページサイズを設定するSetPageSize(...)メソッドがあります。以下のコードスニペットは、いくつかの簡単なステップでページ寸法を更新します：

1. ソースPDFファイルをロードします。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)オブジェクトにページを取得します。
1. 指定されたページを取得します。
1. SetPageSize(..)メソッドを呼び出して、その寸法を更新します。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのSave(..)メソッドを呼び出して、更新されたページ寸法のPDFファイルを生成します。

{{% alert color="primary" %}}

高さと幅のプロパティは基本単位としてポイントを使用します。1インチ = 72ポイント、1cm = 1/2.54インチ = 0.3937インチ = 28.3ポイントです。

{{% /alert %}}

以下のコードスニペットは、PDFページの寸法をA4サイズに変更する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.SetPageSize(597.6, 842.4);
        // Save PDF document
        document.Save(dataDir + "UpdateDimensions_out.pdf"); 
    }
}
```

## PDFページサイズを取得する

Aspose.PDF for .NETを使用して、既存のPDFファイルのPDFページサイズを読み取ることができます。以下のコードサンプルは、C#を使用してPDFページの寸法を読み取る方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Adds a blank page to pdf document
        Page page = document.Pages.Count > 0 ? document.Pages[1] : document.Pages.Add();
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
        // Rotate page at 90 degree angle
        page.Rotate = Rotation.on90;
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
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