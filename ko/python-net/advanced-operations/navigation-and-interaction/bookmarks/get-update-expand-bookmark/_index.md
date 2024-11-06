---
title: 파이썬을 사용하여 북마크 가져오기, 업데이트 및 확장
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: ko/python-net/get-update-and-expand-bookmark/
description: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일에서 북마크를 사용하는 방법에 대해 설명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 북마크 가져오기, 업데이트 및 확장",
    "alternativeHeadline": "PDF 파일에서 북마크 가져오는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 북마크 가져오기",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일에서 북마크를 사용하는 방법에 대해 설명합니다."
}
</script>


## 북마크 가져오기

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에는 PDF 파일의 모든 북마크가 포함되어 있습니다. 이 문서에서는 PDF 파일에서 북마크를 가져오고 특정 북마크가 있는 페이지를 가져오는 방법을 설명합니다.

북마크를 가져오려면 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션을 반복하고 OutlineItemCollection에서 각 북마크를 가져옵니다. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)은 북마크의 모든 속성에 대한 액세스를 제공합니다. 다음 코드 스니펫은 PDF 파일에서 북마크를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 모든 북마크를 반복
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## 북마크의 페이지 번호 가져오기

북마크를 추가한 후에는 북마크 객체와 연관된 목적지 PageNumber를 가져와서 해당 페이지가 몇 페이지인지 알 수 있습니다.

```python

    import aspose.pdf as ap

    # PdfBookmarkEditor 생성
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # PDF 파일 열기
    bookmarkEditor.bind_pdf(input_pdf)
    # 북마크 추출
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "제목:", bookmark.title)
        print(str_level_seprator, "페이지 번호:", bookmark.page_number)
        print(str_level_seprator, "페이지 액션:", bookmark.action)
```

## PDF 문서에서 자식 북마크 가져오기

북마크는 부모와 자식으로 계층적 구조로 구성될 수 있습니다.
 문서 개체의 Outlines 컬렉션을 반복하여 모든 북마크를 가져옵니다. 그러나 자식 북마크도 가져오려면 첫 번째 루프에서 얻은 각 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 개체의 모든 북마크를 반복하십시오. 다음 코드 스니펫은 PDF 문서에서 자식 북마크를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 모든 북마크 반복
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("자식 북마크")
            # 자식 북마크가 있으면 해당 항목도 반복
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDF 문서에서 북마크 업데이트하기

PDF 파일에서 북마크를 업데이트하려면, 먼저 북마크의 인덱스를 지정하여 Document 객체의 OutlineCollection 컬렉션에서 특정 북마크를 가져옵니다. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 객체로 북마크를 가져온 후, 속성을 업데이트하고 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 북마크를 업데이트하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 북마크 객체 가져오기
    outline = document.outlines[1]

    # 자식 북마크 객체 가져오기
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # 출력 저장
    document.save(output_pdf)
```

## 문서 보기 시 확장된 북마크

북마크는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션에 저장되어 있으며, 이는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션 내에 있습니다.
 그러나 PDF 파일을 볼 때 모든 책갈피가 확장된 상태로 필요할 수 있습니다.

이 요구 사항을 충족하려면 각 개요/책갈피 항목의 열기 상태를 열림으로 설정할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 각 책갈피의 열기 상태를 확장된 상태로 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 페이지 보기 모드 설정, 예를 들어, 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
    document.page_mode = ap.PageMode.USE_OUTLINES
    # PDF 파일의 아웃라인 컬렉션에서 각 아웃라인 항목을 순회
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # 아웃라인 항목의 열기 상태 설정
        item.open = True

    # 출력 저장
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
    "applicationCategory": "PDF Manipulation Library for Python",
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