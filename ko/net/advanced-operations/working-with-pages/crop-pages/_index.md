---
title: C#로 PDF 페이지 자르기
linktitle: 페이지 자르기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/crop-pages/
description: Aspose.PDF for .NET을 사용하여 너비, 높이, 블리드, 크롭 및 트림 박스와 같은 페이지 속성을 가져올 수 있습니다.
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
    "abstract": "Aspose.PDF for .NET은 개발자가 PDF의 다양한 페이지 속성에 프로그래밍 방식으로 접근하고 조작할 수 있는 강력한 새로운 기능을 소개합니다. 여기에는 미디어 박스, 블리드 박스, 트림 박스, 아트 박스 및 크롭 박스가 포함됩니다. 이 기능은 PDF 레이아웃을 사용자 정의하는 과정을 간소화하여 문서 프레젠테이션의 정확성을 보장하고 인쇄 품질을 향상시키며 흰색 가장자리를 최소화합니다. 사용하기 쉬운 코드 스니펫을 통해 사용자는 이러한 기능을 애플리케이션에 원활하게 통합하여 PDF 관리 및 조작을 개선할 수 있습니다.",
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
    "description": "Aspose.PDF for .NET을 사용하여 너비, 높이, 블리드, 크롭 및 트림 박스와 같은 페이지 속성을 가져올 수 있습니다."
}
</script>

## 페이지 속성 가져오기

PDF 파일의 각 페이지는 너비, 높이, 블리드, 크롭 및 트림 박스와 같은 여러 속성을 가지고 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우 PDF에도 블리드 박스가 있습니다. 블리드는 페이지의 가장자리를 넘어 확장된 색상(또는 아트워크)의 양입니다. 이는 문서가 인쇄되고 크기가 조정될 때("트림") 잉크가 페이지의 가장자리까지 가도록 보장하는 데 사용됩니다. 페이지가 잘못 잘리더라도 - 트림 마크에서 약간 벗어나 잘리더라도 - 페이지에 흰색 가장자가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 페이지에 실제 내용 주위에 그려진 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **크롭 박스**: 크롭 박스는 PDF 문서가 Adobe Acrobat에서 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: 미디어 박스와 드롭 박스의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.
자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

아래 스니펫은 페이지를 자르는 방법을 보여줍니다:

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

이 예제에서는 샘플 파일 [여기](crop_page.pdf)를 사용했습니다. 처음에 우리의 페이지는 그림 1과 같이 보입니다.

변경 후 페이지는 그림 2와 같이 보입니다.

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