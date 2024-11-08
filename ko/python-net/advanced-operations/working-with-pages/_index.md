---
title: Python에서 PDF 페이지 작업
linktitle: 페이지 작업
type: docs
weight: 20
url: /ko/python-net/working-with-pages/
description: 페이지 추가, 헤더 및 푸터 추가, 워터마크 추가 방법에 대해 이 섹션에서 알 수 있습니다. Aspose.PDF for Python via .NET은 이 주제에 대한 모든 세부 정보를 설명합니다.
lastmod: "2023-04-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python에서 PDF 페이지 작업",
    "alternativeHeadline": "PDF 페이지 작업 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 페이지, pdf 페이지 추가, 페이지 번호 추가, 페이지 회전, 페이지 삭제",
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
    "url": "/python-net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/working-with-pages/"
    },
    "dateModified": "2023-02-04",
    "description": "페이지 추가, 헤더 및 푸터 추가, 워터마크 추가 방법에 대해 이 섹션에서 알 수 있습니다. Aspose.PDF for Python via .NET은 이 주제에 대한 모든 세부 정보를 설명합니다."
}
</script>


**Aspose.PDF for Python via .NET**을 사용하면 파일의 원하는 위치에 PDF 문서에 페이지를 삽입할 수 있으며, PDF 파일의 끝에 페이지를 추가할 수도 있습니다. 이 섹션에서는 Acrobat Reader 없이 PDF에 페이지를 추가하는 방법을 보여줍니다. Aspose의 Python 라이브러리를 사용하여 PDF 파일의 헤더와 푸터에 텍스트나 이미지를 추가하고 문서 내에서 다른 헤더를 선택할 수 있습니다. 또한 Python을 사용하여 프로그래밍 방식으로 PDF 문서의 페이지를 자르기를 시도하세요.

이 섹션에서는 Artifact 클래스를 사용하여 PDF 파일에 워터마크를 추가하는 방법을 배웁니다. 이 작업을 위한 프로그래밍 샘플을 확인할 것입니다. [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 클래스를 사용하여 페이지 번호를 추가합니다. 문서에 스탬프를 추가하려면 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 및 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스를 사용하세요. **Aspose.PDF for Python via .NET**을 사용하여 PDF 파일에 배경 이미지를 생성하기 위해 워터마크 추가를 사용하세요.


당신은 다음을 수행할 수 있습니다:

- [페이지 추가](/pdf/ko/python-net/add-pages/) - 원하는 위치에 페이지를 추가하거나 PDF 파일의 끝에 추가하고 문서에서 페이지를 삭제합니다.
- [페이지 이동](/pdf/ko/python-net/move-pages/) - 한 문서에서 다른 문서로 페이지를 이동합니다.
- [페이지 삭제](/pdf/ko/python-net/delete-pages/) - PageCollection 컬렉션을 사용하여 PDF 파일에서 페이지를 삭제합니다.
- [페이지 크기 변경](/pdf/ko/python-net/change-page-size/) - Aspose.PDF 라이브러리를 사용하여 코드 스니펫으로 PDF 페이지 크기를 변경할 수 있습니다.
- [페이지 회전](/pdf/ko/python-net/rotate-pages/) - 기존 PDF 파일의 페이지 방향을 변경할 수 있습니다.
- [페이지 분할](/pdf/ko/python-net/split-document/) - PDF 파일을 하나 또는 여러 개의 PDF로 분할할 수 있습니다.
- [헤더 및/또는 푸터 추가](/pdf/ko/python-net/add-headers-and-footers-of-pdf-file/) - PDF 파일의 헤더 및 푸터에 텍스트나 이미지를 추가합니다.
- [페이지 자르기](/pdf/ko/python-net/crop-pages/) - 다른 페이지 속성을 사용하여 PDF 문서에서 페이지를 프로그래밍 방식으로 자를 수 있습니다.

- [워터마크 추가](/pdf/ko/python-net/add-watermarks/) - Artifact Class를 사용하여 PDF 파일에 워터마크를 추가합니다.
- [PDF 파일에 페이지 번호 추가](/pdf/ko/python-net/add-page-number/) - PageNumberStamp 클래스는 PDF 파일에 페이지 번호를 추가하는 데 도움이 됩니다.
- [배경 추가](/pdf/ko/python-net/add-backgrounds/) - 배경 이미지는 워터마크를 추가하는 데 사용할 수 있습니다.
- [스탬핑](/pdf/ko/python-net/stamping/) - ImageStamp 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가하고 TextStamp 클래스를 사용하여 텍스트를 추가할 수 있습니다.
- [페이지 속성 가져오기 및 설정](/pdf/ko/python-net/get-and-set-page-properties/) - 이 섹션에서는 PDF 파일의 페이지 수를 가져오고 색상과 같은 PDF 페이지 속성에 대한 정보를 가져오고 페이지 속성을 설정하는 방법을 보여줍니다.

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
    "applicationCategory": "PDF Manipulation Library for Python",
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