---
title: Python을 통해 PDF 페이지를 프로그래밍 방식으로 이동
linktitle: PDF 페이지 이동
type: docs
weight: 100
url: ko/python-net/move-pages/
description: Aspose.PDF for Python via .NET을 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 통해 PDF 페이지를 프로그래밍 방식으로 이동",
    "alternativeHeadline": "Python으로 PDF 페이지를 이동하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 페이지 이동",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Aspose.PDF for Python via .NET을 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요."
}
</script>


## 하나의 PDF 문서에서 다른 문서로 페이지 이동

이 주제는 Python을 사용하여 하나의 PDF 문서에서 다른 문서의 끝으로 페이지를 이동하는 방법을 설명합니다.
페이지를 이동하려면 다음을 수행해야 합니다:

1. 원본 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에서 페이지를 가져옵니다.
1. 대상 문서에 페이지를 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력 PDF를 저장합니다.
1. 원본 문서에서 페이지를 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 합니다.

1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # 출력 파일 저장
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## 여러 페이지를 한 PDF 문서에서 다른 문서로 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 생성합니다.
1. 이동할 페이지 번호로 배열을 정의합니다.
1. 배열을 통해 루프 실행:

1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에서 페이지를 가져옵니다.
1. 대상 문서에 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 페이지를 추가합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력 PDF를 저장합니다.
1. 배열을 사용하여 소스 문서에서 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 페이지를 삭제합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # 출력 파일 저장
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## 현재 PDF 문서에서 페이지를 새 위치로 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스 객체를 만듭니다.
1. [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에서 페이지를 가져옵니다.
1. 페이지를 새 위치에 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)합니다 (예: 끝으로).
1. 이전 위치에서 페이지를 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력 PDF를 저장합니다.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # 출력 파일 저장
    srcDocument.save(output_pdf)