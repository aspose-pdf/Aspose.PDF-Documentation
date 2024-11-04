---
title: 파이썬을 사용하여 PDF 문서 형식화
linktitle: PDF 문서 형식화
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Aspose.PDF for Python via .NET을 사용하여 PDF 문서를 생성하고 형식화하십시오. 다음 코드 스니펫을 사용하여 작업을 해결하십시오.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF 문서 형식화",
    "alternativeHeadline": "파이썬을 통해 .NET에서 PDF 문서를 형식화하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, dotnet, python, pdf 문서 형식화",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Aspose.PDF for Python via .NET을 사용하여 PDF 문서를 생성하고 형식화하십시오. 다음 코드 스니펫을 사용하여 작업을 해결하십시오."
}
</script>


## PDF 문서 형식 지정

### 문서 창 및 페이지 표시 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성을 가져오는 방법과 페이지가 어떻게 표시되는지 이해하는 데 도움이 됩니다. 이러한 속성을 설정하려면:

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다. 이제 Document 객체의 속성을 설정할 수 있습니다. 예를 들어,

- CenterWindow – 화면에 문서 창을 가운데로 배치합니다. 기본값: false.
- Direction – 읽기 순서입니다. 이는 페이지가 나란히 표시될 때 어떻게 배열되는지를 결정합니다. 기본값: 왼쪽에서 오른쪽.
- DisplayDocTitle – 문서 창 타이틀 바에 문서 제목을 표시합니다. 기본값: false (제목이 표시됩니다).
- HideMenuBar – 문서 창의 메뉴 바를 숨기거나 표시합니다. 기본값: false (메뉴 바가 표시됩니다).
- HideToolBar – 문서 창의 도구 모음을 숨기거나 표시합니다. 기본값: false (도구 모음이 표시됩니다).
- HideWindowUI – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다. 
 기본값: false (UI 요소가 표시됩니다).
- NonFullScreenPageMode – 문서가 전체 페이지 모드로 표시되지 않을 때의 모드.
- PageLayout – 페이지 레이아웃.
- PageMode – 문서가 처음 열릴 때 표시되는 방식. 옵션은 축소판 표시, 전체 화면, 첨부 파일 패널 표시입니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 다양한 문서 속성 가져오기
    # 문서 창의 위치 - 기본값: false
    print("CenterWindow :", document.center_window)

    # 주요 읽기 순서; 페이지의 위치 결정
    # 나란히 표시될 때 - 기본값: L2R
    print("Direction :", document.direction)

    # 창의 제목 표시줄에 문서 제목을 표시할지 여부
    # false이면 제목 표시줄에 PDF 파일 이름이 표시됩니다. - 기본값: false
    print("DisplayDocTitle :", document.display_doc_title)

    # 문서 창의 크기를
    # 처음 표시된 페이지의 크기에 맞출지 여부 - 기본값: false
    print("FitWindow :", document.fit_window)

    # 뷰어 응용 프로그램의 메뉴 표시줄을 숨길지 여부 - 기본값: false
    print("HideMenuBar :", document.hide_menubar)

    # 뷰어 응용 프로그램의 도구 표시줄을 숨길지 여부 - 기본값: false
    print("HideToolBar :", document.hide_tool_bar)

    # 스크롤 막대와 같은 UI 요소를 숨길지 여부
    # 페이지 콘텐츠만 표시 - 기본값: false
    print("HideWindowUI :", document.hide_window_ui)

    # 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서를 표시하는 방법.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # 페이지 레이아웃, 즉 단일 페이지, 한 열
    print("PageLayout :", document.page_layout)

    # 문서를 열 때 표시되는 방식
    # 즉 축소판, 전체 화면, 첨부 파일 패널 표시
    print("pageMode :", document.page_mode)

```

### 문서 창 및 페이지 표시 속성 설정

이 주제에서는 문서 창, 뷰어 애플리케이션 및 페이지 표시 속성을 설정하는 방법을 설명합니다. 이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. 저장 메소드를 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 속성은 다음과 같습니다:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

각 속성은 아래 코드에서 사용 및 설명됩니다. 다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 다양한 문서 속성 설정
    # 문서 창의 위치 지정 - 기본값: false
    document.center_window = True

    # 주된 읽기 순서; 페이지의 위치 결정
    # 나란히 표시될 때 - 기본값: L2R
    document.direction = ap.Direction.R2L

    # 창의 제목 표시줄에 문서 제목을 표시할지 여부 지정
    # false일 경우, 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
    document.display_doc_title = True

    # 문서 창의 크기를 첫 번째 표시된 페이지의 크기에 맞추어 조정할지 여부 지정 - 기본값: false
    document.fit_window = True

    # 뷰어 애플리케이션의 메뉴 막대를 숨길지 여부 지정 - 기본값: false
    document.hide_menubar = True

    # 뷰어 애플리케이션의 도구 막대를 숨길지 여부 지정 - 기본값: false
    document.hide_tool_bar = True

    # 스크롤 바와 같은 UI 요소를 숨길지 여부 지정
    # 페이지 내용만 표시되도록 남겨둠 - 기본값: false
    document.hide_window_ui = True

    # 문서의 페이지 모드. 전체 화면 모드 종료 시 문서를 어떻게 표시할지 지정.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # 페이지 레이아웃 지정, 예: 단일 페이지, 한 열
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # 문서를 열 때 어떻게 표시할지 지정
    # 예: 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
    document.page_mode = ap.PageMode.USE_THUMBS

    # 업데이트된 PDF 파일 저장
    document.save(output_pdf)
```


