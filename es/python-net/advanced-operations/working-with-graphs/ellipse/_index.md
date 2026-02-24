---
title: Agregar objeto Elipse al archivo PDF
linktitle: Agregar Elipse
type: docs
weight: 60
url: /es/python-net/add-ellipse/
description: Este artículo explica cómo crear un objeto Elipse en su PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar objeto Elipse al PDF usando Python
Abstract: El artículo ofrece una guía completa sobre cómo usar Aspose.PDF para Python a través de .NET para agregar y personalizar objetos Elipse dentro de documentos PDF. Explica el proceso de crear y manipular elipses, incluyendo la configuración de sus dimensiones, colores y posición, utilizando el módulo de dibujo. Demuestra cómo dibujar elipses en una página PDF, mostrando la capacidad de controlar su apariencia y posición. El ejemplo incluye la configuración de propiedades de borde y la adición de múltiples elipses a un gráfico. Ilustra cómo rellenar elipses con colores específicos, ofreciendo un ejemplo donde dos elipses se rellenan con diferentes colores y se añaden a un documento PDF. Explica cómo insertar texto dentro de objetos Elipse mediante la propiedad de texto del objeto Gráfico. El ejemplo proporcionado muestra cómo establecer propiedades de fuente y añadir texto a
---

## Agregar objeto Elipse

Aspose.PDF para Python a través de .NET permite agregar objetos [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) a documentos PDF. También ofrece la función de rellenar el objeto elipse con un color determinado.

Este ejemplo ilustra cómo dibujar y personalizar elipses de forma programática dentro de un documento PDF usando Aspose.PDF para Python a través de .NET. Al aprovechar el módulo de dibujo, los desarrolladores pueden crear elementos gráficos complejos con un control preciso sobre su apariencia y posición. Esta capacidad es esencial para aplicaciones que requieren la generación dinámica de contenido gráfico dentro de PDFs, como diagramas técnicos, gráficos o ilustraciones personalizadas.

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

![Agregar Elipse](ellipse.png)

## Crear objeto Elipse relleno

El siguiente fragmento de código muestra cómo agregar un objeto [Elipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) que está relleno con color.

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

![Elipse rellena](fill_ellipse.png)

## Agregar texto dentro de la Elipse

Aspose.PDF para Python a través de .NET permite agregar texto dentro del objeto Gráfico. La propiedad Text del objeto Gráfico ofrece la opción de establecer el texto del objeto Gráfico. El siguiente fragmento de código muestra cómo agregar texto dentro de un objeto Elipse.

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

![Texto dentro de la Elipse](text_ellipse.png)

