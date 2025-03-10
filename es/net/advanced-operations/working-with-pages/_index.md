---
title: Trabajando con Páginas PDF en C#
linktitle: Trabajando con Páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/working-with-pages/
description: Cómo agregar páginas, agregar encabezados y pies de página, agregar marcas de agua que puedes conocer en esta sección. Aspose.PDF for .NET te explica todos los detalles sobre este tema.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "Descubre las capacidades avanzadas de Aspose.PDF for .NET para gestionar páginas PDF, incluyendo agregar, mover y eliminar páginas con precisión. Esta función permite a los usuarios mejorar sus documentos PDF incorporando encabezados, pies de página, marcas de agua y tamaños de página personalizados, todo a través de un código C# intuitivo. Optimiza tus flujos de trabajo de documentos con manipulaciones y funcionalidades de personalización de PDF sin problemas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Cómo agregar páginas, agregar encabezados y pies de página, agregar marcas de agua que puedes conocer en esta sección. Aspose.PDF for .NET te explica todos los detalles sobre este tema."
}
</script>

**Aspose.PDF for .NET** te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF. Esta sección muestra cómo agregar páginas a un PDF sin Acrobat Reader. 
Puedes agregar texto o imágenes en los encabezados y pies de página de tu archivo PDF, y elegir diferentes encabezados en tu documento con la biblioteca C# de Aspose. 
Además, intenta recortar páginas en el documento PDF programáticamente usando C#.

Esta sección te enseña cómo agregar marcas de agua en tu archivo PDF utilizando la clase Artifact. Revisarás el ejemplo de programación para esta tarea. 
Agrega el número de página utilizando la clase PageNumberStamp. Para agregar un sello en tu documento, utiliza las clases ImageStamp y TextStamp. Usa la adición de una marca de agua para crear imágenes de fondo en tu archivo PDF con **Aspose.PDF for .NET**.

Puedes hacer lo siguiente:

- [Agregar Páginas](/pdf/es/net/add-pages/) - agregar páginas en la ubicación deseada o al final de un archivo PDF y eliminar una página de tu documento.
- [Mover Páginas](/pdf/es/net/move-pages/) - mover páginas de un documento a otro.
- [Eliminar Páginas](/pdf/es/net/delete-pages/) - eliminar una página de tu archivo PDF utilizando la colección PageCollection.
- [Cambiar Tamaño de Página](/pdf/es/net/change-page-size/) - puedes cambiar el tamaño de la página PDF con un fragmento de código utilizando la biblioteca Aspose.PDF.
- [Rotar Páginas](/pdf/es/net/rotate-pages/) - puedes cambiar la orientación de las páginas en un archivo PDF existente.
- [Dividir Páginas](/pdf/es/net/split-document/) - puedes dividir archivos PDF en uno o múltiples PDF.
- [Agregar Encabezados y/o Pies de Página](/pdf/es/net/add-headers-and-footers-of-pdf-file/) - agregar texto o imágenes en los encabezados y pies de página de tu archivo PDF.
- [Recortar Páginas](/pdf/es/net/crop-pages/) - puedes recortar páginas en el documento PDF programáticamente con diferentes Propiedades de Página.
- [Agregar Marcas de Agua](/pdf/es/net/add-watermarks/) - agregar marcas de agua en tu archivo PDF con la clase Artifact.
- [Agregar Numeración de Página en el Archivo PDF](/pdf/es/net/add-page-number/) - la clase PageNumberStamp te ayudará a agregar un número de página en tu archivo PDF.
- [Agregar Fondos](/pdf/es/net/add-backgrounds/) - las imágenes de fondo se pueden usar para agregar una marca de agua.
- [Sello](/pdf/es/net/stamping/) - puedes usar la clase ImageStamp para agregar un sello de imagen a un archivo PDF y la clase TextStamp para agregar texto.

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