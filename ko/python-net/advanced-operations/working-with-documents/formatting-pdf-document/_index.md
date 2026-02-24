---
title: Python을 사용한 PDF 문서 포맷팅
linktitle: PDF 문서 포맷팅
type: docs
weight: 11
url: /ko/python-net/formatting-pdf-document/
description: Aspose.PDF for Python via .NET를 사용하여 PDF 문서를 만들고 서식 지정합니다. 다음 코드 스니펫을 사용하여 작업을 해결하십시오.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 문서 포맷팅
Abstract: 이 문서는 Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 조작하고 서식 지정하는 포괄적인 가이드를 제공합니다. 문서 창 및 페이지 표시 속성 설정(예 창 중앙 정렬, 읽기 방향, UI 요소 숨기기) 등 PDF 사용자 정의의 다양한 측면을 다룹니다. 이 문서는 `Document` 클래스를 사용하여 이러한 속성을 프로그래밍 방식으로 가져오고 설정하는 방법을 설명합니다. 또한 글꼴 관리에 대해 다루며, Standard Type 1 글꼴 및 기타 글꼴을 PDF에 삽입하여 문서 이식성과 시스템 간 시각적 일관성을 보장하는 방법을 상세히 설명합니다. 기본 글꼴 이름 설정, PDF에서 모든 글꼴을 가져오기, `FontSubsetStrategy`를 사용한 글꼴 삽입 향상 기술도 강조합니다. 또한 `GoToAction` 클래스를 사용하여 PDF 문서의 확대/축소 비율을 조정하고, 양면 인쇄 옵션을 포함한 인쇄 대화 상자 사전 설정 속성을 구성하는 방법을 상세히 설명합니다. 각 섹션에는 이러한 기능을 구현하기 위한 실용적인 예제가 포함된 코드 스니펫이 제공됩니다.
---

## PDF 문서 포맷팅

### 문서 창 및 페이지 표시 속성 가져오기

이 주제에서는 문서 창, 뷰어 애플리케이션 및 페이지 표시 방법에 대한 속성을 어떻게 가져오는지 설명합니다. 이러한 속성을 설정하려면:

PDF 파일을 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 엽니다. 이제 Document 객체의 속성을 다음과 같이 설정할 수 있습니다:

- CenterWindow – 화면 중앙에 문서 창을 배치합니다. 기본값: false.
- Direction – 읽기 순서. 이는 페이지가 나란히 표시될 때 레이아웃을 결정합니다. 기본값: left to right.
- DisplayDocTitle – 문서 창의 제목 표시줄에 문서 제목을 표시합니다. 기본값: false (제목이 표시됩니다).
- HideMenuBar – 문서 창의 메뉴 바를 숨기거나 표시합니다. 기본값: false (메뉴 바가 표시됩니다).
- HideToolBar – 문서 창의 도구 모음을 숨기거나 표시합니다. 기본값: false (도구 모음이 표시됩니다).
- HideWindowUI – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다. 기본값: false (UI 요소가 표시됩니다).
- NonFullScreenPageMode – 전체 화면 모드가 아닐 때 문서가 표시되는 방식.
- PageLayout – 페이지 레이아웃.
- PageMode – 문서를 처음 열 때 표시되는 방식. 옵션으로는 썸네일 표시, 전체 화면, 첨부 파일 패널 표시가 있습니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### 문서 창 및 페이지 표시 속성 설정

이 주제에서는 문서 창, 뷰어 애플리케이션 및 페이지 표시 속성을 설정하는 방법을 설명합니다. 이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

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

각각은 아래 코드에서 사용 및 설명됩니다. 다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Standard Type 1 글꼴 삽입

일부 PDF 문서에는 특별한 Adobe 글꼴 세트의 글꼴이 포함됩니다. 이 세트의 글꼴은 “Standard Type 1 Fonts”라고 부릅니다. 이 세트에는 14개의 글꼴이 포함되어 있으며, 이러한 유형의 글꼴을 삽입하려면 특수 플래그인 [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)를 사용해야 합니다. 아래는 Standard Type 1 Fonts를 포함한 모든 글꼴이 삽입된 문서를 얻기 위해 사용할 수 있는 코드 스니펫입니다:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF 생성 시 글꼴 삽입

Adobe Reader에서 지원하는 14개의 기본 글꼴 외에 다른 글꼴을 사용하려면 PDF 파일을 생성할 때 글꼴 설명을 삽입해야 합니다. 글꼴 정보가 삽입되지 않으면, Adobe Reader는 시스템에 설치된 경우 운영 체제에서 해당 글꼴을 가져오거나, PDF의 글꼴 설명자에 따라 대체 글꼴을 생성합니다.

> 삽입된 글꼴은 호스트 머신에 설치되어 있어야 합니다. 예를 들어 아래 코드에서 ‘Univers Condensed’ 글꼴이 시스템에 설치되어 있습니다.

우리는 'is_embedded' 속성을 사용하여 글꼴 정보를 PDF 파일에 삽입합니다. 이 속성 값을 'True'로 설정하면 전체 글꼴 파일이 PDF에 삽입되어 PDF 파일 크기가 증가한다는 점을 유념해야 합니다. 아래는 PDF에 글꼴 정보를 삽입하는 데 사용할 수 있는 코드 스니펫입니다.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체와 장치에 모두 없는 글꼴이 포함된 경우, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능(장치에 설치되어 있거나 문서에 포함되어)하면, 출력 PDF는 동일한 글꼴을 사용해야 합니다(기본 글꼴로 대체되지 않아야 함). 기본 글꼴 값은 글꼴 파일의 경로가 아니라 글꼴 이름을 포함해야 합니다. 우리는 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려면, [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스에서 제공하는 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오는 방법은 다음 코드 스니펫을 확인하십시오:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### FontSubsetStrategy를 사용한 글꼴 임베딩 개선

다음 코드 스니펫은 [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 속성에 사용되는 [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/)를 설정하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### PDF 파일의 줌 팩터 가져오기 및 설정

때때로 PDF 문서의 현재 줌 팩터가 얼마인지 확인하고 싶을 수 있습니다. Aspose.Pdf를 사용하면 현재 값을 확인하고 설정할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) 클래스의 Destination 속성을 사용하면 PDF 파일에 연결된 줌 값을 가져올 수 있습니다. 마찬가지로 파일의 줌 팩터를 설정하는 데에도 사용할 수 있습니다.

#### 줌 팩터 설정

다음 코드 스니펫은 PDF 파일의 줌 팩터를 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### 줌 팩터 가져오기

다음 코드 스니펫은 PDF 파일의 줌 팩터를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### 인쇄 대화 상자 사전 설정 속성 설정

Aspoose.PDF는 PDF 문서의 [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) 멤버를 설정할 수 있게 합니다. 이를 통해 기본값이 단면인 PDF 문서의 DuplexMode 속성을 변경할 수 있습니다. 아래와 같이 두 가지 방법으로 이를 구현할 수 있습니다.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### PDF 콘텐츠 편집기를 사용한 인쇄 대화 상자 사전 설정 속성 설정

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


