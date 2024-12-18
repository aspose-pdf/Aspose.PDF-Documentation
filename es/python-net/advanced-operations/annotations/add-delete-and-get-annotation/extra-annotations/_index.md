---
title: Anotaciones Extras usando Python
linktitle: Anotaciones Extras
type: docs
weight: 60
url: /es/python-net/extra-annotations/
description: Esta sección describe cómo agregar, obtener y eliminar tipos adicionales de anotaciones de su documento PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotaciones Extras usando Python",
    "alternativeHeadline": "Cómo agregar Anotaciones Extras en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, anotación de enlace, anotación de cuidado",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Esta sección describe cómo agregar, obtener y eliminar tipos adicionales de anotaciones de su documento PDF con Python."
}
</script>


## Cómo agregar una anotación de intercalación en un archivo PDF existente mediante Python

La anotación de intercalación es un símbolo que indica la edición de texto. La anotación de intercalación también es una anotación de marcado, por lo que la clase Caret deriva de la clase Markup y también proporciona funciones para obtener o establecer propiedades de la anotación de intercalación y restablecer el flujo de la apariencia de la anotación de intercalación.
Las anotaciones de intercalación se utilizan a menudo para sugerir cambios, adiciones o modificaciones al texto.

Pasos con los que creamos una anotación de intercalación:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un nuevo [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) y establecer parámetros de intercalación (nuevo Rectángulo, título, asunto, banderas, color). Esta anotación se usa para indicar la inserción de texto.
1. Una vez que podemos agregar anotaciones a la página.

El siguiente fragmento de código muestra cómo agregar una anotación de intercalación a un archivo PDF:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Usuario de Aspose"
    caretAnnotation1.subject = "Texto insertado 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### Obtener Anotación de Acento

Por favor, intente usar el siguiente fragmento de código para obtener la Anotación de Acento en un documento PDF

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

### Eliminar Anotación de Acento

El siguiente fragmento de código muestra cómo eliminar la Anotación de Acento de un archivo PDF usando Python.

```python

    import aspose.pdf as ap

    # Cargar el archivo PDF
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

## Agregar Anotación de Enlace

[Enlaces](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) son anotaciones que abren URLs o se mueven a ciertas posiciones dentro del mismo documento o dentro de un documento externo cuando haces clic.

Una Anotación de Enlace es un área rectangular que se puede colocar en cualquier lugar de la página. Cada enlace tiene una acción PDF correspondiente asociada a él. Esta acción se realiza cuando el usuario hace clic en el área de este enlace.

El siguiente fragmento de código muestra cómo agregar una Anotación de Enlace a un archivo PDF usando un ejemplo de número de teléfono:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Crear objeto TextFragmentAbsorber para encontrar un número de teléfono
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Aceptar el absorbedor solo para la primera página
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Crear Anotación de Enlace y establecer la acción para llamar a un número de teléfono
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Agregar anotación a la página
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### Obtener Anotación de Enlace

Por favor, intente usar el siguiente fragmento de código para obtener [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) del documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Eliminar Anotación de Enlace

El siguiente fragmento de código muestra cómo eliminar la anotación de enlace de un archivo PDF. Para esto, necesitamos encontrar y eliminar todas las anotaciones de enlace en la primera página. Después de esto, guardaremos el documento con la anotación eliminada.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Redactar cierta región de la página con Anotación de Redacción usando Aspose.PDF para Python

Aspose.PDF para Python a través de .NET admite la función de agregar y manipular Anotaciones en un archivo PDF existente. Las Anotaciones de Redacción en documentos PDF tienen el propósito de eliminar o ocultar permanentemente información confidencial del documento. El proceso de editar la información implica cubrir o sombrear contenido específico, como texto, imágenes o gráficos, de manera que restrinja su visibilidad y accesibilidad a otros. Esto asegura que la información sensible permanezca oculta y protegida dentro del documento. Para cumplir con este requisito, se proporciona una clase llamada [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), que se puede usar para redactar ciertas regiones de la página o se puede usar para manipular RedactionAnnotations existentes y redactarlas (es decir, aplanar la anotación y eliminar el texto debajo de ella).

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


### Obtener Anotación de Redacción

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

### Eliminar Anotación de Redacción

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
``