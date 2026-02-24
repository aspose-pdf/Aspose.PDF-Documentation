---
title: PDF 파일에 곡선 객체 추가
linktitle: 곡선 추가
type: docs
weight: 30
url: /ko/python-net/add-curve/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 곡선 객체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 곡선 객체 추가
Abstract: 이 문서는 Aspose.PDF 라이브러리(Python을 .NET을 통해 사용)를 사용하여 PDF 문서에 그래프 곡선을 구현하는 방법을 논의합니다. 프로젝트 라인의 합집합인 그래프 곡선 개념을 소개하고, 단순 베지어 곡선과 채워진 베지어 곡선을 프로그래밍 방식으로 생성하는 과정을 자세히 설명합니다. 문서는 단계별 지침과 코드 스니펫을 제공하여 PDF 내에서 곡선을 그리는 방법을 보여주며, Aspose.PDF의 드로잉 모듈을 사용한 그래픽 요소 조작을 강조합니다. 이 과정에는 `Document` 인스턴스 생성, 지정된 차원을 가진 `Drawing` 객체 정의, 테두리 설정, 그리고 PDF 페이지에 `Graph` 객체를 추가하는 것이 포함됩니다. 이러한 코드 예시의 시각적 결과는 생성된 곡선을 보여주는 이미지로 나타냅니다. 또한 문서는 채워진 곡선 객체의 생성에 대해 탐구하며, 곡선에 색상을 채우는 방법을 보여줍니다. 이는 기술 도면, 차트 또는 PDF 내 맞춤 일러스트와 같은 동적 그래픽 콘텐츠를 생성하는 데 중요합니다.
---

## 곡선 객체 추가

그래프 [곡선](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/)은 프로젝트 라인의 연결된 합집합이며, 각 라인은 보통 이중점에서 다른 세 라인과 만납니다.

이 문서에서는 PDF 문서에서 만들 수 있는 단순 그래프 곡선과 채워진 곡선을 조사합니다.

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에서 프로그래밍 방식으로 베지어 곡선을 그리는 방법을 보여줍니다. 드로잉 모듈을 활용하면 개발자는 외형과 위치를 정밀하게 제어하면서 복잡한 그래픽 요소를 만들 수 있습니다. 이러한 기능은 기술 도면, 차트 또는 맞춤 일러스트와 같이 PDF 내에서 동적으로 그래픽 콘텐츠를 생성해야 하는 애플리케이션에 필수적입니다.

아래 단계에 따라 진행하십시오:

1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 인스턴스를 생성합니다.
1. 특정 차원을 가진 [그리기 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)를 생성합니다.
1. 그리기 객체의 [테두리](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties)를 설정합니다.
1. 페이지의 단락 컬렉션에 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 객체를 추가합니다.
1. PDF 파일을 저장합니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

다음 그림은 코드 스니펫을 실행한 결과를 보여줍니다:

![곡선 그리기](drawing_curve.png)

## 채워진 곡선 객체 만들기

이 예제는 색상으로 채워진 곡선 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

채워진 곡선을 추가한 결과를 확인하십시오:

![채워진 곡선](filled_curve.png)

