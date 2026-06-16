---
title: 파이썬에서 PDF 링크 추출하기
linktitle: 링크 추출
type: docs
weight: 30
url: /ko/python-net/extract-links/
description: Python의 PDF 문서에서 링크 주석과 하이퍼링크를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크를 추출하는 방법
Abstract: .NET을 통한 Python용 Aspose.PDF 링크 추출 가이드에서는 Python을 사용하여 PDF 문서에서 하이퍼링크 주석을 프로그래밍 방식으로 검색하는 방법을 설명합니다.이 문서에는 실용적인 코드 예제가 포함되어 있으며 링크 감사, 탐색 분석 또는 대화형 문서 기능 구축과 같은 작업에 이 기능을 사용하는 방법을 설명합니다.단일 페이지 PDF로 작업하든 대규모 배치를 처리하든, 이 안내서는 하이퍼링크 추출에 대한 명확하고 효율적인 접근 방식을 제공합니다.
---

## PDF 파일에서 링크 추출

이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF의 첫 페이지에 있는 모든 링크 주석을 반복하는 방법을 보여줍니다.주석을 필터링하여 LinkAnnotation 유형의 주석을 식별하고 안전하게 캐스팅한 다음 페이지 색인과 페이지의 사각형 위치를 인쇄합니다.

이는 PDF의 기존 링크 주석에 대한 디버깅, 분석 또는 자동 업데이트에 사용할 수 있습니다.

1. PDF 문서를 로드합니다..문서 (path_infile) 를 사용하여 파일을 엽니다.
1. 첫 페이지에서 주석에 액세스할 수 있습니다.문서.pages [1] .주석을 사용하여 모든 주석을 검색하십시오.
1. 링크 주석 유형만 필터링합니다.각 주석의 annotation_type을 확인하세요.
1. 링크 주석을 캐스팅하고 처리합니다.is_assignable () 및 cast () 를 사용하여 링크 주석 속성에 안전하게 액세스할 수 있도록 하세요.
1. 주석 세부 정보를 인쇄합니다.각 링크의 페이지 색인과 사각형 (위치) 을 출력합니다.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## PDF 파일에서 하이퍼링크 추출

이 코드는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 첫 페이지에서 모든 링크 주석 객체를 추출한 다음 GoTouriAction이 포함된 링크 주석 객체를 식별하는 방법을 보여줍니다.이러한 각 링크에 대해 페이지 색인과 대상 URI를 출력합니다.

이는 다음과 같은 작업에 유용합니다.

- PDF의 외부 링크 감사
- 문서 또는 지원 URL 추출
- 깨지거나 오래된 하이퍼링크 감지

1. PDF 문서를 로드합니다..Document를 사용하여 파일을 엽니다.
1. 첫 페이지에서 모든 링크 주석을 가져옵니다.AnnotationType.link 유형의 주석만 포함하도록 주석을 필터링합니다.
1. 검사를 입력하고 링크 주석으로 변환하십시오.속성에 액세스하기 전에 각 주석이 실제로 링크 어노테이션인지 확인하세요.
1. 링크의 작업 유형을 확인합니다.GoTouriAction을 사용하는 링크 (예: 웹 URL로 연결되는 링크) 를 필터링합니다.
1. URI 및 페이지 색인을 추출하고 인쇄합니다..uri를 사용하여 외부 링크를 가져오고 컨텍스트에는.page_index를 사용하세요.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## 관련 링크 주제

- [파이썬에서 PDF 링크로 작업하기](/pdf/ko/python-net/links/)
- [파이썬으로 PDF 링크 만들기](/pdf/ko/python-net/create-links/)
- [Python을 사용하여 PDF에서 링크 업데이트](/pdf/ko/python-net/update-links/)