---
title: Adicionar objeto Retângulo ao arquivo PDF
linktitle: Adicionar Retângulo
type: docs
weight: 50
url: /pt/python-net/add-rectangle/
description: Este artigo explica como criar um objeto Retângulo no seu PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando objeto Retângulo ao PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre como adicionar e manipular objetos Retângulo em documentos PDF usando Aspose.PDF para Python via .NET. Detalha o processo de criação de um Retângulo e sua integração em um documento PDF, incluindo a definição de bordas e o preenchimento com cores sólidas ou gradientes. O artigo inclui instruções passo a passo com trechos de código que demonstram a criação de um documento PDF, a adição de páginas e a inserção de objetos Retângulo com várias propriedades visuais, como preenchimentos de cor sólida, preenchimentos em gradiente e transparência usando canais alfa. Além disso, explica como controlar a ordem Z (Z-Order) dos objetos Retângulo para gerenciar sua ordem de renderização quando múltiplas formas são adicionadas ao mesmo PDF. Cada seção é acompanhada de exemplos visuais para ilustrar a saída dos trechos de código.
---

## Adicionar objeto Retângulo

Aspose.PDF para Python via .NET oferece o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Você também pode adicionar o objeto [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que também oferece a funcionalidade de preencher o objeto retângulo.

Primeiro, vamos observar a possibilidade de criar um objeto Retângulo.

Siga os passos abaixo:

1. Crie um novo PDF [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicione [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção de páginas do arquivo PDF.
1. Adicione [Fragmento de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) à coleção de parágrafos da instância de página.
1. Crie uma instância de [Gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/).
1. Defina a borda para o [Objeto de desenho](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Adicione o objeto [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) à coleção de formas do objeto Gráfico.
1. Adicione o objeto gráfico à coleção de parágrafos da instância de página.
1. Adicione [Fragmento de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) à coleção de parágrafos da instância de página.
1. E salve seu arquivo PDF

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![Criar Retângulo](create_rectangle.png)

## Criar objeto Retângulo preenchido

Aspose.PDF para Python via .NET também oferece o recurso de preencher o objeto retângulo com uma determinada cor.

O trecho de código a seguir mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que está preenchido com cor.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

Observe o resultado do retângulo preenchido com cor sólida:

![Retângulo preenchido](fill_rectangle.png)

## Adicionar desenho com preenchimento gradiente

Aspose.PDF para Python via .NET suporta o recurso de adicionar objetos gráficos a documentos PDF e, às vezes, é necessário preencher objetos gráficos com cor gradiente.

O trecho de código a seguir mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que está preenchido com cor gradiente.

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

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![Retângulo gradiente](gradient.png)

## Criar Retângulo com canal de cor alfa

Aspose.PDF para Python .NET suporta o preenchimento do objeto retângulo com uma cor específica. Um objeto retângulo também pode ter um canal de cor alfa para proporcionar aparência transparente. O trecho de código a seguir mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) com canal de cor alfa.

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
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![Retângulo com canal alfa](rectangle_color.png)

## Controlar ordem Z das formas

Aspose.PDF para .NET suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Ao adicionar mais de uma instância do mesmo objeto dentro de um arquivo PDF, podemos controlar sua renderização especificando a ordem Z. A ordem Z também é usada quando precisamos renderizar objetos sobrepostos.

O trecho de código a seguir mostra os passos para renderizar objetos [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) um sobre o outro.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![Controlando ordem Z](control.png)
