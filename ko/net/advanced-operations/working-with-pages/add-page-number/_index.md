---
title: C#를 사용하여 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: /ko/net/add-page-number/
description: Aspose.PDF for .NET을 사용하면 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 PDF에 페이지 번호 추가",
    "alternativeHeadline": "PDF에 페이지 번호 스탬프 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 페이지 번호 스탬프",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다."
}
</script>

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다른 부분을 쉽게 찾을 수 있도록 도와줍니다.
**Aspose.PDF for .NET**은 PageNumberStamp를 사용하여 페이지 번호를 추가할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
[PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.

```csharp
// 완성된 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// 페이지 번호 스탬프 생성
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// 스탬프가 배경인지 여부
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// 텍스트 속성 설정
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// 특정 페이지에 스탬프 추가
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
## 실시간 예제

[PDF 페이지 번호 추가](https://products.aspose.app/pdf/page-number)는 PDF에 페이지 번호를 추가하는 기능을 조사할 수 있는 무료 온라인 웹 애플리케이션입니다.

[![PDF에서 C#을 사용하여 페이지 번호 추가 방법](page_number.png)](https://products.aspose.app/pdf/page-number)

## Bates 번호 추가/제거

**Bates 번호** (Bates 도장으로도 알려져 있음)는 법률, 의료 및 비즈니스 분야에서 이미지와 문서에 식별 번호 및/또는 날짜/시간 마크를 스캔하거나 처리할 때 사용됩니다. 예를 들어, 재판 준비를 위한 발견 단계 동안이나 비즈니스 영수증을 식별할 때 사용됩니다. 이 과정은 이미지나 문서의 식별, 보호 및 자동 연속 번호 부여를 제공합니다.

Aspose.PDF는 현재 Bates 번호 지정에 대해 제한적인 지원을 제공합니다. 이 기능은 고객의 요청에 따라 업데이트될 예정입니다.

### Bates 번호 제거 방법

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
```
```html
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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

