---
title: PDF에 헤더와 푸터 추가
linktitle: PDF에 헤더와 푸터 추가
type: docs
weight: 70
url: /ko/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET은 TextStamp 클래스를 사용하여 PDF 파일에 헤더와 푸터를 추가할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에 헤더와 푸터 추가",
    "alternativeHeadline": "PDF 파일에 헤더와 푸터를 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에 헤더 추가, pdf에 푸터 추가",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET은 TextStamp 클래스를 사용하여 PDF 파일에 헤더와 푸터를 추가할 수 있습니다."
}
</script>
**Aspose.PDF for .NET**은 기존 PDF 파일에 헤더와 푸터를 추가할 수 있습니다. PDF 문서에 이미지나 텍스트를 추가할 수도 있습니다. 또한 C#을 사용하여 한 PDF 파일에 다른 헤더를 추가해 보세요.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일 헤더에 텍스트 추가

[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) 클래스를 사용하여 PDF 파일의 헤더에 텍스트를 추가할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등과 같은 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 텍스트를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, PDF의 헤더에 텍스트를 추가하기 위해 Page의 AddStamp 메소드를 호출할 수 있습니다.

TopMargin 속성을 설정하여 PDF의 헤더 영역에 텍스트가 조정되도록 해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Top으로 설정해야 합니다.

다음 코드 스니펫은 C#을 사용하여 PDF 파일 헤더에 텍스트를 추가하는 방법을 보여줍니다.
다음 코드 스니펫은 C#을 사용하여 PDF 파일의 헤더에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// 헤더 생성
TextStamp textStamp = new TextStamp("헤더 텍스트");
// 스탬프의 속성 설정
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// 모든 페이지에 헤더 추가
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// 업데이트된 문서 저장
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## PDF 파일의 푸터에 텍스트 추가

TextStamp 클래스를 사용하여 PDF 파일의 푸터에 텍스트를 추가할 수 있습니다.
TextStamp 클래스를 사용하여 PDF 파일의 바닥글에 텍스트를 추가할 수 있습니다.

{{% alert color="primary" %}}

PDF의 바닥글 영역에 텍스트를 조정하려면 하단 여백 속성을 설정해야 합니다. 또한 수평 정렬을 중앙으로, 수직 정렬을 하단으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 바닥글에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// 바닥글 생성
TextStamp textStamp = new TextStamp("Footer Text");
// 스탬프의 속성 설정
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// 모든 페이지에 바닥글 추가
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// 결과 파일 저장
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## PDF 파일 헤더에 이미지 추가하기

[ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) 클래스를 사용하여 PDF 파일의 헤더에 이미지를 추가할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 이미지를 추가하려면 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그 후, PDF의 헤더에 이미지를 추가하기 위해 Page의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메소드를 호출할 수 있습니다.

{{% alert color="primary" %}}

TopMargin 속성을 설정하여 PDF의 헤더 영역에 이미지가 조정되도록 해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Top으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일 헤더에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예시와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// 헤더 생성
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// 스탬프의 속성 설정
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// 모든 페이지에 헤더 추가
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// 출력 파일 저장
pdfDocument.Save(dataDir + "ImageinHeader_out.pdf");
```
## PDF 파일의 바닥글에 이미지 추가

PDF 파일의 바닥글에 이미지를 추가하려면 Image Stamp 클래스를 사용할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 바닥글에 이미지를 추가하려면 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그 후에는 PDF의 바닥글에 이미지를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

{{% alert color="primary" %}}

PDF의 바닥글 영역에 이미지를 조정하도록 [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) 속성을 설정해야 합니다. 또한 [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment)을 `Center`로, [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment)을 `Bottom`으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다.
다음 코드 스니펫은 C#을 사용하여 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// 바닥글 생성
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// 도장의 속성 설정
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// 모든 페이지에 바닥글 추가
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// 결과 파일 저장
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## 한 PDF 파일에 다양한 머리글 추가

문서의 머리글/바닥글 섹션에 TextStamp를 추가할 때 TopMargin 또는 Bottom Margin 속성을 사용할 수 있지만, 때때로 단일 PDF 문서에 여러 머리글/바닥글을 추가해야 할 필요성이 있을 수 있습니다.
문서의 헤더/푸터 섹션에 TextStamp를 추가할 수 있는 것은 알고 있지만, 때로는 단일 PDF 문서에 여러 헤더/푸터를 추가해야 할 필요가 있을 수 있습니다.

이 요구 사항을 충족하기 위해 개별 TextStamp 객체를 생성하고(객체 수는 필요한 헤더/푸터의 수에 따라 다름) PDF 문서에 추가할 것입니다. 또한 개별 스탬프 객체에 대한 다른 서식 정보를 지정할 수도 있습니다. 다음 예제에서는 Document 객체와 세 개의 TextStamp 객체를 생성한 다음, PDF의 헤더 섹션에 텍스트를 추가하기 위해 페이지의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메소드를 사용했습니다. 다음 코드 스니펫은 Aspose.PDF for .NET을 사용하여 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open source document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Create three stamps
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// Set stamp alignment (place stamp on page top, centered horiznotally)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Specify the font style as Bold
stamp1.TextState.FontStyle = FontStyles.Bold;
// Set the text fore ground color information as red
stamp1.TextState.ForegroundColor = Color.Red;
// Specify the font size as 14
stamp1.TextState.FontSize = 14;

// Now we need to set the vertical alignment of 2nd stamp object as Top
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Set Horizontal alignment information for stamp as Center aligned
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Set the zooming factor for stamp object
stamp2.Zoom = 10;

// Set the formatting of 3rd stamp object
// Specify the Vertical alignment information for stamp object as TOP
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Set the Horizontal alignment inforamtion for stamp object as Center aligned
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Set the rotation angle for stamp object
stamp3.RotateAngle = 35;
// Set pink as background color for stamp
stamp3.TextState.BackgroundColor = Color.Pink;
// Change the font face information for stamp to Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// First stamp is added on first page;
doc.Pages[1].AddStamp(stamp1);
// Second stamp is added on second page;
doc.Pages[2].AddStamp(stamp2);
// Third stamp is added on third page.
doc.Pages[3].AddStamp(stamp3);
// Save the updated document
doc.Save(dataDir + "MultiHeader_out.pdf");
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

