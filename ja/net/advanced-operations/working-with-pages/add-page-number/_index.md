---
title: PDFにページ番号を追加
linktitle: ページ番号を追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ja/net/add-page-number/
description: Aspose.PDF for .NETは、PageNumber Stampクラスを使用してPDFファイルにページ番号スタンプを追加することを可能にします。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Page Number to PDF",
    "alternativeHeadline": "Add Dynamic Page Numbering to PDF",
    "abstract": "Aspose.PDF for .NETは、ページ番号をPDF文書にシームレスに統合する強力なページ番号スタンプ機能を紹介します。この機能は、ユーザーがフォーマット、配置、スタイルをカスタマイズできるようにすることで、文書のナビゲーションと整理を向上させ、より良い可読性とプロフェッショナルなプレゼンテーションを実現します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Page Number, PDF Stamp, Aspose.PDF for .NET, PageNumberStamp class, Document object, PageNumberStamp properties, Bates numbering, PDF document generation, Page number stamp, C# PDF manipulation",
    "wordcount": "559",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETは、PageNumber Stampクラスを使用してPDFファイルにページ番号スタンプを追加することを可能にします。"
}
</script>

すべての文書にはページ番号が必要です。ページ番号は、読者が文書の異なる部分を見つけやすくします。
**Aspose.PDF for .NET**は、PageNumberStampを使用してページ番号を追加することを可能にします。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)クラスを使用して、PDFファイルにページ番号スタンプを追加できます。[PageNumber Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)クラスは、フォーマット、マージン、配置、開始番号など、ページ番号に基づくスタンプを作成するために必要なプロパティを提供します。ページ番号スタンプを追加するには、必要なプロパティを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトと[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp)オブジェクトを作成する必要があります。その後、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)の[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを呼び出して、PDFにスタンプを追加できます。また、ページ番号スタンプのフォント属性を設定することもできます。次のコードスニペットは、PDFファイルにページ番号を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageNumberStamp.pdf"))
    {
        // Create page number stamp
        var pageNumberStamp = new Aspose.Pdf.PageNumberStamp();
        // Whether the stamp is background
        pageNumberStamp.Background = false;
        pageNumberStamp.Format = "Page # of " + document.Pages.Count;
        pageNumberStamp.BottomMargin = 10;
        pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
        pageNumberStamp.StartingNumber = 1;
        // Set text properties
        pageNumberStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        pageNumberStamp.TextState.FontSize = 14.0F;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        pageNumberStamp.TextState.ForegroundColor = Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(pageNumberStamp);
        // Save PDF document
        document.Save(dataDir + "PageNumberStamp_out.pdf");  
    }
}
```

## ライブ例

[PDFページ番号を追加](https://products.aspose.app/pdf/page-number)は、ページ番号追加機能がどのように機能するかを調査できるオンラインの無料ウェブアプリケーションです。

[![C#を使用してPDFにページ番号を追加する方法](page_number.png)](https://products.aspose.app/pdf/page-number)

## ベイツ番号の追加/削除

**ベイツ番号**（ベイツスタンプとも呼ばれる）は、法的、医療、ビジネス分野で、スキャンまたは処理される画像や文書に識別番号や日付/時刻のマークを付けるために使用されます。たとえば、裁判の準備の発見段階やビジネスの領収書を特定する際に使用されます。このプロセスは、画像や文書の識別、保護、および自動連続番号付けを提供します。

Aspose.PDFは、現在ベイツ番号に対して限られたサポートを提供しています。この機能は、顧客のリクエストに応じて更新されます。

### ベイツ番号を削除する方法

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveBatesNumbering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveBatesNumberingInput.pdf"))
    {
        foreach (var page in document.Pages)
        {
            // Remove bates numbering
            var artifacts = page.Artifacts.Where(ar => ar.CustomSubtype == "BatesN");
            foreach (var artifact in artifacts)
            {
                page.Artifacts.Delete(artifact);   
            }
        }
        // Save PDF document
        document.Save(dataDir + "RemoveBatesNumbering_out.pdf");
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