---
title: Python으로 PDF 포트폴리오 작업하기
linktitle: 포트폴리오
type: docs
weight: 20
url: ko/python-net/portfolio/
description: Python으로 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 만들어야 합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python으로 PDF 포트폴리오 작업하기",
    "alternativeHeadline": "PDF 문서에서 포트폴리오 만들기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성 in pdf",
    "keywords": "pdf, python, 포트폴리오",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Python으로 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 만들어야 합니다."
}
</script>


PDF 포트폴리오를 생성하면 다양한 유형의 파일을 하나의 일관된 문서로 통합하고 보관할 수 있습니다. 이러한 문서에는 텍스트 파일, 이미지, 스프레드시트, 프레젠테이션 및 기타 자료가 포함될 수 있으며 모든 관련 자료가 한 곳에 저장되고 정리되도록 합니다.

PDF 포트폴리오는 이를 사용하는 어디서나 고품질로 프레젠테이션을 보여줄 수 있도록 도와줍니다. 일반적으로 PDF 포트폴리오를 생성하는 것은 매우 현재적이고 현대적인 작업입니다.

## PDF 포트폴리오 생성 방법

Aspose.PDF for Python via .NET은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 클래스를 사용하여 가져온 후 document.collection 객체에 파일을 추가합니다. 파일이 추가되면 Document 클래스의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 포트폴리오 문서를 저장합니다.

다음 예제에서는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래 코드는 다음 포트폴리오를 생성합니다.

### Python용 Aspose.PDF로 생성된 PDF 포트폴리오

![Python용 Aspose.PDF로 생성된 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # 문서 객체 인스턴스화
    document = ap.Document()

    # 문서 컬렉션 객체 인스턴스화
    document.collection = ap.Collection()

    # 포트폴리오에 추가할 파일 가져오기
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # 파일 설명 제공
    excel.description = "엑셀 파일"
    word.description = "워드 파일"
    image.description = "이미지 파일"

    # 문서 컬렉션에 파일 추가
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # 포트폴리오 문서 저장
    document.save(output_pdf)
```

## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 줄을 사용해 보세요.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    document.collection.delete()

    # 업데이트된 파일 저장
    document.save(output_pdf)
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
    "applicationCategory": "PDF 조작 라이브러리 for Python",
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