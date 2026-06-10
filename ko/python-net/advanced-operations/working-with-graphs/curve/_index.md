---
title: Python에서 PDF에 곡선 모양 추가
linktitle: 커브 추가
type: docs
weight: 30
url: /ko/python-net/add-curve/
description: Python에서 PDF 파일의 곡선 모양을 그리고 채우는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 곡선 모양 그리기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 곡선 모양을 추가하는 방법을 보여줍니다.Graph 컨테이너에서 윤곽선이 있는 곡선 만들기, 곡선 객체 채우기, 사용자 지정 곡선 경로 렌더링에 대해 설명합니다.
---

## 커브 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [커브](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) 도형을 통해 PDF 페이지로 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.

이 문서에서는 윤곽선 곡선과 채워진 곡선을 모두 만드는 방법을 보여줍니다.

아래 단계를 따르십시오.

1. 작성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 예.
1. 작성 [그래프 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) 특정 치수로.
1. 세트 [테두리](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 그래프 객체용
1. 추가 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 페이지의 단락 모음에 대한 개체.
1. PDF 파일을 저장하세요.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

다음 그림은 코드 스니펫으로 실행한 결과를 보여줍니다.

![드로잉 커브](drawing_curve.png)

## 채워진 곡선 오브젝트 만들기

이 예제에서는 색상으로 채워진 Curve 객체를 추가하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

채워진 곡선을 추가한 결과:

![채워진 곡선](filled_curve.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [파이썬에서 PDF에 호 모양 추가](/pdf/ko/python-net/add-arc/)
- [파이썬에서 PDF에 선 모양 추가](/pdf/ko/python-net/add-line/)
- [Python에서 PDF에 타원 모양 추가](/pdf/ko/python-net/add-ellipse/)