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

## Extract Vector Data from PDF document

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

