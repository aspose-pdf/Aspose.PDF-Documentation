---
title: Agregar anotaciones de figuras usando Python
linktitle: Anotaciones de Figuras
type: docs
weight: 30
url: /es/python-net/figures-annotation/
description: Este artículo describe cómo agregar, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF para Python a través de .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía sobre cómo manipular anotaciones de Figuras en PDF
Abstract: Este artículo proporciona una guía completa sobre cómo agregar, recuperar y eliminar anotaciones de cuadrado, círculo, polígono y polilínea en documentos PDF utilizando Aspose.PDF para Python. Las anotaciones de cuadrado y círculo resaltan visualmente áreas específicas en una página PDF con formas rectangulares y elípticas, respectivamente. El artículo incluye instrucciones paso a paso y fragmentos de código Python para crear estas anotaciones cargando un archivo PDF, configurando propiedades de la anotación como título, color y opacidad, y agregándolas a las páginas del PDF. Además, el artículo detalla métodos para recuperar anotaciones por tipo, imprimiendo sus dimensiones rectangulares, y eliminándolas del documento PDF. También se cubren las anotaciones de polígono y polilínea, donde los polígonos se definen mediante una serie de vértices conectados que forman una forma cerrada, mientras que las polilíneas conectan vértices de manera abierta. El documento proporciona ejemplos de código para ilustrar los procesos de agregar estas anotaciones a un PDF, así como métodos para acceder y eliminarlas.

---

## Agregar anotaciones de Cuadrado y Círculo

En los documentos PDF, una anotación de cuadrado se refiere a un tipo específico de anotación que está representada por una forma cuadrada. Las anotaciones de cuadrado se utilizan para resaltar o llamar la atención sobre un área o sección específica dentro del documento.

Las anotaciones de [Cuadrado](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) y [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) deben mostrar, respectivamente, un rectángulo o una elipse en la página.

Pasos para crear anotaciones de Cuadrado o Círculo:

1. Cargar el archivo PDF - nuevo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear una nueva [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) y establecer parámetros (new Rectangle, title, color, interior_color, opacity).
1. Después necesitamos agregar la anotación de Cuadrado a la página.

El siguiente fragmento de código muestra cómo agregar anotaciones de Cuadrado en una página PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

El siguiente fragmento de código muestra cómo agregar anotaciones de Círculo en una página PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

Como ejemplo, veremos el siguiente resultado de agregar anotaciones de Cuadrado y Círculo a un documento PDF:

![Demo de anotación de Círculo y Cuadrado](circle_demo.png)

### Obtener anotación de Círculo

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de Círculo del documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### Obtener anotación de Cuadrado

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de Cuadrado del documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### Eliminar anotación de Círculo

El siguiente fragmento de código muestra cómo eliminar la anotación de Círculo de un archivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### Eliminar anotación de Cuadrado

El siguiente fragmento de código muestra cómo eliminar la anotación de Cuadrado de un archivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## Agregar anotaciones de Polígono y Polilínea

La herramienta Polilínea le permite crear formas y contornos con un número arbitrario de lados en el documento.

[Anotaciones de Polígono](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) representan polígonos en una página. Pueden tener cualquier número de vértices conectados por líneas rectas.

[Anotaciones de Polilínea](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) son también similares a los polígonos, la única diferencia es que el primer y último vértice no están implícitamente conectados.

Pasos con los que creamos anotaciones de Polígono:

1. Cargar el archivo PDF - nuevo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear una nueva [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) y establecer los parámetros del Polígono (new Rectangle, new Points, title, color, interior_color y opacity).
1. Después podemos agregar anotaciones a la página.

El siguiente fragmento de código muestra cómo agregar anotaciones de Polígono a un archivo PDF:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

El siguiente fragmento de código muestra cómo agregar anotaciones de Polilínea a un archivo PDF:

1. Cargar el archivo PDF - nuevo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear una nueva [Anotaciones de Polilínea](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) y establecer los parámetros del Polígono (new Rectangle, new Points, title, color, interior_color y opacity).
1. Después podemos agregar anotaciones a la página.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### Obtener anotaciones de Polígono y Polilínea

Por favor, intente usar el siguiente fragmento de código para obtener anotaciones de Polígono en el documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

Por favor, intente usar el siguiente fragmento de código para obtener anotaciones de Polilínea en el documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### Eliminar anotaciones de Polígono y Polilínea

El siguiente fragmento de código muestra cómo eliminar anotaciones de Polígono de un archivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

El siguiente fragmento de código muestra cómo eliminar anotaciones de polilínea de un archivo PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


