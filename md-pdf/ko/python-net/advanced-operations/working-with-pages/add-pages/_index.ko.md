---
title: Python으로 PDF에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /python-net/add-pages/
description: 이 기사는 원하는 위치의 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다. C#을 사용하여 PDF 파일에서 페이지를 이동, 제거(삭제)하는 방법을 배웁니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python으로 PDF에 페이지 추가",
    "alternativeHeadline": "PDF 문서에 페이지 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf page, insert pdf page",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "이 기사는 원하는 위치의 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다. Python을 사용하여 PDF 파일에서 페이지를 이동, 제거(삭제)하는 방법을 배웁니다."
}
</script>


Aspose.PDF for Python via .NET API는 Python을 사용하여 PDF 문서의 페이지를 작업할 수 있는 완전한 유연성을 제공합니다. PDF 문서의 모든 페이지는 PDF 페이지 작업에 사용할 수 있는 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)에 저장됩니다. Aspose.PDF for Python via .NET을 사용하면 파일의 원하는 위치에 페이지를 삽입할 수 있으며 PDF 파일의 끝에 페이지를 추가할 수 있습니다. 이 섹션에서는 Python을 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for Python via .NET을 사용하면 파일의 원하는 위치에 페이지를 삽입할 수 있으며 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

### 원하는 위치에 빈 페이지를 PDF 파일에 삽입

PDF 파일에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.

1. 지정된 인덱스로 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 [insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) 메서드를 호출합니다.
1. [save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # PDF에 빈 페이지 삽입
    document.pages.insert(2)
    # 출력 파일 저장
    document.save(output_pdf)
```

### PDF 파일의 끝에 빈 페이지 추가

때때로 문서가 빈 페이지로 끝나는지 확인하고 싶을 때가 있습니다. 이 주제는 PDF 문서의 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일의 끝에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.

1. 매개변수 없이 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 메서드를 호출합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 조각은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # PDF 파일의 끝에 빈 페이지 삽입
    document.pages.add()

    # 출력 파일 저장
    document.save(output_pdf)