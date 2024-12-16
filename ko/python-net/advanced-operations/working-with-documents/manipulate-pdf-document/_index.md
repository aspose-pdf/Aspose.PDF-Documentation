---
title: Python을 통한 PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 20
url: /ko/python-net/manipulate-pdf-document/
description: 이 기사는 Python을 사용하여 PDF A 표준에 대해 PDF 문서를 검증하는 방법, 목차 작업 방법, PDF 만료 날짜 설정 방법 등에 대한 정보를 포함하고 있습니다.
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 통한 PDF 문서 조작",
    "alternativeHeadline": "Python으로 PDF 파일을 조작하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, dotnet, python, pdf 파일 조작",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "이 기사는 Python을 사용하여 PDF A 표준에 대해 PDF 문서를 검증하는 방법, 목차 작업 방법, PDF 만료 날짜 설정 방법 등에 대한 정보를 포함하고 있습니다."
}
</script>


## 파이썬으로 PDF 문서 조작하기

## PDF A 표준(PDF A 1A 및 A 1B)용 PDF 문서 유효성 검사

PDF 문서의 PDF/A-1a 또는 PDF/A-1b 호환성을 검증하려면 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하세요. 이 메서드는 결과를 저장할 파일의 이름과 필요한 유효성 검사 유형 PdfFormat 열거형: PDF_A_1A 또는 PDF_A_1B를 지정할 수 있게 합니다.

다음 코드 스니펫은 PDF/A-1A에 대해 PDF 문서를 검증하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # PDF/A-1a에 대해 PDF 유효성 검사
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

다음 코드 스니펫은 PDF/A-1b에 대해 PDF 문서를 검증하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # PDF/A-1a에 대해 PDF 유효성 검사
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## TOC 작업하기

### 기존 PDF에 TOC 추가

PDF에서 TOC는 "차례"를 의미합니다. 이는 사용자가 문서의 섹션 및 헤딩을 개요로 제공하여 문서를 빠르게 탐색할 수 있게 해주는 기능입니다.

