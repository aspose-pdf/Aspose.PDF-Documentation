---
title: PDF에서 이미지 가져오기 및 검색
linktitle: 이미지 검색 및 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/search-and-get-images-from-pdf-document/
description: Aspose.PDF를 사용하여 Java에서 PDF 문서에서 이미지를 검색하고 추출하는 방법을 배웁니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Search Images in PDF",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Documents",
    "abstract": "Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 이미지를 검색하고 추출하는 새로운 기능을 발견하세요. 이 기능은 여러 페이지에 걸쳐 이미지를 찾는 과정을 간소화하여 사용자가 간단한 코드 스니펫으로 이미지 속성(크기 및 해상도 등)을 쉽게 검색할 수 있도록 합니다. 이 효율적인 이미지 처리 기능을 활용하여 PDF 문서 조작 기술을 향상시키세요.",
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
    "description": "이 섹션에서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 이미지를 검색하고 가져오는 방법을 설명합니다."
}
</script>

ImagePlacementAbsorber를 사용하면 PDF 문서의 모든 페이지에서 이미지를 검색할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

전체 문서에서 이미지를 검색하려면:

1. Pages 컬렉션의 Accept 메서드를 호출합니다. Accept 메서드는 ImagePlacementAbsorber 객체를 매개변수로 사용합니다. 이 메서드는 ImagePlacement 객체의 컬렉션을 반환합니다.
1. ImagePlacements 객체를 반복하여 그 속성(이미지, 크기, 해상도 등)을 가져옵니다.

다음 코드 스니펫은 문서에서 모든 이미지를 검색하는 방법을 보여줍니다.

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

개별 페이지에서 이미지를 가져오려면 다음 코드를 사용하세요:

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