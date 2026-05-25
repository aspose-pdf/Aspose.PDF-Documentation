---
title: Adicionar formas de arco ao PDF em Python
linktitle: Adicionar arco
type: docs
weight: 10
url: /pt/python-net/add-arc/
description: Aprenda como desenhar e preencher formas de arco em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas de arco em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas de arco a documentos PDF com Aspose.PDF for Python via .NET. Ele aborda a criação de arcos contornados, o desenho de segmentos de arco preenchidos e a adição deles a um contêiner Graph.
---

## Adicionar objeto Arc

Aspose.PDF for Python via .NET permite que você adicione [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) formas nas páginas PDF usando o [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Você pode desenhar arcos contornados e segmentos de arco preenchidos para diagramas e ilustrações técnicas.

Siga os passos abaixo:

1. Criar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instância.
1. Criar [Graph object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) com certas dimensões.
1. Definir [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para o objeto Graph.
1. Crie um objeto de arco correspondente.
1. Adicione este objeto à coleção Shapes no objeto graph.
1. Adicionar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

O trecho de código a seguir mostra como adicionar um [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) objeto.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## Criar Objeto de Arco Preenchido

Este exemplo mostra como adicionar um segmento de arco preenchido com cor.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado da adição de um arco preenchido:

![Arco Preenchido](filled_arc.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de círculo ao PDF em Python](/pdf/pt/python-net/add-circle/)
- [Adicionar formas de curva ao PDF em Python](/pdf/pt/python-net/add-curve/)
- [Adicionar formas de linha ao PDF em Python](/pdf/pt/python-net/add-line/)