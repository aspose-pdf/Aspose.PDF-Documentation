---
title: Verificar limites da forma na coleção Shapes usando Python
type: docs
weight: 70
url: /pt/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda como verificar os limites de uma forma quando inserida na coleção Shapes para garantir que ela se encaixe dentro de seu contêiner pai.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Guia sobre como verificar limites de formas em Shapes
Abstract: Este artigo oferece um guia abrangente sobre a utilização do recurso de verificação de limites na coleção Shapes, particularmente em documentos PDF usando Python. O recurso é fundamental para garantir que elementos gráficos, como formas, se encaixem adequadamente dentro de seus contêineres pais. Ele pode ser configurado para lançar uma exceção se o componente exceder os limites do contêiner, assegurando um tratamento de erro robusto. O guia percorre a criação de um novo documento PDF, a adição de uma página e o estabelecimento de um elemento gráfico (uma forma retangular) dentro de um objeto Graph. Instruções detalhadas são fornecidas para instanciar um `Document`, adicionar uma `Page` e criar um objeto `Graph`. Descreve a configuração de uma forma `Rectangle` e a definição do `BoundsCheckMode` para `THROW_EXCEPTION_IF_DOES_NOT_FIT`, que garante que uma exceção seja lançada se a forma não couber nas dimensões especificadas do gráfico. O processo é ilustrado com um exemplo de código Python usando a biblioteca Aspose.PDF, destacando a implementação prática desses recursos.
---

Este artigo fornece um guia detalhado sobre o uso do recurso de verificação de limites na coleção Shapes. Esse recurso garante que os elementos se encaixem dentro de seu contêiner pai e pode ser configurado para lançar uma exceção se o componente não couber.

1. Crie um novo PDF [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Adicione uma Página
1. Crie um [Gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Crie uma Forma Retangular
1. Modo de Verificação de Limites
1. Adicione o [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) ao Gráfico

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
