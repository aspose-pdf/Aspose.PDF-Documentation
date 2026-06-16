---
title: Python에서 PDF에 사각형 모양 추가
linktitle: 사각형 추가
type: docs
weight: 50
url: /ko/python-net/add-rectangle/
description: Python에서 PDF 파일의 사각형 모양을 그리고 채우는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 사각형 모양 그리기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 사각형 모양을 추가하는 방법을 보여줍니다.윤곽선이 있는 사각형, 단색 및 그라데이션 채우기, 알파 투명도, Z-순서 제어에 대해 다룹니다.
---

## 사각형 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 도형을 통해 PDF 페이지로 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.윤곽선이 있는 사각형을 그리고 단색, 그라디언트 또는 투명 채우기를 적용할 수 있습니다.

아래 단계를 따르십시오.

1. 새 PDF 만들기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 추가 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) PDF 파일의 페이지 모음으로
1. 추가 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 페이지 인스턴스의 단락 모음으로
1. 작성 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 예.
1. 테두리 설정 [그래프 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. 추가 [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) Graph 객체의 도형 컬렉션에 대한 객체입니다.
1. 페이지 인스턴스의 단락 컬렉션에 그래프 객체를 추가합니다.
1. 추가 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 페이지 인스턴스의 단락 모음으로
1. 그리고 PDF 파일을 저장하세요

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![사각형 만들기](create_rectangle.png)

## 채워진 사각형 개체 만들기

.NET을 통한 파이썬용 Aspose.PDF 는 사각형 객체를 특정 색상으로 채우는 기능도 제공합니다.

다음 코드 스니펫은 을 추가하는 방법을 보여줍니다. [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 색상으로 채워진 오브젝트.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

단색으로 채워진 직사각형의 결과:

![채워진 직사각형](fill_rectangle.png)

## 그라데이션 채우기로 도면 추가

.NET을 통한 Python용 Aspose.PDF 는 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며 때로는 그래프 객체를 그라디언트 색상으로 채워야 할 수도 있습니다.

다음 코드 스니펫은 을 추가하는 방법을 보여줍니다. [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 그라데이션 컬러로 채워진 오브젝트입니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![그라데이션 직사각형](gradient.png)

## 알파 색상 채널을 사용하여 사각형 만들기

.NET을 통한 파이썬용 Aspose.PDF 또한 알파 색상 채널을 통한 투명성을 지원합니다.

다음 코드 스니펫은 을 추가하는 방법을 보여줍니다. [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 알파 값을 가진 객체.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![사각형 알파 채널 색상](rectangle_color.png)

## 모양의 Z-순서 제어

.NET용 Aspose.PDF 는 PDF 문서에 그래프 개체 (예: 그래프, 선, 사각형 등) 를 추가하는 기능을 지원합니다.PDF 파일 내에 동일한 객체의 인스턴스를 두 개 이상 추가하는 경우 Z-Order를 지정하여 렌더링을 제어할 수 있습니다.Z-Order는 객체를 서로 겹쳐서 렌더링해야 할 때도 사용됩니다.

다음 코드 스니펫은 렌더링 단계를 보여줍니다. [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 서로 겹쳐진 물체들.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![Z 오더 제어](control.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [Python을 사용하여 PDF 그래프의 모양 경계 확인하기](/pdf/ko/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [파이썬에서 PDF에 선 모양 추가](/pdf/ko/python-net/add-line/)
- [Python에서 PDF에 타원 모양 추가](/pdf/ko/python-net/add-ellipse/)