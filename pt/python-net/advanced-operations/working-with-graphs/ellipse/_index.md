---
title: Adicionar objeto Elipse ao arquivo PDF
linktitle: Adicionar Elipse
type: docs
weight: 60
url: /pt/python-net/add-ellipse/
description: Este artigo explica como criar um objeto Elipse no seu PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando objeto Elipse ao PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre como usar Aspose.PDF para Python via .NET para adicionar e personalizar objetos Elipse em documentos PDF. Ele explica o processo de criação e manipulação de elipses, incluindo a definição de suas dimensões, cores e posicionamento, usando o módulo de desenho. Demonstra como desenhar elipses em uma página PDF, mostrando a capacidade de controlar sua aparência e posição. O exemplo inclui a definição de propriedades de borda e a adição de múltiplas elipses a um gráfico. Ilustra como preencher elipses com cores específicas, oferecendo um exemplo onde duas elipses são preenchidas com cores diferentes e adicionadas a um documento PDF. Explica como inserir texto dentro de objetos Elipse utilizando a propriedade de texto do Objeto Gráfico. O exemplo fornecido mostra como definir propriedades de fonte e adicionar texto a
---

## Adicionar objeto Elipse

Aspose.PDF para Python via .NET suporta a adição de objetos [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) a documentos PDF. Também oferece a funcionalidade de preencher o objeto elipse com uma cor específica.

Este exemplo ilustra como desenhar e personalizar elipses programaticamente dentro de um documento PDF usando Aspose.PDF para Python via .NET. Ao utilizar o módulo de desenho, os desenvolvedores podem criar elementos gráficos complexos com controle preciso sobre sua aparência e posicionamento. Essa capacidade é essencial para aplicações que requerem geração dinâmica de conteúdo gráfico em PDFs, como diagramas técnicos, gráficos ou ilustrações personalizadas.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![Adicionar Elipse](ellipse.png)

## Criar objeto Elipse preenchido

O trecho de código a seguir mostra como adicionar um objeto [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) que está preenchido com cor.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![Elipse preenchida](fill_ellipse.png)

## Adicionar texto dentro da Elipse

Aspose.PDF para Python via .NET suporta a adição de texto dentro do Objeto Graph. A propriedade Text do Objeto Graph fornece a opção de definir o texto do Objeto Graph. O trecho de código a seguir mostra como adicionar texto dentro de um objeto Elipse.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Texto dentro da Elipse](text_ellipse.png)

