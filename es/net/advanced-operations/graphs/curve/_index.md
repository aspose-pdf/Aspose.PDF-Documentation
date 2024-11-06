---
title: Añadir objeto curva al archivo PDF
linktitle: Añadir Curva
type: docs
weight: 30
url: es/net/add-curve/
description: Este artículo explica cómo crear un objeto curva en su PDF utilizando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir objeto curva al archivo PDF",
    "alternativeHeadline": "Cómo crear un objeto curva en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, .net, curva en pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto curva en su PDF utilizando Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Curve

Un gráfico [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) es una unión conectada de líneas proyectivas, cada línea se encuentra con otras tres en puntos dobles ordinarios.

Aspose.PDF para .NET muestra cómo usar curvas Bézier en tus gráficos.
Las curvas Bézier son ampliamente utilizadas en gráficos por computadora para modelar curvas suaves. La curva está completamente contenida en la envoltura convexa de sus puntos de control, los puntos pueden mostrarse gráficamente y usarse para manipular la curva de manera intuitiva.
La curva completa está contenida en el cuadrilátero cuyas esquinas son los cuatro puntos dados (su envoltura convexa).

En este artículo, investigaremos simplemente curvas de gráfico y curvas rellenas, que puedes crear en tu documento PDF.

Sigue los pasos a continuación:

1. Crea una instancia de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Establecer [Borde](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para el objeto Dibujo

1. Añadir objeto [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF

```csharp
 public static void ExampleCurve()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto Dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Establecer borde para el objeto Dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Añadir objeto Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
La siguiente imagen muestra el resultado ejecutado con nuestro fragmento de código:

![Dibujo de Curva](drawing_curve.png)

## Crear Objeto de Curva Rellena

Este ejemplo muestra cómo agregar un objeto Curva que está relleno de color.

```csharp
      public static void CurveFilled()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto Dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Establecer borde para el objeto Dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Agregar objeto Grafo a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
Mira el resultado de agregar una Curva Rellena:

![Curva Rellena](filled_curve.png)

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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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

