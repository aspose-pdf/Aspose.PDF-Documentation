---
title: PDF 문서에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /net/add-pages/
description: 이 문서는 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르쳐 줍니다. C#을 사용하여 PDF 파일에서 페이지를 이동하거나 제거(삭제)하는 방법을 배우십시오.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#으로 PDF에 페이지 추가",
    "alternativeHeadline": "PDF 문서에 페이지 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 페이지 추가, pdf 페이지 삽입",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르쳐 줍니다. C#을 사용하여 PDF 파일에서 페이지를 이동하거나 제거(삭제)하는 방법을 배우십시오."
}
</script>
Aspose.PDF for .NET API는 C# 또는 다른 .NET 언어를 사용하여 PDF 문서의 페이지를 작업할 수 있는 완전한 유연성을 제공합니다. 이는 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)에 PDF 문서의 모든 페이지를 유지하여 PDF 페이지 작업에 사용할 수 있습니다.
Aspose.PDF for .NET은 파일의 어느 위치에나 페이지를 삽입하고 PDF 파일 끝에 페이지를 추가할 수 있습니다.
이 섹션에서는 C#을 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for .NET은 파일의 어느 위치에나 페이지를 삽입하고 PDF 파일 끝에 페이지를 추가할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

### 원하는 위치에 PDF 파일에 빈 페이지 삽입

PDF 파일에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1.
1.
1. 출력 PDF를 [저장](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메소드를 사용하여 저장하세요.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```cs
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// 문서 열기
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// PDF에 빈 페이지 삽입
pdfDocument.Pages.Insert(2);
// 출력 파일 저장
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

위 예제에서, 우리는 기본 매개변수를 가진 빈 페이지를 추가했습니다. 문서의 다른 페이지와 같은 페이지 크기를 만들고 싶다면 몇 줄의 코드를 추가해야 합니다:

```cs
var page = pdfDocument.Pages.Insert(2);
// 페이지 1에서 페이지 매개변수 복사
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### PDF 파일 마지막에 빈 페이지 추가하기

문서가 빈 페이지로 끝나도록 하고 싶을 때가 있습니다. 이 주제에서는 PDF 문서 말미에 빈 페이지를 삽입하는 방법에 대해 설명합니다.

PDF 파일 마지막에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 메서드를 매개변수 없이 호출합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일 마지막에 빈 페이지를 삽입하는 방법을 보여줍니다.

```cs
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 으로 이동하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// 문서 열기
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// PDF 파일 끝에 빈 페이지 삽입
pdfDocument.Pages.Add();

// 출력 파일 저장
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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

