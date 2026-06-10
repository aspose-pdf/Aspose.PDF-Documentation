---
title: 파이썬에서 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 30
url: /ko/python-net/add-page-number/
description: Python에서 PDF 문서에 페이지 번호 스탬프를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 페이지 번호를 추가하는 방법
Abstract: 이 문서에서는 더 쉽게 탐색할 수 있도록 문서에 페이지 번호를 추가하는 것의 중요성에 대해 설명하고 PDF 파일에서 이 작업을 수행하기 위한 도구로.NET 라이브러리를 통해 Python용 Aspose.PDF 라이브러리를 소개합니다.이 라이브러리는 서식, 여백, 정렬 및 시작 번호를 포함하여 페이지 번호 스탬프를 사용자 지정하는 속성을 제공하는 PageNumberStamp 클래스를 활용합니다.이 프로세스에는 Document 객체와 PageNumberStamp 객체를 만들고, 원하는 속성을 구성하고, add_stamp () 메서드를 사용하여 PDF 페이지에 스탬프를 적용하는 작업이 포함됩니다.이 문서에서는 사용자 지정 가능한 글꼴 속성을 사용하여 페이지 번호 스탬프를 설정하고 적용하는 방법을 보여주는 Python 코드 예제를 제공합니다.
---

모든 문서에는 페이지 번호가 있어야 합니다.페이지 번호를 사용하면 독자가 문서의 다른 부분을 더 쉽게 찾을 수 있습니다.

**.NET을 통한 파이썬용 Aspose.pdf**를 사용하면 다음과 같이 페이지 번호를 추가할 수 있습니다. [페이지 번호 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## PDF에 페이지 번호 스탬프 추가

PDF에 동적 페이지 번호 스탬프 추가 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 파이썬에 Aspose.PDF 사용하기. [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 객체를 사용하면 총 페이지 수와 함께 현재 페이지 번호를 자동으로 표시할 수 있습니다.이 예제에서는 다음을 사용하여 페이지 번호 스탬프를 만들고 모양 (글꼴, 크기, 스타일, 색상, 정렬 및 여백) 을 사용자 지정하는 방법을 보여줍니다. [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), 특정 항목에 적용 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 를 통해 PDF에서 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 방법.정렬 값은 다음에서 가져옵니다. [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 열거형 및 색상/글꼴/스타일은 다음을 통해 사용할 수 있습니다. [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 과 [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (를 통해 검색된 글꼴) [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)).이 기능은 번호가 매겨진 전문적인 문서를 생성하고 PDF 워크플로우에서 페이지 매김을 자동화하는 데 유용합니다.

1. PDF 문서를 엽니다.
1. 페이지 번호 스탬프를 생성합니다.
1. 스탬프 속성을 설정합니다.
1. 텍스트 스타일을 사용자 지정합니다.
1. 스탬프를 페이지에 적용합니다.
1. 수정한 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## PDF에 로마 숫자 페이지 번호 추가

로마 숫자 형식의 페이지 번호를 PDF 문서의 모든 페이지에 추가합니다.페이지 번호는 다음을 사용하여 스탬프로 추가됩니다. [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), 글꼴, 크기, 스타일, 색상 및 정렬을 사용자 지정할 수 있습니다.를 사용하세요. [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) 열거형을 사용하여 로마 숫자 또는 기타 번호 매기기 체계를 선택합니다.지정한 값에서 번호 매기기를 시작할 수도 있습니다.

1. PDF 문서를 엽니다.
1. 페이지 번호 스탬프를 생성합니다.
1. 스탬프 속성을 구성합니다.
1. 텍스트 모양을 설정합니다.
1. 스탬프를 모든 페이지에 적용합니다.
1. 수정한 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## 라이브 예제

[PDF 페이지 번호 추가](https://products.aspose.app/pdf/page-number) 페이지 번호 추가 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 응용 프로그램입니다.

[![Python을 사용하여 pdf에 페이지 번호를 추가하는 방법](page_number.png)](https://products.aspose.app/pdf/page-number)

## 관련 스탬핑 주제

- [파이썬으로 PDF 페이지에 스탬프 찍기](/pdf/ko/python-net/stamping/)
- [Python에서 PDF에 페이지 스탬프 추가](/pdf/ko/python-net/page-stamps-in-the-pdf-file/)
- [Python에서 PDF에 이미지 스탬프 추가](/pdf/ko/python-net/image-stamps-in-pdf-page/)
- [Python에서 PDF에 텍스트 스탬프 추가](/pdf/ko/python-net/text-stamps-in-the-pdf-file/)