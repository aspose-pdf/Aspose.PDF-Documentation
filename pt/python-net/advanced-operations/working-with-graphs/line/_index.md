---
title: Adicionar formas de linha ao PDF em Python
linktitle: Adicionar linha
type: docs
weight: 40
url: /pt/python-net/add-line/
description: Aprenda como desenhar formas de linha e linhas estilizadas em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de linha em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas de linha a documentos PDF com Aspose.PDF for Python via .NET. Ele cobre a criação de linhas básicas, a configuração de estilos de linha tracejada e o desenho de linhas através de uma página.
---

## Adicionar objeto Line

Aspose.PDF for Python via .NET permite que você adicione [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) formas nas páginas PDF usando o [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Você pode controlar a cor da linha, o padrão de traço e o posicionamento.

Siga os passos abaixo:

1. Criar [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instância.
1. Criar um Objeto de Gráfico
1. Adicionar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto à coleção de parágrafos da página.
1. Criar e Configurar a Linha
1. Adicionar o [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) ao Gráfico
1. Salve nosso arquivo PDF.

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

![Adicionar linha](add_line.png)

## Como adicionar linha pontilhada tracejada ao seu documento PDF

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

Resultado da adição de uma linha pontilhada tracejada:

![Linha Tracejada](dash_line.png)

## Desenhar Linha Através da Página

Você também pode desenhar linhas através da página para formar uma cruz.

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

![Desenhando Linha](draw_line.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de curva ao PDF em Python](/pdf/pt/python-net/add-curve/)
- [Adicionar formas de retângulo ao PDF em Python](/pdf/pt/python-net/add-rectangle/)
- [Verifique os limites das formas em gráficos PDF com Python](/pdf/pt/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
