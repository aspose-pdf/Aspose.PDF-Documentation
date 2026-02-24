---
title: PDF 파일에 사각형 객체 추가
linktitle: 사각형 추가
type: docs
weight: 50
url: /ko/python-net/add-rectangle/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 사각형 객체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 사각형 객체 추가
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 사각형 객체를 추가하고 조작하는 방법에 대한 포괄적인 가이드를 제공합니다. 여기에는 사각형을 생성하고 PDF 문서에 통합하는 과정이 자세히 설명되며, 경계 설정 및 단색 또는 그라데이션 채우기와 같은 채우기 옵션도 포함됩니다. 이 문서에는 PDF 문서 생성, 페이지 추가 및 다양한 시각적 속성을 가진 사각형 객체 삽입(예 단색 채우기, 그라데이션 채우기, 알파 채널을 이용한 투명도) 등을 보여주는 코드 스니펫과 단계별 지침이 포함되어 있습니다. 또한 여러 도형을 동일한 PDF에 추가할 때 사각형 객체의 Z-Order를 제어하여 렌더링 순서를 관리하는 방법을 설명합니다. 각 섹션은 코드 스니펫의 출력 결과를 시각적인 예제로 지원합니다.
---

## 사각형 객체 추가

Aspose.PDF for Python via .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체를 추가하고 사각형 객체를 채우는 기능도 제공합니다.

먼저, 사각형 객체 생성 가능성을 살펴보겠습니다.

아래 단계에 따라 진행하십시오:

1. 새로운 PDF [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 생성합니다.
1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가합니다.
1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)를 추가합니다.
1. [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 인스턴스를 생성합니다.
1. [그리기 객체](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/)의 경계를 설정합니다.
1. 그래프 객체의 도형 컬렉션에 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체를 추가합니다.
1. 페이지 인스턴스의 단락 컬렉션에 그래프 객체를 추가합니다.
1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)를 추가합니다.
1. 그리고 PDF 파일을 저장합니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![사각형 만들기](create_rectangle.png)

## 채워진 사각형 객체 만들기

Aspose.PDF for Python via .NET은 사각형 객체를 특정 색으로 채우는 기능도 제공합니다.

다음 코드 스니펫은 색으로 채워진 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

단색으로 채워진 사각형의 결과를 확인하세요:

![채워진 사각형](fill_rectangle.png)

## 그라데이션 채우기가 있는 그리기 추가

Aspose.PDF for Python via .NET은 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며, 때때로 그래프 객체를 그라데이션 색으로 채워야 할 필요가 있습니다.

다음 코드 스니펫은 그라데이션 색으로 채워진 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![그라데이션 사각형](gradient.png)

## 알파 색 채널이 있는 사각형 만들기

Aspose.PDF for Python .NET은 사각형 객체를 특정 색으로 채우는 것을 지원합니다. 사각형 객체는 투명한 외관을 제공하기 위해 알파 색 채널을 가질 수도 있습니다. 다음 코드 스니펫은 알파 색 채널이 있는 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![알파 채널 색상의 사각형](rectangle_color.png)

## 도형의 Z-Order 제어

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. PDF 파일에 동일한 객체를 여러 개 추가할 경우 Z-Order를 지정하여 렌더링을 제어할 수 있습니다. Z-Order는 객체를 서로 겹쳐서 렌더링해야 할 때도 사용됩니다.

다음 코드 스니펫은 [사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 객체들을 서로 겹쳐서 렌더링하는 단계들을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![Z-Order 제어](control.png)
