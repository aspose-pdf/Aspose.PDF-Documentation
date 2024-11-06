---
title: PDF에서 제목 작업하기
type: docs
weight: 40
url: ko/python-net/working-with-headings/
description: Python을 사용하여 PDF 문서의 제목에 번호 매기기를 생성합니다. Aspose.PDF for Python via .NET은 다양한 종류의 번호 매기기 스타일을 제공합니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 제목 작업하기",
    "alternativeHeadline": "PDF에서 제목 생성하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, headings in pdf",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2022-02-04",
    "description": "Python을 사용하여 PDF 문서의 제목에 번호 매기기를 생성합니다. Aspose.PDF for Python via .NET은 다양한 종류의 번호 매기기 스타일을 제공합니다."
}
</script>


## 제목에 번호 스타일 적용

제목은 문서의 중요한 부분입니다. 작가들은 항상 제목을 독자들에게 더 두드러지고 의미 있게 만들려고 합니다. 문서에 여러 개의 제목이 있는 경우, 작가는 이러한 제목을 구성하기 위한 여러 옵션을 가지고 있습니다. 제목을 구성하는 가장 일반적인 접근 방식 중 하나는 제목을 번호 스타일로 작성하는 것입니다.

[Aspose.PDF for Python via .NET](/pdf/python-net/)은 많은 사전 정의된 번호 스타일을 제공합니다. 이러한 사전 정의된 번호 스타일은 열거형인 [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/)에 저장되어 있습니다. NumberingStyle 열거형의 사전 정의된 값과 그 설명은 아래에 나와 있습니다:

|**제목 유형**|**설명**|
| :- | :- |
|NumeralsArabic|아랍 형식, 예: 1,1.1,...|
|NumeralsRomanUppercase|로마 대문자 형식, 예: I,I.II, ...|
|NumeralsRomanLowercase|로마 소문자 형식, 예: i,i.ii, ...|
|LettersUppercase|영어 대문자 형식, 예: A,A.B, ...|
|LettersLowercase|영어 소문자 형식, 예: a,a.b, ...|
The [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) 속성은 [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) 클래스의 속성으로, 제목의 번호 매기기 스타일을 설정하는 데 사용됩니다.

|**그림: 미리 정의된 번호 매기기 스타일**|
| :- |
위 그림에 표시된 출력을 얻기 위한 소스 코드는 아래 예제에 나와 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.page_info.width = 612.0
    document.page_info.height = 792.0
    document.page_info.margin = ap.MarginInfo()
    document.page_info.margin.left = 72
    document.page_info.margin.right = 72
    document.page_info.margin.top = 72
    document.page_info.margin.bottom = 72

    page = document.pages.add()
    page.page_info.width = 612.0
    page.page_info.height = 792.0
    page.page_info.margin = ap.MarginInfo()
    page.page_info.margin.left = 72
    page.page_info.margin.right = 72
    page.page_info.margin.top = 72
    page.page_info.margin.bottom = 72

    float_box = ap.FloatingBox()
    float_box.margin = page.page_info.margin

    page.paragraphs.add(float_box)

    heading = ap.Heading(1)
    heading.is_in_list = True
    heading.start_number = 1
    heading.text = "목록 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "목록 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "계획의 발효일 현재 계획에 따라 분배될 자산의 가치를 각 허용된"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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
    "applicationCategory": "Python용 .NET을 통한 PDF 조작 라이브러리",
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