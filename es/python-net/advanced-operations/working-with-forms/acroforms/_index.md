---
title: Trabajando con AcroForms usando Python
linktitle: AcroForms
type: docs
weight: 10
url: /es/python-net/acroforms/
description: Con Aspose.PDF para Python puedes crear un formulario desde cero, completar el campo del formulario en un documento PDF, extraer datos del formulario, etc.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con AcroForms usando Python",
    "alternativeHeadline": "Opciones para trabajar con AcroForms en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, acroforms en pdf",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "Con Aspose.PDF para Python puedes crear un formulario desde cero, completar el campo del formulario en un documento PDF, extraer datos del formulario, etc."
}
</script>


## Fundamentos de AcroForms

**AcroForms** - tecnología de formularios PDF única de Adobe. AcroForms es un formulario orientado a la página. Aparecieron por primera vez en 1998. Aceptan entrada en forma de formato de Datos o FDF y formato de Datos de formulario XML o xFDF. Proveedores de terceros apoyan AcroForms. Cuando Adobe introdujo AcroForms, los llamaron el "formulario PDF, que es el autor de Adobe Acrobat Pro/Standard y no es un tipo especial de formulario XFA estático o dinámico. AcroForms son portátiles y funcionan en todas las plataformas.

Puedes usar AcroForms para agregar páginas adicionales al documento de formulario PDF. Gracias al concepto de Plantillas, puedes usar AcroForms para apoyar el llenado del formulario con múltiples registros de base de datos.

PDF 1.7 admite dos métodos diferentes para integrar datos y formularios PDF.

*AcroForms (también conocidos como formularios Acrobat)*, introducidos e incluidos en la especificación de formato PDF 1.2.

Para un aprendizaje más detallado de las capacidades de la biblioteca Java, consulta los siguientes artículos:

- [Crear AcroForm](/pdf/es/python-net/create-form) - crear formulario desde cero con Python.
- [Rellenar AcroForm](/pdf/es/python-net/fill-form) - rellena el campo de formulario en tu documento PDF.
- [Extraer AcroForm](/pdf/es/python-net/extract-form) - obtiene el valor de todos o de un campo individual del documento PDF.

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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>