### 표준 Type 1 글꼴 포함

일부 PDF 문서에는 특수 Adobe 글꼴 세트의 글꼴이 포함되어 있습니다. 이 세트의 글꼴을 "표준 Type 1 글꼴"이라고 합니다. 이 세트에는 14개의 글꼴이 포함되어 있으며, 이 유형의 글꼴을 포함하려면 [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)와 같은 특수 플래그를 사용해야 합니다. 다음은 표준 Type 1 글꼴을 포함하여 모든 글꼴이 포함된 문서를 얻을 수 있는 코드 조각입니다:

```python

    import aspose.pdf as ap

    # 기존 PDF 문서 로드
    document = ap.Document(input_pdf)
    # 문서의 EmbedStandardFonts 속성 설정
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # 글꼴이 이미 포함되어 있는지 확인
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF 생성 시 글꼴 포함

만약 Adobe Reader가 지원하는 14개의 기본 글꼴 외의 다른 글꼴을 사용해야 한다면, PDF 파일을 생성할 때 글꼴 설명을 포함시켜야 합니다. 글꼴 정보가 포함되지 않으면, Adobe Reader는 운영 체제에서 설치된 경우 운영 체제에서 가져오거나 PDF의 글꼴 설명에 따라 대체 글꼴을 구성합니다.

>임베디드 글꼴은 호스트 머신에 설치되어 있어야 합니다. 즉, 다음 코드의 경우 'Univers Condensed' 글꼴이 시스템에 설치되어 있습니다.

우리는 'is_embedded' 속성을 사용하여 PDF 파일에 글꼴 정보를 포함시킵니다. 이 속성의 값을 'True'로 설정하면 PDF 파일 크기가 증가한다는 사실을 알면서도 전체 글꼴 파일을 PDF에 포함시킵니다. 다음은 PDF에 글꼴 정보를 포함시키는 데 사용할 수 있는 코드 스니펫입니다.

```python

    import aspose.pdf as ap

    # 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다
    doc = ap.Document()

    # Pdf 객체에 섹션을 만듭니다
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" 이 예제는 사용자 지정 글꼴을 사용한 샘플 텍스트입니다.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # PDF 문서 저장
    doc.save(output_pdf)
```


### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체와 장치에 없는 글꼴이 포함된 경우, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능하다면(장치에 설치되어 있거나 문서에 포함되어 있는 경우), 출력 PDF는 동일한 글꼴을 가져야 하며(기본 글꼴로 대체되지 않아야 합니다). 기본 글꼴의 값에는 글꼴 파일의 경로가 아닌 글꼴의 이름이 포함되어야 합니다. 우리는 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다:

```python

    import aspose.pdf as ap

    # 글꼴이 누락된 기존 PDF 문서 로드
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # 기본 글꼴 이름 지정
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려는 경우, [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스에서 제공하는 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 메서드를 사용할 수 있습니다.
 다음 코드 스니펫을 확인하여 기존 PDF 문서에서 모든 글꼴을 가져오세요:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### FontSubsetStrategy를 사용하여 글꼴 임베딩 개선

다음 코드 스니펫은 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 속성에 사용된 [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/)를 설정하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # 모든 글꼴은 SubsetAllFonts의 경우 문서에 하위 집합으로 임베딩됩니다.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # 완전히 임베딩된 글꼴에 대해서만 글꼴 하위 집합이 임베딩되며, 문서에 임베딩되지 않은 글꼴은 영향을 받지 않습니다.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### PDF 파일의 줌 팩터 설정 및 가져오기

때때로 PDF 문서의 현재 줌 팩터가 무엇인지 알고 싶을 때가 있습니다. Aspose.Pdf를 사용하면 현재 값을 확인하고 설정할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 클래스의 Destination 속성을 통해 PDF 파일과 연관된 줌 값을 얻을 수 있습니다. 마찬가지로, 파일의 줌 팩터를 설정하는 데에도 사용할 수 있습니다.

#### 줌 팩터 설정

다음 코드 스니펫은 PDF 파일의 줌 팩터를 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 새로운 Document 객체를 인스턴스화
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # 문서 저장
    doc.save(output_pdf)
```

#### 줌 팩터 가져오기

다음 코드 스니펫은 PDF 파일의 줌 팩터를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 새로운 Document 객체를 인스턴스화
    doc = ap.Document(input_pdf)

    # GoToAction 객체 생성
    action = doc.open_action

    # PDF 파일의 줌 팩터 가져오기
    print(action.destination.zoom)
```


### 인쇄 대화 상자 프리셋 속성 설정

Aspose.PDF는 PDF 문서의 [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) 멤버를 설정할 수 있습니다. 이를 통해 기본적으로 단면 인쇄로 설정된 PDF 문서의 DuplexMode 속성을 변경할 수 있습니다. 이는 아래에 표시된 두 가지 다른 방법론을 사용하여 달성할 수 있습니다.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### PDF 콘텐츠 편집기를 사용하여 인쇄 대화 상자 프리셋 속성 설정

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("파일에 단면 뒤집기 짧은 가장자리가 설정되어 있습니다")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```