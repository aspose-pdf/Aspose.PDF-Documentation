---
title: Python을 사용하여 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 40
url: ko/python-net/add-watermarks/
description: 이 문서는 Python을 사용하여 PDF에서 아티팩트를 작업하고 워터마크를 얻는 기능을 설명합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF에 워터마크 추가",
    "alternativeHeadline": "PDF에 워터마크 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf,python, 워터마크 추가",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 Python을 사용하여 PDF에서 아티팩트를 작업하고 워터마크를 얻는 기능을 설명합니다."
}
</script>


**Aspose.PDF for Python via .NET**은 아티팩트를 사용하여 PDF 문서에 워터마크를 추가할 수 있습니다. 이 기사를 확인하여 작업을 해결하십시오.

아티팩트와 작업하려면 Aspose.PDF에는 두 개의 클래스가 있습니다: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/)와 [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

특정 페이지의 모든 아티팩트를 가져오기 위해, [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스에는 Artifacts 속성이 있습니다. 이 주제는 PDF 파일에서 아티팩트와 작업하는 방법을 설명합니다.

## 아티팩트 작업하기

[Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 클래스는 다음과 같은 속성을 포함합니다:

**contents** – 아티팩트 내부 연산자의 컬렉션을 가져옵니다. 지원되는 유형은 System.Collections.ICollection입니다.
**form** – 아티팩트의 XForm을 가져옵니다 (XForm이 사용된 경우). 워터마크, 헤더, 푸터 아티팩트는 모든 아티팩트 내용을 보여주는 XForm을 포함합니다.

**image** – 아티팩트의 이미지를 가져옵니다 (이미지가 있는 경우, 그렇지 않으면 null).
**text** – 아티팩트의 텍스트를 가져옵니다.  
**rectangle** – 페이지에서 아티팩트의 위치를 가져옵니다.  
**rotation** – 아티팩트의 회전을 가져옵니다 (도 단위, 양수 값은 반시계 방향 회전을 나타냅니다).  
**opacity** – 아티팩트의 불투명도를 가져옵니다. 가능한 값은 0에서 1 사이이며, 1은 완전히 불투명합니다.

## 프로그래밍 샘플: PDF 파일에 워터마크 추가하는 방법

다음 코드 스니펫은 Python을 사용하여 PDF 파일의 첫 페이지에 있는 각 워터마크를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Python을 위한 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>