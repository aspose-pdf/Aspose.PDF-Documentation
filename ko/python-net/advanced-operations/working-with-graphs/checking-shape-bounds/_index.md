---
title: Python을 사용하여 Shapes 컬렉션에서 도형 경계 확인
type: docs
weight: 70
url: /ko/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Shapes 컬렉션에 삽입된 도형의 경계를 확인하여 부모 컨테이너에 맞는지 확인하는 방법을 배웁니다.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Shapes에서 도형 경계 확인 가이드
Abstract: 이 문서는 Python을 사용하여 PDF 문서 내 Shapes 컬렉션에서 경계 확인 기능을 활용하는 포괄적인 가이드를 제공합니다. 이 기능은 도형과 같은 그래픽 요소가 부모 컨테이너에 적절히 맞도록 보장하는 데 필수적입니다. 구성 요소가 컨테이너 경계를 초과하면 예외를 발생시키도록 설정할 수 있어 강력한 오류 처리를 보장합니다. 이 가이드는 새 PDF 문서를 생성하고, 페이지를 추가하며, 그래프 객체 내에 사각형 도형을 설정하는 과정을 안내합니다. `Document`를 인스턴스화하고, `Page`를 추가하고, `Graph` 객체를 만드는 단계별 지침이 제공됩니다. `Rectangle` 도형을 설정하고 `BoundsCheckMode`를 `THROW_EXCEPTION_IF_DOES_NOT_FIT`으로 구성하는 방법을 설명하며, 이는 도형이 그래프의 지정된 차원에 맞지 않을 경우 예외가 발생하도록 합니다. 이 과정은 Aspose.PDF 라이브러리를 사용한 Python 코드 예제로 설명되어, 이러한 기능의 실제 구현을 강조합니다.
---

이 문서는 Shapes 컬렉션에서 경계 확인 기능을 사용하는 자세한 가이드를 제공합니다. 이 기능은 요소가 부모 컨테이너에 맞도록 보장하며, 구성 요소가 맞지 않을 경우 예외를 발생시키도록 설정할 수 있습니다.

1. 새 PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. 페이지 추가
1. [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 생성
1. 사각형 도형 만들기
1. 경계 확인 모드
1. [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/)을 Graph에 추가

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
