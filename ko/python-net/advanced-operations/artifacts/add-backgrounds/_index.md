---
title: Python에서 PDF 배경 추가
linktitle: 배경 추가
type: docs
weight: 20
url: /ko/python-net/add-backgrounds/
description: Python에서 PDF 페이지에 이미지 및 단색 배경을 추가하고 배경 이미지의 불투명도를 조정합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 배경을 추가
Abstract: Python에서 PDF 페이지에 이미지 및 단색 배경을 추가하고 배경 이미지의 불투명도를 조정합니다.
---

사용 `BackgroundArtifact` PDF 페이지의 콘텐츠 뒤에 이미지 또는 단색을 배치합니다. 이 예제들은 첫 번째 페이지를 수정합니다.

## PDF에 배경 이미지 추가

이미지 스트림을 `background_image`에 지정하고 아티팩트를 페이지에 추가하세요.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## PDF에 투명도와 함께 배경 이미지 추가

같은 함수에 0에서 1 사이의 불투명도 값을 전달하세요. 반투명 이미지에는 `0.5`를 사용하세요.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## PDF에 배경색 추가

단색 배경을 적용하려면 아티팩트의 `background_color`를 설정하세요.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 관련 항목

- [배경 제거](/pdf/ko/python-net/remove-backgrounds/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
