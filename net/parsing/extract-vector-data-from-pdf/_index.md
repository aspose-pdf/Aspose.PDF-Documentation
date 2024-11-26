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
                "telephone": "\u002B1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B61 2 8006 6987",
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
// Creates a new Document object using the provided input data.
var document = new Document(input);

// Instantiates a new GraphicsAbsorber object to process graphic elements. 
var grAbsorber = new GraphicsAbsorber(); 

// Visits the second page of the document to extract graphic elements. 
grAbsorber.Visit(document.Pages[1]); 

// Retrieves the list of graphic elements from the GraphicsAbsorber. 
var elements = grAbsorber.Elements; 

// Accesses the operators associated with the second graphic element. 
var operations = elements[1].Operators; 

// Retrieves the rectangle associated with the second graphic element. 
var rectangle = elements[1].Rectangle; 

// Gets the position of the second graphic element. 
var position = elements[1].Position;
```

## Extract Vector Data from PDF document

For extraction of Vector Data from PDF, we can use SVG extractor:

```csharp
var document = new Document(input);
document.Pages[1].TrySaveVectorGraphics(outputSvg);
```

### Extract all subpaths to images separately

```csharp
SvgExtractionOptions options = new SvgExtractionOptions
{
    ExtractEverySubPathToSvg = true
};

SvgExtractor extractor = new SvgExtractor(options);
extractor.Extract(page, svgDirPath);
```

### Extract list of elements to single image

```csharp
List<GraphicElement> elements = new List<GraphicElement>();
// Fill elements list needed graphic elements.
SvgExtractor svgExtractor = new SvgExtractor();
svgExtractor.Extract(elements, page, Path.Combine(svgDirPath, "1.svg"));
```

### Extract single element

```csharp
GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
graphicsAbsorber.Visit(page);
XFormPlacement xFormPlacement = graphicsAbsorber.Elements[1] as XFormPlacement;
xFormPlacement.Elements[2].SaveToSvg(page, Path.Combine(svgDirPath,"1.svg"));
```