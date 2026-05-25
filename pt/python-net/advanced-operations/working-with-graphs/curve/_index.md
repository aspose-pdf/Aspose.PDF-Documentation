---
title: Adicionar formas de curva ao PDF em Python
linktitle: Adicionar curva
type: docs
weight: 30
url: /pt/python-net/add-curve/
description: Aprenda como desenhar e preencher formas de curva em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas de curva em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas de curva a documentos PDF com Aspose.PDF for Python via .NET. Ele aborda a criação de curvas contornadas, o preenchimento de objetos de curva e a renderização de caminhos de curva personalizados em um contêiner Graph.
---

## Adicionar objeto Curve

Aspose.PDF for Python via .NET permite que você adicione [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) formas para páginas PDF através do [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe.

Este artigo mostra como criar curvas contornadas e preenchidas.

Siga os passos abaixo:

1. Criar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instância.
1. Criar [Graph object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) com certas dimensões.
1. Definir [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para o objeto Graph.
1. Adicionar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

A imagem a seguir mostra o resultado executado com nosso trecho de código:

![Desenhando Curva](drawing_curve.png)

## Criar Objeto de Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que está preenchido com cor.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado da adição de uma curva preenchida:

![Curva Preenchida](filled_curve.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de arco ao PDF em Python](/pdf/pt/python-net/add-arc/)
- [Adicionar formas de linha ao PDF em Python](/pdf/pt/python-net/add-line/)
- [Adicionar formas de elipse ao PDF em Python](/pdf/pt/python-net/add-ellipse/)