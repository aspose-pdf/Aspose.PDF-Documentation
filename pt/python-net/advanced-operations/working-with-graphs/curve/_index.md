---
title: Adicionar Objeto Curva ao arquivo PDF
linktitle: Adicionar Curva
type: docs
weight: 30
url: /pt/python-net/add-curve/
description: Este artigo explica como criar um objeto curva em seu PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando Objeto Curva ao PDF usando Python
Abstract: O artigo discute a implementação de curvas gráficas em documentos PDF usando a biblioteca Aspose.PDF para Python via .NET. Ele introduz o conceito de curva gráfica, que é a união de linhas projetivas, e detalha o processo de criação de curvas Bézier simples e preenchidas programaticamente. O artigo fornece instruções passo a passo e trechos de código para desenhar curvas dentro de um PDF, destacando a manipulação de elementos gráficos usando o módulo de desenho do Aspose.PDF. O processo inclui criar uma instância `Document`, definir um objeto `Drawing` com dimensões especificadas, definir bordas e adicionar um objeto `Graph` a uma página PDF. Os resultados visuais desses exemplos de código são ilustrados por imagens que mostram as curvas resultantes. O artigo ainda explora a criação de objetos de curva preenchida, demonstrando como definir cores de preenchimento para as curvas, o que é crucial para gerar conteúdo gráfico dinâmico, como diagramas técnicos, gráficos ou ilustrações personalizadas em PDFs.
---

## Adicionar objeto Curva

Um gráfico [Curva](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) é uma união conectada de linhas projetivas, cada linha encontrando três outras em pontos duplos ordinários.

Neste artigo, investigaremos curvas gráficas simples e curvas preenchidas, que você pode criar em seu documento PDF.

Este exemplo ilustra como desenhar uma curva Bézier programaticamente dentro de um documento PDF usando Aspose.PDF para Python via .NET. Ao aproveitar o módulo de desenho, os desenvolvedores podem criar elementos gráficos complexos com controle preciso sobre sua aparência e posicionamento. Essa capacidade é essencial para aplicações que requerem a geração dinâmica de conteúdo gráfico dentro de PDFs, como diagramas técnicos, gráficos ou ilustrações personalizadas.

Siga os passos abaixo:

1. Criar instância [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar [objeto Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) com determinadas dimensões.
1. Definir [borda](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para o objeto Drawing.
1. Adicionar objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à coleção de parágrafos da página.
1. Salvar nosso arquivo PDF.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

A imagem a seguir mostra o resultado obtido com nosso trecho de código:

![Desenho da Curva](drawing_curve.png)

## Criar Objeto Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que está preenchido com cor.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Veja o resultado da adição de uma Curva preenchida:

![Curva Preenchida](filled_curve.png)

