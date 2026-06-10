---
title: 파이썬으로 PDF 문서 포맷 지정하기
linktitle: PDF 문서 서식 지정
type: docs
weight: 11
url: /ko/python-net/formatting-pdf-document/
description: Python에서 PDF 문서의 서식을 지정하고, 글꼴을 포함하고, 뷰어 설정을 제어하고, 표시 옵션을 조정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF 문서 포맷 지정하기
Abstract: 이 문서에서는 Python의 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 조작하고 형식을 지정하는 방법에 대한 포괄적인 가이드를 제공합니다.창 중앙 맞추기, 읽기 방향, UI 요소 숨기기 등 문서 창 및 페이지 표시 속성 설정을 비롯한 PDF 사용자 지정의 다양한 측면을 다룹니다.이 문서에서는 'Document' 클래스를 사용하여 프로그래밍 방식으로 이러한 속성을 검색하고 설정하는 방법을 설명합니다.또한 글꼴 관리에 대해서도 다루며 Standard Type 1 글꼴 및 기타 글꼴을 PDF에 포함하여 문서 이동성과 시스템 전반의 시각적 일관성을 보장하는 방법을 자세히 설명합니다.또한 기본 글꼴 이름을 설정하고, PDF에서 모든 글꼴을 검색하고, 'FontSubsetStrategy'를 사용하여 글꼴 임베딩을 향상시키는 기술을 소개합니다.또한 이 문서에서는 `GoToAction` 클래스를 사용하여 PDF 문서의 확대/축소 비율을 조정하고 양면 인쇄 옵션을 비롯한 인쇄 대화 상자 사전 설정 속성을 구성하는 방법에 대해 자세히 설명합니다.각 섹션에는 코드 스니펫이 함께 제공되어 이러한 기능을 구현하기 위한 실제 예제를 제공합니다.
---

이 안내서는 Python에서 생성한 문서의 PDF 뷰어 동작, 글꼴 포함, 기본 표시 설정 또는 인쇄 기본 설정을 제어해야 할 때 유용합니다.

## PDF 문서 서식 지정

### 문서 창 및 페이지 표시 속성 가져오기

이 항목은 문서 창, 뷰어 응용 프로그램의 속성을 가져오는 방법 및 페이지가 표시되는 방법을 이해하는 데 도움이 됩니다.이러한 속성을 설정하려면:

를 사용하여 PDF 파일을 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.이제 다음과 같은 Document 객체의 속성을 설정할 수 있습니다.

- 중앙 창 — 문서 창을 화면 중앙에 배치합니다.기본값: false입니다.
- 방향 — 읽기 순서.이에 따라 페이지가 나란히 표시될 때 페이지가 배치되는 방식이 결정됩니다.기본값: 왼쪽에서 오른쪽.
- DisplayDocTitle — 문서 창 제목 표시줄에 문서 제목을 표시합니다.기본값: false (제목이 표시됨).
- HidemenuBar — 문서 창의 메뉴 막대를 숨기거나 표시합니다.기본값: false (메뉴 막대가 표시됨).
- 툴바 숨기기 — 문서 창의 툴바를 숨기거나 표시합니다.기본값: false (도구 모음이 표시됨).
- WindowUI 숨기기 — 스크롤 막대와 같은 문서 창 요소를 숨기거나 표시합니다.기본값: false (UI 요소가 표시됨).
- 비FullScreenPageMode — 문서가 전체 페이지 모드로 표시되지 않을 때의 모습입니다.
- 페이지 레이아웃 — 페이지 레이아웃.
- PageMode — 문서를 처음 열 때 표시되는 방식입니다.옵션으로는 썸네일 표시, 전체 화면, 첨부 파일 패널 표시가 있습니다.

다음 코드 스니펫은 를 사용하여 속성을 가져오는 방법을 보여줍니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### 문서 창 및 페이지 표시 속성 설정

이 항목에서는 문서 창, 뷰어 응용 프로그램 및 페이지 표시의 속성을 설정하는 방법을 설명합니다.이러한 다양한 속성을 설정하려면:

1. 를 사용하여 PDF 파일을 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 문서 객체의 속성을 설정합니다.
1. save 방법을 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 속성은 다음과 같습니다.

