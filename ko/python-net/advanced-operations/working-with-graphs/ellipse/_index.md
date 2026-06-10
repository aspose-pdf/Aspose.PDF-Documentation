---
title: Python에서 PDF에 타원 모양 추가
linktitle: 타원 추가
type: docs
weight: 60
url: /ko/python-net/add-ellipse/
description: Python에서 PDF 파일의 타원 모양을 그리고, 채우고, 레이블을 지정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에 타원 모양 그리기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 타원 모양을 추가하는 방법을 보여줍니다.윤곽선이 있는 타원, 채워진 타원, 타원 객체 내부에 텍스트 추가에 대해 설명합니다.
---

## 타원 오브젝트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 다음을 추가할 수 있습니다. [타원](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 를 사용하여 도형을 PDF 페이지로 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 수업.타원 외곽선을 그리고, 채우기 색상을 적용하고, 타원 객체 안에 텍스트를 배치할 수 있습니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![타원 추가](ellipse.png)

## 채워진 타원 오브젝트 만들기

다음 코드 스니펫은 을 추가하는 방법을 보여줍니다. [타원](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 색상으로 채워진 오브젝트.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![채워진 타원](fill_ellipse.png)

## 타원 안에 텍스트 추가

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 셰이프 객체 안에 텍스트를 배치할 수도 있습니다.다음 예제에서는 타원 모양에 텍스트를 추가합니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![타원 내부의 텍스트](text_ellipse.png)

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [Python에서 PDF에 원 모양 추가](/pdf/ko/python-net/add-circle/)
- [Python에서 PDF에 곡선 모양 추가](/pdf/ko/python-net/add-curve/)
- [Python에서 PDF에 사각형 모양 추가](/pdf/ko/python-net/add-rectangle/)
