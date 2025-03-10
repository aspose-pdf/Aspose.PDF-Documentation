---
title: Extraer datos vectoriales de un archivo PDF usando C#
linktitle: Extraer datos vectoriales de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /es/net/extract-vector-data-from-pdf/
description: Aspose.PDF facilita la extracción de datos vectoriales de un archivo PDF. Puedes obtener los datos vectoriales (ruta, polígono, polilínea), como posición, color, ancho de línea, etc.
lastmod: "2024-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Vector Data from a PDF file using C#",
    "alternativeHeadline": "Effortless Vector Data Extraction from PDF with C#",
    "abstract": "Aspose.PDF for .NET ahora ofrece una función innovadora que permite a los usuarios extraer sin problemas datos vectoriales de archivos PDF. Esta funcionalidad incluye acceso detallado a elementos gráficos, como rutas y polígonos, junto con sus propiedades como posición, color y ancho de línea, empoderando a los desarrolladores para manejar gráficos vectoriales de manera eficiente en sus aplicaciones",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "361",
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
    "url": "/net/extract-vector-data-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-vector-data-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Acceso a datos vectoriales desde el documento PDF

Desde la versión 24.2, la biblioteca Aspose.PDF for .NET permite la extracción de datos vectoriales de un archivo PDF. 
El siguiente fragmento de código crea un nuevo objeto Document utilizando algunos datos de entrada, inicializa un 'GraphicsAbsorber' (el GraphicsAbsorber devuelve los datos vectoriales) para manejar elementos gráficos, y luego visita la segunda página del documento para extraer y analizar estos elementos. 
Recupera varias propiedades del segundo elemento gráfico, como sus operadores asociados, rectángulo y posición.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ProcessGraphicsInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate a new GraphicsAbsorber object to process graphic elements
        using (var grAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Visit the second page of the document to extract graphic elements
            grAbsorber.Visit(document.Pages[1]);

            // Retrieve the list of graphic elements from the GraphicsAbsorber
            var elements = grAbsorber.Elements;

            // Access the operators associated with the second graphic element
            var operations = elements[1].Operators;

            // Retrieve the rectangle associated with the second graphic element
            var rectangle = elements[1].Rectangle;

            // Get the position of the second graphic element
            var position = elements[1].Position;
        }
    }
}
```

## Extraer datos vectoriales del documento PDF

Para la extracción de datos vectoriales de PDF, podemos usar el extractor SVG:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveVectorGraphicsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Save vector graphics from the first page to an SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "VectorGraphics_out.svg");
    }
}
```

### Extraer todos los subcampos a imágenes por separado

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAllSubpathsToImagesSeparately()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Path to the directory where SVGs will be saved
    var svgDirPath = dataDir + "SvgOutput/";

    // Create extraction options
    var options = new Aspose.Pdf.Vector.SvgExtractionOptions
    {
        ExtractEverySubPathToSvg = true
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Create SVG extractor
        var extractor = new Aspose.Pdf.Vector.SvgExtractor(options);
        // Extract SVGs from the page
        extractor.Extract(page, svgDirPath);
    }
}
```

### Extraer lista de elementos a una sola imagen

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractListOfElementsToSingleImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Initialize the list of graphic elements
    var elements = new List<Aspose.Pdf.Vector.GraphicElement>();

    // Example: Fill elements list with needed graphic elements (implement your logic here)

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Use SvgExtractor to extract SVGs
        var svgExtractor = new Aspose.Pdf.Vector.SvgExtractor();

        // Extract SVGs from graphic elements on the page
        svgExtractor.Extract(elements, page, Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```

### Extraer un solo elemento

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSingleElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();


    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber object to extract graphic elements
        var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();

        // Get the first page of the document
        var page = document.Pages[1];

        // Process the page to extract graphic elements
        graphicsAbsorber.Visit(page);

        // Extract the graphic element (XFormPlacement) and save it as SVG
        var xFormPlacement = graphicsAbsorber.Elements[1] as Aspose.Pdf.Vector.XFormPlacement;
        xFormPlacement.Elements[2].SaveToSvg(Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```