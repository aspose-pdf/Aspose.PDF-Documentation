---
title: PDF에서 첨부 파일 제거하기
linktitle: 기존 PDF에서 첨부 파일 제거하기
type: docs
weight: 30
url: /python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에서 첨부 파일을 제거하는 Python PDF API를 사용하세요.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 첨부 파일 제거하기",
    "alternativeHeadline": "Python으로 PDF에서 첨부 파일 삭제하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 첨부 파일 삭제",
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
    "url": "/python-net/removing-attachment-from-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/removing-attachment-from-an-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python은 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF 라이브러리를 사용하여 PDF 파일에서 첨부 파일을 제거하는 Python PDF API를 사용하세요."
}
</script>


Aspose.PDF for Python은 PDF 파일에서 첨부 파일을 제거할 수 있습니다. PDF 문서의 첨부 파일은 Document 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션에 저장됩니다.

PDF 파일과 관련된 모든 첨부 파일을 삭제하려면:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션의 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 메서드를 호출합니다.
2. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 업데이트된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 첨부 파일을 제거하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 모든 첨부 파일 삭제
    document.embedded_files.delete()

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
    "applicationCategory": "파이썬용 PDF 조작 라이브러리",
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