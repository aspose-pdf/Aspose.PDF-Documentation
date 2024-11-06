---
title: Añadir objeto Elipse a archivo PDF
linktitle: Añadir Elipse
type: docs
weight: 60
url: es/net/add-ellipse/
description: Este artículo explica cómo crear un objeto Elipse en tu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir objeto Elipse a archivo PDF",
    "alternativeHeadline": "Cómo crear un objeto Elipse en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, elipse en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación Aspose.PDF",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto Elipse en tu PDF usando Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Elipse

Aspose.PDF para .NET admite agregar objetos [Elipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) a documentos PDF. También ofrece la característica de llenar el objeto elipse con un cierto color.

```csharp
 public static void Ellipse()
        {
            // Crear instancia de Documento
            var document = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = document.Pages.Add();

            // Crear objeto Drawing con ciertas dimensiones
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Establecer borde para el objeto Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Elipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Elipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // Agregar objeto Graph a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![Agregar Elipse](ellipse.png)

## Crear Objeto de Elipse Rellena

El siguiente fragmento de código muestra cómo agregar un objeto [Elipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) que está relleno de color.

```csharp
     public static void EllipseFilled()
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

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // Agregar el objeto de Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar el archivo PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Filled Ellipse](fill_ellipse.png)

## Añadir Texto dentro del Elipse

Aspose.PDF para .NET permite añadir texto dentro del Objeto Gráfico. La propiedad de texto del Objeto Gráfico ofrece la opción de configurar el texto del Objeto Gráfico. El siguiente fragmento de código muestra cómo añadir texto dentro de un objeto Rectángulo.

```csharp
        public static void EllipseWithText()
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

            var textFragment = new TextFragment("Ellipse");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // Agregar objeto Gráfico a la colección de párrafos de la página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```

![Texto dentro de la elipse](text_ellipse.png)

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
```

