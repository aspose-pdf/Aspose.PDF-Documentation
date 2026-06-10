---
title: 파이썬에서 PDF에 선 모양 추가
linktitle: 라인 추가
type: docs
weight: 40
url: /ko/python-net/add-line/
description: Python에서 PDF 파일에서 선 모양과 스타일이 지정된 선을 그리는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 선 모양 그리기
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 선 모양을 추가하는 방법을 보여줍니다.기본 선 만들기, 파선 스타일 구성, 페이지 전체에 선 그리기에 대해 설명합니다.
---

## 라인 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [선](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 를 사용하여 PDF 페이지의 도형을 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.선 색상, 대시 패턴 및 배치를 제어할 수 있습니다.

아래 단계를 따르십시오.

1. 작성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 예.
1. 그래프 객체 생성
1. 추가 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 페이지의 단락 모음에 대한 개체.
1. 라인 생성 및 구성
1. 추가 [선](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 그래프로
1. PDF 파일을 저장하세요.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![라인 추가](add_line.png)

## PDF 문서에 점선 대시선을 추가하는 방법

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

점선 파선을 추가한 결과:

![점선](dash_line.png)

## 페이지 전체에 선 그리기

페이지 전체에 선을 그려 십자 모양을 만들 수도 있습니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![드로잉 라인](draw_line.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [Python에서 PDF에 곡선 모양 추가](/pdf/ko/python-net/add-curve/)
- [Python에서 PDF에 사각형 모양 추가](/pdf/ko/python-net/add-rectangle/)
- [Python을 사용하여 PDF 그래프의 모양 경계 확인하기](/pdf/ko/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
