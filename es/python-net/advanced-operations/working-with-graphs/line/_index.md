---
title: Agregar objeto Línea al archivo PDF
linktitle: Agregar línea
type: docs
weight: 40
url: /es/python-net/add-line/
description: Este artículo explica cómo crear un objeto línea en su PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar objeto Línea al PDF usando Python
Abstract: El artículo discute cómo agregar objetos línea a un documento PDF usando Aspose.PDF para Python a través de .NET. Explica el proceso de crear una instancia `Document` y agregar un objeto `Graph` al PDF. El artículo proporciona pasos detallados para crear y configurar un objeto `Line`, incluyendo la especificación de su patrón de guiones y color. Incluye fragmentos de código que demuestran cómo agregar una línea simple, una línea punteada y guionada, y cómo dibujar líneas a lo largo de una página para formar un patrón de cruz. Cada sección está acompañada de una representación visual del PDF resultante. Esta guía sirve como un recurso práctico para desarrolladores que buscan mejorar sus documentos PDF con elementos gráficos usando Aspose.PDF.
---

## Agregar objeto Línea

Aspose.PDF para Python a través de .NET admite la función de agregar objetos de gráfico (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También puede aprovechar para agregar el objeto [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) donde también puede especificar el patrón de guiones, color y otros formatos para el elemento Line.

Siga los pasos a continuación:

1. Crear instancia de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un objeto Graph
1. Agregar el objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) a la colección de párrafos de la página.
1. Crear y configurar la Línea
1. Agregar el [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) al Graph
1. Guardar nuestro archivo PDF.

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

![Agregar línea](add_line.png)

## Cómo agregar una línea punteada y guionada a su documento PDF

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

Veamos el resultado:

![Línea guionada](dash_line.png)

## Dibujar línea a lo largo de la página

También podemos usar el objeto línea para dibujar una cruz comenzando desde la esquina inferior izquierda a la esquina superior derecha y de la esquina superior izquierda a la esquina inferior derecha.

Por favor, revise el siguiente fragmento de código para cumplir con este requisito.

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

![Dibujando línea](draw_line.png)


