---
title: 파이썬에서 PDF 배경 추가
linktitle: 배경 추가
type: docs
weight: 20
url: /ko/python-net/add-backgrounds/
description: .NET을 통해 파이썬용 Aspose.PDF 의 BackgroundArtifact 클래스를 사용하여 파이썬에서 PDF 페이지에 배경 이미지를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 배경을 추가하는 방법
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 배경 이미지를 사용하는 방법에 대해 설명합니다.배경 이미지를 개별 페이지 개체에 통합할 수 있는 `BackgroundArtifact` 클래스를 활용하여 문서에 워터마크나 섬세한 디자인을 추가하는 기능을 중점적으로 설명합니다.이 문서에서는 이 기능을 구현하는 방법을 보여주는 실용적인 코드 예제를 제공합니다.이 프로세스에는 새 PDF 문서 만들기, 페이지 추가, `Background Artifact` 개체 만들기, 배경 이미지 설정, 페이지의 아티팩트 컬렉션에 배경 아티팩트 추가 등이 포함됩니다.마지막으로 수정된 문서는 PDF 파일로 저장됩니다.이 기법을 사용하면 PDF 문서를 시각적으로 더 잘 표현할 수 있습니다.
---

## PDF에 배경 이미지 추가

배경 이미지를 사용하여 문서에 워터마크 또는 기타 미묘한 디자인을 추가할 수 있습니다..NET을 통한 Python용 Aspose.PDF 문서에서 각 PDF 문서는 페이지 모음이고 각 페이지에는 아티팩트 컬렉션이 포함되어 있습니다. [배경 아티팩트](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) 클래스는 페이지 개체에 배경 이미지를 추가하는 데 사용할 수 있습니다.

이 방법은 장식 이미지를 검색 가능한 문서 텍스트로 바꾸지 않고 주요 PDF 내용 뒤에 배치해야 할 때 유용합니다.

다음 코드 스니펫은 Python에서 BackgroundArtifact 객체를 사용하여 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

1. PDF 문서를 로드합니다.
1. 배경 아티팩트 만들기.
1. 이미지 파일을 로드합니다.
1. 아티팩트를 페이지에 첨부합니다.
1. 업데이트된 문서를 저장합니다.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF에 불투명도가 있는 배경 이미지 추가

파이썬용 Aspose.PDF 를 사용하여 PDF 페이지에 반투명 배경 이미지를 추가합니다.

불투명도를 적용하면 배경 이미지가 부분적으로 투명해져서 원본 페이지 내용 (텍스트, 이미지 등) 이 선명하게 보입니다.이는 특히 다음과 같은 경우에 유용합니다.

- 워터마크
- 브랜딩 오버레이
- 미묘한 디자인 개선

배경이 아티팩트로 추가되어 모든 페이지 콘텐츠 뒤에 그대로 유지됩니다.

1. PDF 문서를 로드합니다.
1. 배경 아티팩트 만들기.
1. 이미지 파일을 로드합니다.
1. 불투명도 수준을 설정합니다.
1. 아티팩트를 페이지에 첨부합니다.
1. 업데이트된 문서를 저장합니다.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF에 배경색 추가

파이썬용 Aspose.PDF 파일을 사용하여 PDF 페이지에 단색 배경색을 적용합니다.

1. PDF 문서를 로드합니다.
1. 배경 아티팩트 만들기.
1. 배경색을 설정합니다.
1. 아티팩트를 페이지에 첨부합니다.
1. 업데이트된 문서를 저장합니다.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF에서 배경 제거

파이썬용 Aspose.PDF 파일을 사용하여 PDF 페이지에서 배경 아티팩트를 제거합니다.
PDF의 배경은 아티팩트로 저장되는 경우가 많은데, 이 메서드는 배경 요소로 분류된 아티팩트만 선택적으로 식별하여 제거합니다.

1. PDF 문서를 로드합니다.
1. 페이지 아티팩트에 액세스합니다.
1. 배경 아티팩트를 필터링합니다.
1. 배경 요소를 수집하세요.
1. 배경 아티팩트를 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## 관련 아티팩트 주제

- [파이썬에서 PDF 아티팩트로 작업하기](/pdf/ko/python-net/artifacts/)
- [파이썬에서 PDF에 워터마크 추가](/pdf/ko/python-net/add-watermarks/)
- [파이썬에서 PDF에 베이츠 넘버링 추가](/pdf/ko/python-net/add-bates-numbering/)
- [PDF 파일의 아티팩트 유형 수 계산](/pdf/ko/python-net/counting-artifacts/)