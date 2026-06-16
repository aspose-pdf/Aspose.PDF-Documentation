---
title: 파이썬에서 PDF 링크 업데이트
linktitle: 링크 업데이트
type: docs
weight: 20
url: /ko/python-net/update-links/
description: Python에서 PDF 링크 모양과 대상을 업데이트하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크를 업데이트하는 방법
Abstract: .NET을 통한 링크 업데이트에 관한 Python용 Aspose.PDF 안내서는 Python을 사용하여 PDF 문서 내에서 하이퍼링크 동작을 수정하는 과정을 개발자에게 안내합니다.특정 페이지, 외부 웹 사이트 또는 기타 PDF 파일을 가리키도록 링크 대상을 변경하는 방법을 설명합니다.이 문서에서는 텍스트 색상을 비롯한 링크 주석의 모양을 조정하는 방법도 다루고 각 시나리오에 대한 실용적인 코드 예제를 제공합니다.이 리소스는 오래된 URL을 수정하든 탐색을 향상시키든 관계없이 프로그래밍 방식으로 링크를 관리하는 명확하고 효율적인 접근 방식을 제공합니다.
---

## 링크 주석 텍스트 색상 업데이트

이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF의 첫 페이지에서 모든 링크 주석을 감지한 다음 글꼴 색상을 빨간색으로 변경하여 각 링크 근처의 텍스트를 강조 표시하는 방법을 보여줍니다.각 링크 사각형 주위의 영역이 약간 확장된 TextFragmentAbsorber를 사용하여 근처에 있는 텍스트를 찾아 수정합니다.

다음과 같은 용도로 사용할 수 있습니다.

- 문서에 링크를 시각적으로 표시하기
- 연계 콘텐츠 강조를 통한 접근성 강화
- 검토 또는 내보내기 전 PDF 파일 사전 처리

스크립트는 각 링크 주석에 대해 사각형 경계를 검색하고 주변 텍스트를 포함하도록 해당 영역을 약간 확장하여 더 넓은 시각적 식별을 가능하게 합니다.그런 다음 이 확장된 영역에 TextFragmentAbsorber를 적용하여 해당 영역 내에 있는 텍스트 조각을 추출합니다.캡처된 이러한 조각은 글꼴 색상을 빨간색으로 변경하여 수정되므로 주변 텍스트를 강조하고 검토할 수 있도록 효과적으로 표시할 수 있습니다.이러한 업데이트를 모두 적용한 후에는 강조 표시된 주석과 관련 텍스트가 보존되어 수정된 문서가 출력 경로에 저장됩니다.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## 테두리 업데이트

스크립트는 문서의 첫 페이지에 초점을 맞추고 모든 주석을 필터링하여 LINK 유형의 주석만 선택합니다. 이러한 주석은 일반적으로 하이퍼링크나 탐색 트리거와 같은 대화형 요소를 나타냅니다.코드는 이러한 각 링크 주석에 대해 LinkAnnotation 유형으로 캐스팅하고 색상 속성을 빨간색으로 업데이트하여 다른 내용과 차별화되도록 시각적으로 강조 표시합니다.모든 링크 주석을 수정한 후 업데이트된 문서는 새 스타일을 유지하면서 정의된 출력 위치에 저장됩니다.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## 웹 대상 업데이트

경로가 정해지면 Aspose.PDF 라이브러리를 사용하여 원본 문서를 로드하여 내용을 수정할 수 있습니다.그런 다음 스크립트는 문서의 첫 페이지에 초점을 맞추어 모든 주석을 필터링하고 일반적으로 클릭 가능한 영역이나 하이퍼링크를 나타내는 링크 유형의 주석만 선택합니다.유형 오류를 방지하고 안전한 처리를 위해 is_assignable로 각 주석을 검사한 다음 적절한 링크 주석 유형으로 캐스팅합니다.링크가 GoTouriAction과 연결된 경우, 즉 웹 주소를 가리키는 경우 스크립트는 사용자를 “로 리디렉션하도록 해당 URI를 업데이트합니다.”https://www.aspose.com". 마지막으로 원하는 변경 사항이 모두 적용된 후 수정된 문서가 지정된 출력 경로에 저장됩니다.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## 관련 링크 주제

- [파이썬에서 PDF 링크로 작업하기](/pdf/ko/python-net/links/)
- [파이썬으로 PDF 링크 만들기](/pdf/ko/python-net/create-links/)
- [파이썬에서 PDF 링크 추출하기](/pdf/ko/python-net/extract-links/)