---
title: PDF 파일에 타원 개체 추가
linktitle: 타원 추가
type: docs
weight: 60
url: /ko/python-net/add-ellipse/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에 타원 개체를 만드는 방법을 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 타원 개체 추가
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에서 타원 개체를 추가하고 사용자 지정하는 방법에 대한 포괄적인 가이드를 제공합니다. 드로잉 모듈을 사용하여 타원의 차원, 색상 및 위치를 설정하는 등 타원을 생성하고 조작하는 과정을 설명합니다. PDF 페이지에 타원을 그리는 방법을 시연하며, 외관과 위치를 제어할 수 있음을 보여줍니다. 예제에서는 테두리 속성을 설정하고 그래프에 여러 타원을 추가하는 방법을 포함합니다. 특정 색으로 타원을 채우는 방법을 예시로, 두 개의 타원을 서로 다른 색으로 채워 PDF 문서에 추가하는 사례를 제공합니다. 그래프 개체의 텍스트 속성을 활용하여 타원 개체 내부에 텍스트를 삽입하는 방법도 설명합니다. 제공된 예제는 글꼴 속성을 설정하고 텍스트를 추가하는 방법을 보여줍니다.
---

## 타원 개체 추가

Aspose.PDF for Python via .NET은 PDF 문서에 [타원](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 객체를 추가하는 것을 지원합니다. 또한 특정 색으로 타원 객체를 채우는 기능도 제공합니다.

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서 내에서 타원을 프로그래밍 방식으로 그리고 사용자 지정하는 방법을 보여줍니다. 드로잉 모듈을 활용함으로써 개발자는 외관과 위치를 정밀하게 제어할 수 있는 복잡한 그래픽 요소를 만들 수 있습니다. 이 기능은 기술 다이어그램, 차트 또는 맞춤형 일러스트레이션과 같이 PDF 내에서 그래픽 콘텐츠를 동적으로 생성해야 하는 애플리케이션에 필수적입니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![타원 추가](ellipse.png)

## 채워진 타원 개체 만들기

다음 코드 조각은 색으로 채워진 [타원](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 객체를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![채워진 타원](fill_ellipse.png)

## 타원 내부에 텍스트 추가

Aspose.PDF for Python via .NET은 그래프 객체 내부에 텍스트를 추가하는 것을 지원합니다. 그래프 객체의 텍스트 속성을 사용하면 그래프 객체의 텍스트를 설정할 수 있습니다. 다음 코드 조각은 타원 객체 내부에 텍스트를 추가하는 방법을 보여줍니다.

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

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![타원 내부 텍스트](text_ellipse.png)

