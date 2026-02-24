---
title: Adicionar objeto Arco ao arquivo PDF
linktitle: Adicionar Arco
type: docs
weight: 10
url: /pt/python-net/add-arc/
description: Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando objeto Arco ao PDF usando Python
Abstract: O artigo fornece um guia detalhado sobre como adicionar e personalizar objetos arco em documentos PDF usando Aspose.PDF para Python via .NET. Destaca a capacidade da biblioteca de incorporar elementos gráficos como arcos, crucial para aplicações que necessitam de geração dinâmica de conteúdo PDF, como diagramas técnicos e ilustrações personalizadas. O artigo inclui instruções passo a passo e trechos de código que demonstram como criar uma instância `Document`, configurar um objeto `Drawing` com dimensões e propriedades de borda especificadas, e adicionar objetos `Graph` e `Arc` a uma página PDF. Além disso, aborda o processo de preenchimento de objetos arco com cor, mostrando como definir propriedades de preenchimento para arcos e linhas, e finalmente salvar o documento PDF. Os exemplos fornecidos servem como um guia prático para desenvolvedores que buscam aproveitar o Aspose.PDF para manipulações gráficas precisas em arquivos PDF.
---

## Adicionar objeto Arco

Aspose.PDF para Python via .NET suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Também oferece a funcionalidade de preencher o objeto arco com uma cor específica.

Este exemplo ilustra como desenhar arcos programaticamente dentro de um documento PDF usando Aspose.PDF para Python via .NET. Ao aproveitar o módulo de desenho, desenvolvedores podem criar elementos gráficos complexos, como arcos, com controle preciso sobre sua aparência e posicionamento. Essa capacidade é essencial para aplicações que requerem geração dinâmica de conteúdo gráfico em PDFs, como diagramas técnicos, gráficos ou ilustrações personalizadas.

Siga os passos abaixo:

1. Crie uma instância [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) com determinadas dimensões.
1. Defina a [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para o objeto Drawing.
1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

O trecho de código a seguir mostra como adicionar um objeto [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/).

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## Criar objeto Arco preenchido

O próximo exemplo mostra como adicionar um objeto Arc que é preenchido com cor e determinadas dimensões.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Vamos ver o resultado de adicionar um Arco preenchido:

![Arco Preenchido](filled_arc.png)