기존 PDF 파일에 TOC를 추가하려면 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스의 Heading 클래스를 사용합니다. [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스는 새로운 PDF 파일을 생성하고 기존 PDF 파일을 조작할 수 있습니다. 기존 PDF에 TOC를 추가하려면 Aspose.Pdf 네임스페이스를 사용합니다. 다음 코드 스니펫은 Python을 통해 .NET에서 기존의 PDF 파일 내부에 목차를 생성하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 기존 PDF 파일을 로드합니다
    doc = ap.Document(input_pdf)

    # PDF 파일의 첫 번째 페이지에 접근합니다
    tocPage = doc.pages.insert(1)

    # TOC 정보를 나타내기 위한 객체를 생성합니다
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # TOC 제목을 설정합니다
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # TOC 요소로 사용할 문자열 객체를 생성합니다
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Heading 객체를 생성합니다
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Heading 객체의 대상 페이지를 지정합니다
        heading2.destination_page = doc.pages[i + 2]

        # 대상 페이지
        heading2.top = doc.pages[i + 2].rect.height

        # 대상 좌표
        segment2.text = titles[i]

        # TOC를 포함하는 페이지에 헤딩을 추가합니다
        tocPage.paragraphs.add(heading2)

    # 업데이트된 문서를 저장합니다
    doc.save(output_pdf)
```


### 서로 다른 TOC 레벨에 대해 다른 TabLeaderType 설정하기

Aspose.PDF for Python을 사용하면 서로 다른 TOC 레벨에 대해 다른 TabLeaderType을 설정할 수 있습니다. [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/)의 [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 설정해야 합니다.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # LeaderType 설정
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("목차")
    title.text_state.font_size = 30
    toc_info.title = title

    # Pdf 문서의 섹션 컬렉션에 목록 섹션 추가
    tocPage.toc_info = toc_info
    # 왼쪽 여백을 설정하여 네 가지 수준 목록의 형식을 정의
    # 및 각 수준의 텍스트 형식 설정

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Pdf 문서에 섹션 생성
    page = doc.pages.add()

    # 섹션에 네 개의 헤딩 추가
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "샘플 헤딩" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # 목차에 헤딩 추가.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # Pdf 저장
    doc.save(output_pdf)
```


### 목차에서 페이지 번호 숨기기

목차에 제목과 함께 페이지 번호를 표시하지 않으려면 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 클래스의 [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 false로 사용할 수 있습니다. 다음 코드 스니펫을 확인하여 목차에서 페이지 번호를 숨기세요:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Pdf 문서의 섹션 컬렉션에 목록 섹션 추가
    toc_page.toc_info = toc_info
    # 각 레벨의 왼쪽 여백과 텍스트 형식 설정을 설정하여 네 레벨 목록의 형식을 정의

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # 섹션에 네 개의 제목 추가
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### 목차 추가 시 페이지 번호 사용자 지정

PDF 문서에 목차를 추가할 때 페이지 번호를 사용자 지정하는 것이 일반적입니다. 예를 들어, 페이지 번호 앞에 P1, P2, P3 등과 같은 접두어를 추가해야 할 수 있습니다. 이러한 경우, Aspose.PDF for Python은 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 클래스의 [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 제공하여 페이지 번호를 사용자 지정할 수 있습니다. 다음 코드 샘플과 같이 사용할 수 있습니다.

```python

    import aspose.pdf as ap

    # 기존 PDF 파일 로드
    doc = ap.Document(input_pdf)
    # PDF 파일의 첫 번째 페이지에 액세스
    toc_page = doc.pages.insert(1)
    # 목차 정보를 나타내는 객체 생성
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # 목차의 제목 설정
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Heading 객체 생성
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Heading 객체의 대상 페이지 지정
        heading2.destination_page = doc.pages[i + 1]
        # 대상 페이지
        heading2.top = doc.pages[i + 1].rect.height
        # 대상 좌표
        segment2.text = "Page " + str(i)
        # 목차가 포함된 페이지에 heading 추가
        toc_page.paragraphs.add(heading2)

    # 업데이트된 문서 저장
    doc.save(output_pdf)

```


## PDF 만료 날짜 설정 방법

우리는 PDF 파일에 액세스 권한을 적용하여 특정 사용자 그룹이 PDF 문서의 특정 기능/객체에 액세스할 수 있도록 합니다. PDF 파일 액세스를 제한하기 위해 일반적으로 암호화를 적용하고, 사용자가 문서를 액세스/보기할 때 PDF 파일 만료에 대한 유효한 메시지를 받도록 PDF 파일 만료를 설정해야 할 수도 있습니다.

```python

    import aspose.pdf as ap

    # Document 객체 인스턴스화
    doc = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    doc.pages.add()
    # 페이지 객체의 단락 컬렉션에 텍스트 조각 추가
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # PDF 만료 날짜를 설정하기 위한 JavaScript 객체 생성
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # JavaScript를 PDF 열기 동작으로 설정
    doc.open_action = javaScript

    # PDF 문서 저장
    doc.save(output_pdf)
```


## 파이썬에서 작성 가능한 PDF 평탄화

PDF 문서에는 라디오 버튼, 체크박스, 텍스트 상자, 목록 등과 같은 대화형 작성 가능한 위젯이 포함된 양식이 자주 포함됩니다. 다양한 응용 프로그램 목적을 위해 편집할 수 없게 만들려면 PDF 파일을 평탄화해야 합니다. Aspose.PDF는 몇 줄의 코드만으로 파이썬에서 PDF를 평탄화하는 기능을 제공합니다:

```python

    import aspose.pdf as ap

    # 소스 PDF 양식 로드
    doc = ap.Document(input_pdf)

    # 작성 가능한 PDF 평탄화
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 업데이트된 문서 저장
    doc.save(output_pdf)
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://releases.aspose.com/pdf/python-net",
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