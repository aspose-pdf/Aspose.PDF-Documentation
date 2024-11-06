---
title: C#를 사용하여 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: ko/net/image-stamps-in-pdf-page/
description: Aspose.PDF 라이브러리를 사용하여 PDF 문서에 ImageStamp 클래스로 이미지 스탬프를 추가합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 PDF에 이미지 스탬프 추가",
    "alternativeHeadline": "C#를 사용하여 PDF에 이미지 스탬프 추가",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDF 문서 생성",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF 라이브러리를 사용하여 PDF 문서에 ImageStamp 클래스로 이미지 스탬프를 추가합니다."
}
</script>

## PDF 파일에 이미지 스탬프 추가하기

PDF 파일에 이미지 스탬프를 추가하기 위해 ImageStamp 클래스를 사용할 수 있습니다. ImageStamp 클래스는 높이, 너비, 불투명도 등과 같은 이미지 기반 스탬프를 생성하는 데 필요한 속성들을 제공합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

이미지 스탬프를 추가하는 방법:

1. 필요한 속성을 사용하여 Document 객체와 ImageStamp 객체를 생성합니다.
1. PDF에 스탬프를 추가하기 위해 Page 클래스의 AddStamp 메소드를 호출합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// 이미지 스탬프 생성
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// 특정 페이지에 스탬프 추가
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
## 도장 추가 시 이미지 품질 제어

도장 객체로 이미지를 추가할 때 이미지의 품질을 제어할 수 있습니다. ImageStamp 클래스의 Quality 속성을 이용하여 이를 수행합니다. 이는 이미지의 품질을 퍼센트로 나타냅니다 (유효 값은 0..100).

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// 이미지 도장 생성
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## 플로팅 박스에서 배경으로 이미지 도장 사용

Aspose.PDF API를 사용하면 플로팅 박스에서 배경으로 이미지 도장을 추가할 수 있습니다.
Aspose.PDF API는 부유 상자에 배경으로 이미지 스탬프를 추가할 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Document 객체를 인스턴스화합니다.
Document doc = new Document();
// PDF 문서에 페이지를 추가합니다.
Page page = doc.Pages.Add();
// FloatingBox 객체를 생성합니다.
FloatingBox aBox = new FloatingBox(200, 100);
// FloatingBox의 왼쪽 위치를 설정합니다.
aBox.Left = 40;
// FloatingBox의 상단 위치를 설정합니다.
aBox.Top = 80;
// FloatingBox의 수평 정렬을 설정합니다.
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// FloatingBox의 단락 컬렉션에 텍스트 조각을 추가합니다.
aBox.Paragraphs.Add(new TextFragment("main text"));
// FloatingBox에 테두리를 설정합니다.
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// 배경 이미지를 추가합니다.
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// FloatingBox의 배경색을 설정합니다.
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// 페이지 객체의 단락 컬렉션에 FloatingBox를 추가합니다.
page.Paragraphs.Add(aBox);
// PDF 문서를 저장합니다.
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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

