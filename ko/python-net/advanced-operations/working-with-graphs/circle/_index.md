---
title: PDF 파일에 원 객체 추가
linktitle: 원 추가
type: docs
weight: 20
url: /ko/python-net/add-circle/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 원 객체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 원 객체 추가
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에 원 객체를 만드는 가이드를 제공합니다. 윤곽선이 있는 원 그래픽과 채워진 원 그래픽을 추가하는 과정을 설명하며, 데이터가 전체를 나타낼 때 원 그래프가 여러 범주에 걸친 데이터를 표시하는 유용한 도구가 될 수 있음을 강조합니다. 문서에서는 `Document` 인스턴스를 생성하고, 특정 크기의 `Drawing` 객체를 설정하며, 테두리를 적용하고, PDF 페이지에 `Graph` 객체를 추가하는 단계별 지침을 포함합니다. 코드 예제는 간단한 원과 채워진 원을 그리는 방법을 보여주며, 색상을 설정하고 원에 텍스트를 추가하는 자세한 방법을 제공합니다. 이러한 작업의 시각적 결과도 제시되어, 동적 그래픽 요소로 PDF 콘텐츠를 강화하는 Aspose.PDF의 기능을 보여줍니다.
---

## 원 객체 추가

막대 그래프와 마찬가지로, 원 그래프는 여러 개별 범주에 걸친 데이터를 표시하는 데 사용할 수 있습니다. 하지만 막대 그래프와 달리, 원 그래프는 전체를 구성하는 모든 범주의 데이터가 있을 때만 사용할 수 있습니다. 이제 Aspose.PDF for Python .NET을 사용하여 [원](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) 객체를 추가하는 방법을 살펴보겠습니다.

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에 프로그래밍 방식으로 원을 그리는 방법을 보여줍니다. drawing 모듈을 활용하면 개발자는 외관과 위치를 정확히 제어하여 복잡한 그래픽 요소를 만들 수 있습니다. 이 기능은 기술 다이어그램, 차트 또는 맞춤 일러스트레이션과 같이 PDF 내에 동적 그래픽 콘텐츠를 생성해야 하는 애플리케이션에 필수적입니다.

아래 단계에 따라 진행하십시오:

1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 인스턴스를 생성합니다.
1. [그리기 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)를 특정 치수로 생성합니다.
1. [테두리](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties)를 그리기 객체에 설정합니다.
1. [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 객체를 페이지의 단락 컬렉션에 추가합니다.
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

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

그린 원은 다음과 같이 표시됩니다:

![Drawing Circle](drawing_circle.png)

## 채워진 원 객체 만들기

이 예제는 색으로 채워진 원 객체를 추가하는 방법을 보여줍니다.

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

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

채워진 원을 추가한 결과를 확인해 보겠습니다:

![Filled Circle](filled_circle.png)


