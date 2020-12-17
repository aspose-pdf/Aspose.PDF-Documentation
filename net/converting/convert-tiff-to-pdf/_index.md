---
title: Convert TIFF to PDF
type: docs
weight: 130
url: /net/convert-tiff-to-pdf/
lastmod: "2020-12-16"
description: Aspose.PDF for .NET allows converting multi-page or multi-frame TIFF images to PDF applications. 
---

**Aspose.PDF** file format supported, be it a single frame or multi-frame TIFF image. It means that you can convert the TIFF image to PDF in your .NET applications. 

TIFF or TIF, Tagged Image File Format, represents raster images that are meant for usage on a variety of devices that comply with this file format standard. TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image. So you can convert the TIFF image to PDF in your .NET applications. Therefore, we will consider an example of converting multi-page TIFF image to multi-page PDF document with below steps:

1. Instantiate an instance of Document class
1. Load input TIFF image
1. Get FrameDimension of the frames
1. Add new page for each frame
1. Finally, save images to PDF pages

Moreover, the following code snippet shows how to convert multi-page or multi-frame TIFF image to PDF with C#:

```csharp
// Initalize new Document
Document pdf = new Document();

//Load TIFF image into stream
MemoryStream ms = new MemoryStream();
new FileStream(dataDir + @"Aspose.tiff", FileMode.Open).CopyTo(ms);
Bitmap myimage = new Bitmap(ms);
// Convert multi page or multi frame TIFF to PDF
FrameDimension dimension = new FrameDimension(myimage.FrameDimensionsList[0]);
int frameCount = myimage.GetFrameCount(dimension);

// Iterate through each frame
for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
{
    Page sec = pdf.Pages.Add();

    myimage.SelectActiveFrame(dimension, frameIdx);

    MemoryStream currentImage = new MemoryStream();
    myimage.Save(currentImage, ImageFormat.Tiff);

    Aspose.Pdf.Image imageht = new Aspose.Pdf.Image();
    imageht.ImageStream = currentImage;
    sec.Paragraphs.Add(imageht);
}

// Save output PDF file
pdf.Save(dataDir + "TifftoPDF.pdf");
```
