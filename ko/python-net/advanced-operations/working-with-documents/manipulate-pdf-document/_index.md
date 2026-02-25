---
title: Python을 통해 .NET에서 PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 20
url: /ko/python-net/manipulate-pdf-document/
description: 이 문서는 Python을 사용하여 PDF A 표준에 대한 PDF 문서를 검증하는 방법, TOC 작업 방법, PDF 만료 날짜 설정 방법 등에 대한 정보를 포함합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 문서 조작 가이드
Abstract: 이 문서는 Python, 특히 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 조작하는 포괄적인 가이드를 제공합니다. 여기에는 `Document` 클래스의 `validate` 메서드를 사용하여 PDF/A-1a 및 PDF/A-1b 규격 준수를 검증하는 기능을 포함한 여러 기능이 다루어집니다. 또한 PDF 파일에서 목차(TOC)를 추가, 사용자 지정 및 관리하는 방법, 서로 다른 TabLeaderTypes 설정, 페이지 번호 숨기기, 접두사를 사용한 페이지 번호 사용자 지정 등에 대해 자세히 설명합니다. 추가로, JavaScript를 삽입하여 접근 제한을 위한 PDF 문서의 만료 날짜를 설정하는 방법과 PDF의 입력 가능한 양식을 플래튼하여 편집할 수 없게 만드는 방법을 설명합니다. 각 섹션은 Aspose.PDF를 사용한 Python 구현을 보여주는 코드 스니펫과 함께 제공됩니다.
---

## Python에서 PDF 문서 조작

## PDF A 표준 (A 1A 및 A 1B)용 PDF 문서 검증

PDF/A-1a 또는 PDF/A-1b 호환성을 위해 PDF 문서를 검증하려면 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하십시오. 이 메서드를 통해 결과를 저장할 파일 이름과 필요한 검증 유형인 PdfFormat 열거형 : PDF_A_1A 또는 PDF_A_1B를 지정할 수 있습니다.

다음 코드 스니펫은 PDF/A-1A에 대한 PDF 문서 검증 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

다음 코드 스니펫은 PDF/A-1b에 대한 PDF 문서 검증 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## 목차 작업

### 기존 PDF에 목차 추가

PDF에서 TOC는 "Table of Contents"를 의미합니다. 이는 섹션 및 제목의 개요를 제공함으로써 사용자가 문서를 빠르게 탐색할 수 있게 하는 기능입니다.

기존 PDF 파일에 TOC를 추가하려면 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스의 Heading 클래스를 사용합니다. [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스는 새 PDF를 생성하고 기존 PDF를 조작할 수 있습니다. 기존 PDF에 TOC를 추가하려면 Aspose.Pdf 네임스페이스를 사용합니다. 다음 코드 스니펫은 Python을 통해 .NET에서 기존 PDF 파일 내부에 목차를 생성하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### 각 TOC 레벨에 서로 다른 TabLeaderType 설정

Python용 Aspose.PDF는 각 TOC 레벨에 서로 다른 TabLeaderType을 설정할 수도 있습니다. [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 의 [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 설정해야 합니다.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

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

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### TOC에서 페이지 번호 숨기기

페이지 번호를 표시하고 싶지 않은 경우, TOC의 제목과 함께 페이지 번호를 표시하지 않으려면 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 클래스의 [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 false 로 설정할 수 있습니다. 다음 코드 스니펫을 확인하여 목차에서 페이지 번호를 숨기는 방법을 확인하십시오:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

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
    # Add four headings in the section
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

### TOC 추가 시 페이지 번호 사용자 지정

PDF 문서에 TOC를 추가할 때 페이지 번호를 사용자 지정하는 경우가 흔합니다. 예를 들어, 페이지 번호 앞에 P1, P2, P3 등과 같은 접두사를 추가해야 할 수 있습니다. 이러한 경우, Python용 Aspose.PDF는 [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 클래스의 [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 속성을 제공하여 다음 코드 예시와 같이 페이지 번호를 사용자 지정할 수 있습니다.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## PDF 만료 날짜 설정 방법

우리는 PDF 파일에 접근 권한을 적용하여 특정 사용자 그룹이 PDF 문서의 특정 기능/객체에 접근하도록 합니다. PDF 파일 접근을 제한하기 위해 일반적으로 암호화를 적용하고, 사용자가 문서를 열람할 때 PDF 파일 만료에 대한 유효한 알림을 제공하도록 PDF 파일 만료를 설정해야 하는 경우가 있습니다.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Python에서 입력 가능한 PDF 플래튼

PDF 문서에는 라디오 버튼, 체크박스, 텍스트 박스, 목록 등과 같은 인터랙티브한 입력 위젯이 포함되는 경우가 많습니다. 다양한 애플리케이션 목적을 위해 이를 편집 불가능하게 만들려면 PDF 파일을 플래튼해야 합니다.
Aspose.PDF는 Python에서 몇 줄의 코드만으로 PDF를 플래튼하는 기능을 제공합니다:

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


