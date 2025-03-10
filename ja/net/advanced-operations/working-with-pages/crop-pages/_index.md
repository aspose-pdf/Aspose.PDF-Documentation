---
title: PDFページをプログラムでトリミングする C#
linktitle: ページをトリミング
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ja/net/crop-pages/
description: Aspose.PDF for .NETを使用して、幅、高さ、ブリード、クロップ、トリムボックスなどのページプロパティを取得できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NETは、開発者がPDFのさまざまなページプロパティ（メディアボックス、ブリードボックス、トリムボックス、アートボックス、クロップボックスなど）にプログラムでアクセスし、操作できる強力な新機能を導入します。この機能により、PDFレイアウトのカスタマイズプロセスが効率化され、文書のプレゼンテーションの精度が確保され、印刷品質が向上し、白いエッジが最小限に抑えられます。使いやすいコードスニペットを使用することで、ユーザーはこれらの機能をアプリケーションにシームレスに統合し、PDFの管理と操作を改善できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETを使用して、幅、高さ、ブリード、クロップ、トリムボックスなどのページプロパティを取得できます。"
}
</script>

## ページプロパティを取得する

PDFファイルの各ページには、幅、高さ、ブリード、クロップ、トリムボックスなどのいくつかのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

- **メディアボックス**: メディアボックスは、最も大きなページボックスです。これは、文書がPostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えばA4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDF文書が表示または印刷されるメディアの物理的なサイズを決定します。
- **ブリードボックス**: 文書にブリードがある場合、PDFにもブリードボックスがあります。ブリードは、ページの端を超えて延びる色（またはアートワーク）の量です。これは、文書が印刷されてサイズにカット（「トリム」）されたときに、インクがページの端まで届くことを保証するために使用されます。ページがトリムマークからわずかに外れてカットされても、ページに白いエッジは現れません。
- **トリムボックス**: トリムボックスは、印刷およびトリミング後の文書の最終サイズを示します。
- **アートボックス**: アートボックスは、文書内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションでPDF文書をインポートする際に使用されます。
- **クロップボックス**: クロップボックスは、Adobe AcrobatでPDF文書が表示される「ページ」サイズです。通常の表示では、Adobe Acrobatではクロップボックスの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdf仕様書、特に10.10.1ページ境界を参照してください。
- **Page.Rect**: メディアボックスとドロップボックスの交差点（一般的に見える長方形）です。以下の図はこれらのプロパティを示しています。
詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

以下のスニペットは、ページをトリミングする方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

この例では、サンプルファイルを[こちら](crop_page.pdf)で使用しました。最初に私たちのページは図1のように見えます。

変更後、ページは図2のように見えます。

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