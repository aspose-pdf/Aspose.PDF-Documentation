---
title: Python을 사용하여 PDF에 텍스트 스탬프 추가
linktitle: PDF 파일의 텍스트 스탬프
type: docs
weight: 20
url: /ko/python-net/text-stamps-in-the-pdf-file/
description: Aspose.PDF for Python 라이브러리의 TextStamp 클래스를 사용하여 PDF 문서에 텍스트 스탬프를 추가합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 텍스트 스탬프를 추가하는 방법
Abstract: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일에 텍스트 스탬프를 추가하는 포괄적인 가이드를 제공합니다. 여기에서는 `TextStamp` 클래스를 사용하여 글꼴 크기, 스타일, 색상 및 정렬과 같은 속성을 가진 맞춤형 텍스트 스탬프를 만드는 방법을 설명합니다. 문서는 간단한 텍스트 스탬프를 추가하고, 텍스트 정렬을 구성하며, 채우기 스트로크 텍스트와 같은 고급 렌더링 모드를 적용하는 코드 스니펫을 포함합니다. 첫 번째 섹션에서는 `Document`와 `TextStamp` 객체를 생성하고, 텍스트 속성을 설정한 뒤 특정 페이지에 스탬프를 추가하는 과정을 설명합니다. 두 번째 섹션에서는 `text_alignment` 속성을 소개하여 텍스트를 수평 및 수직으로 정렬하는 방법을 보여주며, PDF 페이지에 텍스트를 가운데 정렬하는 코드 예제를 제공합니다. 마지막 섹션에서는 렌더링 모드에 대해 논의하고, `TextState` 객체를 사용해 스트로크 색상 및 렌더링 모드를 설정한 후 스탬프에 적용하여 채우기 스트로크 텍스트를 추가하는 방법을 시연합니다. 각 섹션은 이해와 구현을 돕기 위한 실용적인 예제와 함께 제공됩니다.
---

## Python으로 텍스트 스탬프 추가

PDF 파일에 텍스트 스탬프를 추가하려면 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스를 사용할 수 있습니다. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등 텍스트 기반 스탬프를 만들기 위해 필요한 속성을 제공합니다. 텍스트 스탬프를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, Page의 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 메서드를 호출하여 PDF에 스탬프를 추가할 수 있습니다. 다음 코드 스니펫은 PDF 파일에 텍스트 스탬프를 추가하는 방법을 보여줍니다. 이는 PDF 페이지에 주석, 워터마크 또는 라벨을 추가할 때 유용합니다.

1. PDF 문서를 엽니다.
1. TextStamp 객체를 생성합니다.
1. 스탬프 배경 동작을 설정합니다.
1. 페이지에 스탬프를 배치합니다.
1. 필요에 따라 스탬프를 회전합니다.
1. 텍스트 속성을 설정합니다.
1. 페이지에 스탬프를 추가합니다.
1. 수정된 PDF 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

