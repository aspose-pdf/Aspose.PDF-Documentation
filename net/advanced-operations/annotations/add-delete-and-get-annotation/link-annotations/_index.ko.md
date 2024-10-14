---
title: PDF에서 링크 주석 사용하기
linktitle: 링크 주석
type: docs
weight: 70
url: /net/link-annotations/
description: Aspose.PDF for .NET을 사용하면 PDF 문서에서 링크 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에 대한 링크 주석 사용",
    "alternativeHeadline": "PDF에 링크 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 텍스트 주석",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다."
}
</script>
## 기존 PDF 파일에 링크 주석 추가

> 다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

[링크 주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)은 하이퍼링크, 다른 곳의 목적지, 문서를 나타냅니다. PDF 표준에 따르면 링크 주석은 세 가지 경우에 사용할 수 있습니다: 페이지 뷰 열기, 파일 열기, 웹 페이지 열기.

### 페이지 뷰를 열기 위해 링크 주석 사용하기

주석을 생성하기 위해 몇 가지 추가 단계가 수행되었습니다. 데모를 위해 텍스트 조각을 찾기 위해 2개의 TextFragmentAbsorbers를 사용했습니다. 첫 번째는 링크 주석 텍스트용이고, 두 번째는 문서의 일부 장소를 나타냅니다.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
주석을 생성하기 위해 우리는 몇 가지 단계를 따랐습니다:

1. `LinkAnnotation`을 생성하고 페이지 객체와 주석과 대응하는 텍스트 단편의 사각형을 전달하세요.
1. `Action`을 `GoToAction`으로 설정하고 원하는 목적지로 `XYZExplicitDestination`을 전달하세요. 원하는 목적지를 페이지, 왼쪽 좌표, 상단 좌표, 확대 비율을 기반으로 `XYZExplicitDestination`을 생성했습니다.
1. 페이지 주석 컬렉션에 주석을 추가하세요.
1. 문서를 저장하세요.

### 명명된 목적지를 사용하는 링크 주석

다양한 문서를 처리할 때, 타이핑을 하면서 주석이 가리킬 위치를 모르는 상황이 발생합니다.
이 경우 특별한 (명명된) 목적지를 사용할 수 있으며 코드는 다음과 같이 보일 것입니다:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

다른 장소에서 명명된 목적지를 생성할 수 있습니다.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### 파일을 열기 위한 링크 주석 사용

위의 예제들에서 사용된 것과 동일한 접근 방식이 파일을 열기 위한 주석을 생성할 때 사용됩니다.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

차이점은 `GoToAction` 대신 `GoToRemoteAction`을 사용한다는 것입니다. GoToRemoteAction의 생성자는 파일 이름과 페이지 번호 두 가지 매개변수를 받습니다.
또 다른 형태를 사용하여 파일 이름과 일부 목적지를 전달할 수 있습니다. 명백히, 그것을 사용하기 전에 해당 목적지를 생성해야 합니다.

### 웹 페이지를 열기 위한 링크 주석 사용

웹 페이지를 열려면 `Action`을 `GoToURIAction` 객체로 설정하십시오.
생성자 매개변수로 하이퍼링크 또는 다른 종류의 URI를 전달할 수 있습니다. 예를 들어, 전화 번호를 호출하는 작업을 구현하기 위해 `callto`를 사용할 수 있습니다.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // 링크 주석을 생성하고 전화 번호를 호출하는 작업을 설정
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## 장식된 링크 주석 추가

테두리를 사용하여 링크 주석을 사용자 정의할 수 있습니다. 아래 예제에서는 너비가 3pt인 파란색 점선 테두리를 만들 것입니다.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

또 다른 예제는 브라우저 스타일을 시뮬레이션하고 링크에 밑줄을 사용하는 방법을 보여줍니다.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### 링크 주석 가져오기

PDF 문서에서 LinkAnnotation을 가져오려면 다음 코드 스니펫을 사용해 보십시오.

```csharp
class ExampleLinkAnnotations
{
    // 문서 디렉토리 경로.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // PDF 파일 로드
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // 각 링크 주석의 URL 출력
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // 하이퍼링크와 관련된 텍스트 출력
            Console.WriteLine(extractedText);
        }
    }
}
```
### 링크 주석 삭제

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 1페이지의 모든 링크 주석을 찾아서 제거해야 합니다. 이후 주석이 제거된 문서를 저장합니다.

```csharp
class ExampleLinkAnnotations
{
    // 문서 디렉토리 경로.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // PDF 파일 로드
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // 1페이지의 모든 링크 주석 찾기 및 삭제
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // 주석이 제거된 문서 저장
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
