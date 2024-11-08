---
title: Python을 사용하여 PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /ko/python-net/extract-images-from-pdf-file/
description: 이 섹션에서는 Python 라이브러리를 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.
lastmod: "2023-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF 파일에서 이미지 추출",
    "alternativeHeadline": "PDF에서 이미지 추출하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, Python, pdf에서 이미지 추출",
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
    "url": "/python-net/extract-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "이 섹션에서는 Python 라이브러리를 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다."
}
</script>


Do you need to separate images from your PDF files? For simplified management, archiving, analysis, or sharing images of your documents, use **Aspose.PDF for Python** and extract images from PDF files.

이미지를 PDF 파일에서 분리해야 합니까? 문서의 이미지를 간편하게 관리, 보관, 분석 또는 공유하려면 **Aspose.PDF for Python**을 사용하여 PDF 파일에서 이미지를 추출하세요.

Images are held in each page's [resources](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection's [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximagecollection/) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

이미지는 각 페이지의 [리소스](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션의 [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximagecollection/) 컬렉션에 보관됩니다. 특정 페이지를 추출하려면 이미지의 특정 인덱스를 사용하여 이미지 컬렉션에서 이미지를 가져옵니다.

The image's index returns an [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) object. This object provides a [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) 객체를 반환합니다. 이 객체는 추출된 이미지를 저장하는 데 사용할 수 있는 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 제공합니다. 다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_file)

    # 특정 이미지 추출
    xImage = document.pages[2].resources.images[1]
    outputImage = io.FileIO(output_image, "w")

    # 출력 이미지 저장
    xImage.save(outputImage)
    outputImage.close()
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
    "applicationCategory": "Python용 PDF 처리 라이브러리",
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