---
title: PDF에서 C#을 사용하여 PDF 페이지 스탬프 추가
linktitle: PDF 파일의 페이지 스탬프
type: docs
weight: 30
url: ko/net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for .NET 라이브러리와 PdfPageStamp 클래스를 사용하여 PDF 문서에 페이지 스탬프를 추가합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 C#을 사용하여 PDF 페이지 스탬프 추가",
    "alternativeHeadline": "PDF에서 C#을 사용하여 PDF 페이지 스탬프 추가",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 문서 생성",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/net/page-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리와 PdfPageStamp 클래스를 사용하여 PDF 문서에 페이지 스탬프를 추가합니다."
}
</script>
## C#으로 페이지 스탬프 추가하기

[PdfPageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp)는 그래픽, 텍스트, 테이블을 포함하는 복합 스탬프를 적용할 때 사용할 수 있습니다. 다음 예제는 Adobe InDesign, Illustrator, Microsoft Word를 사용하여 문구류와 같은 스탬프를 만드는 방법을 보여줍니다. 입력 문서가 있다고 가정하고 파란색과 자주색 테두리를 적용하려고 합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
public static void AddPageStamp()
{
    var inputFileName = "sample-4pages.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "PageStamp.pdf";
    var document = new Document(_dataDir + inputFileName);

    var bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1)
    {
        Height = 800,
        Background = true
    };

    var plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2)
    {
        Height = 800,
        Background = true
    };

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.Pages[i].AddStamp(bluePageStamp);
        else
            document.Pages[i].AddStamp(plumPageStamp);
    }

    document.Save(_dataDir + outputFileName);
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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

