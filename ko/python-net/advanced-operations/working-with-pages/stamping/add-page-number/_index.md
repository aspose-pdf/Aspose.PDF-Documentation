---
title: Python을 사용하여 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 30
url: /ko/python-net/add-page-number/
description: Aspose.PDF for Python via .NET은 PageNumber Stamp 클래스를 사용하여 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 페이지 번호를 추가하는 방법
Abstract: 이 문서는 문서에 페이지 번호를 추가하여 탐색을 용이하게 하는 중요성을 논의하고, PDF 파일에서 이를 구현하기 위한 도구로 Aspose.PDF for Python via .NET 라이브러리를 소개합니다. 이 라이브러리는 페이지 번호 스탬프를 사용자 정의할 수 있는 속성을 제공하는 PageNumberStamp 클래스를 활용하며, 형식, 여백, 정렬 및 시작 번호 등을 설정할 수 있습니다. 프로세스는 Document 객체와 PageNumberStamp 객체를 생성하고 원하는 속성을 구성한 뒤, add_stamp() 메서드를 사용하여 PDF 페이지에 스탬프를 적용하는 것을 포함합니다. 이 문서는 사용자 정의 가능한 글꼴 속성을 사용하여 페이지 번호 스탬프를 설정하고 적용하는 방법을 보여주는 Python 코드 예제를 제공합니다.
---

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 다양한 부분을 더 쉽게 찾을 수 있게 합니다.

**Aspose.PDF for Python via .NET**은 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)을 사용하여 페이지 번호를 추가할 수 있습니다.

## PDF에 페이지 번호 스탬프 추가

ASPose.PDF for Python을 사용하여 PDF에 동적 페이지 번호 스탬프를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 에 추가합니다. [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) 객체는 현재 페이지 번호와 총 페이지 수를 자동으로 표시할 수 있게 합니다. 이 예제는 페이지 번호 스탬프를 생성하고, [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)를 사용하여 모양(글꼴, 크기, 스타일, 색상, 정렬 및 여백)을 사용자 정의하고, [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드를 통해 PDF의 특정 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 적용하는 방법을 보여줍니다. 정렬 값은 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 열거형에서 가져오며, 색상/글꼴/스타일은 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 및 [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (글꼴은 [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods) 로 찾음)를 통해 사용할 수 있습니다. 이 기능은 전문적인 번호 매긴 문서를 생성하고 PDF 워크플로에서 페이지 매김을 자동화하는 데 유용합니다.

1. PDF 문서를 엽니다.
1. 페이지 번호 스탬프를 생성합니다.
1. 스탬프 속성을 설정합니다.
1. 텍스트 스타일을 사용자 정의합니다.
1. 스탬프를 페이지에 적용합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## PDF에 로마 숫자 페이지 번호 추가

PDF 문서의 모든 페이지에 로마 숫자 형식으로 페이지 번호를 추가합니다. 페이지 번호는 [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/)를 사용하여 스탬프로 추가되며, 글꼴, 크기, 스타일, 색상 및 정렬을 사용자 정의할 수 있습니다. 로마 숫자 또는 다른 번호 매김 방식을 선택하려면 [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) 열거형을 사용합니다. 번호 매김은 지정된 값에서 시작하도록 설정할 수도 있습니다.

1. PDF 문서를 엽니다.
1. 페이지 번호 스탬프를 생성합니다.
1. 스탬프 속성을 구성합니다.
1. 텍스트 외관을 설정합니다.
1. 스탬프를 모든 페이지에 적용합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

## 실시간 예제

[Add PDF page numbers](https://products.aspose.app/pdf/page-number) 은 페이지 번호 추가 기능이 작동하는 방식을 확인할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Python을 사용하여 PDF에 페이지 번호를 추가하는 방법](page_number.png)](https://products.aspose.app/pdf/page-number)


