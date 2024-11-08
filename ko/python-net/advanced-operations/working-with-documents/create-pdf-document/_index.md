---
title: Python을 사용하여 PDF 생성하는 방법
linktitle: PDF 문서 생성
type: docs
weight: 10
url: /ko/python-net/create-pdf-document/
description: Aspose.PDF for Python via .NET으로 PDF 문서를 생성하고 형식화합니다.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF 생성하는 방법",
    "alternativeHeadline": "Python을 통해 처음부터 PDF 문서 생성",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, dotnet, pdf 문서 생성",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NET으로 PDF 문서를 생성하고 형식화합니다."
}
</script>


**Aspose.PDF for Python via .NET**는 개발자가 .NET 응용 프로그램용 Python에서 몇 줄의 코드만으로 PDF 파일을 생성, 로드, 수정 및 변환할 수 있도록 하는 PDF 조작 API입니다.

## 간단한 PDF 파일 생성 방법

Aspose.PDF를 사용하여 Python을 통해 .NET에서 PDF를 생성하려면 다음 단계를 따르십시오:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
1. Document 객체의 [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 컬렉션에 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 추가합니다.
1. 페이지의 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap

    # 문서 객체 초기화
    document = ap.Document()
    # 페이지 추가
    page = document.pages.add()
    # 새 페이지에 텍스트 추가
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # 업데이트된 PDF 저장
    document.save(output_pdf)
```