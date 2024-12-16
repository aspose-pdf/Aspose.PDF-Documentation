---
title: 파이썬을 사용하여 북마크 추가 및 삭제
linktitle: 북마크 추가 및 삭제
type: docs
weight: 10
url: /ko/python-net/add-and-delete-bookmark/
description: 파이썬을 사용하여 PDF 문서에 북마크를 추가할 수 있습니다. PDF 문서에서 모든 또는 특정 북마크를 삭제할 수 있습니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "북마크 추가 및 삭제",
    "alternativeHeadline": "PDF에서 북마크 추가 및 삭제 방법",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 북마크 삭제, 북마크 추가",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "파이썬을 사용하여 PDF 문서에 북마크를 추가할 수 있습니다. PDF 문서에서 모든 또는 특정 북마크를 삭제할 수 있습니다."
}
</script>


## PDF 문서에 책갈피 추가하기

책갈피는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션에 있으며, 이는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션 내에 있습니다.

PDF에 책갈피를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 사용하여 PDF 문서를 엽니다.
1. 책갈피를 생성하고 해당 속성을 정의합니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션을 Outlines 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 문서에 책갈피를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 책갈피 객체 생성
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # 대상 페이지 번호 설정
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # 문서의 아웃라인 컬렉션에 책갈피 추가
    document.outlines.append(outline)

    # 출력 저장
    document.save(output_pdf)
```


## PDF 문서에 자식 북마크 추가

북마크는 중첩될 수 있으며, 부모와 자식 북마크의 계층적 관계를 나타냅니다. 이 문서는 PDF에 2단계 북마크인 자식 북마크를 추가하는 방법을 설명합니다.

PDF 파일에 자식 북마크를 추가하려면 먼저 부모 북마크를 추가하세요:

1. 문서를 엽니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)에 북마크를 추가하고, 그 속성을 정의합니다.
1. Document 객체의 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 OutlineItemCollection을 추가합니다.

자식 북마크는 위에서 설명한 것처럼 부모 북마크와 동일하게 생성되지만 부모 북마크의 Outlines 컬렉션에 추가됩니다.

다음 코드 조각은 PDF 문서에 자식 북마크를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 부모 북마크 객체 생성
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "부모 개요"
    outline.italic = True
    outline.bold = True

    # 자식 북마크 객체 생성
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "자식 개요"
    childOutline.italic = True
    childOutline.bold = True

    # 부모 북마크의 컬렉션에 자식 북마크 추가
    outline.append(childOutline)
    # 문서의 개요 컬렉션에 부모 북마크 추가
    document.outlines.append(outline)

    # 출력 저장
    document.save(output_pdf)
```


## PDF 문서에서 모든 북마크 삭제하기

PDF의 모든 북마크는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 저장됩니다. 이 문서에서는 PDF 파일에서 모든 북마크를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 북마크를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 Delete 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 수정된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 북마크를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 모든 북마크 삭제
    document.outlines.delete()

    # 업데이트된 파일 저장
    document.save(output_pdf)

```

## PDF 문서에서 특정 북마크 삭제하기

PDF 파일에서 특정 북마크를 삭제하려면:

1. 책갈피 제목을 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 Delete 메서드에 매개변수로 전달합니다.  
1. 그런 다음 Document 객체의 Save 메서드를 사용하여 업데이트된 파일을 저장합니다.

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션을 제공합니다. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) 메서드는 메서드에 전달된 제목을 가진 책갈피를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 책갈피를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 제목으로 특정 아웃라인 삭제
    document.outlines.delete("Child Outline")

    # 업데이트된 파일 저장
    document.save(output_pdf)