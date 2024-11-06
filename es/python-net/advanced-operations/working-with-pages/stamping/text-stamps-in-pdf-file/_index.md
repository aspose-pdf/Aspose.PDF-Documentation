---
title: Agregar sellos de texto en PDF mediante Python
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: es/python-net/text-stamps-in-the-pdf-file/
description: Agregue un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF para Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Agregar sellos de texto en PDF Python",
    "alternativeHeadline": "Agregar sellos de texto en PDF Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, generación de documentos",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Agregue un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF para Python."
}
</script>


## Añadir Sello de Texto con Python

Puede usar la clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para agregar un sello de texto en un archivo PDF. La clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) proporciona las propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente, y color de fuente, etc. Para agregar un sello de texto, necesita crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puede llamar al método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la Página para agregar el sello en el PDF. El siguiente fragmento de código le muestra cómo agregar un sello de texto en el archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear sello de texto
    text_stamp = ap.TextStamp("Sample Stamp")
    # Configurar si el sello es de fondo
    text_stamp.background = True
    # Establecer origen
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotar sello
    text_stamp.rotate = ap.Rotation.ON90
    # Configurar propiedades de texto
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Agregar sello a una página en particular
    document.pages[1].add_stamp(text_stamp)

    # Guardar documento de salida
    document.save(output_pdf)
```


## Definir alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características más demandadas y Aspose.PDF para Python es completamente capaz de agregar tanto marcas de agua de imagen como de texto. Tenemos una clase llamada [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) que proporciona la función de agregar sellos de texto sobre el archivo PDF. Recientemente ha habido un requisito para admitir la característica de especificar la alineación del texto al usar el objeto TextStamp. Así que, para cumplir con este requisito, hemos introducido la propiedad [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) en la clase [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). Usando esta propiedad, podemos especificar la alineación de texto [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties).

Los siguientes fragmentos de código muestran un ejemplo de cómo cargar un documento PDF existente y agregar un TextStamp sobre él.

```python

    import aspose.pdf as ap

    # Instanciar objeto Documento con archivo de entrada
    doc = ap.Document(input_pdf)
    # Instanciar objeto FormattedText con cadena de ejemplo
    text = ap.facades.FormattedText("This")
    # Agregar nueva línea de texto a FormattedText
    text.add_new_line_text("es un ejemplo")
    text.add_new_line_text("Centrado")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Objeto")
    # Crear objeto TextStamp usando FormattedText
    stamp = ap.TextStamp(text)
    # Especificar la alineación horizontal del sello de texto como centrado
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Especificar la alineación vertical del sello de texto como centrado
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Especificar la alineación horizontal del texto de TextStamp como centrado
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Establecer margen superior para el objeto sello
    stamp.top_margin = 20
    # Agregar el objeto sello sobre la primera página del documento
    doc.pages[1].add_stamp(stamp)

    # Guardar el documento actualizado
    doc.save(output_pdf)
```


## Rellenar Texto de Trazo como Sello en un Archivo PDF

Hemos implementado la configuración del modo de renderizado para escenarios de adición y edición de texto. Para renderizar texto de trazo, cree un objeto TextState para transferir propiedades avanzadas. Establezca el color para el trazo. Después, configure el modo de renderizado de texto. El siguiente paso es vincular TextState y agregar el Sello.

El siguiente fragmento de código demuestra cómo agregar Texto de Trazo de Relleno:

```python

    import aspose.pdf as ap

    # Crear un objeto TextState para transferir propiedades avanzadas
    ts = ap.text.TextState()
    # Establecer color para el trazo
    ts.stroking_color = ap.Color.gray
    # Establecer modo de renderizado de texto
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Cargar un documento PDF de entrada
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAGADO COMPLETAMENTE",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Vincular TextState
    stamp.bind_text_state(ts)
    # Establecer origen X,Y
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Agregar Sello
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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