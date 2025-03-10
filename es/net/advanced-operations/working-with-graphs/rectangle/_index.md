---
title: Agregar objeto Rectángulo a archivo PDF
linktitle: Agregar Rectángulo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/add-rectangle/
description: Este artículo explica cómo crear un objeto Rectángulo en su PDF utilizando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "La nueva función en Aspose.PDF for .NET permite a los usuarios agregar objetos Rectángulo a documentos PDF sin problemas. Esta funcionalidad incluye opciones para personalizar los rectángulos con colores sólidos, rellenos degradados y transparencia, ofreciendo una mejor personalización visual y control de capas para el contenido PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artículo explica cómo crear un objeto Rectángulo en su PDF utilizando Aspose.PDF for .NET."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar objeto Rectángulo

Aspose.PDF for .NET admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tiene la ventaja de agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) donde también ofrece la función de rellenar el objeto rectángulo con un color determinado, controlar el Z-Order, agregar relleno de color degradado, etc.

Primero, veamos la posibilidad de crear un objeto Rectángulo.

Siga los pasos a continuación:

1. Cree un nuevo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF.
1. Agregue [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la colección de páginas del archivo PDF.
1. Agregue [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) a la colección de párrafos de la instancia de página.
1. Cree una instancia de [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).
1. Establezca el borde para el [Objeto de dibujo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing).
1. Cree una instancia de Rectángulo.

1. Agregue el objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) a la colección de formas del objeto Gráfico.
1. Agregue el objeto gráfico a la colección de párrafos de la instancia de página.
1. Agregue [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) a la colección de párrafos de la instancia de página.

1. Y guarde su archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![Crear Rectángulo](create_rectangle.png)

## Crear objeto Rectángulo relleno

Aspose.PDF for .NET también ofrece la función de rellenar el objeto rectángulo con un color determinado.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que está relleno de color.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

Mire el resultado del rectángulo relleno de color sólido:

![Rectángulo Relleno](fill_rectangle.png)

## Agregar Dibujo con Relleno Degradado

Aspose.PDF for .NET admite la función de agregar objetos gráficos a documentos PDF y, a veces, es necesario rellenar objetos gráficos con Color Degradado. Para rellenar objetos gráficos con Color Degradado, necesitamos establecer setPatterColorSpace con el objeto gradientAxialShading como sigue.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que está relleno con Color Degradado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![Rectángulo Degradado](gradient.png)

## Crear Rectángulo con canal de color alfa

Aspose.PDF for .NET admite rellenar el objeto rectángulo con un color determinado. Un objeto rectángulo también puede tener un canal de color alfa para dar una apariencia transparente. El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) con canal de color alfa.

Los píxeles de la imagen pueden almacenar información sobre su opacidad junto con el valor de color. Esto permite crear imágenes con áreas transparentes o semi-transparentes.

En lugar de hacer un color transparente, cada píxel almacena información sobre cuán opaco es. Estos datos de opacidad se llaman canal alfa y generalmente se almacenan después de los canales de color del píxel.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![Color de Canal Alfa del Rectángulo](rectangle_color.png)

## Controlar Z-Order del Rectángulo

Aspose.PDF for .NET admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. Al agregar más de una instancia del mismo objeto dentro del archivo PDF, podemos controlar su renderizado especificando el Z-Order. El Z-Order también se utiliza cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar objetos [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) uno encima del otro.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![Controlando Z Order](control.png)

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