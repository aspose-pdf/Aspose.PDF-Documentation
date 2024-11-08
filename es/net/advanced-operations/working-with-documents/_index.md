---
title: Trabajando con Documentos PDF usando C#
linktitle: Trabajando con Documentos
type: docs
weight: 10
url: /es/net/working-with-documents/
description: Este artículo describe las manipulaciones que se pueden realizar con el documento con la biblioteca Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-document/
    - /net/working-with-document-facades/
    - /net/create-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Documentos PDF usando C#",
    "alternativeHeadline": "Manipulación de Documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, documentos pdf",
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
    "url": "/net/working-with-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo describe las manipulaciones que se pueden realizar con el documento con la biblioteca Aspose.PDF."
}
</script>

PDF significa Formato de Documento Portátil, utilizado para mostrar documentos en forma electrónica independiente del software, hardware o sistema operativo en el que se visualizan.

El PDF es un estándar abierto, mantenido hoy por la Organización Internacional para la Estandarización (ISO).

El objetivo original era preservar y proteger el contenido y el diseño de un documento, sin importar en qué plataforma o programa informático se visualice. Esta es la razón por la cual los PDF son difíciles de editar y, a veces, incluso extraer información de ellos es un desafío.

Pero **Aspose.PDF for .NET** puede ayudarte a enfrentar la mayoría de las tareas que surgen al trabajar con un documento PDF.

Puedes hacer lo siguiente:

- [Formatear Documento PDF](/pdf/es/net/formatting-pdf-document/) - crear un documento, obtener y establecer propiedades del documento, incrustar fuentes y otras operaciones con archivos PDF.
- [Manipular Documento PDF](/pdf/es/net/manipulate-pdf-document/) - validar un documento PDF para el estándar PDF A, trabajar con TOC, establecer fecha de caducidad del PDF, y etc.
- [Optimizar PDF](/pdf/es/net/optimize-pdf/) - optimizar contenido de página, optimizar tamaño de archivo, eliminar objetos no utilizados, comprimir todas las imágenes para una optimización exitosa del documento.
- [Optimizar PDF](/pdf/es/net/optimize-pdf/) - optimizar el contenido de la página, optimizar el tamaño del archivo, eliminar objetos no utilizados, comprimir todas las imágenes para una optimización exitosa del documento.
- [Fusionar PDF](/pdf/es/net/merge-pdf-documents/) - fusionar múltiples archivos PDF en un solo documento PDF utilizando C#.
- [Dividir PDF](/pdf/es/net/split-document/) - dividir páginas PDF en archivos PDF individuales en sus aplicaciones .NET.
- [Concatenar archivos PDF en una carpeta](/pdf/es/net/concatenating-all-pdf-files-in-particular-folder/) - concatenar todos los archivos PDF en una carpeta en particular utilizando la clase PdfFileEditor.
- [Concatenar múltiples archivos PDF usando MemoryStreams](/pdf/es/net/concatenate-pdf-documents/) - aprenderás cómo concatenar múltiples archivos PDF utilizando MemoryStreams con C#.
- [Trabajar con Encabezados](/pdf/es/net/working-with-headings/) - puedes crear numeración en el encabezado de tu documento PDF con C#.

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

