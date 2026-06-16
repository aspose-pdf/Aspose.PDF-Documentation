---
title: 파이썬에서 PDF 문서 조작하기
linktitle: PDF 문서 조작하기
type: docs
weight: 20
url: /ko/python-net/manipulate-pdf-document/
description: TOC 관리 및 PDF/A 검사를 포함하여 Python에서 PDF 문서를 검증, 구성 및 수정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 문서 조작 가이드
Abstract: 이 문서에서는 Python, 특히 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 조작하는 방법에 대한 포괄적인 가이드를 제공합니다.여기서는 `Document` 클래스의 `validate` 메서드를 사용하여 PDF/A-1a 및 PDF/A-1b 호환성에 대한 PDF 문서의 유효성을 검사하는 것을 비롯한 여러 기능을 다룹니다.또한 다양한 TabLeader 유형 설정, 페이지 번호 숨기기, 접두사를 사용한 페이지 번호 지정 사용자 지정 등 PDF 파일에 목차 (TOC) 를 추가, 사용자 지정 및 관리하는 방법도 자세히 설명합니다.또한 이 문서에서는 액세스 제한을 위해 JavaScript를 내장하여 PDF 문서의 만료 날짜를 설정하는 방법과 채울 수 있는 양식을 PDF에 통합하여 편집할 수 없게 만드는 방법에 대해 설명합니다.각 섹션에는 Python에서 Aspose.PDF 를 사용하여 이러한 기능을 구현하는 방법을 보여주는 코드 스니펫이 함께 제공됩니다.
---

이 페이지는 PDF 규정 준수를 확인하고, 목차를 작성 또는 사용자 지정하고, 문서 만료 동작을 설정하거나, Python 워크플로에서 채울 수 있는 PDF를 병합해야 할 때 유용합니다.

## 파이썬에서 PDF 문서 조작하기

## PDF A 표준 (A 1A 및 A 1B) 에 대한 PDF 문서 유효성 검사

PDF 문서의 PDF/A-1a 또는 PDF/a-1b 호환성을 확인하려면 다음을 사용하십시오. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업 [유효성을 검사합니다](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.이 메서드를 사용하면 결과를 저장할 파일의 이름과 필요한 검증 유형인 PDF형식 열거 (PDF_A_1A 또는 PDF_A_1B) 를 지정할 수 있습니다.

다음 코드 스니펫은 PDF/A-1A용 PDF 문서의 유효성을 검사하는 방법을 보여줍니다.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

다음 코드 스니펫은 PDF/A-1b용 PDF 문서의 유효성을 검사하는 방법을 보여줍니다.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## TOC로 작업하기

### 기존 PDF에 목차 추가

PDF의 TOC는 “목차”의 약자입니다.섹션 및 제목에 대한 개요를 제공하여 사용자가 문서를 빠르게 탐색할 수 있게 해주는 기능입니다. 

기존 PDF 파일에 목차를 추가하려면 의 Heading 클래스를 사용하십시오. [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스.더 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 네임스페이스는 새 PDF 파일을 만들거나 기존 PDF 파일을 조작할 수 있습니다.기존 PDF에 목차를 추가하려면 Aspose.Pdf 네임스페이스를 사용하십시오.다음 코드 스니펫은.NET을 통해 Python을 사용하여 기존 PDF 파일 내에 목차를 만드는 방법을 보여줍니다.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 다양한 TOC 레벨에 대해 다른 테이블 리더 유형 설정

파이썬용 Aspose.PDF 기능을 사용하면 TOC 수준에 따라 다른 테이블 리더 유형을 설정할 수도 있습니다.다음을 설정해야 합니다. [라인_대시](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 의 재산 [TOC 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
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

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### TOC에서 페이지 번호 숨기기

TOC의 제목과 함께 페이지 번호를 표시하지 않으려는 경우 다음을 사용할 수 있습니다. [is_show_page_번호](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 의 재산 [TOC 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 클래스는 거짓입니다.목차에서 페이지 번호를 숨기려면 다음 코드 스니펫을 확인하세요.

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### TOC 추가 시 페이지 번호 사용자 지정

PDF 문서에 목차를 추가하는 동안 목차의 페이지 번호 매기기를 사용자 정의하는 것이 일반적입니다.예를 들어 페이지 번호 앞에 P1, P2, P3 등과 같은 접두사를 추가해야 할 수 있습니다.이런 경우, 파이썬용 Aspose.PDF 는 다음을 제공합니다. [페이지_번호_접두사](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) 의 재산 [TOC 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 다음 코드 샘플과 같이 페이지 번호를 사용자 지정하는 데 사용할 수 있는 클래스입니다.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## PDF 만료일 설정 방법

특정 사용자 그룹이 PDF 문서의 특정 기능/개체에 액세스할 수 있도록 PDF 파일에 대한 액세스 권한을 적용합니다.PDF 파일 액세스를 제한하기 위해 일반적으로 암호화를 적용하며, 문서에 액세스하거나 문서를 보는 사용자에게 PDF 파일 만료에 관한 유효한 메시지를 받을 수 있도록 PDF 파일 만료 시간을 설정해야 할 수도 있습니다.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## 채울 수 있는 PDF를 파이썬으로 병합

PDF 문서에는 종종 라디오 버튼, 확인란, 텍스트 상자, 목록 등과 같이 채울 수 있는 대화형 위젯이 있는 양식이 포함됩니다. 다양한 응용 목적으로 편집할 수 없도록 하려면 PDF 파일을 평평하게 해야 합니다.
Aspose.PDF 는 단 몇 줄의 코드로 파이썬에서 PDF를 평면화하는 함수를 제공합니다.

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 문서 포맷 지정하기](/pdf/ko/python-net/formatting-pdf-document/)
- [파이썬으로 PDF 파일 만들기](/pdf/ko/python-net/create-pdf-document/)
- [파이썬에서 PDF 파일 최적화하기](/pdf/ko/python-net/optimize-pdf/)
