---
title: Anotaciones adhesivas en PDF usando Python
linktitle: Anotación adhesiva
type: docs
weight: 50
url: /es/python-net/sticky-annotations/
description: Descubre cómo agregar anotaciones adhesivas en documentos PDF usando Aspose.PDF en Python a través de .NET para comentarios y retroalimentación.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía sobre cómo manipular anotaciones adhesivas en PDF
Abstract: Este artículo ofrece una guía detallada sobre cómo gestionar anotaciones de marca de agua en documentos PDF utilizando la biblioteca Aspose.PDF para Python. Explica el proceso de agregar, recuperar y eliminar anotaciones de marca de agua para garantizar la autenticidad y la marca del documento. La anotación de marca de agua puede usarse para incrustar gráficos, como logotipos, con un tamaño y posición fijos en una página. La guía incluye fragmentos de código que demuestran cómo agregar una anotación de marca de agua en una posición específica con opacidad ajustable, así como cómo recuperar y eliminar anotaciones de marca de agua existentes. Los ejemplos de código ilustran el uso de la biblioteca Aspose.PDF para manipular documentos PDF de forma programática, ofreciendo un enfoque práctico para que los desarrolladores integren funcionalidades de marca de agua en sus aplicaciones.
---

## Agregar anotación de marca de agua

La anotación de marca de agua es la más visible y fácil de visualizar y transmitir. Es la mejor manera de colocar en tu documento PDF un logotipo u otro signo que confirme su originalidad.

Una anotación de marca de agua debe utilizarse para representar gráficos que se impriman en un tamaño y posición fijos en una página, sin importar las dimensiones de la página impresa.

Puedes agregar texto de marca de agua usando [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) en una posición específica de la página PDF. La opacidad de la marca de agua también puede controlarse usando la propiedad [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Por favor verifica el siguiente fragmento de código para agregar WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Obtener anotación de marca de agua

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Eliminar anotación de marca de agua

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


