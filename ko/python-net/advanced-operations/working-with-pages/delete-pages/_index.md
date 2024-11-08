---
title: Python으로 프로그래밍 방식으로 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 80
url: /ko/python-net/delete-pages/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python으로 프로그래밍 방식으로 PDF 페이지 삭제",
    "alternativeHeadline": "PDF 페이지 제거 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 페이지 삭제, pdf 페이지 제거",
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
    "url": "/python-net/delete-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다."
}
</script>


Aspose.PDF for Python via .NET을 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에서 특정 페이지를 삭제합니다.

## PDF 파일에서 페이지 삭제

1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 메서드를 호출하고 페이지의 인덱스를 지정합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 업데이트된 PDF 파일을 저장합니다.
다음 코드 스니펫은 Python을 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 특정 페이지 삭제
    document.pages.delete(2)

    # 업데이트된 PDF 저장
    document.save(output_pdf)