---
title: Agregar formas de elipse a PDF en Python
linktitle: Agregar elipse
type: docs
weight: 60
url: /es/python-net/add-ellipse/
description: Aprenda cómo dibujar, rellenar y etiquetar formas de elipse en archivos PDF con Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de elipse en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de elipse a documentos PDF con Aspose.PDF for Python via .NET. Cubre elipses contorneadas, elipses rellenas y la incorporación de texto dentro de objetos elipse.
---

## Agregar objeto Ellipse

Aspose.PDF for Python via .NET le permite agregar [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) formas a páginas PDF con el [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase. Puedes dibujar contornos de elipse, aplicar colores de relleno y colocar texto dentro de los objetos elipse.

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

![Agregar elipse](ellipse.png)

## Crear objeto elipse relleno

El siguiente fragmento de código muestra cómo agregar un [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) objeto que está relleno de color.

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

![Elipse rellena](fill_ellipse.png)

## Agregar texto dentro de la elipse

Aspose.PDF for Python via .NET también te permite colocar texto dentro de objetos de forma. El siguiente ejemplo agrega texto a las formas de elipse.

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

![Texto dentro de la elipse](text_ellipse.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas de círculo al PDF en Python](/pdf/es/python-net/add-circle/)
- [Agregar formas de curva al PDF en Python](/pdf/es/python-net/add-curve/)
- [Agregar formas rectangulares al PDF en Python](/pdf/es/python-net/add-rectangle/)
