---
title: Python에서 PDF에 텍스트 스탬프 추가
linktitle: PDF 파일의 텍스트 스탬프
type: docs
weight: 20
url: /ko/python-net/text-stamps-in-the-pdf-file/
description: Python에서 PDF 문서에 텍스트 스탬프를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 텍스트 스탬프를 추가하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 텍스트 스탬프를 추가하는 방법에 대한 포괄적인 가이드를 제공합니다.여기서는 `TextStamp` 클래스를 사용하여 글꼴 크기, 스타일, 색상 및 정렬과 같은 속성을 가진 사용자 지정 가능한 텍스트 스탬프를 만드는 방법을 간략하게 설명합니다.이 문서에는 간단한 텍스트 스탬프를 추가하고, 텍스트 정렬을 구성하고, 필 스트로크 텍스트와 같은 고급 렌더링 모드를 적용하는 방법을 보여주는 코드 스니펫이 포함되어 있습니다.첫 번째 섹션에서는 'Document' 및 'TextStamp' 객체 생성, 텍스트 속성 설정, 특정 페이지에 스탬프 추가에 대해 설명합니다.두 번째 섹션에서는 텍스트를 가로 및 세로로 정렬하는 `text_alignment` 속성을 소개하고 PDF 페이지에서 텍스트를 중앙에 배치하는 코드 예제를 제공합니다.마지막 섹션에서는 렌더링 모드에 대해 설명하고, 스탬프에 바인딩하기 전에 `TextState` 객체를 사용하여 필 스트로크 텍스트를 추가하여 획 색상과 렌더링 모드를 설정하는 방법을 보여줍니다.각 섹션에는 이해와 구현을 용이하게 하기 위한 실제 예제가 함께 제공됩니다.
---

## Python으로 텍스트 스탬프 추가하기

사용할 수 있습니다 [텍스트 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) PDF 파일에 텍스트 스탬프를 추가하는 클래스입니다. [텍스트 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스는 글꼴 크기, 글꼴 스타일, 글꼴 색상 등과 같은 텍스트 기반 스탬프를 만드는 데 필요한 속성을 제공합니다. 텍스트 스탬프를 추가하려면 필수 속성을 사용하여 Document 객체와 TextStamp 객체를 만들어야 합니다.그런 다음 호출할 수 있습니다. [스탬프 추가 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) PDF에 스탬프를 추가하는 페이지 메서드입니다.다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다.이는 PDF 페이지에 주석, 워터마크 또는 레이블을 추가할 때 유용합니다.

1. PDF 문서를 엽니다.
1. 텍스트스탬프 객체를 생성합니다.
1. 스탬프 배경 동작을 설정합니다.
1. 스탬프를 페이지에 배치합니다.
1. 필요한 경우 스탬프를 회전시킵니다.
1. 텍스트 속성을 설정합니다.
1. 페이지에 스탬프를 추가합니다.
1. 수정된 PDF 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## 관련 스탬핑 주제

- [파이썬으로 PDF 페이지에 스탬프 찍기](/pdf/ko/python-net/stamping/)
- [Python에서 PDF에 페이지 스탬프 추가](/pdf/ko/python-net/page-stamps-in-the-pdf-file/)
- [Python에서 PDF에 이미지 스탬프 추가](/pdf/ko/python-net/image-stamps-in-pdf-page/)
- [파이썬에서 PDF에 페이지 번호 추가](/pdf/ko/python-net/add-page-number/)