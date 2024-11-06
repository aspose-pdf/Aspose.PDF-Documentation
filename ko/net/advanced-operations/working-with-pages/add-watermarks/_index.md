---
title: C#을 사용하여 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 90
url: ko/net/add-watermarks/
description: 이 문서는 C#을 프로그래밍 방식으로 PDF에서 아티팩트를 작업하고 워터마크를 얻는 기능에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용하여 PDF에 워터마크 추가",
    "alternativeHeadline": "PDF에 워터마크 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 워터마크 추가",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 C#을 프로그래밍 방식으로 PDF에서 아티팩트를 작업하고 워터마크를 얻는 기능에 대해 설명합니다."
}
</script>

**Aspose.PDF for .NET** 은 Artifacts를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 이 문서를 확인하여 작업을 해결하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

Adobe Acrobat으로 생성된 워터마크는 아티팩트(14.8.2.2 PDF 사양의 실제 콘텐츠 및 아티팩트에서 설명)라고 합니다. 아티팩트를 다루기 위해 Aspose.PDF는 [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 클래스와 [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection) 클래스를 가지고 있습니다.

특정 페이지의 모든 아티팩트를 가져오기 위해 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스에는 Artifacts 속성이 있습니다. 이 주제는 PDF 파일에서 아티팩트를 다루는 방법을 설명합니다.

## 아티팩트 다루기

[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 클래스는 다음과 같은 속성을 포함합니다:

**Artifact.Type** – 아티팩트 유형을 가져옵니다(아티팩트.ArtifactType 열거형의 값을 지원하며 배경, 레이아웃, 페이지, 페이지 번호 및 정의되지 않음을 포함합니다).
**Artifact.Type** – 아티팩트 타입을 가져옵니다 (Artifact.ArtifactType 열거형의 값 지원, 값에는 Background, Layout, Page, Pagination 및 Undefined가 포함됩니다).
**Artifact.Subtype** – 아티팩트 하위 타입을 가져옵니다 (Artifact.ArtifactSubtype 열거형의 값 지원, 값에는 Background, Footer, Header, Undefined, Watermark가 포함됩니다).

{{% alert color="primary" %}}

Adobe Acrobat으로 생성된 워터마크는 타입이 Pagination이고 하위 타입이 Watermark입니다.

{{% /alert %}}

**Artifact.Contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 타입은 System.Collections.ICollection입니다.
**Artifact.Form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용된 경우). 워터마크, 헤더 및 푸터 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.
**Artifact.Image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있으면, 그렇지 않으면 null).
**Artifact.Text** – 아티팩트의 텍스트를 가져옵니다.
**Artifact.Rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.
**Artifact.Rotation** – 아티팩트의 회전을 가져옵니다 (도 단위, 양수 값은 반시계 방향 회전을 나타냅니다).
**Artifact.Rotation** – 아티팩트의 회전(도 단위, 양수 값은 반시계 방향 회전을 나타냄)을 가져옵니다.
**Artifact.Opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0…1 범위이며, 1은 완전 불투명을 의미합니다.

## 프로그래밍 예제: PDF 파일에 워터마크 추가 방법

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 첫 페이지에 각 워터마크를 얻는 방법을 보여줍니다.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
}
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

