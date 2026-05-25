---
title: Adicionar formas de retângulo ao PDF em Python
linktitle: Adicionar Retângulo
type: docs
weight: 50
url: /pt/python-net/add-rectangle/
description: Aprenda como desenhar e preencher formas de retângulo em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas de retângulo em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas de retângulo a documentos PDF com Aspose.PDF for Python via .NET. Ele cobre retângulos contornados, preenchimentos sólidos e gradientes, transparência alfa e controle de ordem Z.
---

## Adicionar objeto Rectangle

Aspose.PDF for Python via .NET permite que você adicione [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) formas para páginas PDF através do [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Você pode desenhar retângulos contornados e aplicar preenchimentos sólidos, gradientes ou transparentes.

Siga os passos abaixo:

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicionar [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para a coleção de páginas do arquivo PDF.
1. Adicionar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) para a coleção de parágrafos da instância da página.
1. Criar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) instância.
1. Definir borda para [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto.
1. Adicionar [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto para a coleção de formas do objeto Graph.
1. Adicionar objeto de gráfico à coleção de parágrafos da instância de página.
1. Adicionar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) para a coleção de parágrafos da instância da página.
1. E salve seu arquivo PDF

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

![Criar Retângulo](create_rectangle.png)

## Criar Objeto Retângulo Preenchido

Aspose.PDF for Python via .NET também oferece o recurso de preencher o objeto retângulo com uma certa cor.

O trecho de código a seguir mostra como adicionar um [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto que está preenchido com cor.

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

Resultado do retângulo preenchido com uma cor sólida:

![Retângulo Preenchido](fill_rectangle.png)

## Adicionar Desenho com Preenchimento em Degradê

O Aspose.PDF for Python via .NET oferece o recurso de adicionar objetos de gráfico a documentos PDF e, às vezes, é necessário preencher os objetos de gráfico com Cor em Degradê.

O trecho de código a seguir mostra como adicionar um [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto que está preenchido com Cor em Degradê.

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

![Retângulo de Gradiente](gradient.png)

## Criar Retângulo com Canal de Cor Alfa

Aspose.PDF for Python via .NET também suporta transparência por meio de um canal de cor alfa.

O trecho de código a seguir mostra como adicionar um [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objeto com valores alfa.

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

![Cor do Canal Alfa do Retângulo](rectangle_color.png)

## Controlar a Ordem Z das formas

Aspose.PDF for .NET suporta o recurso de adicionar objetos gráficos (por exemplo gráfico, linha, retângulo etc.) a documentos PDF. Ao adicionar mais de uma instância do mesmo objeto dentro do arquivo PDF, podemos controlar sua renderização especificando a Ordem Z. A Ordem Z também é usada quando precisamos renderizar objetos um sobre o outro.

O fragmento de código a seguir mostra as etapas para renderizar [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objetos uns sobre os outros.

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

![Controlando a ordem Z](control.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Verifique os limites das formas em gráficos PDF com Python](/pdf/pt/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Adicionar formas de linha ao PDF em Python](/pdf/pt/python-net/add-line/)
- [Adicionar formas de elipse ao PDF em Python](/pdf/pt/python-net/add-ellipse/)