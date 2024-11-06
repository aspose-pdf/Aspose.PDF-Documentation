---
title: 파이썬을 사용하여 페이지 속성 가져오기 및 설정하기
linktitle: 페이지 속성 가져오기 및 설정하기
type: docs
weight: 90
url: ko/python-net/get-and-set-page-properties/
description: 이 섹션에서는 PDF 파일의 페이지 수를 가져오는 방법, 색상과 같은 PDF 페이지 속성에 대한 정보를 얻는 방법 및 페이지 속성을 설정하는 방법을 보여줍니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 페이지 속성 가져오기 및 설정하기",
    "alternativeHeadline": "PDF 페이지 속성 가져오기 및 설정하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 페이지 속성 가져오기, 페이지 속성 설정하기",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF for Python via .NET을 사용하면 Python 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오고, 색상과 같은 PDF 페이지 속성 정보를 얻고 페이지 속성을 설정하는 방법을 보여줍니다. 제공된 예제는 Python으로 작성되었습니다.

## PDF 파일의 페이지 수 가져오기

문서 작업을 할 때, 종종 몇 개의 페이지가 포함되어 있는지 알고 싶어합니다. Aspose.PDF를 사용하면 이 작업은 두 줄의 코드로 충분합니다.

PDF 파일의 페이지 수를 얻으려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다.
1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 Count 속성(Document 객체에서)을 사용하여 문서의 총 페이지 수를 가져옵니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 페이지 수 가져오기
    print("Page Count:", str(len(document.pages)))
```


### 문서를 저장하지 않고 페이지 수 얻기

때때로 우리는 PDF 파일을 즉석에서 생성하며, PDF 파일 생성 중에 파일을 시스템이나 스트림에 저장하지 않고 PDF 파일의 페이지 수를 얻어야 하는 요구 사항(목차 생성 등)을 마주칠 수 있습니다. 이 요구 사항을 충족하기 위해 Document 클래스에 [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드가 도입되었습니다. 문서를 저장하지 않고 페이지 수를 얻는 단계를 보여주는 아래 코드 스니펫을 살펴보십시오.

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    document = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    page = document.pages.add()
    # 루프 인스턴스 생성
    for i in range(0, 300):
        # 페이지 객체의 단락 컬렉션에 TextFragment 추가
        page.paragraphs.add(ap.text.TextFragment("페이지 수 테스트"))
    # 정확한 페이지 수를 얻기 위해 PDF 파일의 단락 처리
    document.process_paragraphs()
    # 문서의 페이지 수 출력
    print("문서의 페이지 수 =", str(len(document.pages)))
```


## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 여백 상자, 재단 상자와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

### **페이지 속성 이해하기: Artbox, BleedBox, CropBox, MediaBox, TrimBox 및 Rect 속성의 차이점**

- **미디어 상자**: 미디어 상자는 가장 큰 페이지 상자입니다. 이는 PostScript 또는 PDF로 문서를 인쇄할 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 상자는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 상자**: 문서에 블리드가 있는 경우 PDF에도 블리드 상자가 있습니다.
 Bleed는 페이지의 가장자리를 넘어서는 색상(또는 예술 작품)의 양입니다. 이는 문서가 인쇄되고 크기에 맞게 잘렸을 때(“트림됨”) 잉크가 페이지의 가장자리까지 도달하도록 보장하기 위해 사용됩니다. 페이지가 잘못 트림되더라도 - 트림 마크에서 약간 벗어나 잘리더라도 - 페이지에 하얀 가장자리가 나타나지 않습니다.
- **Trim box**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **Art box**: 아트 박스는 문서의 실제 페이지 내용을 둘러싸고 있는 상자입니다. 이 페이지 박스는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다.
  이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하세요.

### **페이지 속성 접근하기**

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다. PDF 파일의 모든 페이지는 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에 포함되어 있습니다.

여기에서 인덱스를 사용하여 개별 Page 객체에 접근하거나 foreach 루프를 사용하여 컬렉션을 순회하여 모든 페이지를 가져올 수 있습니다. 개별 페이지에 접근한 후에는 해당 속성을 얻을 수 있습니다. 다음 코드 스니펫은 페이지 속성을 얻는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    # 특정 페이지 가져오기
    page = document.pages[1]
    # 페이지 속성 가져오기
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Page Number :", page.number)
    print("Rotate :", page.rotate)
```

## PDF 파일의 특정 페이지 가져오기

Aspose.PDF for Python은 PDF를 개별 페이지로 [분할하고](/pdf/python-net/split-pdf-document/) 이를 PDF 파일로 저장할 수 있습니다. PDF 파일에서 지정된 페이지를 가져와 새 PDF로 저장하는 작업은 매우 유사합니다: 원본 문서를 열고, 페이지에 접근하고, 새 문서를 생성하여 이 페이지를 추가합니다.

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection)은 PDF 파일 내의 페이지를 보유합니다. 이 컬렉션에서 특정 페이지를 가져오려면:

1. Pages 속성을 사용하여 페이지 인덱스를 지정합니다.
1. 새로운 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 생성합니다.
1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 새 Document 객체에 추가합니다.
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 출력을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 특정 페이지를 가져와 새 파일로 저장하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 특정 페이지 가져오기
    page = document.pages[2]

    # 페이지를 PDF 파일로 저장
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## 페이지 색상 결정

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공하며, 페이지가 사용하는 색상 유형 - RGB, 흑백, 회색조 또는 미정 - 을 포함합니다.

PDF 파일의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에 포함됩니다.
 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 속성은 페이지의 요소 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 얻거나 결정하려면 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체의 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 속성을 사용합니다.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 반복하여 색상 정보를 얻는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 소스 PDF 파일 열기
    document = ap.Document(input_pdf)
    # PDF 파일의 모든 페이지를 반복
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # 특정 PDF 페이지의 색상 유형 정보 얻기
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("페이지 # " + str(page_number) + " 는 흑백입니다.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("페이지 # " + str(page_number) + " 는 회색조입니다.")

        if page_color_type == ap.ColorType.RGB:
            print("페이지 # " + str(page_number) + " 는 RGB입니다.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("페이지 # " + str(page_number) + " 색상은 정의되지 않았습니다.")
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>