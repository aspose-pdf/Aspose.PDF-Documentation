---
title: Añadir objeto círculo al archivo PDF
linktitle: Añadir círculo
type: docs
weight: 20
url: es/net/add-circle/
description: Este artículo explica cómo crear un objeto círculo en tu PDF utilizando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir objeto círculo al archivo PDF",
    "alternativeHeadline": "Cómo crear un objeto círculo en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, círculo en pdf",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto círculo en tu PDF utilizando Aspose.PDF para .NET."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Añadir objeto Circle

Como los gráficos de barras, los gráficos circulares se pueden utilizar para mostrar datos en una serie de categorías separadas. Sin embargo, a diferencia de los gráficos de barras, los gráficos circulares solo se pueden utilizar cuando tienes datos para todas las categorías que componen el todo. Así que vamos a ver cómo añadir un objeto [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) con Aspose.PDF para .NET.

Sigue los pasos a continuación:

1. Crear instancia de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Crear [objeto de dibujo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) con ciertas dimensiones

1. Establecer [Borde](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para el objeto de dibujo

1. Añadir objeto [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF

```csharp
        public static void Circle()
        {
            // Crear instancia de Document
            var document = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto de dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Establecer borde para el objeto de dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Añadir objeto Graph a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
Nuestro círculo dibujado se verá así:

![Dibujo de Círculo](drawing_circle.png)

## Crear Objeto de Círculo Rellenado

Este ejemplo muestra cómo agregar un objeto Círculo que está relleno de color.

```csharp
        public static void CircleFilled()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto de Dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Establecer borde para el objeto de Dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Círculo");

            graph.Shapes.Add(circle);

            // Añadir objeto de Grafo a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
Veamos el resultado de agregar un Círculo lleno:

![Círculo Lleno](filled_circle.png)

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

