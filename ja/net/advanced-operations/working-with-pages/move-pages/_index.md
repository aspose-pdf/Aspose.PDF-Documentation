---
title: PDFページをプログラムで移動する C#
linktitle: PDFページを移動する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/move-pages/
description: Aspose.PDF for .NETを使用して、希望の場所またはPDFファイルの最後にページを移動してみてください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NETは、ユーザーがPDFページをドキュメント間でプログラムで移動したり、同じドキュメント内で再配置したりできる強力な新機能を紹介します。この機能により、開発者は指定された場所にページを挿入し、ドキュメントの整合性を維持しながらページの整理を簡単に管理できるようになります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETを使用して、希望の場所またはPDFファイルの最後にページを移動してみてください。"
}
</script>

## PDFドキュメントから別のPDFドキュメントへのページの移動

このトピックでは、C#を使用して1つのPDFドキュメントから別のドキュメントの最後にページを移動する方法を説明します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

ページを移動するには、次の手順を実行します。

1. ソースPDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. 目的地PDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションからページを取得します。
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)メソッドを使用して目的地ドキュメントにページを追加します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。
1. ソースドキュメントで[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)メソッドを使用してページを削除します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用してソースPDFを保存します。

次のコードスニペットは、1ページを移動する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## PDFドキュメントから別のPDFドキュメントへの複数ページの移動

1. ソースPDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. 目的地PDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. 移動するページ番号の配列を定義します。
1. 配列をループします：
    1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションからページを取得します。
    1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)メソッドを使用して目的地ドキュメントにページを追加します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。
1. 配列を使用してソースドキュメントで[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2)メソッドを使用してページを削除します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用してソースPDFを保存します。

次のコードスニペットは、1つのPDFドキュメントから別のPDFドキュメントに複数のページを移動する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## 現在のPDFドキュメント内の新しい場所にページを移動する

1. ソースPDFファイルを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションからページを取得します。
1. 新しい場所（例えば、最後）にページを[Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)メソッドを使用して追加します。
1. 前の場所で[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)メソッドを使用してページを削除します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力PDFを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
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