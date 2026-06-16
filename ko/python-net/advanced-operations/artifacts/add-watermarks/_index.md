---
title: 파이썬에서 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 30
url: /ko/python-net/add-watermarks/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 파일에 워터마크 아티팩트를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 워터마크를 추가하는 방법
Abstract: 이 문서에서는 .NET을 통해 Python용 Aspose.PDF 를 사용하여 아티팩트 관리를 통해 PDF 문서에 워터마크를 추가하는 방법에 대해 설명합니다.아티팩트 처리를 위한 주요 클래스인 '아티팩트'와 '아티팩트 컬렉션'을 소개하고 'Page' 클래스의 '아티팩트' 속성을 통해 아티팩트에 액세스하는 방법을 설명합니다.이 문서에서는 '콘텐츠', '형식', '이미지', '텍스트', '사각형', '회전', '불투명도'와 같은 속성을 포함하여 'Artifact' 클래스의 속성을 자세히 설명합니다. 이를 통해 PDF 파일 내의 아티팩트를 포괄적으로 조작할 수 있습니다.또한 Python을 사용하여 PDF의 첫 페이지에 프로그래밍 방식으로 워터마크를 추가하는 방법을 보여주는 실제 예제도 제공됩니다.코드 스니펫은 PDF 문서에 추가하고 변경 사항을 저장하기 전에 텍스트, 정렬, 회전 및 불투명도를 설정하여 `Watermark Artifact`의 생성 및 구성을 보여줍니다.
---

PDF에 워터마크 아티팩트 추가 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .NET을 통해 파이썬용 Aspose.PDF 사용.워터마크는 브랜딩, 보안 또는 정보 제공 목적으로 페이지에 적용되는 시각적 오버레이입니다.이 예제에서는 구성 방법을 보여줍니다. [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 모양, 위치 지정 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 과 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)에 워터마크를 적용하기 전의 회전 및 투명도 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## PDF에서 워터마크 추출

1. PDF 문서를 로드합니다.
1. 페이지 아티팩트에 액세스합니다.
1. 워터마크 아티팩트를 필터링합니다.
1. 워터마크 요소를 수집하세요.
1. 워터마크 속성을 추출합니다.
1. 워터마크 정보를 출력합니다.

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## PDF에 워터마크 추가

파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 텍스트 워터마크를 추가합니다.

1. PDF 문서를 로드합니다.
1. 텍스트 상태를 생성합니다.
1. 워터마크 아티팩트를 생성합니다.
1. 워터마크 텍스트와 스타일을 설정합니다.
1. 위치 지정 및 회전을 구성합니다.
1. 불투명도 및 배경 동작을 설정합니다.
1. 페이지에 워터마크를 첨부합니다.
1. 업데이트된 문서를 저장합니다.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## PDF 페이지에서 워터마크 아티팩트 제거 

Python용 Aspose.PDF API를 사용하여 PDF 문서의 특정 페이지에서 워터마크 아티팩트를 제거합니다.이 접근 방식은 페이지 아티팩트로 저장된 워터마크 요소 (특히 페이지 매김 워터마크 하위 유형으로 분류된 요소) 를 대상으로 하고, 이를 반복하고, 업데이트된 문서를 저장하기 전에 삭제합니다.

1. PDF 문서를 로드합니다.
1. 페이지 아티팩트에 액세스합니다.
1. 워터마크 아티팩트를 필터링합니다.
1. 워터마크 아티팩트를 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## 관련 아티팩트 주제

- [파이썬에서 PDF 아티팩트로 작업하기](/pdf/ko/python-net/artifacts/)
- [파이썬에서 PDF 배경 추가](/pdf/ko/python-net/add-backgrounds/)
- [파이썬에서 PDF에 베이츠 넘버링 추가](/pdf/ko/python-net/add-bates-numbering/)
- [PDF 파일의 아티팩트 유형 수 계산](/pdf/ko/python-net/counting-artifacts/)