---
title: Tooltip en PDF usando Python
linktitle: Tooltip en PDF
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: Aprende cómo agregar un tooltip al fragmento de texto en PDF usando Python y Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tooltip en PDF usando Python",
    "alternativeHeadline": "Agregar Tooltip en PDF al Texto",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, agregar tooltip en pdf",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Aprende cómo agregar un tooltip al fragmento de texto en PDF usando Python y Aspose.PDF"
}
</script>


## Agregar Tooltip al Texto Buscado mediante un Botón Invisible

Este código demuestra cómo agregar tooltips a fragmentos de texto específicos en un documento PDF usando Aspose.PDF. Los tooltips se muestran cuando el cursor del ratón se coloca sobre el texto correspondiente.

El siguiente fragmento de código te mostrará cómo lograr esta funcionalidad:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Mueve el cursor del ratón aquí para mostrar un tooltip")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Mueve el cursor del ratón aquí para mostrar un tooltip muy largo"
        )
    )
    document.save(output_pdf)

    # Abre el documento con texto
    document = ap.Document(output_pdf)
    # Crea un objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
    absorber = ap.text.TextFragmentAbsorber(
        "Mueve el cursor del ratón aquí para mostrar un tooltip"
    )
    # Acepta el absorber para las páginas del documento
    document.pages.accept(absorber)
    # Obtén los fragmentos de texto extraídos
    text_fragments = absorber.text_fragments

    # Recorre los fragmentos
    for fragment in text_fragments:
        # Crea un botón invisible en la posición del fragmento de texto
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # El valor de alternate_name se mostrará como tooltip por una aplicación de visualización
        field.alternate_name = "Tooltip para el texto."
        # Agrega el campo de botón al documento
        document.form.add(field)

    # A continuación, será una muestra de un tooltip muy largo
    absorber = ap.text.TextFragmentAbsorber(
        "Mueve el cursor del ratón aquí para mostrar un tooltip muy largo"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Establece texto muy largo
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Guarda el documento
    document.save(output_pdf)
```


## Crear un Bloque de Texto Oculto y Mostrarlo al Pasar el Ratón

Este fragmento de código en Python muestra cómo agregar texto flotante a un documento PDF, que aparece cuando el cursor del ratón se coloca sobre un área específica.

Primero, se crea un nuevo documento PDF y se le añade un párrafo que contiene el texto "Mueva el cursor del ratón aquí para mostrar texto flotante". Luego, se guarda el documento.

A continuación, se vuelve a abrir el documento guardado y se crea un objeto TextAbsorber para encontrar el fragmento de texto previamente añadido. Este fragmento de texto se utiliza entonces para definir la posición y las características del campo de texto flotante.

Se crea un objeto TextBoxField para representar el campo de texto flotante, y sus propiedades como posición, valor, estado de solo lectura y visibilidad se configuran en consecuencia. Además, se asigna un nombre único y características de apariencia al campo.

El campo de texto flotante se añade al formulario del documento, y se crea un campo de botón invisible en la posición del fragmento de texto original.
 HideAction events se asignan al campo de botón, especificando que el campo de texto flotante debe aparecer cuando el cursor del mouse entra en su vecindad y desaparecer cuando el cursor sale.

Finalmente, el campo de botón se agrega al formulario del documento y se guarda el documento modificado.

Este fragmento de código proporciona un método para crear elementos de texto flotante interactivos en un documento PDF usando Aspose.PDF para Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Mueva el cursor del mouse aquí para mostrar el texto flotante")
    )
    document.save(output_pdf)

    # Abrir documento con texto
    document = ap.Document(output_pdf)
    # Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular
    absorber = ap.text.TextFragmentAbsorber(
        "Mueva el cursor del mouse aquí para mostrar el texto flotante"
    )
    # Aceptar el absorbedor para las páginas del documento
    document.pages.accept(absorber)
    # Obtener el primer fragmento de texto extraído
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Crear campo de texto oculto para texto flotante en el rectángulo especificado de la página
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Establecer texto a mostrar como valor del campo
    floating_field.value = 'Este es el "campo de texto flotante".'
    # Recomendamos hacer que el campo sea 'solo lectura' para este escenario
    floating_field.read_only = True
    # Establecer la bandera 'oculto' para hacer que el campo sea invisible al abrir el documento
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # No es necesario pero permitido establecer un nombre de campo único
    floating_field.partial_name = "FloatingField_1"

    # No es necesario, pero mejora establecer características de apariencia del campo
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Agregar campo de texto al documento
    document.form.add(floating_field)
    # Crear botón invisible en la posición del fragmento de texto
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Crear nueva acción de ocultar para el campo (anotación) especificado y la bandera de invisibilidad.
    # (También puede referirse al campo flotante por el nombre si lo especificó anteriormente.)
    # Agregar acciones en la entrada/salida del mouse en el campo de botón invisible

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Agregar campo de botón al documento
    document.form.add(button_field)

    # Guardar documento
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python a través de .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>