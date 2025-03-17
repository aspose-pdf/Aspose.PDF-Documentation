---
title: Trabajando con Gráficas en archivos PDF
linktitle: Trabajando con Gráficas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/working-with-graphs/
description: Este artículo explica qué es una Gráfica, cómo crear un objeto de rectángulo relleno y otras funciones
lastmod: "2022-02-17"
sitemap:
changefreq: "weekly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Descubre la poderosa nueva función para generar y manipular gráficas dentro de documentos PDF utilizando Aspose.PDF for .NET. Esta funcionalidad permite a los desarrolladores crear una variedad de formas de gráficas, incluyendo arcos, círculos, líneas y rectángulos, mejorando la presentación visual de los datos en sus aplicaciones. Optimiza tu proceso de generación de PDF y entrega visualizaciones de datos dinámicas con facilidad",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "335",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2025-03-17",
    "description": "Este artículo explica qué es una Gráfica, cómo crear un objeto de rectángulo relleno y otras funciones"
}
</script>

## ¿Qué es una Gráfica?

Agregar gráficas a documentos PDF es una tarea muy común para los desarrolladores al trabajar con Adobe Acrobat Writer u otras aplicaciones de procesamiento de PDF. Hay muchos tipos de gráficas que se pueden utilizar en aplicaciones PDF.
[Aspose.PDF for .NET](/pdf/net/) también admite la adición de gráficas a documentos PDF. Para este propósito, se proporciona la clase Gráfica. La Gráfica es un elemento a nivel de párrafo y se puede agregar a la colección de Párrafos en una instancia de Página. Una instancia de Gráfica contiene una colección de Formas.

Los siguientes tipos de formas son compatibles con la clase [Gráfica](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/graph):

- [Arco](/pdf/es/net/add-arc/) - a veces también llamado una bandera, es un par ordenado de vértices adyacentes, pero a veces también se llama una línea dirigida.
- [Círculo](/pdf/es/net/add-circle/) - muestra datos utilizando un círculo dividido en sectores. Usamos un gráfico circular (también llamado gráfico de pastel) para mostrar cómo los datos representan porciones de un todo o un grupo.
- [Curva](/pdf/es/net/add-curve/) - es una unión conectada de líneas proyectivas, cada línea se encuentra con tres otras en puntos dobles ordinarios.
- [Línea](/pdf/es/net/add-line) - los gráficos de líneas se utilizan para mostrar datos continuos y pueden ser útiles para predecir eventos futuros cuando muestran tendencias a lo largo del tiempo.
- [Rectángulo](/pdf/es/net/add-rectangle/) - es una de las muchas formas fundamentales que verás en gráficas, puede ser muy útil para ayudarte a resolver un problema.
- [Elipse](/pdf/es/net/add-ellipse/) - es un conjunto de puntos en un plano, creando una forma ovalada y curva.

Las siguientes operaciones son compatibles con los tipos de formas:
- [Verificar límites](/pdf/es/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - verificar los límites de la forma en la colección de Formas.

Los detalles anteriores también se representan en las figuras a continuación:

![Figuras en Gráficas](graphs.png)

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