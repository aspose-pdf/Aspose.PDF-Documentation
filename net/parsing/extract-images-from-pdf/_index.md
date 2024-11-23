---
title: Extract Images from PDF C#
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for .NET in C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Images are held in each page's [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) collection's [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image's index returns an [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) object. This object provides a Save method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document document = new Document(dataDir+ "ExtractImages.pdf");

// Extract a particular image
XImage xImage = document.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Save output image
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Save updated PDF file
document.Save(dataDir);
```
