---
title: 파이썬에서 PDF에 아크 모양 추가
linktitle: 아크 추가
type: docs
weight: 10
url: /ko/python-net/add-arc/
description: Python에서 PDF 파일의 호 모양을 그리고 채우는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 호 모양 그리기
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 호 모양을 추가하는 방법을 보여줍니다.윤곽선이 있는 호를 만들고, 채워진 호 세그먼트를 그리고, Graph 컨테이너에 추가하는 방법을 다룹니다.
---

## 아크 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [아크](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 를 사용하여 PDF 페이지의 도형을 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.다이어그램과 테크니컬 일러스트레이션에 윤곽선이 있는 호와 채워진 호 세그먼트를 그릴 수 있습니다.

아래 단계를 따르십시오.

1. 작성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 예.
1. 작성 [그래프 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 특정 치수로.
1. 세트 [테두리](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 그래프 객체용
1. 해당하는 아크 오브젝트를 생성합니다.
1. 이 객체를 그래프 객체의 Shapes 컬렉션에 추가합니다.
1. 추가 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 페이지의 단락 모음에 대한 개체.
1. PDF 파일을 저장하세요.

다음 코드 스니펫은 을 추가하는 방법을 보여줍니다. [아크](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 목적.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## 채워진 아크 오브젝트 만들기

이 예제에서는 색상으로 채워진 호 세그먼트를 추가하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

채워진 호를 추가한 결과:

![채워진 아크](filled_arc.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [Python에서 PDF에 원 모양 추가](/pdf/ko/python-net/add-circle/)
- [Python에서 PDF에 곡선 모양 추가](/pdf/ko/python-net/add-curve/)
- [파이썬에서 PDF에 선 모양 추가](/pdf/ko/python-net/add-line/)