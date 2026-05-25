---
title: Adicionar formas de círculo ao PDF em Python
linktitle: Adicionar círculo
type: docs
weight: 20
url: /pt/python-net/add-circle/
description: Aprenda como desenhar e preencher formas de círculo em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de círculo em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas de círculo a documentos PDF com Aspose.PDF for Python via .NET. Ele cobre a criação de círculos contornados, preenchimento de círculos com cor e a inserção de texto dentro de objetos de círculo.
---

## Adicionar objeto de círculo

Aspose.PDF for Python via .NET permite que você adicione [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) formas para páginas PDF através do [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Use círculos para diagramas, anotações e elementos visuais simples.

Siga os passos abaixo:

1. Criar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instância.
1. Criar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) com certas dimensões.
1. Definir [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para o objeto Graph.
1. Adicionar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Nosso círculo desenhado ficará assim:

![Desenhando Círculo](drawing_circle.png)

## Criar Objeto de Círculo Preenchido

Este exemplo mostra como adicionar um círculo e preenchê‑lo com cor.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado da adição de um círculo preenchido:

![Círculo Preenchido](filled_circle.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de arco ao PDF em Python](/pdf/pt/python-net/add-arc/)
- [Adicionar formas de elipse ao PDF em Python](/pdf/pt/python-net/add-ellipse/)
- [Adicionar formas de retângulo ao PDF em Python](/pdf/pt/python-net/add-rectangle/)