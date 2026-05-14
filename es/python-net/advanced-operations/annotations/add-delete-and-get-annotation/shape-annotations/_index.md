---
title: Anotaciones de forma mediante Python
linktitle: Anotaciones de forma
type: docs
weight: 20
url: /es/python-net/shape-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de línea, cuadrado, círculo, polígono y polilínea en documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones geométricas de PDF en Python.
Abstract: Este artículo explica cómo crear, leer y eliminar anotaciones de forma en documentos PDF usando Aspose.PDF for Python via .NET. Cubre anotaciones de línea, cuadrado, círculo, polígono y polilínea, con cada flujo de trabajo dividido en pasos pequeños y ejemplos de código completos.
---

Este artículo muestra cómo trabajar con anotaciones de forma en documentos PDF usando Aspose.PDF for Python via .NET.

El script de ejemplo muestra varios flujos de trabajo de anotación basados en geometría:

- anotaciones de línea
- anotaciones cuadradas
- anotaciones de círculo
- anotaciones de polígonos
- anotaciones de polilínea

## Anotación de línea 

### Agregar anotación de línea 

Este ejemplo agrega una anotación de línea a la primera página y configura los estilos de flecha, el ancho de línea y una ventana emergente.

#### Abra el PDF de origen

```python
document = ap.Document(infile)
```

#### Crear y configurar la anotación de línea

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Adjuntar el popup y guardar el PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Obtener anotación de línea 

Para inspeccionar anotaciones de línea, filtre la colección de anotaciones en la primera página y convierta cada resultado a `LineAnnotation` para que puedas leer sus puntos de inicio y fin.

#### Cargar el PDF y recopilar anotaciones de línea

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Imprime las coordenadas de la línea

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Ejemplo completo

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Eliminar anotación de línea 

Este flujo de trabajo elimina todas las anotaciones de línea de la primera página y guarda el PDF actualizado.

#### Buscar anotaciones de línea para eliminar

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Eliminar las anotaciones y guardar el PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## Anotaciones de Cuadrado y Círculo

### Agregar anotación cuadrada 

Las anotaciones de tipo cuadrado son útiles para marcar áreas rectangulares en un documento. Este ejemplo crea una anotación de tipo cuadrado con ajustes de borde, relleno y transparencia.

#### Abra el PDF y cree la anotación cuadrada

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Añadir la anotación y guardar el PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Obtener anotación cuadrada 

Para inspeccionar anotaciones cuadradas, filtre las anotaciones de la primera página por el `SQUARE` escribe e imprime cada rectángulo.

#### Cargar el documento y recopilar anotaciones cuadradas

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Imprimir los rectángulos de anotación

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Ejemplo completo

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Eliminar anotación cuadrada 

Este flujo de trabajo elimina todas las anotaciones cuadradas de la primera página y guarda el documento.

#### Buscar y eliminar anotaciones cuadradas

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Agregar anotación de círculo 

Las anotaciones de círculo marcan áreas redondeadas en un PDF. Este ejemplo agrega una anotación de círculo con color de relleno, opacidad y una anotación emergente.

#### Abra el PDF y cree la anotación de círculo

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Adjuntar el popup y guardar el PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Obtener anotación de círculo 

Para inspeccionar anotaciones de círculo, filtre las anotaciones de la página por el `CIRCLE` escriba e imprima sus rectángulos.

#### Cargar el documento y recopilar anotaciones de círculo

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Imprimir los rectángulos de anotación

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Ejemplo completo

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Eliminar anotación de círculo 

Este flujo de trabajo elimina todas las anotaciones de círculo de la primera página y guarda el PDF de salida.

#### Buscar y eliminar anotaciones de círculo

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Anotaciones de Polígono y Polilínea

### Agregar anotación de polígono 

Las anotaciones de polígono definen una forma cerrada de varios puntos. Este ejemplo crea una anotación de polígono a partir de un rectángulo y una lista de puntos.

#### Abra el PDF y cree la anotación de polígono

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
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
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Añadir la anotación y guardar el PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
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
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Obtener anotación de polígono 

Para inspeccionar anotaciones de polígono, filtre las anotaciones de la primera página por el `POLYGON` escribe e imprime cada rectángulo de anotación.

#### Cargar el documento y recopilar anotaciones de polígonos

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Imprimir los rectángulos de anotación

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Ejemplo completo

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Eliminar anotación de polígono 

Este flujo de trabajo elimina todas las anotaciones de polígonos de la primera página y guarda el PDF actualizado.

#### Buscar y eliminar anotaciones de polígono

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Agregar anotación de polilínea 

Las anotaciones de polilínea definen una ruta abierta a través de varios puntos. Este ejemplo crea una anotación de polilínea con una nota emergente.

#### Abra el PDF y cree la anotación de polilínea

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
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
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Adjuntar el popup y guardar el PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Ejemplo completo

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
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
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### Obtener anotación PolyLine 

Para inspeccionar anotaciones de polilínea, filtre las anotaciones de la página por el `POLY_LINE` escriba e imprima sus rectángulos.

#### Cargue el documento y recopile anotaciones de polilínea

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Imprimir los rectángulos de anotación

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Ejemplo completo

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### Eliminar anotación de polilínea 

Este flujo de trabajo elimina todas las anotaciones de polilínea de la primera página y guarda el PDF de salida.

#### Buscar y eliminar anotaciones de polilínea

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Temas relacionados

- [Importar y Exportar Anotaciones](/python-net/import-export-annotations/)
- [Anotaciones Interactivas](/python-net/interactive-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones multimedia](/python-net/media-annotations/)
- [Anotaciones de seguridad](/python-net/security-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
- [Anotaciones de marca de agua](/python-net/watermark-annotations/)
