---
title: PDF 파일에 라인 객체 추가
linktitle: 라인 추가
type: docs
weight: 40
url: /ko/python-net/add-line/
description: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 라인 객체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 라인 객체 추가
Abstract: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 라인 객체를 추가하는 방법을 논의합니다. `Document` 인스턴스를 생성하고 PDF에 `Graph` 객체를 추가하는 과정을 설명합니다. 라인 객체를 생성하고 구성하는 자세한 단계가 제공되며, 대시 패턴 및 색상을 지정하는 방법도 포함됩니다. 간단한 라인, 점선 라인, 페이지 전체에 교차 패턴을 형성하는 라인을 그리는 코드 스니펫이 포함되어 있습니다. 각 섹션에는 결과 PDF의 시각적 표현이 함께 제공됩니다. 이 가이드는 Aspose.PDF를 사용하여 그래픽 요소로 PDF 문서를 향상시키려는 개발자를 위한 실용적인 리소스입니다.
---

## 라인 객체 추가

Aspose.PDF for Python via .NET은 PDF 문서에 그래프 객체(예: 그래프, 라인, 사각형 등)를 추가하는 기능을 지원합니다. 또한 [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 객체를 추가할 수 있으며, 여기서 대시 패턴, 색상 및 기타 형식을 지정할 수 있습니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 인스턴스를 생성합니다.
1. 그래프 객체 만들기
1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 객체를 추가합니다.
1. 라인을 생성하고 구성합니다.
1. [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) 를 Graph에 추가합니다.
1. PDF 파일을 저장합니다.

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
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Add Line](add_line.png)

## PDF 문서에 점선 라인 추가 방법

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
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

결과를 확인해 봅시다:

![Dashed Line](dash_line.png)

## 페이지 전체에 라인 그리기

우리는 라인 객체를 사용하여 왼쪽 아래에서 오른쪽 위 코너까지, 그리고 왼쪽 위 코너에서 오른쪽 아래 코너까지 교차선을 그릴 수도 있습니다.

다음 코드 스니펫을 확인하여 이 요구사항을 구현하십시오.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Drawing Line](draw_line.png)


