---
title: PDF内の画像を取得して検索する
linktitle: 画像を検索して取得する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/search-and-get-images-from-pdf-document/
description: Aspose.PDFを使用してJavaでPDFドキュメントから画像を検索して抽出する方法を学びます。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Search Images in PDF",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Documents",
    "abstract": "Aspose.PDFライブラリを使用してPDFドキュメントから画像を検索して抽出する新しい機能を発見してください。この機能は、複数のページにわたる画像の位置を特定するプロセスを簡素化し、ユーザーが簡単なコードスニペットで画像のプロパティ（寸法や解像度など）を簡単に取得できるようにします。この効率的な画像処理機能を活用して、PDFドキュメントの操作スキルを向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get images, search images, PDF document, Aspose.PDF library, ImagePlacementAbsorber, ImagePlacements, .NET PDF manipulation, document image extraction, image placement properties, code examples",
    "wordcount": "316",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、Aspose.PDFライブラリを使用してPDFドキュメントから画像を検索して取得する方法を説明します。"
}
</script>

ImagePlacementAbsorberを使用すると、PDFドキュメント内のすべてのページの画像を検索できます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

ドキュメント全体で画像を検索するには：

1. PagesコレクションのAcceptメソッドを呼び出します。Acceptメソッドは、ImagePlacementAbsorberオブジェクトをパラメータとして受け取ります。これにより、ImagePlacementオブジェクトのコレクションが返されます。
1. ImagePlacementsオブジェクトをループして、そのプロパティ（画像、寸法、解像度など）を取得します。

次のコードスニペットは、ドキュメント内のすべての画像を検索する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(abs);

        // Loop through all ImagePlacements, get image and ImagePlacement properties
        foreach (var imagePlacement in abs.ImagePlacements)
        {
            // Get the image using ImagePlacement object
            var image = imagePlacement.Image;

            // Display image placement properties for all placements
            Console.Out.WriteLine("image width: " + imagePlacement.Rectangle.Width);
            Console.Out.WriteLine("image height: " + imagePlacement.Rectangle.Height);
            Console.Out.WriteLine("image LLX: " + imagePlacement.Rectangle.LLX);
            Console.Out.WriteLine("image LLY: " + imagePlacement.Rectangle.LLY);
            Console.Out.WriteLine("image horizontal resolution: " + imagePlacement.Resolution.X);
            Console.Out.WriteLine("image vertical resolution: " + imagePlacement.Resolution.Y);
        }
    }
}

```

個々のページから画像を取得するには、次のコードを使用します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromAnIndividualPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages[1].Accept(abs);
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