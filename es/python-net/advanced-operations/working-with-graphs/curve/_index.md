---
title: Agregar objeto de curva al archivo PDF
linktitle: Agregar curva
type: docs
weight: 30
url: /es/python-net/add-curve/
description: Este artículo explica cómo crear un objeto de curva en su PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar objeto de curva al PDF usando Python
Abstract: El artículo analiza la implementación de curvas gráficas en documentos PDF usando la biblioteca Aspose.PDF para Python a través de .NET. Introduce el concepto de curva gráfica, que es una unión de líneas proyectivas, y detalla el proceso de creación tanto de curvas Bézier simples como rellenas de forma programática. El artículo ofrece instrucciones paso a paso y fragmentos de código para dibujar curvas dentro de un PDF, resaltando la manipulación de elementos gráficos mediante el módulo de dibujo de Aspose.PDF. El proceso incluye crear una instancia de `Document`, definir un objeto `Drawing` con dimensiones especificadas, establecer bordes y agregar un objeto `Graph` a una página PDF. Los resultados visuales de estos ejemplos de código se ilustran mediante imágenes que muestran las curvas resultantes. Además, el artículo explora la creación de objetos de curva rellenos, demostrando cómo establecer colores de relleno para las curvas, lo que es crucial para generar contenido gráfico dinámico como diagramas técnicos, gráficos o ilustraciones personalizadas en PDFs.
---

## Agregar objeto Curva

Una [Curva](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) es una unión conectada de líneas proyectivas, cada una de las cuales se encuentra con tres más en puntos dobles ordinarios.

En este artículo, investigaremos simples curvas gráficas y curvas rellenas que puede crear en su documento PDF.

Este ejemplo ilustra cómo dibujar una curva Bézier de forma programática dentro de un documento PDF usando Aspose.PDF para Python a través de .NET. Aprovechando el módulo de dibujo, los desarrolladores pueden crear elementos gráficos complejos con control preciso sobre su apariencia y posición. Esta capacidad es esencial para aplicaciones que requieren la generación dinámica de contenido gráfico dentro de PDFs, como diagramas técnicos, gráficos o ilustraciones personalizadas.

Siga los pasos a continuación:

1. Crear una instancia de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con ciertas dimensiones.
1. Establecer [borde](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Drawing.
1. Agregar el objeto [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) a la colección de párrafos de la página.
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

La siguiente imagen muestra el resultado ejecutado con nuestro fragmento de código:

![Curva dibujada](drawing_curve.png)

## Crear objeto de Curva rellena

Este ejemplo muestra cómo agregar un objeto Curva que está relleno con color.

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

Observe el resultado de agregar una Curva rellena:

![Curva rellena](filled_curve.png)

