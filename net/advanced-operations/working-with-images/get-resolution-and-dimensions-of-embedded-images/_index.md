---
title: Get Resolution and Dimensions of Images
linktitle: Get Resolution and Dimensions
type: docs
weight: 40
url: /net/get-resolution-and-dimensions-of-embedded-images/
description: This section shows details in getting resolution and dimensions of Embedded Images
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "How to get Resolution and Dimensions of Embedded Images",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, get resolution, get dimensions",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "This section shows details in getting resolution and dimensions of Embedded Images"
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

This topic explains how to use the operator classes in the Aspose.PDF namespace which provide the capability to get resolution and dimension information about images without having to extract them.

There are different ways of achieving this. This article explains how to use an `arraylist` and [image placement classes](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. First, load the source PDF file (with images).
1. Then create an ArrayList object to hold the names of any images in the document.
1. Get the images using the Page.Resources.Images property.
1. Create a stack object to hold the image's graphics state and use it to keep track of different image states.
1. Create a ConcatenateMatrix object which defines current transformation. It also supports scaling, rotating, and skewing any content. It concatenates the new matrix with previous one. Please note that we cannot define the transformation from scratch but only modify the existing transformation.
1. Because we can modify the matrix with ConcatenateMatrix, we may also need to revert back to the original image state. Use GSave and GRestore operators. These operators are paired so they should be called together. For example, if you do some graphics work with complex transformations and finally return transformations back to initial state, the approach will be something like this:

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

As a result, text is drawn in regular form but some transformations are performed between the text operators. In order to display the image or to draw form objects and images, we need to use the Do operator.

We also have a class named XImage which provides two properties,l Width and Height, which can be used to get image dimensions.

1. Perform some calculations to compute the image resolution.
1. Display the information in a Command Prompt along with the image name.

The following code snippet shows you how to get an image's dimensions and resolution without extracting the image from the PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Load the source PDF file
Document document = new Document(dataDir +  "ImageInformation.pdf");

// Define the default resolution for image
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Define array list object which will hold image names
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(document.Pages[1].Resources.Images.Names);
// Insert an object to stack
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Get all the operators on first page of document
foreach (Operator op in document.Pages[1].Contents)
{
    // Use GSave/GRestore operators to revert the transformations back to previously set
    Operators.GSave opSaveState = op as Operators.GSave;
    Operators.GRestore opRestoreState = op as Operators.GRestore;
    // Instantiate ConcatenateMatrix object as it defines current transformation matrix.
    Operators.ConcatenateMatrix opCtm = op as Operators.ConcatenateMatrix;
    // Create Do operator which draws objects from resources. It draws Form objects and Image objects
    Operators.Do opDo = op as Operators.Do;

    if (opSaveState != null)
    {
        // Save previous state and push current state to the top of the stack
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Throw away current state and restore previous one
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Multiply current matrix with the state matrix
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // In case this is an image drawing operator
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Create XImage object to hold images of first pdf page
            XImage image = document.Pages[1].Resources.Images[opDo.Name];

            // Get image dimensions
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Get Height and Width information of image
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Compute resolution based on above information
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Display Dimension and Resolution information of each image
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
```

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
