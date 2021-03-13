---
title: Working with Image Placement
linktitle: Working with Image Placement
type: docs
weight: 50
url: /net/working-with-image-placement/
description: This section describes the features of working with image placement PDF file using C# library.
lastmod: "2021-01-27"
---

With the release of Aspose.PDF for .NET 7.0.0, we introduced classes called [ImagePlacement](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) and [ImagePlacementCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) which provide similar capability as the classes described above to get an image’s resolution and position in a PDF document.

- ImagePlacementAbsorber performs image usage search as the ImagePlacement objects collection.
- ImagePlacement provides the members Resolution and Rectangle that return actual image placement values.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();


// Load the source PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
           
// Load the contents of first page
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Get image properties
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);

    // Retrieve image with visible dimensions
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // Retrieve image from resources
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // Create bitmap with actual dimensions
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
    }
}
```

