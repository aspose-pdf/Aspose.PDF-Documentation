---
title: Añadir Número de Página a PDF con Python
linktitle: Añadir Número de Página
type: docs
weight: 30
url: /python-net/add-page-number/
description: Aspose.PDF para Python a través de .NET te permite añadir un Sello de Número de Página a tu archivo PDF usando la clase PageNumberStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Número de Página a PDF con Python",
    "alternativeHeadline": "Cómo añadir Sello de Número de Página a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, sello de número de página",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para Python a través de .NET te permite añadir un Sello de Número de Página a tu archivo PDF usando la clase PageNumberStamp."
}
</script>


All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.  
**Aspose.PDF para Python vía .NET** le permite agregar números de página con [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

Puede usar la clase [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) para agregar un sello de número de página en un archivo PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) clase proporciona las propiedades necesarias para crear un sello basado en el número de página como formato, márgenes, alineaciones, número de inicio, etc. Para agregar un sello de número de página, necesitas crear un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y un objeto [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) usando las propiedades requeridas. Después de eso, puedes llamar al método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para agregar el sello en el PDF. También puedes establecer los atributos de fuente del sello de número de página. El siguiente fragmento de código te muestra cómo agregar números de página en un archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear sello de número de página
    page_number_stamp = ap.PageNumberStamp()
    # Si el sello es de fondo
    page_number_stamp.background = False
    page_number_stamp.format = "Página # de " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Establecer propiedades de texto
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # Agregar sello a una página en particular
    document.pages[1].add_stamp(page_number_stamp)

    # Guardar documento de salida
    document.save(output_pdf)
```

## Ejemplo en Vivo

[Agregar números de página en PDF](https://products.aspose.app/pdf/page-number) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de agregar números de página.

[![Cómo agregar un número de página en PDF usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)