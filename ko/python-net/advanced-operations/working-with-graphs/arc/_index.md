---
title: PDF 파일에 Arc 객체 추가
linktitle: Arc 추가
type: docs
weight: 10
url: /ko/python-net/add-arc/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 arc 객체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 Arc 객체 추가
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 arc 객체를 추가하고 사용자 정의하는 방법에 대한 자세한 가이드를 제공합니다. 이 라이브러리가 아크와 같은 그래픽 요소를 통합할 수 있는 기능을 강조하며, 이는 기술 다이어그램 및 맞춤 일러스트레이션과 같이 동적 PDF 콘텐츠 생성을 필요로 하는 애플리케이션에 중요합니다. 본 문서에서는 `Document` 인스턴스를 생성하고, 지정된 크기와 테두리 속성을 가진 `Drawing` 객체를 설정하며, PDF 페이지에 `Graph` 및 `Arc` 객체를 추가하는 단계별 지침과 코드 예제를 포함합니다. 또한, arc 객체를 색으로 채우는 과정과 아크와 선에 대한 채우기 속성을 설정하는 방법을 보여주고 최종적으로 PDF 문서를 저장하는 방법을 다룹니다. 제공된 예제들은 PDF 파일에서 정밀한 그래픽 조작을 활용하려는 개발자들에게 실용적인 안내서 역할을 합니다.
---

## Arc 객체 추가

Aspose.PDF for Python via .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 arc 객체를 특정 색상으로 채우는 기능도 제공합니다.

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에 프로그래밍 방식으로 아크를 그리는 방법을 보여줍니다. drawing 모듈을 활용하면 개발자는 아크와 같은 복잡한 그래픽 요소를 외관과 위치를 정밀하게 제어하면서 생성할 수 있습니다. 이러한 기능은 기술 다이어그램, 차트 또는 맞춤 일러스트레이션과 같이 PDF 안에서 그래픽 콘텐츠를 동적으로 생성해야 하는 애플리케이션에 필수적입니다.

다음 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 인스턴스를 생성합니다.
1. [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)을(를) 특정 차원으로 생성합니다.
1. Drawing 객체에 대한 [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) 를 설정합니다.
1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 객체를 추가합니다.
1. PDF 파일을 저장합니다.

다음 코드 스니펫은 [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## 채워진 Arc 객체 생성

다음 예제는 색상과 특정 차원으로 채워진 Arc 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

채워진 Arc를 추가한 결과를 확인해 보겠습니다:

![채워진 Arc](filled_arc.png)

