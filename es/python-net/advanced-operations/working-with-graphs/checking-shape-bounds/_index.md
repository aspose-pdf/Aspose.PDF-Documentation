---
title: Comprobar los límites de forma en la colección Shapes usando Python
type: docs
weight: 70
url: /es/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprende cómo comprobar los límites de una forma cuando se inserta en la colección Shapes para garantizar que encaje dentro de su contenedor padre.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Guía para comprobar los límites de forma en Shapes
Abstract: Este artículo ofrece una guía completa sobre cómo utilizar la función de verificación de límites en la colección Shapes, particularmente dentro de documentos PDF usando Python. La función es fundamental para garantizar que los elementos gráficos, como las formas, se ajusten adecuadamente dentro de sus contenedores padres. Puede configurarse para lanzar una excepción si el componente supera los límites del contenedor, asegurando un manejo de errores robusto. La guía recorre la creación de un nuevo documento PDF, la adición de una página y el establecimiento de un elemento gráfico (una forma rectangular) dentro de un objeto gráfico. Se proporcionan instrucciones detalladas para instanciar un `Document`, añadir una `Page` y crear un objeto `Graph`. Describe la configuración de una forma `Rectangle` y la configuración del `BoundsCheckMode` a `THROW_EXCEPTION_IF_DOES_NOT_FIT`, lo que garantiza que se lance una excepción si la forma no cabe dentro de las dimensiones especificadas del gráfico. El proceso se ilustra con un ejemplo de código Python usando la biblioteca Aspose.PDF, resaltando la implementación práctica de estas funciones.
---

Este artículo proporciona una guía detallada sobre el uso de la función de verificación de límites en la colección Shapes. Esta función garantiza que los elementos se ajusten dentro de su contenedor padre y puede configurarse para lanzar una excepción si el componente no encaja.

1. Crea un nuevo PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Añade una página
1. Crea un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Crea una forma Rectangle
1. Modo de verificación de límites
1. Añade el [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) al Graph

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
