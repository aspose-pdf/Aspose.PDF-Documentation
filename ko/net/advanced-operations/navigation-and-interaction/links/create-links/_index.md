---
title: Create Links in PDF file with C#
linktitle: Create Links
type: docs
weight: 10
url: /ko/net/create-links/
description: 이 섹션에서는 C#을 사용하여 PDF 문서에 링크를 생성하는 방법에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "How to create Links in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, create link in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 C#을 사용하여 PDF 문서에 링크를 생성하는 방법에 대해 설명합니다."
}
</script>
다음 코드 스니펫도 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서 작동합니다.

## 링크 생성

문서에 애플리케이션 링크를 추가함으로써, 문서에서 애플리케이션으로 링크할 수 있습니다. 이는 예를 들어 튜토리얼의 특정 지점에서 독자가 특정 행동을 취하도록 유도하거나 기능이 풍부한 문서를 만들고자 할 때 유용합니다. 애플리케이션 링크를 생성하는 방법:

1. [문서 생성](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체.
1. 링크를 추가하고자 하는 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. 페이지와 [직사각형](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 사용하여 [링크주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 생성합니다.
1. [링크주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1.
1. [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) 객체를 생성할 때 실행하려는 응용 프로그램을 지정하세요.
1. 링크를 페이지 객체의 [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) 속성에 추가하세요.
1. 마지막으로, 문서 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 업데이트된 PDF를 저장하세요.

다음 코드 조각은 PDF 파일에서 응용 프로그램에 대한 링크를 생성하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// 문서 열기
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// 링크 생성
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// 업데이트된 문서 저장
document.Save(dataDir);
```
### PDF 파일에서 PDF 문서 링크 생성

Aspose.PDF for .NET을 사용하면 외부 PDF 파일에 링크를 추가하여 여러 문서를 연결할 수 있습니다. PDF 문서 링크를 생성하려면:

1. 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 그런 다음 링크를 추가하려는 특정 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. Page 및 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1. Action 속성을 [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction) 객체로 설정합니다.
1.
1. 페이지 객체의 주석 컬렉션에 링크를 추가하세요.
1. 문서 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 업데이트된 PDF를 저장하세요.

다음 코드 스니펫은 PDF 파일에서 PDF 문서 링크를 생성하는 방법을 보여줍니다.

 ```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// 문서 열기
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// 링크 생성
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// 업데이트된 문서 저장
document.Save(dataDir);
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

