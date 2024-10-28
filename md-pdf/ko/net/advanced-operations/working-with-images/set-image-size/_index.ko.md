---
title: 이미지 크기 설정
linktitle: 이미지 크기 설정
type: docs
weight: 80
url: /net/set-image-size/
description: 이 섹션에서는 C# 라이브러리를 사용하여 PDF 파일의 이미지 크기를 설정하는 방법을 설명합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "이미지 크기 설정",
    "alternativeHeadline": "C#을 사용하여 PDF 파일의 이미지 크기를 설정하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 이미지 크기 설정",
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
    "url": "/net/set-image-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-image-size/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 C# 라이브러리를 사용하여 PDF 파일의 이미지 크기를 설정하는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

PDF 파일에 추가되는 이미지의 크기를 설정할 수 있습니다. 크기를 설정하려면 Aspose.Pdf.Image 클래스의 FixWidth 및 FixHeight 속성을 사용할 수 있습니다. 다음 코드 스니펫은 이미지 크기를 설정하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Document 객체 인스턴스화
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지 추가
Aspose.Pdf.Page page = doc.Pages.Add();
// 이미지 인스턴스 생성
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// 포인트 단위로 이미지 너비와 높이 설정
img.FixWidth = 100;
img.FixHeight = 100;
// 이미지 유형을 SVG로 설정
img.FileType = Aspose.Pdf.ImageFileType.Unknown;
// 소스 파일 경로
img.File = dataDir + "aspose-logo.jpg";
page.Paragraphs.Add(img);
// 페이지 속성 설정
page.PageInfo.Width = 800;
page.PageInfo.Height = 800;
dataDir = dataDir + "SetImageSize_out.pdf";
// 결과 PDF 파일 저장
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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

