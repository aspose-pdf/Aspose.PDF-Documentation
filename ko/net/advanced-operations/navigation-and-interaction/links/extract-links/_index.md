---
title: PDF 파일에서 링크 추출
linktitle: 링크 추출
type: docs
weight: 30
url: /ko/net/extract-links/
description: C#을 사용하여 PDF에서 링크를 추출합니다. 이 주제는 AnnotationSelector 클래스를 사용하여 링크를 추출하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에서 링크 추출",
    "alternativeHeadline": "PDF에서 링크 추출하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서 링크 추출",
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
    "url": "/net/extract-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-links/"
    },
    "dateModified": "2022-02-04",
    "description": "C#을 사용하여 PDF에서 링크를 추출합니다. 이 주제는 AnnotationSelector 클래스를 사용하여 링크를 추출하는 방법을 설명합니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일에서 링크 추출

링크는 PDF 파일에서 주석으로 표현되므로 링크를 추출하려면 모든 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 추출합니다.

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 링크를 추출할 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 클래스를 사용하여 지정된 페이지에서 모든 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 추출합니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 객체를 페이지 객체의 Accept 메서드에 전달합니다.
다음 코드 스니펫은 PDF 파일에서 링크를 추출하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// 문서 열기
Document document = new Document(dataDir+ "ExtractLinks.pdf");
// 작업 추출
Page page = document.Pages[1];
AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
page.Accept(selector);
IList<Annotation> list = selector.Selected;
Annotation annotation = (Annotation)list[0];
dataDir = dataDir + "ExtractLinks_out.pdf";
// 업데이트된 문서 저장
document.Save(dataDir);
```

