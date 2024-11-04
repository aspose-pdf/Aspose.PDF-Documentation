---
title: Python을 사용하여 PDF에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: 이 섹션에서는 Python 라이브러리를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF에 이미지 추가",
    "alternativeHeadline": "PDF에 이미지 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf에 이미지 추가",
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
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 Python 라이브러리를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다."
}
</script>


## 기존 PDF 파일에 이미지 추가하기

다음 코드 스니펫은 PDF 파일에 이미지를 추가하는 방법을 보여줍니다.

1. 입력 PDF 파일을 로드합니다.
1. 이미지가 배치될 페이지 번호를 지정합니다.
1. 페이지에서 이미지의 위치를 정의하려면 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스의 [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출합니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## 기존 PDF 파일에 이미지 추가하기 (Facades)

PDF 파일에 이미지를 추가하는 또 다른 간단한 방법도 있습니다.
 [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/) 클래스의 [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 메서드를 사용할 수 있습니다. [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) 메서드는 추가할 이미지, 이미지를 추가해야 하는 페이지 번호 및 좌표 정보를 필요로 합니다. 그런 다음, 업데이트된 PDF 파일을 저장하고 [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) 메서드를 사용하여 PdfFileMend 객체를 닫습니다. 다음 코드 스니펫은 기존 PDF 파일에 이미지를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    mender = ap.facades.PdfFileMend()

    # 텍스트를 추가할 PdfFileMend 객체 생성
    mender.bind_pdf(input_file)

    # PDF 파일에 이미지 추가
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # 변경 사항 저장
    mender.save(output_pdf)

    # PdfFileMend 객체 닫기
    mender.close()

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
    "applicationCategory": "Python용 PDF 조작 라이브러리",
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