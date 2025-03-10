---
title: Trabajando con Texto en PDF usando C#
linktitle: Trabajando con Texto
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/working-with-text/
description: Esta sección explica varias técnicas de manejo de texto. Aprende cómo agregar, reemplazar, rotar y buscar texto usando Aspose.PDF y C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "Descubre potentes capacidades de manipulación de texto en PDFs usando Aspose.PDF for .NET. Esta característica permite a los usuarios agregar, reemplazar, rotar y dar formato al texto dentro de documentos PDF, mejorando la interactividad y personalización del documento. Potencia tus aplicaciones con funcionalidades de búsqueda eficientes y técnicas de manejo de texto flexibles diseñadas para desarrolladores de C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta sección explica varias técnicas de manejo de texto. Aprende cómo agregar, reemplazar, rotar y buscar texto usando Aspose.PDF y C#."
}
</script>

Todos a veces necesitamos agregar texto al archivo PDF. Por ejemplo, cuando deseas agregar una traducción debajo del texto principal, colocar un pie de foto junto a una imagen, o simplemente completar un formulario de solicitud. También es útil si todos los elementos de texto pueden ser formateados en el estilo que desees. Las manipulaciones de texto más populares en tu archivo PDF son: agregar texto a PDF, formatear texto dentro del archivo PDF, reemplazar y rotar texto en tu documento. **Aspose.PDF for .NET** es la mejor solución que tiene todo lo que necesitas para interactuar con el contenido PDF.

 Puedes hacer lo siguiente:

- [Agregar Texto a archivo PDF](/pdf/net/add-text-to-pdf-file/) - agrega texto a tu PDF, usa fuentes de strem y archivos, agrega una cadena HTML, agrega un hipervínculo, etc.
- [Tooltip de PDF](/pdf/net/pdf-tooltip/) - puedes agregar un tooltip al texto buscado añadiendo un botón invisible usando C#.
- [Formateo de Texto dentro de PDF](/pdf/net/text-formatting-inside-pdf/) - Muchas características puedes agregar a tu documento al formatear el texto dentro de él. Agrega sangría, agrega borde de texto, agrega texto subrayado, agrega salto de línea con la biblioteca Aspose.PDF.
- [Usando FloatingBox](/pdf/net/floating-box/) - la herramienta Floating Box es una herramienta especial para colocar texto y otro contenido en una página PDF.
- [Reemplazar Texto en PDF](/pdf/net/replace-text-in-pdf/) - para reemplazar texto en todas las páginas de un documento PDF. Primero necesitas usar TextFragmentAbsorber.
- [Rotar Texto Dentro de PDF](/pdf/net/rotate-text-inside-pdf/) - rota texto dentro de PDF usando la propiedad de rotación de la clase TextFragment.
- [Buscar y Obtener Texto de Páginas de Documento PDF](/pdf/net/search-and-get-text-from-pdf/) - puedes usar la clase TextFragmentAbsorber para buscar y obtener texto de las páginas.
- [Determinar Salto de Línea](/pdf/net/determine-line-break/) - este tema explica cómo rastrear el salto de línea de fragmentos de texto de múltiples líneas.

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