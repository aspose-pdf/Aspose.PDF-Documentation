---
title: PDF C#에 텍스트 스탬프 추가
linktitle: PDF 파일에 텍스트 스탬프
type: docs
weight: 20
url: /ko/net/text-stamps-in-the-pdf-file/
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에 텍스트 스탬프를 추가합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF C#에 텍스트 스탬프 추가",
    "alternativeHeadline": "PDF C#에 텍스트 스탬프 추가",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에 텍스트 스탬프를 추가합니다."
}
</script>
## C#을 사용하여 텍스트 스탬프 추가

[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) 클래스를 사용하여 PDF 파일에 텍스트 스탬프를 추가할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등과 같이 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 텍스트 스탬프를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, PDF에 스탬프를 추가하기 위해 페이지의 AddStamp 메소드를 호출할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// 텍스트 스탬프 생성
TextStamp textStamp = new TextStamp("Sample Stamp");
// 스탬프가 배경인지 설정
textStamp.Background = true;
// 원점 설정
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// 스탬프 회전
textStamp.Rotate = Rotation.on90;
// 텍스트 속성 설정
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// 특정 페이지에 스탬프 추가
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
## TextStamp 객체의 정렬 정의

PDF 문서에 워터마크를 추가하는 것은 자주 요구되는 기능 중 하나이며 Aspose.PDF for .NET은 이미지뿐만 아니라 텍스트 워터마크를 추가할 수 있습니다. [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp)라는 클래스는 PDF 파일 위에 텍스트 스탬프를 추가하는 기능을 제공합니다. 최근에는 TextStamp 객체를 사용할 때 텍스트의 정렬을 지정하는 기능을 지원하는 요구사항이 있었습니다. 이 요구사항을 충족시키기 위해 TextStamp 클래스에 TextAlignment 속성을 도입했습니다. 이 속성을 사용하여 수평 텍스트 정렬을 지정할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서를 로드하고 그 위에 TextStamp를 추가하는 예를 보여줍니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// 입력 파일로 Document 객체를 인스턴스화합니다.
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// 샘플 문자열로 FormattedText 객체를 인스턴스화합니다.
FormattedText text = new FormattedText("This");
// FormattedText에 새 텍스트 라인을 추가합니다.
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// FormattedText를 사용하여 TextStamp 객체를 생성합니다.
TextStamp stamp = new TextStamp(text);
// 텍스트 스탬프의 수평 정렬을 중앙 정렬로 지정합니다.
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// 텍스트 스탬프의 수직 정렬을 중앙 정렬로 지정합니다.
stamp.VerticalAlignment = VerticalAlignment.Center;
// TextStamp의 텍스트 수평 정렬을 중앙 정렬로 지정합니다.
stamp.TextAlignment = HorizontalAlignment.Center;
// 스탬프 객체에 위쪽 마진을 설정합니다.
stamp.TopMargin = 20;
// 문서의 첫 페이지에 스탬프 객체를 추가합니다.
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// 업데이트된 문서를 저장합니다.
doc.Save(dataDir);
```
## PDF 파일에 스트로크 텍스트 스탬프 채우기

텍스트 추가 및 편집 시나리오에 대한 렌더링 모드 설정을 구현했습니다. 스트로크 텍스트를 렌더링하려면 TextState 객체를 생성하고 RenderingMode를 TextRenderingMode.StrokeText로 설정한 다음 StrokingColor 속성에 대한 색상을 선택하십시오. 나중에 BindTextState() 메서드를 사용하여 스탬프에 TextState를 바인딩합니다.

다음 코드 스니펫은 스트로크 텍스트 채우기를 추가하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// 고급 속성을 전달하는 TextState 객체를 생성합니다.
TextState ts = new TextState();
// 스트로크 색상 설정
ts.StrokingColor = Color.Gray;
// 텍스트 렌더링 모드 설정
ts.RenderingMode = TextRenderingMode.StrokeText;
// 입력 PDF 문서를 로드합니다.
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// TextState 바인드
stamp.BindTextState(ts);
// X, Y 원점 설정
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// 스탬프 추가
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "영어"
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

