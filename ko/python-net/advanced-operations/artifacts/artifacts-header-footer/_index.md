---
title: Python을 사용하여 PDF 머리말과 꼬리말 관리하기
linktitle: PDF 머리글 및 바닥글 관리
type: docs
weight: 70
url: /ko/python-net/artifacts-header-footer/
description: Python과 Aspose.PDF 를 사용하여 PDF 문서의 머리말과 꼬리말을 관리하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 머리말과 꼬리말을 추가, 사용자 지정 및 제거하는 방법
Abstract: 머리말과 꼬리말 관리는 비즈니스, 출판 및 자동화 워크플로우에서 PDF 문서 작업을 할 때 일반적으로 필요한 사항입니다.이 문서에서는 Aspose.PDF for Python을 사용하여 글꼴, 크기, 색상 및 정렬과 같은 사용자 지정 스타일을 사용하여 전문가 수준의 머리글과 바닥글을 추가하는 방법을 보여줍니다.또한 머리말과 꼬리말과 같은 기존 페이지 매김 아티팩트를 감지하고 PDF 페이지에서 제거하는 방법도 보여줍니다.개발자는 재사용 가능한 함수와 명확한 예제를 통해 브랜딩, 보고 또는 파일 정리를 위해 이러한 기능을 문서 처리 시스템에 빠르게 통합할 수 있습니다.
---

## 스타일이 적용된 텍스트 아티팩트 만들기

이 유틸리티 함수는 Python용 Aspose.PDF 를 사용하여 PDF 페이지용 재사용 가능한 텍스트 아티팩트를 만드는 방법을 설명합니다.글꼴 설정, 색상, 크기 및 정렬을 포함하여 일관된 서식을 사용하여 스타일이 지정된 머리글 또는 바닥글을 생성하도록 설계되었습니다.이 함수는 아티팩트 생성을 추상화하여 다양한 페이지 수준의 텍스트 장식에 재사용할 수 있도록 합니다.

1. 아티팩트 오브젝트를 인스턴스화합니다.
1. 아티팩트 텍스트 내용을 설정합니다.
1. 텍스트 스타일 적용
1. 정렬을 설정합니다.
1. 구성된 아티팩트를 반환합니다.

```python
from os import path
import aspose.pdf as ap
import sys

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

## PDF에 머리글 추가

1. 입력 PDF를 엽니다.
1. “샘플 헤더”라는 텍스트로 헤더 아티팩트를 생성합니다.
1. 첫 페이지에 추가합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## PDF에 바닥글 추가

1. 입력 PDF를 엽니다.
1. “샘플 푸터”라는 텍스트로 푸터 아티팩트를 생성합니다.
1. 첫 페이지에 추가합니다.
1. 출력 파일을 저장합니다.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## 머리글 또는 바닥글 아티팩트 삭제

1. PDF를 엽니다.
1. 페이지네이션 머리글 또는 바닥글로 표시된 아티팩트를 찾을 수 있습니다.
1. 첫 페이지에서 삭제하세요.
1. 정리한 문서를 저장합니다.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## 관련 아티팩트 주제

- [파이썬에서 PDF 아티팩트로 작업하기](/pdf/ko/python-net/artifacts/)
- [파이썬에서 PDF 배경 추가](/pdf/ko/python-net/add-backgrounds/)
- [파이썬에서 PDF에 베이츠 넘버링 추가](/pdf/ko/python-net/add-bates-numbering/)
- [PDF 파일의 아티팩트 유형 수 계산](/pdf/ko/python-net/counting-artifacts/)