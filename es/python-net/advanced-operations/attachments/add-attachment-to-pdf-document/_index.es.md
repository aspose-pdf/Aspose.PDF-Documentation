---
title: Añadiendo un archivo adjunto a un documento PDF utilizando Python
linktitle: Añadiendo un archivo adjunto a un documento PDF
type: docs
weight: 10
url: /python-net/add-attachment-to-pdf-document/
description: Esta página describe cómo agregar un archivo adjunto a un archivo PDF con Aspose.PDF para Python a través de la biblioteca .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadiendo un archivo adjunto a un documento PDF mediante Python",
    "alternativeHeadline": "Cómo agregar archivos adjuntos a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, archivos adjuntos en pdf",
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
    "url": "/python-net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Esta página describe cómo agregar un archivo adjunto a un archivo PDF con Aspose.PDF para Python a través de la biblioteca .NET"
}
</script>


Attachments pueden contener una amplia variedad de información y pueden ser de diversos tipos de archivos. Este artículo explica cómo agregar un adjunto a un archivo PDF.

1. Crea un nuevo proyecto de Python.
1. Importa el paquete Aspose.PDF
1. Crea un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crea un objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) con el archivo que estás agregando y la descripción del archivo.
1. Agrega el objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) a la colección [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), con el método [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) de la colección.

La colección [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contiene todos los adjuntos en el archivo PDF.
 El siguiente fragmento de código te muestra cómo agregar un adjunto en un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Configurar nuevo archivo para ser agregado como adjunto
    fileSpecification = ap.FileSpecification(attachment_file, "Archivo de texto de ejemplo")

    # Añadir adjunto a la colección de adjuntos del documento
    document.embedded_files.append(fileSpecification)

    # Guardar nuevo resultado
    document.save(output_pdf)