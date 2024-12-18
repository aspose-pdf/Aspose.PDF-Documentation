---
title: PDF에서 링크 업데이트
linktitle: 링크 업데이트
type: docs
weight: 20
url: /ko/net/update-links/
description: PDF에서 프로그래밍 방식으로 링크를 업데이트합니다. 이 가이드는 C# 언어로 PDF에서 링크를 업데이트하는 방법에 대한 것입니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 링크 업데이트",
    "alternativeHeadline": "PDF에서 링크를 업데이트하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF에서 링크 업데이트",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "PDF에서 프로그래밍 방식으로 링크를 업데이트합니다. 이 가이드는 C# 언어로 PDF에서 링크를 업데이트하는 방법에 대한 것입니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일에서 링크 업데이트

PDF 파일에 하이퍼링크 추가에서 논의한 것처럼, [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 클래스는 PDF 파일에 링크를 추가할 수 있게 해줍니다. PDF 파일 내부에서 기존 링크를 가져오는 데 사용되는 비슷한 클래스도 있습니다. 기존 링크를 업데이트해야 할 때 이것을 사용하세요. 기존 링크를 업데이트하려면:

1. PDF 파일을 로드하세요.
1. PDF 파일에서 특정 페이지로 이동하세요.
1. [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) 객체의 Destination 속성을 사용하여 링크 목적지를 지정하세요.
1. 목적지 페이지는 [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) 생성자를 사용하여 지정됩니다.

### 동일 문서의 페이지로 링크 대상 설정

다음 코드 조각은 PDF 파일에서 링크를 업데이트하고 그 대상을 문서의 두 번째 페이지로 설정하는 방법을 보여줍니다.
다음 코드 조각은 PDF 파일에서 링크를 업데이트하고 대상을 문서의 두 번째 페이지로 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하실 수 있습니다.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDF 파일을 로드합니다.
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// 문서 첫 페이지의 첫 번째 링크 주석을 가져옵니다.
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// 링크 수정: 링크 목적지 변경
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// 링크 객체에 대한 목적지를 지정합니다.
// 첫 번째 매개변수는 문서 객체, 두 번째는 목적지 페이지 번호입니다.
// 5번째 인수는 해당 페이지를 표시할 때 줌 인수입니다. 2를 사용하면 페이지가 200% 줌으로 표시됩니다.
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// 업데이트된 링크를 포함하여 문서를 저장합니다.
doc.Save(dataDir);
```
### 웹 주소로 링크 목적지 설정

하이퍼링크를 업데이트하여 웹 주소를 가리키도록 하려면 [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) 객체를 인스턴스화하고 LinkAnnotation의 Action 속성에 전달하세요. 다음 코드 스니펫은 PDF 파일의 링크를 업데이트하고 그 목표를 웹 주소로 설정하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDF 파일 로드
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// 문서 첫 페이지에서 첫 번째 링크 주석 가져오기
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// 링크 수정: 링크 작업 변경 및 웹 주소로 목표 설정
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// 업데이트된 링크로 문서 저장
doc.Save(dataDir);
```
### 다른 PDF 파일로 링크 대상 설정

다음 코드 스니펫은 PDF 파일에서 링크를 업데이트하고 그 대상을 다른 PDF 파일로 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDF 파일을 로드합니다.
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// 다음 줄은 목적지를 업데이트합니다, 파일은 업데이트하지 않습니다.
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// 다음 줄은 파일을 업데이트합니다.
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// 링크가 업데이트된 문서를 저장합니다.
document.Save(dataDir);
```

### 링크 주석 텍스트 색상 업데이트

링크 주석은 텍스트를 포함하지 않습니다.
링크 주석에 텍스트가 포함되어 있지 않습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉터리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDF 파일을 로드합니다.
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // 주석 아래의 텍스트를 검색합니다.
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // 텍스트의 색상을 변경합니다.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// 링크가 업데이트된 문서를 저장합니다.
doc.Save(dataDir);
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

