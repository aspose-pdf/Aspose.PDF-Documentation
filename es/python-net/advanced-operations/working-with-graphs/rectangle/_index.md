---
title: Agregar objeto Rectángulo al archivo PDF
linktitle: Agregar rectángulo
type: docs
weight: 50
url: /es/python-net/add-rectangle/
description: Este artículo explica cómo crear un objeto Rectángulo en su PDF usando Aspose.PDF para Python mediante .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar objeto Rectángulo a PDF usando Python
Abstract: El artículo ofrece una guía completa sobre cómo agregar y manipular objetos Rectángulo en documentos PDF usando Aspose.PDF para Python mediante .NET. Detalla el proceso de crear un Rectángulo e integrarlo en un documento PDF, incluyendo la configuración de bordes y el relleno con colores sólidos o degradados. El artículo incluye instrucciones paso a paso con fragmentos de código que demuestran la creación de un documento PDF, la adición de páginas y la inserción de objetos Rectángulo con diversas propiedades visuales, como rellenos de color sólido, rellenos degradados y transparencia mediante canales alfa. Además, explica cómo controlar el Z-Order de los objetos Rectángulo para gestionar su orden de renderizado cuando se agregan múltiples formas al mismo PDF. Cada sección está respaldada con ejemplos visuales que ilustran el resultado de los fragmentos de código.
---

## Agregar objeto Rectángulo

Aspose.PDF for Python via .NET soporta la función de agregar objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. También obtiene la capacidad de agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) donde también se ofrece la función de rellenar el objeto rectángulo.

Primero, veamos la posibilidad de crear un objeto Rectángulo.

Siga los pasos a continuación:

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregar [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) a la colección de páginas del archivo PDF.
1. Agregar [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) a la colección de párrafos de la instancia de página.
1. Crear una instancia de [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/).
1. Establecer el borde para [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Agregar objeto [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) a la colección de formas del objeto Graph.
1. Agregar objeto gráfico a la colección de párrafos de la instancia de página.
1. Agregar [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) a la colección de párrafos de la instancia de página.
1. Y guarde su archivo PDF

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

![Crear Rectángulo](create_rectangle.png)

## Crear objeto Rectángulo con relleno

Aspose.PDF for Python via .NET también ofrece la función de rellenar el objeto rectángulo con un color determinado.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que está rellenado con color.

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

Observe el resultado del rectángulo rellenado con color sólido:

![Rectángulo relleno](fill_rectangle.png)

## Agregar dibujo con relleno degradado

Aspose.PDF for Python via .NET soporta la función de agregar objetos gráficos a documentos PDF y, a veces, es necesario rellenar los objetos gráficos con color degradado.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que está rellenado con color degradado.

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

![Rectángulo degradado](gradient.png)

## Crear Rectángulo con canal de color Alpha

Aspose.PDF para Python .NET soporta rellenar el objeto rectángulo con un color determinado. Un objeto rectángulo también puede tener un canal de color Alpha para dar una apariencia transparente. El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) con canal de color Alpha.

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

![Color de canal Alpha del Rectángulo](rectangle_color.png)

## Controlar el orden Z de las formas

Aspose.PDF para .NET soporta la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. Al agregar más de una instancia del mismo objeto dentro de un archivo PDF, podemos controlar su renderizado especificando el orden Z. El orden Z también se usa cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar objetos [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) uno encima del otro.

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

![Controlando el orden Z](control.png)
