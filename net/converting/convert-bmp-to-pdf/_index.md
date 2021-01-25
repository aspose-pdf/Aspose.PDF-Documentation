---
title: Convert BMP to PDF | C#
linktitle: Convert BMP to PDF
type: docs
weight: 220
url: /net/convert-bmp-to-pdf/
lastmod: "2021-01-15"
description: You may easily convert BMP bitmap files to PDF used to store digital bitmap images separately from the display device using Aspose.PDF. for NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convert BMP files to PDF document using **Aspose.PDF for .NET** library.

<abbr title="Bitmap Image File">BMP</abbr> images are Files having extension. BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format.
You can convert BMP to PDF files with Aspose.PDF for .NET API. Therefore, you can follow the following steps to convert BMP images:

1. Initialize a new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document)
1. Load input BMP image
1. Finally, save the output PDF file

So the following code snippet follows these steps and shows how to convert BMP to PDF using C#:

```csharp
Initialize empty PDF document
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Load sample BMP image file
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Save output PDF document
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```
## Applies to

|**Platform**|**Supported**|**Comments**|
| :- | :- |:- |
|Windows .NET|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|Linux .NET Core|2.0-3.1 | |
