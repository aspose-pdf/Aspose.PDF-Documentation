---
title: Trabajando con Texto en PDF usando C#
linktitle: Trabajando con Texto
type: docs
weight: 30
url: es/net/working-with-text/
description: Esta sección explica varias técnicas de manejo de texto. Aprende cómo agregar, reemplazar, rotar, buscar texto usando Aspose.PDF y C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Texto en PDF usando C#",
    "alternativeHeadline": "Agregar, Rotar, Buscar y Eliminar Texto en Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, agregar texto, buscar texto, eliminar texto, manipular texto en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección explica varias técnicas de manejo de texto. Aprende cómo agregar, reemplazar, rotar, buscar texto usando Aspose.PDF y C#."
}
</script>
Todos necesitamos en algún momento agregar texto a un archivo PDF. Por ejemplo, cuando quieres añadir una traducción debajo del texto principal, colocar un pie de foto junto a una imagen o simplemente llenar un formulario de solicitud. También es útil si todos los elementos de texto pueden formatearse en el estilo que desees. Las manipulaciones de texto más populares en tu archivo PDF son: agregar texto al PDF, formatear texto dentro del archivo PDF, reemplazar y rotar texto en tu documento. **Aspose.PDF para .NET** es la mejor solución que tiene todo lo que necesitas para interactuar con el contenido del PDF.

Eres capaz de hacer lo siguiente:

- [Agregar texto al archivo PDF](/pdf/net/add-text-to-pdf-file/) - añade texto a tu PDF, usa fuentes de stream y archivos, añade una cadena HTML, añade un hipervínculo, etc.
- [Tooltip de PDF](/pdf/net/pdf-tooltip/) - puedes añadir un tooltip al texto buscado agregando un botón invisible usando C#.
- [Formateo de texto dentro del PDF](/pdf/net/text-formatting-inside-pdf/) - Muchas características que puedes añadir a tu documento al formatear el texto dentro de él.
- [Formato de texto dentro de PDF](/pdf/net/text-formatting-inside-pdf/) - Muchas características que puedes agregar a tu documento al formatear el texto dentro de él.
- [Reemplazar texto en PDF](/pdf/net/replace-text-in-pdf/) - para reemplazar texto en todas las páginas de un documento PDF. Primero necesitas usar TextFragmentAbsorber.
- [Rotar texto dentro de PDF](/pdf/net/rotate-text-inside-pdf/) - rotar texto dentro de PDF usando la propiedad de rotación de la clase TextFragment.
- [Buscar y obtener texto de las páginas de un documento PDF](/pdf/net/search-and-get-text-from-pdf/) - puedes usar la clase TextFragmentAbsorber para buscar y obtener un texto de las páginas.
- [Determinar salto de línea](/pdf/net/determine-line-break/) - este tema explica cómo rastrear el salto de línea de fragmentos de texto de múltiples líneas.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


