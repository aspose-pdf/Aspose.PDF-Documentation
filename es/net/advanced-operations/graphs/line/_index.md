---
title: Agregar objeto de línea al archivo PDF
linktitle: Agregar línea
type: docs
weight: 40
url: es/net/add-line/
description: Este artículo explica cómo crear un objeto de línea en su PDF utilizando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Agregar objeto de línea al archivo PDF",
    "alternativeHeadline": "Cómo crear un objeto de línea en el archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, línea en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de documentación de Aspose.PDF",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto de línea en su PDF utilizando Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Linea

Aspose.PDF para .NET soporta la característica de añadir objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tienes la ventaja de añadir un objeto [Line](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) donde puedes especificar el patrón de guiones, color y otros formatos para el elemento Linea.

Sigue los pasos a continuación:

1. Crea un nuevo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF

1. Añade [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la colección de páginas del archivo PDF

1. Crea una instancia de [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. Añade el objeto Gráfico a la colección de párrafos de la instancia de página.

1. Crea una instancia de [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. Establece el ancho de línea.
1. Guarde su archivo PDF.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que está lleno de color.

```csharp
        public static void AddLineObjectToPDF()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear instancia de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Agregar objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);

            // Crear instancia de Rectángulo
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Especificar color de relleno para el objeto Gráfico
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // Agregar objeto rectángulo a la colección de formas del objeto Gráfico
            graph.Shapes.Add(line);

            // Guardar archivo PDF
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## Cómo agregar una línea de puntos y guiones a tu documento PDF

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto de Dibujo con ciertas dimensiones
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Agregar objeto de dibujo a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(canvas);

            // Crear objeto Línea
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Establecer color para el objeto Línea
            line.GraphInfo.Color = Color.Red;
            // Especificar arreglo de guiones para el objeto línea
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Establecer la fase de guión para la instancia de Línea
            line.GraphInfo.DashPhase = 1;
            // Agregar línea a la colección de formas del objeto de dibujo
            canvas.Shapes.Add(line);
            // Guardar archivo PDF
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
![Línea Discontinua](dash_line.png)

## Dibujar una Línea a Través de la Página

También podemos usar el objeto de línea para dibujar una cruz que comience desde la esquina Inferior-Izquierda hasta la esquina Superior-Derecha y desde la esquina Superior-Izquierda hasta la esquina Inferior-Derecha.

Por favor, revise el siguiente fragmento de código para cumplir con este requisito.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // Crear instancia de Documento
            var document = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();
            // Establecer el margen de la página en todos los lados como 0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // Crear objeto Gráfico con Ancho y Alto igual a las dimensiones de la página
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // Crear el primer objeto de línea que comienza desde la esquina Inferior-Izquierda hasta la esquina Superior-Derecha de la página
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // Añadir línea a la colección de formas del objeto Gráfico
            graph.Shapes.Add(line);
            // Dibujar línea desde la esquina Superior-Izquierda de la página hasta la esquina Inferior-Derecha de la página
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // Añadir línea a la colección de formas del objeto Gráfico
            graph.Shapes.Add(line2);

            // Añadir objeto Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Dibujo de línea](draw_line.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para biblioteca .NET",
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
    "applicationCategory": "Biblioteca de manipulación PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/crear-documento-pdf/captura-de-pantalla.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


