---
title: Anotaciones extra usando Python
linktitle: Anotaciones extra
type: docs
weight: 60
url: /es/python-net/extra-annotations/
description: Aprende cómo agregar anotaciones extra, como resaltados o notas, a PDFs en Python con Aspose.PDF para mejorar el contenido de los PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía sobre cómo manipular anotaciones extra en PDF
Abstract: El artículo ofrece una guía completa sobre cómo agregar, recuperar y eliminar diferentes tipos de anotaciones en un archivo PDF usando Python, específicamente con la biblioteca Aspose.PDF. Cubre tres tipos de anotaciones Caret, Link y Redaction. El artículo explica que las anotaciones Caret se utilizan para sugerencias de edición de texto. Describe el proceso de cargar un archivo PDF, crear una anotación Caret con parámetros específicos (como rectángulo, título, asunto, banderas y color), añadirla al documento y guardar los cambios. Se proporcionan fragmentos de código para agregar, recuperar y eliminar anotaciones Caret. Las anotaciones Link se utilizan para crear áreas clicables que redirigen a URL o a posiciones específicas del documento. La guía incluye instrucciones y código para agregar una anotación Link identificando un fragmento de texto (p. ej., un número de teléfono), estableciendo una acción y gestionando estas anotaciones.
---

## Cómo agregar una anotación Caret a un archivo PDF existente mediante Python

La anotación Caret es un símbolo que indica edición de texto. La anotación Caret también es una anotación de marcado, por lo que la clase Caret deriva de la clase Markup y también proporciona funciones para obtener o establecer propiedades de la anotación Caret y restablecer el flujo de su apariencia.
Las anotaciones Caret se utilizan a menudo para sugerir cambios, adiciones o modificaciones al texto.

Pasos para crear una anotación Caret:

1. Cargar el archivo PDF - nuevo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear una nueva [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) y establecer los parámetros del Caret (nuevo Rectangle, título, asunto, banderas, color). Esta anotación se utiliza para indicar la inserción de texto.
1. Una vez que podemos agregar anotaciones a la página.

El siguiente fragmento de código muestra cómo agregar una anotación Caret a un archivo PDF:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Obtener anotación Caret

Por favor, prueba usando el siguiente fragmento de código para obtener una anotación Caret en un documento PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Eliminar anotación Caret

El siguiente fragmento de código muestra cómo eliminar una anotación Caret de un archivo PDF usando Python.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Redactar cierta región de página con anotación Redaction usando Aspose.PDF para Python

Aspose.PDF para Python vía .NET admite la característica de agregar y manipular anotaciones en un archivo PDF existente. Las anotaciones Redaction en documentos PDF sirven para eliminar o ocultar permanentemente información confidencial del documento. El proceso de edición de la información implica cubrir o sombrear contenido específico, como texto, imágenes o gráficos, de manera que se restrinja su visibilidad y accesibilidad para otros. Esto garantiza que la información sensible permanezca oculta y protegida dentro del documento. Para cumplir con este requisito, se proporciona una clase denominada [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), que puede usarse para redactar ciertas regiones de página o para manipular anotaciones Redaction existentes y redactarlas (es decir, aplanar la anotación y eliminar el texto debajo de ella).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Obtener anotación Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Eliminar anotación Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



