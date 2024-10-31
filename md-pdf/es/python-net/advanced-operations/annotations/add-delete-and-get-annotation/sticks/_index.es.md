---
title: Anotaciones adhesivas en PDF usando Python
linktitle: Anotación adhesiva
type: docs
weight: 50
url: /python-net/sticky-annotations/
description: Este tema trata sobre las anotaciones adhesivas, como ejemplo mostramos la Anotación de Marca de Agua en el texto.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotaciones adhesivas en PDF usando Python",
    "alternativeHeadline": "Cómo agregar Anotaciones Adhesivas en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, anotaciones adhesivas, anotación de marca de agua",
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
    "url": "/python-net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/sticky-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Este tema trata sobre las anotaciones adhesivas, como ejemplo mostramos la Anotación de Marca de Agua en el texto usando la Biblioteca Python."
}
</script>


## Añadir Anotación de Marca de Agua

La más visible y fácil de visualizar y transmitir es la Anotación de Marca de Agua. Esta es la mejor manera de colocar en su documento PDF un logotipo o cualquier otro signo que confirme su originalidad.

Se debe usar una anotación de marca de agua para representar gráficos que se imprimirán en un tamaño y posición fijos en una página, independientemente de las dimensiones de la página impresa.

Puede agregar Texto de Marca de Agua utilizando [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) en una posición específica de la página PDF. La opacidad de la Marca de Agua también se puede controlar usando la propiedad [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Por favor, consulte el siguiente fragmento de código para agregar WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Crear Anotación
    # Cargar objeto Página para agregar Anotación
    page = document.pages[1]

    # Crear Anotación
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Agregar anotación a la colección de Anotaciones de la Página
    page.annotations.append(wa)

    # Crear TextState para la configuración de Fuente
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Establecer nivel de opacidad del Texto de la Anotación
    wa.opacity = 0.5

    # Agregar Texto en la Anotación
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```


## Obtener Anotación de Marca de Agua

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

## Eliminar Anotación de Marca de Agua

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