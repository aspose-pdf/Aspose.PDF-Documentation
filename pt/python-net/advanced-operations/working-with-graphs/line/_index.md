---
title: Adicionar objeto de linha ao arquivo PDF
linktitle: Adicionar linha
type: docs
weight: 40
url: /pt/python-net/add-line/
description: Este artigo explica como criar um objeto de linha no seu PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando objeto de linha ao PDF usando Python
Abstract: O artigo discute como adicionar objetos de linha a um documento PDF usando Aspose.PDF para Python via .NET. Ele explica o processo de criação de uma instância `Document` e a adição de um objeto `Graph` ao PDF. O artigo fornece etapas detalhadas para criar e configurar um objeto `Line`, incluindo a especificação do padrão de traço e da cor. Inclui trechos de código que demonstram como adicionar uma linha simples, uma linha pontilhada e tracejada, e como desenhar linhas através de uma página para formar um padrão em cruz. Cada seção é acompanhada por uma representação visual do PDF resultante. Este guia serve como um recurso prático para desenvolvedores que desejam aprimorar seus documentos PDF com elementos gráficos usando Aspose.PDF.
---

## Adicionar objeto de linha

O Aspose.PDF para Python via .NET oferece suporte ao recurso de adicionar objetos de gráfico (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Você também tem a possibilidade de adicionar o objeto [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) onde pode especificar o padrão de traço, cor e outras formatações para o elemento Line.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um objeto Graph
1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à coleção de parágrafos da página.
1. Crie e configure a Line
1. Adicione o [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) ao Graph
1. Salve o nosso arquivo PDF.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Adicionar linha](add_line.png)

## Como adicionar linha pontilhada e tracejada ao seu documento PDF

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

Vamos verificar o resultado:

![Linha tracejada](dash_line.png)

## Desenhar linha através da página

Também podemos usar o objeto de linha para desenhar uma cruz começando do canto inferior esquerdo ao canto superior direito e do canto superior esquerdo ao canto inferior direito.

Por favor, veja o trecho de código a seguir para atender a esse requisito.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Desenhando linha](draw_line.png)


