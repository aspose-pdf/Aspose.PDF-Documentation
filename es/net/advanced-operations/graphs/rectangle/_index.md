---
title: Agregar objeto Rectángulo al archivo PDF
linktitle: Agregar Rectángulo
type: docs
weight: 50
url: es/net/add-rectangle/
description: Este artículo explica cómo crear un objeto Rectángulo en su PDF utilizando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Agregar objeto Rectángulo al archivo PDF",
    "alternativeHeadline": "Cómo crear un objeto Rectángulo en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, rectángulo en pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo crear un objeto Rectángulo en su PDF utilizando Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Rectángulo

Aspose.PDF para .NET soporta la característica de añadir objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tienes la ventaja de añadir un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) donde también se ofrece la característica de llenar el objeto rectángulo con un cierto color, controlar el Z-Order, añadir relleno de color gradiente y etc.

Primero, veamos la posibilidad de crear un objeto Rectángulo.

Sigue los pasos a continuación:

1. Crea un nuevo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF

1. Añade [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la colección de páginas del archivo PDF

1. Añade [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) a la colección de párrafos de la instancia de página

1. Crea una instancia de [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. Crear instancia de Rectángulo

1. Añadir objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) a la colección de formas del objeto Gráfico

1. Añadir objeto gráfico a la colección de párrafos de la instancia de página

1. Añadir [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) a la colección de párrafos de la instancia de página

1. Y guardar tu archivo PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Crear objeto gráfico con dimensiones igual a las especificadas para el objeto Rectángulo
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Podemos cambiar la posición de la instancia del gráfico
                IsChangePosition = false,
                // Establecer la posición de coordenada Izquierda para la instancia del Gráfico
                Left = x,
                // Establecer la posición de coordenada Superior para el objeto Gráfico
                Top = y
            };
            // Añadir un rectángulo dentro del "gráfico"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Establecer el color de relleno del rectángulo
            rect.GraphInfo.FillColor = color;
            // Color del objeto gráfico
            rect.GraphInfo.Color = color;
            // Añadir rectángulo a la colección de formas de la instancia del gráfico
            graph.Shapes.Add(rect);
            // Establecer Z-Índice para el objeto rectángulo
            graph.ZIndex = zindex;
            // Añadir gráfico a la colección de párrafos del objeto de página
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## Crear Objeto de Rectángulo Lleno

Aspose.PDF para .NET también ofrece la característica de llenar un objeto rectángulo con un color determinado.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que está lleno de color.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Agregar objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);

            // Crear instancia de Rectángulo
            var rect = new Rectangle(100, 100, 200, 120);

            // Especificar color de relleno para el objeto Gráfico
            rect.GraphInfo.FillColor = Color.Red;

            // Agregar objeto rectángulo a la colección de formas del objeto Gráfico
            graph.Shapes.Add(rect);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
Mire el resultado de un rectángulo lleno de color sólido:

![Rectángulo lleno](fill_rectangle.png)

## Agregar dibujo con relleno degradado

Aspose.PDF para .NET admite la característica de agregar objetos gráficos a documentos PDF y a veces es necesario llenar objetos gráficos con Color Degradado. Para llenar objetos gráficos con Color Degradado, necesitamos configurar setPatterColorSpace con el objeto gradientAxialShading como sigue.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que está lleno de Color Degradado.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Agregar objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);
            // Crear instancia de Rectángulo
            var rect = new Rectangle(0, 0, 300, 300);
            // Especificar color de relleno para el objeto Gráfico
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Agregar objeto rectángulo a la colección de formas del objeto Gráfico
            graph.Shapes.Add(rect);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectángulo degradado](gradient.png)

## Crear rectángulo con canal alfa de color

Aspose.PDF para .NET admite llenar el objeto rectángulo con un color determinado. Un objeto rectángulo también puede tener un canal de color Alfa para dar apariencia transparente. El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) con canal de color Alfa.

Los píxeles de la imagen pueden almacenar información sobre su opacidad junto con el valor del color. Esto permite crear imágenes con áreas transparentes o semitransparentes.

En lugar de hacer un color transparente, cada píxel almacena información sobre cuán opaco es. Estos datos de opacidad se llaman canal alfa y generalmente se almacenan después de los canales de color del píxel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Agregar objeto graph a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);
            // Crear instancia de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);
            // Especificar color de relleno para el objeto Graph
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Agregar objeto rectángulo a la colección de formas del objeto Graph
            graph.Shapes.Add(rect);

            // Crear segundo objeto rectángulo
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Agregar instancia de graph a la colección de párrafos del objeto de página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## Controlar el Orden Z de Rectángulo

Aspose.PDF para .NET soporta la característica de añadir objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. Al añadir más de una instancia del mismo objeto dentro de un archivo PDF, podemos controlar su renderización especificando el Orden Z. El Orden Z también se usa cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) uno encima del otro.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instanciar objeto de la clase Document
            Document doc1 = new Document();
            /// Añadir página a la colección de páginas del archivo PDF
            Page page1 = doc1.Pages.Add();
            // Establecer tamaño de la página PDF
            page1.SetPageSize(375, 300);
            // Establecer margen izquierdo del objeto página como 0
            page1.PageInfo.Margin.Left = 0;
            // Establecer margen superior del objeto página como 0
            page1.PageInfo.Margin.Top = 0;
            // Crear un nuevo rectángulo con Color como Rojo, Orden Z como 0 y ciertas dimensiones
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Crear un nuevo rectángulo con Color como Azul, Orden Z como 0 y ciertas dimensiones
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Crear un nuevo rectángulo con Color como Verde, Orden Z como 0 y ciertas dimensiones
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Guardar el archivo PDF resultante
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Controlando el Orden Z](control.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
    "applicationCategory": "Biblioteca de Manipulación PDF para .NET",
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


