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

## Access to Vector Data from PDF document

Since the the 24.2 release, Aspose.PDF for .NET library allows vector data extraction from a PDF file.
The next code snippet creates a new Document object using some input data, initializes a 'GraphicsAbsorber'(the GraphicsAbsorber returns the vector data) to handle graphic elements, and then visits the second page of the document to extract and analyze these elements.
It retrieves various properties of the second graphic element, such as its associated operators, rectangle, and position.

```csharp
// Creates a new Document object using the provided input data.
var doc = new Document(input);

// Instantiates a new GraphicsAbsorber object to process graphic elements. 
var grAbsorber = new GraphicsAbsorber(); 

// Visits the second page of the document to extract graphic elements. 
grAbsorber.Visit(doc.Pages[1]); 

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
var doc = new Document(input);
doc.Pages[1].TrySaveVectorGraphics(outputSvg);
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