---
title:  Extract Vector Data from a PDF file using C#
linktitle:  Extract Vector Data from PDF
type: docs
weight: 80
url: /net/extract-vector-data-from-pdf/
description: Aspose.PDF makes it easy to extract vector data from a PDF file. You can get the vector data (path, polygon, polyline), such as position, color, linewidth, etc.
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
    "abstract": "Aspose.PDF for .NET now offers an innovative feature that enables users to seamlessly extract vector data from PDF files. This functionality includes detailed access to graphic elements, such as paths and polygons, along with their properties like position, color, and linewidth, empowering developers to handle vector graphics efficiently in their applications",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Access to Vector Data from PDF document

Since the the 24.2 release, Aspose.PDF for .NET library allows vector data extraction from a PDF file.
The next code snippet creates a new Document object using some input data, initializes a 'GraphicsAbsorber'(the GraphicsAbsorber returns the vector data) to handle graphic elements, and then visits the second page of the document to extract and analyze these elements.
It retrieves various properties of the second graphic element, such as its associated operators, rectangle, and position.

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

## Extract Vector Data from PDF document

For extraction of Vector Data from PDF, we can use SVG extractor:

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

### Extract all subpaths to images separately

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

        // Create SVG extractor using 'using' block
        var extractor = new Aspose.Pdf.Vector.SvgExtractor(options);
        // Extract SVGs from the page
        extractor.Extract(page, svgDirPath);
    }
}
```

### Extract list of elements to single image

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExtractListOfElementsToSingleImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Path to the directory where SVGs will be saved
    var svgDirPath = dataDir + "SvgOutput/";

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
        svgExtractor.Extract(elements, page, Path.Combine(svgDirPath, "VectorGraphics_out.svg"));
    }
}
```

### Extract single element

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExtractSingleElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Path to the directory where SVGs will be saved
    var svgDirPath = dataDir + "SvgOutput/";

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
        xFormPlacement.Elements[2].SaveToSvg(Path.Combine(svgDirPath, "VectorGraphics_out.svg"));
    }
}
```