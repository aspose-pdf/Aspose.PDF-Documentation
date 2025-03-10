---
title: 스탬프에서 텍스트 추출하기 C#
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/extract-text-from-stamps/
description: Aspose.PDF for .NET의 특별한 기능인 스탬프 주석에서 텍스트 추출하는 방법을 배우십시오.
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text From Stamps using C#",
    "alternativeHeadline": "Extract Text from PDF Stamp Annotations with Ease",
    "abstract": "PDF 문서의 스탬프 주석에서 텍스트를 검색하기 위해 특별히 설계된 Aspose.PDF for .NET의 강력한 텍스트 추출 기능을 발견하십시오. 이 새로운 기능은 프로세스를 간소화하여 개발자가 간결한 코드 스니펫을 사용하여 스탬프 주석 내의 텍스트에 쉽게 접근하고 조작할 수 있도록 하여 PDF 관리 작업의 생산성과 효율성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "168",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/extract-text-from-stamps/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-stamps/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 스탬프 주석에서 텍스트 추출하기

Aspose.PDF for NET를 사용하면 스탬프 주석에서 텍스트를 추출할 수 있습니다. PDF에서 스탬프 주석의 텍스트를 추출하기 위해 다음 단계를 사용할 수 있습니다.

1. `Document` 클래스 객체를 생성합니다.
1. 페이지의 주석 목록에서 원하는 `Annotation`을 가져옵니다.
1. `TextAbsorber` 클래스의 새 객체를 정의합니다.
1. TextAbsorber의 방문 메서드를 사용하여 텍스트를 가져옵니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractStampText.pdf"))
    {
        Aspose.Pdf.Annotations.Annotation item = document.Pages[1].Annotations[1];
        if (item is Aspose.Pdf.Annotations.StampAnnotation annot)
        {
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            Aspose.Pdf.XForm appearance = annot.Appearance["N"];
            absorber.Visit(appearance);
            Console.WriteLine(absorber.Text);
        }
    }
}
```