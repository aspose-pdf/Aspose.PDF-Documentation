---
title: Python에서 PDF 헤더 및 푸터 추가
linktitle: 헤더와 푸터 추가
type: docs
weight: 70
url: /ko/python-net/artifacts-header-footer/
description: Python에서 PDF 페이지에 스타일이 적용된 헤더 및 푸터 아티팩트를 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 헤더와 푸터를 추가
Abstract: Python에서 PDF 페이지에 스타일이 적용된 헤더 및 푸터 아티팩트를 추가합니다.
---

사용 `HeaderArtifact` 그리고 `FooterArtifact` PDF 페이지에 실행 텍스트를 추가하려면. 이 예제들은 첫 번째 페이지에 아티팩트를 추가합니다.

## 스타일이 적용된 텍스트 아티팩트 만들기

추가 예제를 실행하기 전에 이 도우미 함수를 정의하세요. 이 함수는 머리글과 바닥글에 같은 글꼴, 크기, 색상, 정렬을 적용합니다.

```python
import aspose.pdf as ap

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact
```

## PDF에 헤더 추가

도우미 함수에 `HeaderArtifact`를 전달하고 반환된 아티팩트를 페이지에 추가하세요.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## PDF에 바닥글 추가

도우미 함수에 `FooterArtifact`를 전달하고 반환된 아티팩트를 페이지에 추가하세요.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## 관련 항목

- [머리글 및 바닥글 제거](/pdf/ko/python-net/remove-headers-footers/)
- [Python에서 PDF 아티팩트 작업](/pdf/ko/python-net/artifacts/)
