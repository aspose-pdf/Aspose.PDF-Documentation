---
title: Agregar, Eliminar y Obtener Anotaciones
linktitle: Agregar, Eliminar y Obtener Anotaciones
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/add-delete-and-get-annotation/
description: Con Aspose.PDF for .NET puedes agregar, eliminar y obtener anotaciones de tu archivo PDF. Consulta todas las listas de anotaciones para resolver tu tarea.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add, Delete and Get Annotation",
    "alternativeHeadline": "Manage PDF Annotations with Aspose.PDF for .NET",
    "abstract": "Mejora tus capacidades de manipulación de PDF con la nueva función Agregar, Eliminar y Obtener Anotaciones en Aspose.PDF for .NET. Esta poderosa funcionalidad permite a los usuarios gestionar sin problemas las anotaciones dentro de sus archivos PDF, ofreciendo una edición simplificada y una mejor interacción con el contenido. Descubre cómo trabajar con varios tipos de anotaciones para satisfacer tus necesidades específicas de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add annotation, delete annotation, get annotation, Aspose.PDF for .NET, PDF document generation, PDF annotations, multimedia annotation, PDF text annotation, highlights annotation, PDF manipulation library",
    "wordcount": "174",
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
    "url": "/net/add-delete-and-get-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-delete-and-get-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Con Aspose.PDF for .NET puedes agregar, eliminar y obtener anotaciones de tu archivo PDF. Consulta todas las listas de anotaciones para resolver tu tarea."
}
</script>

**¿Qué son las anotaciones en documentos PDF?**

Estas son objetos adicionales que agregas a tu archivo para expandir el contenido del texto, hacer ediciones, comentarios para otros usuarios. También es posible hacer que el texto en el documento sea más legible, resaltarlo, subrayarlo o agregar texto completamente nuevo.

Hemos combinado los diferentes tipos de anotaciones disponibles para la biblioteca Aspose.PDF for .NET en grupos:

- [Anotación de Texto PDF](/pdf/es/net/text-annotation/)
- [Anotación de Resaltados PDF](/pdf/es/net/highlights-annotation/)
- [Anotación de Figuras PDF](/pdf/es/net/figures-annotation/)
- [Anotación Multimedia](/pdf/es/net/multimedia-annotation/)
- [Anotaciones Adhesivas PDF](/pdf/es/net/sticky-annotations/)
- [Anotaciones de Enlace](/pdf/es/net/link-annotations/)
- [Anotaciones Extra](/pdf/es/net/extra-annotations/)

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