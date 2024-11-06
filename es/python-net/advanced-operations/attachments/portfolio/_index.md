---
title: Trabajando con Portafolio en PDF usando Python
linktitle: Portafolio
type: docs
weight: 20
url: es/python-net/portfolio/
description: Cómo Crear un Portafolio en PDF con Python. Debe usar un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio en PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Portafolio en PDF usando Python",
    "alternativeHeadline": "Crear Portafolio en documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf en pdf",
    "keywords": "pdf, python, portafolio",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Cómo Crear un Portafolio en PDF con Python. Debe usar un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio en PDF."
}
</script>


Crear un portafolio PDF permite consolidar y archivar diferentes tipos de archivos en un solo documento coherente. Dicho documento podría incluir archivos de texto, imágenes, hojas de cálculo, presentaciones y otros materiales, y garantizar que todo el material relevante esté almacenado y organizado en un solo lugar.

El portafolio PDF ayudará a mostrar tu presentación de una manera de alta calidad, donde sea que lo uses. En general, crear un portafolio PDF es una tarea muy actual y moderna.

## Cómo Crear un Portafolio PDF

Aspose.PDF para Python a través de .NET permite crear documentos de Portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Agrega un archivo en un objeto document.collection después de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Cuando los archivos han sido agregados, usa el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase Document para guardar el documento del portafolio.

El siguiente ejemplo utiliza un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.

El siguiente código resulta en el siguiente portafolio.

### Un Portafolio PDF creado con Aspose.PDF para Python

![Un Portafolio PDF creado con Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    document = ap.Document()

    # Instanciar objeto Collection del documento
    document.collection = ap.Collection()

    # Obtener archivos para añadir al portafolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Proporcionar descripción de los archivos
    excel.description = "Archivo Excel"
    word.description = "Archivo Word"
    image.description = "Archivo de Imagen"

    # Añadir archivos a la colección del documento
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Guardar documento del portafolio
    document.save(output_pdf)
```

## Eliminar archivos del Portafolio PDF

Para eliminar/quitar archivos del portafolio PDF, intente usar las siguientes líneas de código.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Guardar archivo actualizado
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>