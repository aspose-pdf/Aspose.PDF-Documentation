---
title: Anotación de resaltados PDF usando Python
linktitle: Anotación de resaltados
type: docs
weight: 20
url: /es/python-net/highlights-annotation/
description: Aprenda cómo agregar anotaciones de resaltado a archivos PDF en Python usando Aspose.PDF para enfatizar el texto.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía sobre cómo manipular anotaciones de resaltados en PDF
Abstract: El artículo ofrece una guía completa sobre cómo utilizar anotaciones de marcado de texto en documentos PDF, centrada en las funcionalidades proporcionadas por la biblioteca Aspose.PDF en Python. Explica el propósito y uso de diferentes tipos de anotaciones, incluidos los resaltados, subrayados, tachados y anotaciones onduladas, cada una diseñada para enfatizar o modificar el texto de diversas maneras. El documento describe los pasos necesarios para agregar estas anotaciones a un PDF, incluyendo la carga del documento, la creación de las anotaciones con parámetros específicos como título y color, y su inserción en la página deseada. Además, el artículo incluye fragmentos de código para recuperar anotaciones de un PDF, permitiendo a los usuarios filtrar e imprimir los detalles de las anotaciones según el tipo. Finalmente, detalla el proceso para eliminar anotaciones, proporcionando ejemplos de código para remover cada tipo de anotación de marcado de texto del documento. Esta guía sirve como un recurso práctico para desarrolladores que buscan manipular anotaciones de texto en archivos PDF de forma programática usando Python.
---

Las anotaciones de marcado de texto en PDF se utilizan para resaltar, subrayar, tachar o agregar notas al texto del documento. Estas anotaciones están destinadas a destacar o llamar la atención sobre partes específicas del texto. Tales anotaciones permiten a los usuarios marcar visualmente o modificar el contenido de un archivo PDF.

La anotación de resaltado se utiliza para marcar el texto con un fondo de color, usualmente amarillo, para indicar su importancia o relevancia.

La anotación de subrayado es una línea colocada bajo el texto seleccionado para indicar importancia, énfasis o sugerir ediciones.

La anotación de tachado incluye la eliminación o el tachado de un texto particular para mostrar que ha sido borrado, reemplazado o que ya no es válido.

La línea ondulada se usa para subrayar el texto y señalar un tipo diferente de énfasis, como errores ortográficos, posibles problemas o cambios propuestos.

## Agregar anotación de marcado de texto

Para agregar una anotación de marcado de texto al documento PDF, necesitamos realizar las siguientes acciones:

1. Cargar el archivo PDF - nuevo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Crear anotaciones:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) y establecer los parámetros (título, color).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) y establecer los parámetros (título, color).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) y establecer los parámetros (título, color).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) y establecer los parámetros (título, color).
1. Después debemos agregar todas las anotaciones a la página.

### Agregar anotación de resaltado

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### Agregar anotación de tachado

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

### Agregar anotación ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### Agregar anotación de subrayado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## Obtener anotación de marcado de texto

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de marcado de texto del documento PDF.

### Obtener anotación de resaltado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### Obtener anotación de tachado

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


### Obtener anotación ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### Obtener anotación de subrayado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## Eliminar anotación de marcado de texto

El siguiente fragmento de código muestra cómo eliminar la anotación de marcado de texto de un archivo PDF.

### Eliminar anotación de resaltado

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### Eliminar anotación de tachado

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

### Eliminar anotación ondulada

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Eliminar anotación de subrayado

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



