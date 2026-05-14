---
title: Agregar formas de línea al PDF en Python
linktitle: Agregar línea
type: docs
weight: 40
url: /es/python-net/add-line/
description: Aprenda cómo dibujar formas de línea y líneas con estilo en archivos PDF en Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de línea en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de línea a documentos PDF con Aspose.PDF for Python via .NET. Cubre la creación de líneas básicas, la configuración de estilos de línea punteada y el dibujo de líneas a través de una página.
---

## Agregar objeto Line

Aspose.PDF for Python via .NET le permite agregar [Línea](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) formas a páginas PDF usando el [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase. Puede controlar el color de la línea, el patrón de guiones y la ubicación.

Siga los pasos a continuación:

1. Crear [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instancia.
1. Crear un objeto de gráfico
1. Agregar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto a la colección de párrafos de la página.
1. Crear y configurar la línea
1. Agregar el [Línea](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) al gráfico
1. Guarde nuestro archivo PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Agregar línea](add_line.png)

## Cómo agregar una línea punteada y discontinua a su documento PDF

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Resultado de agregar una línea punteada y discontinua:

![Línea discontinua](dash_line.png)

## Dibujar línea a través de la página

También puedes dibujar líneas a través de la página para formar una cruz.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Dibujo de línea](draw_line.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas de curva al PDF en Python](/pdf/es/python-net/add-curve/)
- [Agregar formas rectangulares al PDF en Python](/pdf/es/python-net/add-rectangle/)
- [Verifique los límites de la forma en gráficos PDF con Python](/pdf/es/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
