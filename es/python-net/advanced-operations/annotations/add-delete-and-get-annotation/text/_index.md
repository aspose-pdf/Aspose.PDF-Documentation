---
title: Uso de anotación de texto para PDF con Python
linktitle: Anotación de texto
type: docs
weight: 10
url: /es/python-net/text-annotation/
description: Aspose.PDF para Python le permite agregar, obtener y eliminar anotaciones de texto de su documento PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Guía sobre cómo manipular anotaciones de texto en PDF
Abstract: Este artículo proporciona una guía completa sobre cómo manipular anotaciones de texto dentro de archivos PDF utilizando la biblioteca Aspose.PDF para Python. Cubre la adición, recuperación y eliminación de varios tipos de anotaciones, incluyendo Text, Free Text y StrikeOutAnnotations. Las anotaciones de texto son notas adjuntas a una ubicación específica dentro de un PDF, mostradas como iconos que revelan el texto en una ventana emergente al abrirse. Las anotaciones de texto libre muestran el texto directamente en la página, mientras que las StrikeOutAnnotations tapan el texto con una línea para indicar su eliminación o desestimación. El proceso implica agregar anotaciones a la colección Annotations de una página usando el método `add()`, y se proporcionan ejemplos para cada tipo de anotación. Los fragmentos de código ilustran cómo implementar estas tareas, incluyendo la creación de anotaciones con propiedades específicas como título, asunto, color y banderas, así como la recuperación y eliminación de anotaciones de páginas PDF. Esta guía sirve como un recurso práctico para desarrolladores que buscan mejorar documentos PDF mediante la manipulación de anotaciones usando Aspose.PDF.
---

## Cómo agregar anotación de texto a un archivo PDF existente

Una anotación de texto es una anotación adjunta a una ubicación específica en un documento PDF. Cuando está cerrada, la anotación se muestra como un ícono; cuando se abre, debe mostrar una ventana emergente que contiene el texto de la nota con la fuente y el tamaño elegidos por el lector.

Las anotaciones se encuentran en la colección [Anotaciones](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) de una página en particular. Esta colección contiene las anotaciones sólo de esa página individual; cada página tiene su propia colección de Anotaciones.

Para agregar una anotación a una página concreta, agréguela a la colección de Anotaciones de esa página con el método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. Primero, cree una anotación que desea agregar al PDF.
1. Luego abra el PDF de entrada.
1. Añada la anotación a la colección [Anotaciones](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) del objeto 'page'.

El siguiente fragmento de código le muestra cómo agregar una anotación en una página PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## Obtener anotación de texto de un archivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## Eliminar anotación de texto de un archivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## Cómo agregar (o crear) una nueva anotación de texto libre

Una anotación de texto libre muestra texto directamente en la página. La clase [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) permite crear este tipo de anotación. En el siguiente fragmento, agregamos una anotación de texto libre encima de la primera aparición de la cadena.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## Obtener anotación de texto libre de un archivo PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## Eliminar anotación de texto libre de un archivo PDF

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### Tachar palabras usando StrikeOutAnnotation

Aspose.PDF para Python le permite agregar, eliminar y actualizar anotaciones en documentos PDF. Una de las clases también le permite tachar anotaciones. Cuando se aplica una StrikeOutAnnotation a un PDF, se dibuja una línea a través del texto especificado, indicando que debe ser eliminado o ignorado.

El siguiente fragmento de código muestra cómo agregar una [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) a un PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```


## Obtener StrikeOutAnnotation de PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

## Eliminar StrikeOutAnnotation de PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



