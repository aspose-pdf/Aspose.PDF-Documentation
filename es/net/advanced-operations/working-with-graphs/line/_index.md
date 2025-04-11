---
title: Agregar objeto de línea a archivo PDF
linktitle: Agregar línea
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/add-line/
description: Este artículo explica cómo crear un objeto de línea en su PDF utilizando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Line Object to PDF file",
    "alternativeHeadline": "Enhance PDFs with Custom Line Objects Using .NET",
    "abstract": "Mejore sus documentos PDF agregando sin problemas objetos de línea con Aspose.PDF for .NET. Esta nueva funcionalidad permite un control preciso sobre los atributos de la línea, incluidos los patrones de guiones y colores, lo que permite a los usuarios crear representaciones gráficas visualmente atractivas dentro de sus archivos PDF. Descubra cómo implementar esta función fácilmente con ejemplos de código completos e instrucciones claras paso a paso.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Line Object, PDF manipulation, Aspose.PDF for .NET, Line object, Drawing in PDF, Graph object, Rectangle in PDF, Dotted Dashed Line, Draw Line Across the Page, PDF document generation",
    "wordcount": "729",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artículo explica cómo crear un objeto de línea en su PDF utilizando Aspose.PDF for .NET."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Agregar objeto de línea

Aspose.PDF for .NET admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tiene la ventaja de agregar un objeto [Línea](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/line) donde también puede especificar el patrón de guiones, el color y otros formatos para el elemento Línea.

Siga los pasos a continuación:

1. Cree un nuevo [Documento](https://reference.aspose.com/pdf/es/net/aspose.pdf/document) PDF.
1. Agregue una [Página](https://reference.aspose.com/pdf/es/net/aspose.pdf/page) a la colección de páginas del archivo PDF.
1. Cree una instancia de [Gráfico](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/graph).
1. Agregue el objeto Gráfico a la colección de párrafos de la instancia de página.
1. Cree una instancia de [Rectángulo](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/rectangle).
1. Establezca el ancho de la línea.
1. Agregue el objeto [Rectángulo](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/rectangle) a la colección de formas del objeto Gráfico.

1. Guarde su archivo PDF.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/es/net/aspose.pdf.drawing/rectangle) que está relleno de color.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineObjectToPDF()
{
    // The path to the document directory
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

        // Create Line instance with specified coordinates
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Specify dash settings for the line
        line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
        line.GraphInfo.DashPhase = 1;

        // Add line object to shapes collection of Graph object
        graph.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "AddLineObject_out.pdf");
    }
}
```

![Agregar línea](add_line.png)

## Cómo agregar una línea punteada a su documento PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DashLengthInBlackAndDashLengthInWhite()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add drawing object to paragraphs collection of page instance
        page.Paragraphs.Add(canvas);

        // Create Line object
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Set color for Line object
        line.GraphInfo.Color = Aspose.Pdf.Color.Red;

        // Specify dash array for line object
        line.GraphInfo.DashArray = new int[] { 3, 2 }; // Dash and gap lengths in points

        // Set the dash phase for Line instance
        line.GraphInfo.DashPhase = 1;

        // Add line to shapes collection of drawing object
        canvas.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
    }
}
```

Veamos el resultado:

![Línea punteada](dash_line.png)

## Dibujar línea a través de la página

También podemos usar el objeto línea para dibujar una cruz comenzando desde la esquina inferior izquierda hasta la esquina superior derecha y desde la esquina superior izquierda hasta la esquina inferior derecha.

Por favor, eche un vistazo al siguiente fragmento de código para cumplir con este requisito.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleLineAcrossPage()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set page margin on all sides as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;

        // Create Graph object with Width and Height equal to page dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(
            (float)page.PageInfo.Width,
            (float)page.PageInfo.Height);

        // Create first line object starting from Lower-Left to Top-Right corner of page
        var line1 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            (float)page.Rect.LLX, 0,
            (float)page.PageInfo.Width,
            (float)page.Rect.URY
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line1);

        // Create second line object starting from Top-Left corner to Bottom-Right corner of page
        var line2 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            0, (float)page.Rect.URY,
            (float)page.PageInfo.Width, (float)page.Rect.LLX
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "ExampleLineAcrossPage_out.pdf");
    }
}
```

![Dibujando línea](draw_line.png)

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