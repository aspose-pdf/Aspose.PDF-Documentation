---
title: Cambiar el tamaño de página de PDF con C#
linktitle: Cambiar el tamaño de página de PDF
type: docs
weight: 40
url: es/net/change-page-size/
description: Cambiar el tamaño de página de su documento PDF utilizando la biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cambiar el tamaño de página de PDF con C#",
    "alternativeHeadline": "Redimensionar página de PDF con .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, cambiar tamaño de pdf, redimensionar pdf",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Cambiar el tamaño de página de su documento PDF utilizando la biblioteca Aspose.PDF para .NET."
}
</script>

## Cambiar el Tamaño de Página de PDF

Aspose.PDF para .NET le permite cambiar el tamaño de página de PDF con simples líneas de código en sus aplicaciones .NET. Este tema explica cómo actualizar/cambiar las dimensiones de página (tamaño) de un archivo PDF existente.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contiene el método SetPageSize(...) que le permite establecer el tamaño de la página. El fragmento de código a continuación actualiza las dimensiones de la página en unos pocos pasos fáciles:

1. Cargar el archivo PDF fuente.
1. Obtener las páginas en el objeto [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Obtener una página dada.
1. Llamar al método SetPageSize(..) para actualizar sus dimensiones.
1. Llamar al método Save(..) de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) para generar el archivo PDF con dimensiones de página actualizadas.

{{% alert color="primary" %}}

Tenga en cuenta que las propiedades de altura y anchura utilizan puntos como unidad básica, donde 1 pulgada = 72 puntos y 1 cm = 1/2.54 pulgadas = 0.3937 pulgadas = 28.3 puntos.
Tenga en cuenta que las propiedades de altura y anchura utilizan puntos como unidad básica, donde 1 pulgada = 72 puntos y 1 cm = 1/2.54 pulgadas = 0.3937 pulgadas = 28.3 puntos.

{{% /alert %}}

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## Obtener tamaño de página PDF

Puede leer el tamaño de página de un archivo PDF existente usando Aspose.PDF para .NET. El siguiente ejemplo de código muestra cómo leer las dimensiones de la página PDF usando C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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
Sure, I just need you to provide the document or the content that you want to translate into Spanish. Please paste the text here, and I'll help you with the translation while preserving the original markdown formatting.
