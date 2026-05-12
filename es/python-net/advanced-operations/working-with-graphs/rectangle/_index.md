---
title: Agregar formas de rectángulo a PDF en Python
linktitle: Agregar rectángulo
type: docs
weight: 50
url: /es/python-net/add-rectangle/
description: Aprenda cómo dibujar y rellenar formas de rectángulo en archivos PDF con Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de rectángulo en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de rectángulo a documentos PDF con Aspose.PDF for Python via .NET. Cubre rectángulos contorneados, rellenos sólidos y degradados, transparencia alfa y control del orden Z.
---

## Agregar objeto Rectangle

Aspose.PDF for Python via .NET le permite agregar [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) formas a páginas PDF a través del [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase. Puede dibujar rectángulos contorneados y aplicar rellenos sólidos, degradados o transparentes.

Siga los pasos a continuación:

1. Crea un nuevo PDF [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregar [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección de páginas del archivo PDF.
1. Agregar [Fragmento de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) a la colección de párrafos de la instancia de página.
1. Crear [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) instancia.
1. Establecer borde para [Objeto de gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Agregar [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto a la colección de shapes del objeto Graph.
1. Agregar objeto gráfico a la colección de párrafos de la instancia de página.
1. Agregar [Fragmento de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) a la colección de párrafos de la instancia de página.
1. Y guarde su archivo PDF

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![Crear rectángulo](create_rectangle.png)

## Crear objeto de rectángulo relleno

Aspose.PDF for Python via .NET también ofrece la funcionalidad de rellenar el objeto de rectángulo con un color determinado.

El siguiente fragmento de código muestra cómo agregar un [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto que está relleno de color.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

Resultado del rectángulo rellenado con un color sólido:

![Rectángulo Relleno](fill_rectangle.png)

## Agregar dibujo con relleno degradado

Aspose.PDF for Python via .NET admite la función de agregar objetos de gráfico a documentos PDF y, a veces, es necesario rellenar los objetos de gráfico con Color degradado.

El siguiente fragmento de código muestra cómo agregar un [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto que está rellenado con Color degradado.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![Rectángulo de degradado](gradient.png)

## Crear rectángulo con canal de color alfa

Aspose.PDF for Python via .NET también admite la transparencia a través de un canal de color alfa.

El siguiente fragmento de código muestra cómo agregar un [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto con valores alfa.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![Color del canal alfa del rectángulo](rectangle_color.png)

## Controlar Z-Order de las formas

Aspose.PDF for .NET admite la función de agregar objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. Al agregar más de una instancia del mismo objeto dentro del archivo PDF, podemos controlar su renderizado especificando el Z-Order. Z-Order también se utiliza cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objetos uno encima del otro.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![Control del orden Z](control.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Verifique los límites de la forma en gráficos PDF con Python](/pdf/es/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Agregar formas de línea al PDF en Python](/pdf/es/python-net/add-line/)
- [Agregar formas elípticas al PDF en Python](/pdf/es/python-net/add-ellipse/)