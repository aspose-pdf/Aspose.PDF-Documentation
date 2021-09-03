---
title: Convert TIFF to PDF | C#
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /net/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for .NET allows converting multi-page or multi-frame TIFF images to PDF applications.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF** file format supported, be it a single frame or multi-frame <abbr title="Tag Image File Format">TIFF</abbr> image. It means that you can convert the TIFF image to PDF in your .NET applications.

TIFF or TIF, Tagged Image File Format, represents raster images that are meant for usage on a variety of devices that comply with this file format standard. TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image.

You can convert TIFF to PDF in the same manner as the rest raster file formats graphics:

```csharp
Initialize empty PDF document
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Load sample BMP image file
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Save output PDF document
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

In case you need to convert multi-page TIFF image to multi-page PDF document and control some params, i.g. width or aspect ratio, please follow these steps:

1. Instantiate an instance of Document class
1. Load input TIFF image
1. Get FrameDimension of the frames
1. Add new page for each frame
1. Finally, save images to PDF pages

The following code snippet shows how to convert multi-page or multi-frame TIFF image to PDF with C#:

```csharp
public static void TiffToPDF2()
{
    // Initalize new Document
    Document pdf = new Document();

    //Load TIFF image into stream
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // Convert multi page or multi frame TIFF to PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // Iterate through each frame
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            //Apply some other options
            //ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // Save output PDF file
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
