---
title: Trabajando con Gráficos en archivo PDF
linktitle: Trabajando con Gráficos
type: docs
weight: 70
url: /es/net/graphs/
description: Este artículo explica lo que es un Gráfico, cómo crear un objeto de rectángulo lleno y otras funciones
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Gráficos en archivo PDF",
    "alternativeHeadline": "Cómo crear gráficos en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, gráficos en pdf",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica lo que es un Gráfico, cómo crear un objeto de rectángulo lleno y otras funciones"
}
</script>
## Qué es Graph

Agregar gráficos a documentos PDF es una tarea muy común para los desarrolladores mientras trabajan con Adobe Acrobat Writer u otras aplicaciones de procesamiento de PDF. Existen muchos tipos de gráficos que se pueden usar en aplicaciones PDF.
[Aspose.PDF for .NET](/pdf/es/net/) también admite la adición de gráficos a documentos PDF. Para este propósito, se proporciona la clase Graph. Graph es un elemento a nivel de párrafo y se puede agregar a la colección Paragraphs en una instancia de Page. Una instancia de Graph contiene una colección de Shapes.

Los siguientes tipos de formas son compatibles con la clase [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/es/net/add-arc/) - a veces también llamado bandera es un par ordenado de vértices adyacentes, pero a veces también llamado línea dirigida.
- [Circle](/pdf/es/net/add-circle/) - muestra datos utilizando un círculo dividido en sectores. Usamos un gráfico circular (también llamado gráfico de pastel) para mostrar cómo los datos representan porciones de un todo o un grupo.
- [Curve](/pdf/es/net/add-curve/) - es una unión conectada de líneas proyectivas, cada línea se encuentra con otras tres en puntos dobles ordinarios.
- [Curva](/pdf/es/net/add-curve/) - es una unión conectada de líneas proyectivas, cada línea se encuentra con otras tres en puntos dobles ordinarios.
- [Línea](/pdf/es/net/add-line) - los gráficos de líneas se utilizan para mostrar datos continuos y pueden ser útiles para predecir eventos futuros cuando muestran tendencias a lo largo del tiempo.
- [Rectángulo](/pdf/es/net/add-rectangle/) - es una de las muchas formas fundamentales que verás en los gráficos, puede ser muy útil para ayudarte a resolver un problema.
- [Elipse](/pdf/es/net/add-ellipse/) - es un conjunto de puntos en un plano, creando una forma ovalada y curvada.

Los detalles anteriores también están representados en las figuras a continuación:

![Figuras en Gráficos](graphs.png)

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

