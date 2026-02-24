---
title: Python을 사용하여 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 30
url: /ko/python-net/add-watermarks/
description: 이 문서는 아티팩트를 활용하고 PDF에 워터마크를 프로그래밍 방식으로 Python을 사용하여 적용하는 기능에 대해 설명합니다.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 워터마크를 추가하는 방법
Abstract: 이 문서는 .NET을 통해 Python용 Aspose.PDF를 사용하여 아티팩트 관리를 통해 PDF 문서에 워터마크를 추가하는 방법을 다룹니다. 아티팩트를 처리하기 위한 주요 클래스인 `Artifact`와 `ArtifactCollection`을 소개하고, 이들에 어떻게 `Page` 클래스의 `Artifacts` 속성을 통해 접근하는지 설명합니다. 또한 `Artifact` 클래스의 속성들을 자세히 설명하는데, 여기에는 `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, `opacity`와 같은 속성이 포함되어 PDF 파일 내에서 아티팩트를 포괄적으로 조작할 수 있게 해 줍니다. 추가로 실용적인 예제가 제공되어 Python을 사용해 PDF 첫 페이지에 프로그래밍 방식으로 워터마크를 추가하는 방법을 보여줍니다. 코드 스니펫은 `WatermarkArtifact`의 생성 및 구성, 텍스트, 정렬, 회전 및 투명도 설정을 보여주며, 이를 PDF 문서에 추가하고 변경 사항을 저장하는 과정을 설명합니다.
---

## 프로그래밍 예제: PDF 파일에 워터마크 추가 방법

Aspose.PDF for Python via .NET을 사용하여 PDF에 워터마크 아티팩트를 추가합니다 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). 워터마크는 페이지에 브랜드, 보안 또는 정보 제공을 위해 적용되는 시각적 오버레이입니다. 이 예제에서는 워터마크를 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 적용하기 전에 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 외관, [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 및 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)을 사용한 위치 지정, 회전 및 투명도를 구성하는 방법을 보여줍니다.

1. 워터마크 아티팩트를 생성합니다 (참조 [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. 텍스트 상태를 구성합니다 (참조 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. 텍스트를 워터마크에 바인딩합니다.
1. [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 및 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)를 사용하여 위치와 스타일을 정의합니다.
1. 페이지의 [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션을 통해 워터마크를 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 첨부합니다 (참조 [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. 업데이트된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 사용하여 저장합니다.

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


