---
title: Añadir sellos de imagen en PDF usando Python
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: es/python-net/image-stamps-in-pdf-page/
description: Añadir el sello de imagen en tu documento PDF usando la clase ImageStamp con la biblioteca Aspose.PDF para Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using Python",
    "alternativeHeadline": "Add Image stamps in PDF using Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, document generation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Añadir el sello de imagen en tu documento PDF usando la clase ImageStamp con la biblioteca Aspose.PDF para Python."
}
</script>


## Añadir Sello de Imagen en Archivo PDF

Puede utilizar la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para añadir un sello de imagen a un archivo PDF. La clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) proporciona las propiedades necesarias para crear un sello basado en una imagen, como altura, anchura, opacidad, etc.

Para añadir un sello de imagen:

1. Cree un objeto Document y un objeto ImageStamp utilizando las propiedades requeridas.
1. Llame al método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para añadir el sello al PDF.

El siguiente fragmento de código muestra cómo añadir un sello de imagen en el archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear sello de imagen
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Añadir sello a una página en particular
    document.pages[1].add_stamp(image_stamp)

    # Guardar documento de salida
    document.save(output_pdf)
```


## Controlar la Calidad de la Imagen al Agregar un Sello

Al agregar una imagen como un objeto de sello, puedes controlar la calidad de la imagen. La propiedad [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) se utiliza para este propósito. Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear sello de imagen
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Agregar sello a una página en particular
    document.pages[1].add_stamp(image_stamp)

    # Guardar documento de salida
    document.save(output_pdf)
```

## Sello de Imagen como Fondo en un Cuadro Flotante

Aspose.PDF para Python API te permite agregar un sello de imagen como fondo en un cuadro flotante.
 El atributo [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la clase [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) se puede utilizar para establecer la imagen de fondo para un cuadro flotante como se muestra en el siguiente ejemplo de código.

```python

    import aspose.pdf as ap

    # Crear objeto Document
    document = ap.Document()
    # Añadir página al documento PDF
    page = document.pages.add()
    # Crear objeto FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # Establecer posición izquierda para FloatingBox
    box.left = 40
    # Establecer posición superior para FloatingBox
    box.top = 80
    # Establecer la alineación horizontal para FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Añadir fragmento de texto a la colección de párrafos de FloatingBox
    box.paragraphs.add(ap.text.TextFragment("texto principal"))
    # Establecer borde para FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Añadir imagen de fondo
    box.background_image = img
    # Establecer color de fondo para FloatingBox
    box.background_color = ap.Color.yellow
    # Añadir FloatingBox a la colección de párrafos del objeto page
    page.paragraphs.add(box)
    # Guardar el documento PDF
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