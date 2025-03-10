---
title: PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ko/net/add-page-number/
description: Aspose.PDF for .NET는 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있게 해줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/get-and-set-page-properties/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Page Number to PDF",
    "alternativeHeadline": "Add Dynamic Page Numbering to PDF",
    "abstract": "Aspose.PDF for .NET는 페이지 번호를 PDF 문서에 원활하게 통합할 수 있는 강력한 페이지 번호 스탬프 기능을 소개합니다. 이 기능은 사용자가 형식, 정렬 및 스타일을 사용자 정의하여 가독성과 전문적인 프레젠테이션을 향상시킴으로써 문서 탐색 및 조직을 개선합니다.",
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
    "description": "Aspose.PDF for .NET는 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있게 해줍니다."
}
</script>

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다양한 부분을 찾는 데 더 쉽게 해줍니다.
**Aspose.PDF for .NET**는 PageNumberStamp를 사용하여 페이지 번호를 추가할 수 있게 해줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다. [PageNumber Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) 클래스는 형식, 여백, 정렬, 시작 번호 등과 같은 페이지 번호 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 페이지 번호 스탬프를 추가하려면 필요한 속성을 사용하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체와 [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) 객체를 생성해야 합니다. 그 후, [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 호출하여 PDF에 스탬프를 추가할 수 있습니다. 페이지 번호 스탬프의 글꼴 속성도 설정할 수 있습니다. 다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

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

## 실시간 예제

[PDF 페이지 번호 추가](https://products.aspose.app/pdf/page-number)는 페이지 번호 추가 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![C#를 사용하여 PDF에 페이지 번호 추가하는 방법](page_number.png)](https://products.aspose.app/pdf/page-number)

## Bates 번호 매기기 추가/제거

**Bates 번호 매기기**(Bates stamping이라고도 함)는 법률, 의료 및 비즈니스 분야에서 이미지와 문서에 식별 번호 및/또는 날짜/시간 마크를 배치하는 데 사용됩니다. 예를 들어, 재판 준비의 발견 단계에서 또는 비즈니스 영수증을 식별하는 동안 스캔되거나 처리될 때 사용됩니다. 이 과정은 이미지나 문서의 식별, 보호 및 자동 연속 번호 매기기를 제공합니다.

Aspose.PDF는 현재 Bates 번호 매기기에 대한 제한된 지원을 제공합니다. 이 기능은 고객의 요청에 따라 업데이트될 것입니다.

### Bates 번호 매기기 제거 방법

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