- 센터 윈도우
- 방향
- 문서 제목 표시
- 창 맞추기
- 바 숨기기
- 툴바 숨기기
- 윈도우 UI 숨기기
- 비전체 화면 페이지 모드
- 페이지 레이아웃
- 페이지 모드

각각은 아래 코드에서 사용되고 설명됩니다.다음 코드 스니펫은 를 사용하여 속성을 설정하는 방법을 보여줍니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### 표준 유형 1 글꼴 포함

일부 PDF 문서에는 특수 Adobe 글꼴 세트의 글꼴이 있습니다.이 세트의 글꼴을 “표준 유형 1 글꼴”이라고 합니다.이 세트에는 14개의 글꼴이 포함되어 있으며 이러한 유형의 글꼴을 포함하려면 특수 플래그를 사용해야 합니다 (예: [임베드_표준_글꼴](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties).다음은 표준 유형 1 글꼴을 포함하여 모든 글꼴이 포함된 문서를 가져오는 데 사용할 수 있는 코드 스니펫입니다.

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF를 만드는 동안 글꼴 포함하기

Adobe Reader에서 지원하는 14가지 코어 글꼴 이외의 글꼴을 사용해야 하는 경우 PDF 파일을 생성할 때 글꼴 설명을 포함해야 합니다.글꼴 정보가 포함되어 있지 않은 경우 Adobe Reader는 시스템에 설치된 경우 운영 체제에서 해당 정보를 가져오거나 PDF의 글꼴 설명자에 따라 대체 글꼴을 생성합니다.

>호스트 컴퓨터에 포함된 글꼴을 설치해야 한다는 점에 유의하십시오. 즉, 다음 코드의 경우 'Univers Condensed' 글꼴이 시스템 위에 설치되어 있어야 합니다.

글꼴 정보를 PDF 파일에 포함하려면 'is_embedded' 속성을 사용합니다.이 속성의 값을 'True'로 설정하면 PDF 파일 크기가 커진다는 사실을 알고 전체 글꼴 파일이 PDF에 포함됩니다.다음은 글꼴 정보를 PDF에 포함시키는 데 사용할 수 있는 코드 스니펫입니다.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체 및 장치에서 사용할 수 없는 글꼴이 포함된 경우 API는 이러한 글꼴을 기본 글꼴로 대체합니다.글꼴을 사용할 수 있는 경우 (장치에 설치되거나 문서에 포함된 글꼴), 출력 PDF의 글꼴은 동일해야 합니다 (기본 글꼴로 바꿔서는 안 됨).기본 글꼴 값에는 글꼴 파일 경로가 아닌 글꼴 이름이 포함되어야 합니다.문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다.다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다.

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려면 다음을 사용할 수 있습니다. [폰트_유틸리티](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 에서 제공되는 방법 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.기존 PDF 문서에서 모든 글꼴을 가져오려면 다음 코드 스니펫을 확인하십시오.

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### FontSubset 전략을 사용하여 글꼴 임베딩 개선

다음 코드 스니펫은 설정 방법을 보여줍니다. [글꼴 서브셋 전략](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) 사용 [폰트_유틸리티](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 재산:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### PDF 파일의 확대/축소 비율 설정

때로는 PDF 문서의 현재 확대/축소 비율을 확인하고 싶을 때가 있습니다.Aspose.Pdf 파일을 사용하면 현재 값을 확인할 수 있을 뿐만 아니라 값을 설정할 수도 있습니다.

더 [액션으로 이동](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 클래스 대상 속성을 사용하면 PDF 파일과 관련된 확대/축소 값을 가져올 수 있습니다.마찬가지로 파일의 확대/축소 비율을 설정하는 데 사용할 수 있습니다.

#### 확대/축소 비율 설정

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 설정하는 방법을 보여줍니다.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### 줌 팩터 가져오기

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 가져오는 방법을 보여줍니다.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 파일 만들기](/pdf/ko/python-net/create-pdf-document/)
- [파이썬에서 PDF 문서 조작하기](/pdf/ko/python-net/manipulate-pdf-document/)
- [파이썬에서 PDF 파일 최적화하기](/pdf/ko/python-net/optimize-pdf/)
