---
title: Añadir Anotaciones de Figuras usando Python
linktitle: Anotaciones de Figuras
type: docs
weight: 30
url: /es/python-net/figures-annotation/
description: Este artículo describe cómo agregar, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF para Python a través de .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Anotaciones de Figuras usando Python",
    "alternativeHeadline": "Cómo agregar Anotaciones de Figuras en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, anotaciones de figuras, anotación de polígono, anotación de línea, anotación de cuadrado, anotación de círculo",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Este artículo describe cómo agregar, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF para Python"
}
</script>


## Agregar Anotaciones de Cuadro y Círculo

En los documentos PDF, una anotación de cuadro se refiere a un tipo específico de anotación que se representa mediante una forma cuadrada. Las anotaciones de cuadro se utilizan para resaltar o llamar la atención sobre un área o sección específica dentro del documento.

Las anotaciones de [Cuadro](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) y [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) mostrarán, respectivamente, un rectángulo o una elipse en la página.

Pasos para crear Anotaciones de Cuadro o Círculo:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear nueva [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) y establecer parámetros (nuevo Rectángulo, título, color, color_interior, opacidad).
1. Después necesitamos agregar la Anotación de Cuadro a la página.

El siguiente fragmento de código muestra cómo agregar Anotaciones de Cuadro en una página PDF.

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

El siguiente fragmento de código te muestra cómo añadir anotaciones de círculo en una página PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
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

![Demostración de Anotación de Círculo y Cuadrado](circle_demo.png)

### Obtener Anotación de Círculo

Por favor, intente usar el siguiente fragmento de código para Obtener Anotación de Círculo del documento PDF.

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

### Obtener Anotación de Cuadrado

Por favor, intente usar el siguiente fragmento de código para Obtener Anotación de Cuadrado del documento PDF.

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

### Eliminar Anotación de Círculo

El siguiente fragmento de código muestra cómo eliminar una anotación de círculo de un archivo PDF.

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

### Eliminar anotación de cuadrado

El siguiente fragmento de código muestra cómo eliminar una anotación de cuadrado de un archivo PDF.

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

## Agregar anotaciones de polígono y polilínea

La herramienta Polilínea te permite crear formas y contornos con un número arbitrario de lados en el documento.

[Polygon Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) representan polígonos en una página. Pueden tener cualquier número de vértices conectados por líneas rectas.

[Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) son también similares a los polígonos, la única diferencia es que los primeros y últimos vértices no están conectados implícitamente.

Pasos con los que creamos anotaciones de Polígono:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear nueva [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) y establecer parámetros del Polígono (nuevo Rectángulo, nuevos Puntos, título, color, color_interior y opacidad).
1. Después podemos añadir anotaciones a la página.

El siguiente fragmento de código muestra cómo añadir anotaciones de Polígono a un archivo PDF:

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


El siguiente fragmento de código muestra cómo añadir anotaciones de polilínea a un archivo PDF:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear nuevas [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) y configurar los parámetros del polígono (nuevo Rectangle, nuevos Points, título, color, interior_color y opacidad).
1. Después podemos añadir las anotaciones a la página.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    # Crear una nueva anotación de polilínea
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

    # Añadir la anotación a la página
    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```


### Obtener Anotaciones de Polígono y Polilínea

Por favor, intente usar el siguiente fragmento de código para obtener anotaciones de polígono en un documento PDF.

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

Por favor, intente usar el siguiente fragmento de código para obtener anotaciones de polilínea en un documento PDF.

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

### Eliminar Anotaciones de Polígono y Polilínea

El siguiente fragmento de código muestra cómo eliminar anotaciones de polígono de un archivo PDF.

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>