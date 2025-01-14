---
title: Working with Vector Graphics
linktitle: Working with Vector Graphics
type: docs
weight: 120
url: /net/working-with-vector-graphics/
description: This article describes the features of working with GraphicsAbsorber tool using C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics in PDF",
    "alternativeHeadline": "Programmatically manipulate PDF vector graphics",
    "abstract": "Programmatically manipulate vector graphics in PDF documents using the new GraphicsAbsorber class. Aspose.PDF for .NET C# library allows for precise control over graphic elements, enabling actions like moving, removing, and adding graphics to enhance PDF visuals. The tool offers both individual and bulk manipulation methods for optimal performance",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "GraphicsAbsorber, Vector Graphics, PDF Manipulation, C# library, Aspose.PDF, Move Graphics, Remove Graphics, Add Graphics, PDF Vector Graphics",
    "wordcount": "967",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "This section describes the features of working with GraphicsAbsorber PDF file using C# library."
}
</script>

In this chapter, we'll explore how to use the powerful `GraphicsAbsorber` class to interact with vector graphics within PDF documents. Whether you need to move, remove, or add graphics, this guide will show you how to perform these tasks effectively. Let’s get started!

## Introduction<a name="introduction"></a>

Vector graphics are a crucial component of many PDF documents, used to represent images, shapes, and other graphical elements. Aspose.PDF provides the `GraphicsAbsorber` class, which allows developers to programmatically access and manipulate these graphics. By using the `Visit` method of `GraphicsAbsorber`, you can extract vector graphics from a specified page and perform various operations, such as moving, removing, or copying them to other pages.

## 1. Extracting Graphics with `GraphicsAbsorber`<a name="extracting-graphics"></a>

The first step in working with vector graphics is to extract them from a PDF document. Here’s how you can do it using the `GraphicsAbsorber` class:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UsingGraphicsAbsorber()
{
    // Path to the document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Step 1: Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Step 2: Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Step 3: Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}

```

### Explanation:

1. **Create a Document Object**: A new `Document` object is instantiated with the path to the target PDF file.
2. **Create an Instance of `GraphicsAbsorber`**: This class captures all graphics elements from a specified page.
3. **Visit Method**: The `Visit` method is called on the first page, allowing `GraphicsAbsorber` to absorb the vector graphics.
4. **Iterate Through Extracted Elements**: The code loops through each extracted element, printing information such as page number, position, and the number of drawing operators involved.

## 2. Moving Graphics<a name="moving-graphics"></a>

Once you have extracted the graphics, you can move them to a different position on the same page. Here’s how you can achieve this:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void MoveGraphics()
{
    // Path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Move graphics by shifting their X and Y coordinates
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "MoveGraphics_out.pdf");
        }
    }
}
```

### Key Points:

- **SuppressUpdate**: This method temporarily suspends updates to improve performance when making multiple changes.
- **ResumeUpdate**: This method resumes updates and applies changes made to the graphics' positions.
- **Element Positioning**: The position of each graphic is adjusted by changing its `X` and `Y` coordinates.

## 3. Removing Graphics<a name="removing-graphics"></a>

There are scenarios where you might want to remove specific graphics from a page. Aspose.PDF offers two methods to accomplish this:

### Method 1: Using Rectangle Boundary

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void RemoveGraphicsMethod1()
{
    // Path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suppress updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove those inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                if (rectangle.Contains(element.Position))
                {
                    element.Remove(); // Remove the graphic element
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### Method 2: Using a Collection of Removed Elements

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void RemoveGraphicsMethod2()
{
    // Path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection to store the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Iterate through the extracted elements and add those inside the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the graphics elements from the page
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### Explanation:

- **Rectangle Boundary**: Define a rectangle area to specify which graphics to remove.
- **Suppress and Resume Updates**: Ensure efficient removal without intermediate rendering.

## 4. Adding Graphics to Another Page<a name="adding-graphics"></a>

Graphics absorbed from one page can be added to another page within the same document. Here are two methods to achieve this:

### Method 1: Adding Graphics Individually

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddToAnotherPageMethod1()
{
    // Path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### Method 2: Adding Graphics as a Collection

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddToAnotherPageMethod2()
{
    // Path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics elements to the second page at once
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### Key Points:

- **SuppressUpdate and ResumeUpdate**: These methods help in maintaining performance while making bulk changes.
- **AddOnPage vs. AddGraphics**: Use `AddOnPage` for individual additions and `AddGraphics` for bulk additions.

## Conclusion

In this chapter, we explored how to use the `GraphicsAbsorber` class to extract, move, remove, and add vector graphics within PDF documents using Aspose.PDF. By mastering these techniques, you can significantly enhance the visual presentation of your PDFs and create dynamic, visually appealing documents.

Feel free to experiment with the code examples and adapt them to your specific use cases. Happy coding!

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
