---
title: Trabajando con Páginas PDF en C#
linktitle: Trabajando con Páginas
type: docs
weight: 20
url: es/net/working-with-pages/
description: Cómo agregar páginas, encabezados y pies de página, agregar marcas de agua puedes saber en esta sección. Aspose.PDF para .NET te explica todos los detalles sobre este tema.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Páginas PDF en C#",
    "alternativeHeadline": "Cómo trabajar con Páginas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, página pdf, agregar página pdf, agregar número de página, rotar página, eliminar página",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Cómo agregar páginas, encabezados y pies de página, agregar marcas de agua puedes saber en esta sección. Aspose.PDF para .NET te explica todos los detalles sobre este tema."
}
</script>

**Aspose.PDF para .NET** te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF. Esta sección muestra cómo añadir páginas a un PDF sin Acrobat Reader.
Puedes añadir texto o imágenes en los encabezados y pies de página de tu archivo PDF, y elegir diferentes encabezados en tu documento con la biblioteca C# de Aspose.
También, intenta recortar páginas en un documento PDF programáticamente usando C#.

Esta sección te enseña cómo añadir marcas de agua en tu archivo PDF usando la clase Artifact. Revisarás el ejemplo de programación para esta tarea.
Añade número de página usando la clase PageNumberStamp. Para añadir un Sello en tu documento usa las clases ImageStamp y TextStamp. Usa la adición de una marca de agua para crear imágenes de fondo en tu archivo PDF con **Aspose.PDF para .NET**.

Eres capaz de hacer lo siguiente:

- [Añadir Páginas](/pdf/net/add-pages/) - añadir páginas en la ubicación deseada o al final de un archivo PDF y eliminar una página de tu documento.
- [Mover Páginas](/pdf/net/move-pages/) - mover páginas de un documento a otro.
- [Mover Páginas](/pdf/net/move-pages/) - mueve páginas de un documento a otro.
- [Eliminar Páginas](/pdf/net/delete-pages/) - elimina páginas de tu archivo PDF usando la colección PageCollection.
- [Cambiar Tamaño de Página](/pdf/net/change-page-size/) - puedes cambiar el tamaño de la página PDF con un fragmento de código usando la biblioteca Aspose.PDF.
- [Rotar Páginas](/pdf/net/rotate-pages/) - puedes cambiar la orientación de las páginas en un archivo PDF existente.
- [Dividir Páginas](/pdf/net/split-document/) - puedes dividir archivos PDF en uno o múltiples PDF.
- [Agregar Encabezados y/o Pies de Página](/pdf/net/add-headers-and-footers-of-pdf-file/) - agrega texto o imágenes en los encabezados y pies de página de tu archivo PDF.
- [Recortar Páginas](/pdf/net/crop-pages/) - puedes recortar páginas en un documento PDF programáticamente con diferentes Propiedades de Página.
- [Agregar Marcas de Agua](/pdf/net/add-watermarks/) - agrega marcas de agua en tu archivo PDF con la Clase Artifact.
- [Agregar Numeración de Páginas en Archivo PDF](/pdf/net/add-page-number/) - la clase PageNumberStamp te ayudará a agregar un Número de Página en tu archivo PDF.
- [Agregar Numeración de Páginas en Archivo PDF](/pdf/net/add-page-number/) - La clase PageNumberStamp te ayudará a agregar un número de página en tu archivo PDF.
- [Agregar Fondos](/pdf/net/add-backgrounds/) - las imágenes de fondo se pueden utilizar para agregar una marca de agua.
- [Estampado](/pdf/net/stamping/) - puedes usar la clase ImageStamp para agregar un sello de imagen a un archivo PDF y la clase TextStamp para agregar texto.

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

