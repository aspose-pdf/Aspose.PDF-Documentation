---
title: Agregar objeto de círculo al archivo PDF
linktitle: Agregar círculo
type: docs
weight: 20
url: /es/python-net/add-circle/
description: Este artículo explica cómo crear un objeto de círculo en su PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar objeto de círculo al PDF usando Python
Abstract: El artículo ofrece una guía sobre el uso de Aspose.PDF para Python a través de .NET para crear objetos de círculo dentro de documentos PDF. Explica el proceso de añadir gráficos de círculos contorneados y rellenos, destacando cómo los diagramas circulares pueden ser una herramienta útil para mostrar datos en múltiples categorías cuando los datos representan un todo completo. El artículo incluye instrucciones paso a paso para crear una instancia de `Document`, configurar un objeto `Drawing` con dimensiones específicas, aplicar un borde y añadir un objeto `Graph` a una página PDF. Los ejemplos de código demuestran cómo dibujar un círculo simple y un círculo relleno, con instrucciones detalladas sobre cómo establecer colores y añadir texto al círculo. También se presentan resultados visuales de estas operaciones, mostrando las capacidades de Aspose.PDF para mejorar el contenido del PDF con elementos gráficos dinámicos.
---

## Agregar objeto de círculo

Al igual que los diagramas de barras, los diagramas circulares pueden usarse para mostrar datos en varias categorías separadas. Sin embargo, a diferencia de los diagramas de barras, los diagramas circulares solo pueden usarse cuando se dispone de datos para todas las categorías que componen el conjunto total. Así que veamos cómo añadir un objeto [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) con Aspose.PDF para Python .NET.

Este ejemplo ilustra cómo dibujar programáticamente un círculo dentro de un documento PDF usando Aspose.PDF para Python a través de .NET. Aprovechando el módulo de dibujo, los desarrolladores pueden crear elementos gráficos complejos con un control preciso sobre su apariencia y posicionamiento. Esta capacidad es esencial para aplicaciones que requieren la generación dinámica de contenido gráfico dentro de PDFs, como diagramas técnicos, gráficos o ilustraciones personalizadas.

Siga los pasos a continuación:

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un [objeto Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con ciertas dimensiones.
1. Establecer el [borde](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Drawing.
1. Añadir el objeto [Gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) a la colección de párrafos de la página.
1. Guardar nuestro archivo PDF.

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

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Nuestro círculo dibujado se verá así:

![Círculo dibujado](drawing_circle.png)

## Crear objeto de círculo relleno

Este ejemplo muestra cómo añadir un objeto Círculo que está relleno con color.

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

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Veamos el resultado de añadir un Círculo relleno:

![Círculo relleno](filled_circle.png)


