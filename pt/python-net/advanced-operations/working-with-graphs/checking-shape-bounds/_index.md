---
title: Verificar limites de forma em gráficos PDF com Python
linktitle: Verificar limites de forma
type: docs
weight: 70
url: /pt/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Saiba como validar os limites de forma em coleções de gráficos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar limites de forma de gráfico em arquivos PDF usando Python
Abstract: Este artigo mostra como validar os limites de forma em coleções de Graph com Aspose.PDF for Python via .NET. Ele aborda a configuração do BoundsCheckMode, a detecção de formas fora do intervalo e o tratamento seguro de exceções de limites.
---

## Verificar limites de forma em um Graph

Quando você adiciona formas a um [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), você pode habilitar a validação de limites para garantir que cada forma caiba na área do gráfico.

Usar [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) para definir o comportamento quando uma forma está fora do intervalo. Neste exemplo, `THROW_EXCEPTION_IF_DOES_NOT_FIT` é usado para gerar uma exceção.

Siga os passos abaixo:

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Criar um [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) e adicioná-lo à página.
1. Criar um [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que se estende fora dos limites do gráfico.
1. Definir modo de verificação de limites para `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Adicione o retângulo e trate a exceção.
1. Salve o documento.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Observações

- Usar `THROW_EXCEPTION_IF_DOES_NOT_FIT` quando a validação estrita de layout é necessária.
- Para comportamento permissivo, escolha outro `BoundsCheckMode` opção baseada nas suas necessidades de layout.

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de retângulo ao PDF em Python](/pdf/pt/python-net/add-rectangle/)
- [Adicionar formas de linha ao PDF em Python](/pdf/pt/python-net/add-line/)
- [Adicionar formas de elipse ao PDF em Python](/pdf/pt/python-net/add-ellipse/)
