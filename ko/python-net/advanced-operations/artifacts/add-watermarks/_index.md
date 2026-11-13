---
title: Python에서 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 30
url: /ko/python-net/add-watermarks/
description: Python에서 PDF 페이지에 스타일이 적용된 텍스트 워터마크 아티팩트를 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 워터마크 추가
Abstract: Python에서 PDF 페이지에 스타일이 적용된 텍스트 워터마크 아티팩트를 추가합니다.
---

사용 `WatermarkArtifact` PDF의 첫 페이지에 텍스트 워터마크를 추가하려면.

## PDF에 워터마크 추가

텍스트와 스타일을 설정한 다음 정렬, 회전 및 불투명도를 구성합니다. 설정 `is_background` 페이지 콘텐츠 뒤에 워터마크를 배치하기 위해.

```python
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

## 관련 항목

- [워터마크 세부 정보 추출](/pdf/ko/python-net/extract-watermarks/)
- [워터마크 제거](/pdf/ko/python-net/remove-watermarks/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
