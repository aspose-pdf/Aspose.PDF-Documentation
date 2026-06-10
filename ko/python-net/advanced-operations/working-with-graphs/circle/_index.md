---
title: Python에서 PDF에 원 모양 추가
linktitle: 서클 추가
type: docs
weight: 20
url: /ko/python-net/add-circle/
description: Python에서 PDF 파일의 원 모양을 그리고 채우는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 원 모양 그리기
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 원 모양을 추가하는 방법을 보여줍니다.윤곽선이 있는 원 만들기, 원으로 색상 채우기, 원 개체 안에 텍스트 배치 등을 다룹니다.
---

## 서클 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [서클](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) 도형을 통해 PDF 페이지로 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.다이어그램, 주석, 간단한 시각적 요소에는 원을 사용하세요.

아래 단계를 따르십시오.

1. 작성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 예.
1. 작성 [그래프 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 특정 치수로.
1. 세트 [테두리](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 그래프 객체용
1. 추가 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 페이지의 단락 모음에 대한 개체.
1. PDF 파일을 저장하세요.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

그려진 원은 다음과 같습니다.

![드로잉 서클](drawing_circle.png)

## 채워진 원 오브젝트 만들기

이 예제에서는 원을 추가하고 색상으로 채우는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

채워진 원을 추가한 결과:

![채워진 원형](filled_circle.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [파이썬에서 PDF에 호 모양 추가](/pdf/ko/python-net/add-arc/)
- [Python에서 PDF에 타원 모양 추가](/pdf/ko/python-net/add-ellipse/)
- [Python에서 PDF에 사각형 모양 추가](/pdf/ko/python-net/add-rectangle/)