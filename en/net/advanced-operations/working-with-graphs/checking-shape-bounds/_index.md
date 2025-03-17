---
title: Check shape bounds in Shapes collection
type: docs
weight: 70
url: /net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Learn how to check the bounds of an shape when inserted into the Shapes collection to ensure it fits within its parent container.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Aspose.PDF for .NET's new bounds-checking feature in the `Drawing.Graph.Shapes` collection automatically validates element dimensions against parent containers, preventing layout overflow. It triggers exceptions when elements exceed container limits, enforcing strict size constraints during insertion to ensure precise PDF formatting and streamline design accuracy",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1000",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-02-28",
    "description": ""
}
</script>

## Introduction
This document provides a detailed guide on using the bounds-checking feature in the Shapes collection. This feature ensures that elements fit within their parent container and can be configured to throw an exception if the component does not fit. We will walk through the steps to implement this functionality and provide a complete example.

## Prerequisites
You will need the following:
* Visual Studio 2019 or later
* Aspose.PDF for .NET 25.3 or later
* A sample PDF file that contains some pages

You can download the Aspose.PDF for .NET library from the official website or install it using the NuGet Package Manager in Visual Studio.

## Steps
Here are the steps to complete the task:
1. Create a new document and add a page.
2. Create a `Graph` object with specified dimensions.
3. Create a `Shape` object with specified dimensions.
4. Set the `BoundsCheckMode` to `ThrowExceptionIfDoesNotFit`.
5. Attempt to add the shape to the graph.

Let's see how to implement these steps in C# code.

### Step 1: Create a New Document and Add a Page
First, create a new PDF document and add a page to it.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Step 2: Create a Graph Object with Specified Dimensions
Next, create a `Graph` object with a width and height of 100 units. Position the graph 10 units from the top and 15 units from the left of the page. Add a black border to the graph.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Step 3: Create an Shape object (for example, Rectangle) with specified dimensions
Create a Rectangle object with a width and height of 50 units. Position the rectangle at (-1, 0), which is outside the bounds of the graph.

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Step 4: Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
Set the `BoundsCheckMode` to `ThrowExceptionIfDoesNotFit` to ensure that an exception is thrown if the rectangle does not fit within the graph.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Step 5: Attempt to Add the Rectangle to the Graph
Attempt to add the rectangle to the graph. This will throw an `Aspose.Pdf.BoundsOutOfRangeException` because the rectangle does not fit within the graph's dimensions.

```csharp
graph.Shapes.Add(rect);
```

## Output
After executing the code, the expected output will be an `Aspose.Pdf.BoundsOutOfRangeException` with the message:

```
Bounds not fit. Container dimensions: 100x100
```

## Troubleshooting
In case of issues, here are a few tips:
* Ensure that the `BoundsCheckMode` is set correctly.
* Verify that the dimensions of the element and the container are accurate.
* Check the positioning of the element within the container.

## Complete Example
Below is a complete example demonstrating all the steps combined:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusion
The bounds-checking feature in the Shapes collection is a powerful tool for ensuring elements fit within parent containers. You can prevent layout issues in your PDF documents by setting the BoundsCheckMode to ThrowExceptionIfDoesNotFit. This feature is particularly useful in scenarios where precise element positioning and sizing are critical. For further details, visit the [official documentation](https://docs.aspose.com/pdf/net/).
