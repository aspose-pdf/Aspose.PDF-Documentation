---
title: Python에서 벡터 그래픽으로 작업하기
linktitle: 벡터 그래픽으로 작업하기
type: docs
weight: 100
url: /ko/python-net/working-with-vector-graphics/
description: Python에서 GraphicsAbsorber를 사용하여 PDF 페이지 간에 벡터 그래픽을 추출, 이동, 제거 및 복사하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 그래픽스 업소버를 사용하여 Python에서 PDF 벡터 그래픽을 검사하고 조작할 수 있습니다.
Abstract: 이 문서에서는 GraphicsAbsorber 클래스를 사용하여.NET을 통해 파이썬용 Aspose.PDF 에서 벡터 그래픽을 사용하는 방법을 설명합니다.Python 워크플로의 저수준 제어를 사용하여 PDF 페이지에서 벡터 요소를 추출하고, 이동 또는 제거하고, 페이지 간에 그래픽을 복사하는 방법을 알아봅니다.
---

[.NET을 통한 파이썬용 Aspose.PDF](/pdf/ko/python-net/) 를 제공합니다 [그래픽 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) PDF 페이지에 이미 있는 벡터 그래픽에 액세스하고 조작하기 위한 클래스입니다.이를 호출해 주세요. `visit` 모든 페이지에서 패스, 모양 및 기타 그래픽 연산자를 추출한 다음 필요에 따라 해당 요소를 이동, 제거 또는 복사하는 메서드를 사용합니다.

처음부터 새 모양을 그리는 대신 기존 PDF에 포함된 벡터 드로잉 요소를 검사하거나 수정해야 하는 경우 이 페이지를 사용하십시오.

## 그래픽스 추출

추출은 모든 벡터 그래픽 작업의 시작점입니다. `GraphicsAbsorber` 페이지의 내용 스트림을 읽고 각 그래픽 요소를 페이지 참조, 위치 및 원시 연산자와 함께 표시합니다.

1. PDF 문서를 엽니다.
1. 만들기 [그래픽 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) 예.
1. 전화 `visit` 대상 페이지에서 채울 수 있습니다. `elements`.
1. 이터레이션 오버 `elements` 위치 및 작업자 수를 검사합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` 의 일부입니다 `aspose.pdf.vector` 네임스페이스로, PDF 콘텐츠 스트림의 벡터 그래픽과 상호 작용하도록 특별히 설계되었습니다.

## 움직이는 그래픽

추출 후 새로 설정 `position` 각 요소에 대해 동일한 페이지에 재배치하십시오.업데이트를 마무리하세요 `suppress_update` / `resume_update` 콘텐츠 스트림 쓰기를 단일 작업으로 일괄 처리하기 위한 호출을 통해 중복 리페인팅을 방지합니다.

1. PDF 문서를 엽니다.
1. 만들기 `GraphicsAbsorber` 및 전화 `visit` 대상 페이지에.
1. 전화 `suppress_update` 콘텐츠 스트림 쓰기를 일시 중지합니다.
1. 업데이트 `position` 각 요소에 대해
1. 전화 `resume_update` 모든 변경 사항을 한 번에 커밋합니다.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## 그래픽 제거

페이지에서 특정 벡터 요소를 삭제하려면 위치 또는 경계 사각형을 기준으로 필터링한 다음 제거합니다.Aspose.PDF for Python은 요소를 인라인으로 제거할지 아니면 먼저 수집할지에 따라 두 가지 접근 방식을 제공합니다.

### 방법 1: 사각형 경계를 사용하여 인라인 제거

이 접근 방식은 사각형을 기준으로 각 요소의 위치를 확인하고 호출합니다. `element.remove()` 루프 바로 내부.간결한 코드를 원하고 나중에 제거된 세트를 검사할 필요가 없을 때 사용하세요.

1. PDF 문서를 엽니다.
1. 만들기 `GraphicsAbsorber` 및 전화 `visit` 대상 페이지에.
1. 대상 정의 [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. 전화 `suppress_update` 콘텐츠 스트림 쓰기를 일시 중지합니다.
1. 이터레이션 `elements`, 전화 `remove()` 위치가 직사각형 내부에 있는 각 요소에 대해
1. 전화 `resume_update` 삭제를 커밋합니다.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### 방법 2: 먼저 요소를 수집한 다음 삭제

이 접근 방식은 일치하는 요소를 다음과 같이 수집합니다. [그래픽 요소 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) 컬렉션을 다음 사람에게 전달합니다. `page.delete_graphics`.삭제를 커밋하기 전에 제거할 항목을 검토하거나 기록해야 할 때 사용하세요.

1. PDF 문서를 엽니다.
1. 만들기 `GraphicsAbsorber` 및 전화 `visit` 대상 페이지에.
1. 대상 사각형을 정의합니다.
1. 이터레이션 `elements` 일치하는 요소를 a에 추가 `GraphicElementCollection`.
1. 전화 `page.contents.suppress_update` 콘텐츠 스트림 쓰기를 일시 중지합니다.
1. 전화 `page.delete_graphics` 컬렉션과 함께.
1. 전화 `page.contents.resume_update` 삭제를 커밋합니다.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## 다른 페이지에 그래픽 추가

한 페이지에서 추출한 벡터 요소를 같은 문서의 다른 페이지에 배치할 수 있습니다.요소를 하나씩 추가하거나 한 번의 호출로 전체 컬렉션을 전달하는 두 가지 방법을 사용할 수 있습니다.

### 방법 1: 요소를 개별적으로 추가

대상 페이지에 배치하기 전에 개별 요소를 필터링하거나 변형하는 등 요소별 제어가 필요한 경우 이 방법을 사용하십시오.

1. PDF 문서를 엽니다.
1. 만들기 `GraphicsAbsorber` 및 전화 `visit` 소스 페이지에.
1. 문서에 새 대상 페이지를 추가합니다.
1. 전화 `page_2.contents.suppress_update` 콘텐츠 스트림 쓰기를 일시 중지합니다.
1. 전화 `element.add_on_page(page_2)` 각 요소에 대해.
1. 전화 `page_2.contents.resume_update` 모든 추가 사항을 커밋합니다.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### 방법 2: 전체 컬렉션을 한 번에 추가

수동으로 반복하지 않고 추출된 모든 요소를 한 번의 작업으로 페이지에 복사하려는 경우 이 방법을 사용하십시오.

1. PDF 문서를 엽니다.
1. 만들기 `GraphicsAbsorber` 및 전화 `visit` 소스 페이지에.
1. 문서에 새 대상 페이지를 추가합니다.
1. 전화 `page_2.contents.suppress_update` 콘텐츠 스트림 쓰기를 일시 중지합니다.
1. 전화 `page_2.add_graphics` 전체와 함께 `elements` 컬렉션.
1. 전화 `page_2.contents.resume_update` 모든 추가 사항을 커밋합니다.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## 관련 주제

- [파이썬에서의 고급 PDF 작업](/pdf/ko/python-net/advanced-operations/)
- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [파이썬에서 PDF 연산자로 작업하기](/pdf/ko/python-net/working-with-operators/)
- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
