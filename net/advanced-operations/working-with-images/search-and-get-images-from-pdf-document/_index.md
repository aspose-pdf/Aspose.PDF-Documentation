---
title: Search and Get Images from PDF Document
linktitle: Search and Get Images
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: This section explain how to search and get images from PDF document with Aspose.PDF library.
lastmod: "2021-01-27"
---

The ImagePlacementAbsorber allows you to search among images on all pages in a PDF document.

To search a whole document for images:

1. Call the Pages collection’s Accept method. The Accept method takes an ImagePlacementAbsorber object as a parameter. This returns a collection of ImagePlacement objects.
1. Loop through the ImagePlacements objects and get their properties (Image, dimensions, resolution and so on).

The following code snippet shows how to search a document for all its images.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Create ImagePlacementAbsorber object to perform image placement search
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Accept the absorber for all the pages
doc.Pages.Accept(abs);

// Loop through all ImagePlacements, get image and ImagePlacement Properties
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Get the image using ImagePlacement object
    XImage image = imagePlacement.Image;

    // Display image placement properties for all placements
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);
}
```

To get an image from an individual page, use the following code:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
```
