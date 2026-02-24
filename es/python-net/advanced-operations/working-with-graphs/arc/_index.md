---
title: Agregar objeto Arco al archivo PDF
linktitle: Agregar Arco
type: docs
weight: 10
url: /es/python-net/add-arc/
description: Este artículo explica cómo crear un objeto de arco en su PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Añadiendo objeto Arco al PDF usando Python
Abstract: El artículo ofrece una guía detallada sobre cómo agregar y personalizar objetos de arco dentro de documentos PDF usando Aspose.PDF para Python a través de .NET. Destaca la capacidad de la biblioteca para incorporar elementos gráficos como arcos, cruciales para aplicaciones que necesitan generación dinámica de contenido PDF, como diagramas técnicos e ilustraciones personalizadas. El artículo incluye instrucciones paso a paso y fragmentos de código que demuestran cómo crear una instancia de `Document`, configurar un objeto `Drawing` con dimensiones y propiedades de borde especificadas, y agregar objetos `Graph` y `Arc` a una página PDF. Además, cubre el proceso de rellenar objetos de arco con color, mostrando cómo establecer propiedades de relleno para arcos y líneas, y finalmente guardar el documento PDF. Los ejemplos proporcionados sirven como una guía práctica para desarrolladores que buscan aprovechar Aspose.PDF para manipulaciones gráficas precisas en archivos PDF.
---

## Agregar objeto Arco

Aspose.PDF para Python a través de .NET soporta la función de agregar objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. También ofrece la función de rellenar un objeto arco con un color determinado.

Este ejemplo ilustra cómo dibujar arcos programáticamente dentro de un documento PDF usando Aspose.PDF para Python a través de .NET. Al aprovechar el módulo de dibujo, los desarrolladores pueden crear elementos gráficos complejos, como arcos, con control preciso sobre su apariencia y posicionamiento. Esta capacidad es esencial para aplicaciones que requieren generación dinámica de contenido gráfico dentro de PDFs, como diagramas técnicos, gráficos o ilustraciones personalizadas.

Siga los pasos a continuación:

1. Crear una instancia de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con determinadas dimensiones.
1. Establecer el [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Drawing.
1. Agregar el objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) a la colección de párrafos de la página.
1. Guardar nuestro archivo PDF.

El siguiente fragmento de código muestra cómo agregar un objeto [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) .

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

## Crear objeto Arco relleno

El siguiente ejemplo muestra cómo agregar un objeto Arc que está relleno con color y con determinadas dimensiones.

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

Veamos el resultado de agregar un Arco relleno:

![Arco relleno](filled_arc.png)

