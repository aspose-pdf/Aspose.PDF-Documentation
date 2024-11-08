---
title: .NET에서 아티팩트 다루기
linktitle: 아티팩트 다루기
type: docs
weight: 110
url: /ko/net/artifacts/
description: Aspose.PDF for .NET을 사용하면 PDF 페이지에 배경 이미지를 추가하고 Artifact 클래스를 사용하여 각 워터마크를 가져올 수 있습니다.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": ".NET에서 아티팩트 다루기",
    "alternativeHeadline": "PDF 문서의 아티팩트",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서의 아티팩트",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 PDF 페이지에 배경 이미지를 추가하고 Artifact 클래스를 사용하여 각 워터마크를 가져올 수 있습니다."
}
</script>
PDF의 아티팩트는 문서의 실제 내용이 아닌 그래픽 객체나 기타 요소입니다. 일반적으로 장식, 레이아웃 또는 배경 목적으로 사용됩니다. 아티팩트의 예는 페이지 헤더, 푸터, 구분선 또는 의미를 전달하지 않는 이미지를 포함합니다.

PDF에서 아티팩트의 목적은 내용 요소와 비내용 요소를 구분할 수 있게 하는 것입니다. 이는 접근성에 중요하며, 화면 독자 및 기타 보조 기술이 아티팩트를 무시하고 관련 내용에 집중할 수 있습니다. 아티팩트는 인쇄, 검색 또는 복사에서 생략될 수 있기 때문에 PDF 문서의 성능과 품질을 향상시킬 수도 있습니다.

PDF에서 요소를 아티팩트로 생성하려면 [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 클래스를 사용해야 합니다.
다음과 같은 유용한 속성을 포함합니다:

- **Artifact.Type** – 아티팩트 유형을 가져옵니다(배경, 레이아웃, 페이지, 페이지 번호 및 정의되지 않음을 포함하는 Artifact.ArtifactType 열거형 값 지원).
- **Artifact.Type** – 아티팩트 유형을 가져옵니다 (Artifact.ArtifactType 열거형의 값 지원, 값에는 Background, Layout, Page, Pagination 및 Undefined가 포함됩니다).
- **Artifact.Subtype** – 아티팩트 하위 유형을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값 지원, 값에는 Background, Footer, Header, Undefined, Watermark가 포함됩니다).
- **Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있으면 해당 이미지, 그렇지 않으면 null).
- **Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.
- **Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
- **Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용된 경우). 워터마크, 헤더 및 푸터 아티팩트는 모든 아티팩트 컨텐츠를 보여주는 XForm을 포함합니다.
- **Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.
- **Artifact.Rotation** – 아티팩트의 회전을 가져옵니다 (도 단위, 양의 값은 반시계 방향 회전을 나타냅니다).
- **Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다.
- **Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다.

다음 클래스들도 아티팩트 작업에 유용할 수 있습니다:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## 기존 워터마크 작업

Adobe Acrobat으로 생성된 워터마크는 아티팩트라고 불립니다(14.8.2.2 실제 콘텐츠와 아티팩트의 PDF 사양에서 설명).

특정 페이지의 모든 워터마크를 가져오기 위해, [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스에는 Artifacts 속성이 있습니다.

다음 코드 스니펫은 PDF 파일의 첫 페이지에 있는 모든 워터마크를 가져오는 방법을 보여줍니다.

_참고:_ 이 코드는 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.
_Note:_ 이 코드는 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## 배경으로서의 아티팩트 다루기

배경 이미지는 문서에 워터마크나 기타 미묘한 디자인을 추가하는 데 사용될 수 있습니다. Aspose.PDF for .NET에서 각 PDF 문서는 페이지들의 모음이며 각 페이지는 아티팩트의 모음을 포함합니다. [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) 클래스를 사용하여 페이지 객체에 배경 이미지를 추가할 수 있습니다.

다음 코드 스니펫은 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
만약 여러분이 어떤 이유로 단색 배경을 사용하고 싶다면, 이전 코드를 다음과 같이 변경하세요:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## 특정 유형의 아티팩트 카운팅

특정 유형의 아티팩트(예를 들어, 워터마크의 총 개수)의 총 개수를 계산하려면 다음 코드를 사용하세요:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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

