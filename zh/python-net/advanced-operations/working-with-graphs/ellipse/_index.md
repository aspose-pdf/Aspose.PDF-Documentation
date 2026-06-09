---
title: 在 Python 中向 PDF 添加椭圆形状
linktitle: 添加椭圆
type: docs
weight: 60
url: /zh/python-net/add-ellipse/
description: 了解如何在 Python 中绘制、填充并标记 PDF 文件中的椭圆形状。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制椭圆形状
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加椭圆形状。它涵盖了描边椭圆、填充椭圆以及在椭圆对象内部添加文本。
---

## 添加 Ellipse 对象

Aspose.PDF for Python via .NET 允许您添加 [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 使用 the 将形状添加到 PDF 页面 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类。您可以绘制椭圆轮廓、设置填充颜色，并在椭圆对象内部放置文本。

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

![添加椭圆](ellipse.png)

## 创建填充椭圆对象

以下代码片段展示了如何添加 a。 [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) 被颜色填充的对象。

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

![已填充椭圆](fill_ellipse.png)

## 在椭圆内添加文本

Aspose.PDF for Python via .NET 还允许您在形状对象内放置文本。下面的示例向椭圆形状添加文本。

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

![椭圆内的文本](text_ellipse.png)

## 相关图形主题

- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中向 PDF 添加圆形](/pdf/zh/python-net/add-circle/)
- [在 Python 中向 PDF 添加曲线形状](/pdf/zh/python-net/add-curve/)
- [在 Python 中向 PDF 添加矩形形状](/pdf/zh/python-net/add-rectangle/)
