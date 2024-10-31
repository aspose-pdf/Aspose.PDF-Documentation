---
title: 아크로폼 추출 - Python에서 PDF의 양식 데이터 추출
linktitle: 아크로폼 추출
type: docs
weight: 30
url: /python-net/extract-form/
keywords: python에서 pdf 양식 데이터 추출
description: Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 양식을 추출합니다. PDF 파일의 개별 필드에서 값을 가져옵니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "아크로폼 추출",
    "alternativeHeadline": "Python에서 PDF에서 아크로폼 추출하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 아크로폼 추출",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/@AsposePDF",
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
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 양식을 추출합니다. PDF 파일의 개별 필드에서 값을 가져옵니다."
}
</script>


## 폼에서 데이터 추출

### PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오려면 모든 폼 필드를 탐색한 다음 Value 속성을 사용하여 값을 가져와야 합니다. [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/)라는 기본 필드 유형에서 Form 컬렉션에서 각 필드를 가져와 그 [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) 속성에 접근합니다.

다음 Python 코드 스니펫은 PDF 문서의 모든 필드에서 값을 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    pdfDocument = ap.Document(input_file)

    # 모든 필드에서 값 가져오기
    for formField in pdfDocument.form.fields:
        # 필요에 따라 이름과 값을 분석
        print("필드 이름 : " + formField.partial_name)
        print("값 : " + str(formField.value))
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>