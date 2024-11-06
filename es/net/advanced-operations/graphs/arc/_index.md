---
title: Añadir objeto Arco al archivo PDF
linktitle: Añadir Arco
type: docs
weight: 10
url: es/net/add-arc/
description: Este artículo explica cómo crear un objeto arco en tu PDF utilizando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir objeto Arco al archivo PDF",
    "alternativeHeadline": "Cómo crear un Arco en el archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, arco en pdf",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto arco en tu PDF utilizando Aspose.PDF para .NET."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Arco

Aspose.PDF para .NET soporta la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También ofrece la característica de llenar un objeto arco con un color determinado.

Siga los pasos a continuación:

1. Crear instancia de [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Crear [objeto de dibujo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) con ciertas dimensiones

1. Establecer [Borde](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para el objeto de dibujo

1. Agregar objeto [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF

El siguiente fragmento de código muestra cómo agregar un objeto [Arco](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto de dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Establecer borde para el objeto de dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // Agregar objeto Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## Crear Objeto de Arco Relleno

El siguiente ejemplo muestra cómo agregar un objeto Arco que está relleno con color y ciertas dimensiones.

```csharp
        public static void ArcFilled()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto de Dibujo con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Establecer borde para el objeto de Dibujo
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // Agregar objeto de Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
Veamos el resultado de agregar un arco lleno:

![Arco Lleno](filled_arc.png)

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

