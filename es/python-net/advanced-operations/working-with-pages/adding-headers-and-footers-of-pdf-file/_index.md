---
title: Añadir encabezado y pie de página al PDF usando Python
linktitle: Añadir encabezado y pie de página al PDF
type: docs
weight: 50
url: es/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Python a través de .NET te permite añadir encabezados y pies de página a tu archivo PDF usando la clase TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir encabezado y pie de página al PDF usando Python",
    "alternativeHeadline": "Cómo añadir encabezado y pie de página al archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, añadir encabezado, añadir pie de página en pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para Python a través de .NET te permite añadir encabezados y pies de página a tu archivo PDF usando la clase TextStamp."
}
</script>


**Aspose.PDF for Python via .NET** le permite agregar encabezados y pies de página en su archivo PDF existente. Puede agregar imágenes o texto a un documento PDF. Además, intente agregar diferentes encabezados en un archivo PDF con Python.

## Agregar texto en el encabezado del archivo PDF

Puede usar la clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para agregar texto en el encabezado de un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el encabezado, necesita crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puede llamar al método 'add_stamp' de la Página para agregar el texto en el encabezado del PDF.

Necesita configurar la propiedad [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) de tal manera que ajuste el texto en el área del encabezado de su PDF. También necesita configurar 'horizontal_alignment' a Center y 'vertical_alignment' a Top.

El siguiente fragmento de código le muestra cómo agregar texto en el encabezado de un archivo PDF con Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear encabezado
    textStamp = ap.TextStamp("Header Text")
    # Establecer propiedades del sello
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Agregar encabezado en todas las páginas
    for page in document.pages:
        page.add_stamp(textStamp)

    # Guardar documento actualizado
    document.save(output_pdf)
```

## Agregar Texto en el Pie de Página del Archivo PDF

Puede usar la clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para agregar texto en el pie de página de un archivo PDF.
 Clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el pie de página, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método 'add_stamp' de la Página para agregar el texto en el pie de página del PDF.

El siguiente fragmento de código te muestra cómo agregar texto en el pie de página de un archivo PDF con Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Crear pie de página
    textStamp = ap.TextStamp("Texto del Pie de Página")
    # Establecer propiedades del sello
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Agregar pie de página en todas las páginas
    for page in document.pages:
        page.add_stamp(textStamp)

    # Guardar archivo PDF actualizado
    document.save(output_pdf)
```

## Añadir Imagen en el Encabezado de un Archivo PDF

Puedes usar la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para añadir una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen, como el tamaño de fuente, el estilo de fuente y el color de fuente, etc. Para agregar una imagen en el encabezado, necesitas crear un objeto Document y un objeto Image Stamp utilizando las propiedades necesarias. Después de eso, puedes llamar al método 'add_stamp' de la Page para agregar la imagen en el encabezado del PDF.

El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF con Python:

```python 

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear encabezado
    image_stamp = ap.ImageStamp(input_image)
    # Establecer propiedades del sello
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Agregar encabezado en todas las páginas
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Guardar documento actualizado
    document.save(output_pdf)
```

## Agregar Imagen en el Pie de Página del Archivo PDF

Puedes usar la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para agregar una imagen en el pie de página de un archivo PDF. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class proporciona propiedades necesarias para crear un sello basado en imagen como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el pie de página, necesitas crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método 'add_stamp' de la Página para agregar la imagen en el pie de página del PDF.

El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Crear pie de página
    image_stamp = ap.ImageStamp(input_image)
    # Establecer propiedades del sello
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Agregar pie de página en todas las páginas
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Guardar archivo PDF actualizado
    document.save(output_pdf)
```

## Añadir diferentes encabezados en un archivo PDF

Sabemos que podemos añadir TextStamp en la sección de Encabezado/Pie de página del documento utilizando las propiedades [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) o [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties), pero a veces podemos tener el requisito de añadir múltiples encabezados/pies de página en un único documento PDF. **Aspose.PDF para Python a través de .NET** explica cómo hacer esto.

Para cumplir con este requisito, crearemos objetos individuales de TextStamp (el número de objetos depende del número de encabezados/pies de página requeridos) y los añadiremos al documento PDF.
 Podemos especificar también diferente información de formato para cada objeto sello individual. En el siguiente ejemplo, hemos creado un objeto Document y tres objetos TextStamp y luego hemos utilizado el método 'add_stamp' de Page para añadir el texto en la sección del encabezado del PDF. El siguiente fragmento de código te muestra cómo añadir una imagen en el pie de página de un archivo PDF con Aspose.PDF para Python:

```python

    import aspose.pdf as ap

    # Crear tres sellos
    stamp1 = ap.TextStamp("Encabezado 1")
    stamp2 = ap.TextStamp("Encabezado 2")
    stamp3 = ap.TextStamp("Encabezado 3")

    # Establecer la alineación del sello (colocar el sello en la parte superior de la página, centrado horizontalmente)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Especificar el estilo de fuente como Negrita
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Establecer la información del color del texto de primer plano como rojo
    stamp1.text_state.foreground_color = ap.Color.red
    # Especificar el tamaño de fuente como 14
    stamp1.text_state.font_size = 14

    # Ahora necesitamos establecer la alineación vertical del segundo objeto sello como Superior
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Establecer la información de alineación horizontal para el sello como Centrado
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Establecer el factor de zoom para el objeto sello
    stamp2.zoom = 10

    # Establecer el formato del tercer objeto sello
    # Especificar la información de alineación vertical para el objeto sello como SUPERIOR
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Establecer la información de alineación horizontal para el objeto sello como Centrado
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Establecer el ángulo de rotación para el objeto sello
    stamp3.rotate_angle = 35
    # Establecer el color de fondo del sello como rosa
    stamp3.text_state.background_color = ap.Color.pink
    # Cambiar la información de la fuente del sello a Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # El primer sello se añade en la primera página;
    document.pages[1].add_stamp(stamp1)
    # El segundo sello se añade en la segunda página;
    document.pages[2].add_stamp(stamp2)
    # El tercer sello se añade en la tercera página.
    document.pages[3].add_stamp(stamp3)

    # Guardar el documento actualizado
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>