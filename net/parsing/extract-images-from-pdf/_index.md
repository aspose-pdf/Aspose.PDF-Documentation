---
title: Extract Images from PDF C#
linktitle: Extract Images from PDF C#
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for .NET in C#
lastmod: "2020-12-23"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Images are held in each page's [Resources](https://apireference.aspose.com/net/pdf/aspose.pdf/resources) collection's [Images](https://apireference.aspose.com/net/pdf/aspose.pdf/resources/properties/images) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image's index returns an [XImage](https://apireference.aspose.com/net/pdf/aspose.pdf/ximage) object. This object provides a Save method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```csharp
 // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// Extract a particular image
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Save output image
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Save updated PDF file
pdfDocument.Save(dataDir);
```
