---
title: Working with Vector Graphics
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /net/working-with-vector-graphics/
description: This article describes the features of working with GraphicsAbsorber tool using C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics",
    "alternativeHeadline": "Enhance PDF Graphics Manipulation with С№",
    "abstract": "Discover the advanced capabilities of the GraphicsAbsorber tool in Aspose.PDF for .NET, allowing developers to seamlessly manipulate vector graphics in PDF documents. This feature enables precise extraction, movement, and removal of graphics, as well as the ability to add them to different pages, enhancing your PDF manipulation workflow with greater flexibility and control",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "889",
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

In this chapter, we'll explore how to use the powerful `GraphicsAbsorber` class to interact with vector graphics within PDF documents. Whether you need to move, remove, or add graphics, this guide will show you how to perform these tasks effectively.

## Introduction<a name="introduction"></a>

Vector graphics are a crucial component of many PDF documents, used to represent images, shapes, and other graphical elements. Aspose.PDF provides the `GraphicsAbsorber` class, which allows developers to programmatically access and manipulate these graphics. By using the `Visit` method of `GraphicsAbsorber`, you can extract vector graphics from a specified page and perform various operations, such as moving, removing, or copying them to other pages.

## Extracting Graphics with `GraphicsAbsorber`<a name="extracting-graphics"></a>

The first step in working with vector graphics is to extract them from a PDF document. Here’s how you can do it using the `GraphicsAbsorber` class:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UsingGraphicsAbsorber()
{
    // Step 1: The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Step 2: Open the document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Step 3: Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Step 4: Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Step 5: Display information about the extracted elements
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

1. **Create a Document Object**: A new `Document` object is instantiated with the path to the target PDF file.
2. **Create an Instance of `GraphicsAbsorber`**: This class captures all graphics elements from a specified page.
3. **Visit Method**: The `Visit` method is called on the first page, allowing `GraphicsAbsorber` to absorb the vector graphics.
4. **Iterate Through Extracted Elements**: The code loops through each extracted element, printing information such as page number, position, and the number of drawing operators involved.

## Moving Graphics<a name="moving-graphics"></a>

Once you have extracted the graphics, you can move them to a different position on the same page. Here’s how you can achieve this:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void MoveGraphics()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance using 'using' block
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Loop through each extracted graphic element and shift its position
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                // Move graphics by shifting its X and Y coordinates
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save the modified document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate**: This method temporarily suspends updates to improve performance when making multiple changes.
- **ResumeUpdate**: This method resumes updates and applies changes made to the graphics' positions.
- **Element Positioning**: The position of each graphic is adjusted by changing its `X` and `Y` coordinates.

## Removing Graphics<a name="removing-graphics"></a>

There are scenarios where you might want to remove specific graphics from a page. Aspose.PDF offers two methods to accomplish this:

### Method 1: Using Rectangle Boundary

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void RemoveGraphicsMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber using 'using' block
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suspend updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove elements inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                // Check if the graphic's position falls within the rectangle
                if (rectangle.Contains(element.Position))
                {
                    // Remove the graphic element
                    element.Remove();
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save the modified document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Method 2: Using a Collection of Removed Elements

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void RemoveGraphicsMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber using 'using' block
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection for the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Add elements within the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the selected graphic elements
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();
        }

        // Save the updated document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **Rectangle Boundary**: Define a rectangle area to specify which graphics to remove.
- **Suppress and Resume Updates**: Ensure efficient removal without intermediate rendering.

## Adding Graphics to Another Page<a name="adding-graphics"></a>

Graphics absorbed from one page can be added to another page within the same document. Here are two methods to achieve this:

### Method 1: Adding Graphics Individually

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddToAnotherPageMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance using 'using' block
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element from the first page to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page.
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save the updated document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Method 2: Adding Graphics as a Collection

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddToAnotherPageMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open document using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance using 'using' block
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics at once from the first page to the second page
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save the updated document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate and ResumeUpdate**: These methods help in maintaining performance while making bulk changes.
- **AddOnPage vs. AddGraphics**: Use `AddOnPage` for individual additions and `AddGraphics` for bulk additions.

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
