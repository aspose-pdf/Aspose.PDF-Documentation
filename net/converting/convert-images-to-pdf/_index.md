---
title: Convert images to PDF 
type: docs
weight: 100
url: /net/convert-images-to-pdf/
description: You can very easy convert a JPG image to PDF. Also, you can convert an image to PDF with the same  height and width of the page.
---

# Convert images to PDF

You can very easy convert a JPG image to PDF by following steps:

1. Initialize object of Document class
1. Add a new Page to PDF document
1. Load JPG image and add to paragraph
1. Save output PDF

The code snippet below shows how to convert JPG Image to PDF using C#:
```csharp
// Load input JPG file
String path = dataDir + "Aspose.jpg";

// Initialize new PDF document
Document doc = new Document();

// Add empty page in empty document
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Add image on a page
page.Paragraphs.Add(image);

// Save output PDF file
doc.Save(dataDir + "ImagetoPDF.pdf");
```
Then you can see how to convert an image to PDF with the **same height and width of the page**. We will be getting the image dimensions and accordingly set the page dimensions of PDF document with the below steps:

1. Load input image file
1. Get the height and width of the image
1. Set height, width, and margins of a page
1. Save the output PDF file

Following code snippet shows how to convert an Image to PDF with same page height and width using C#:

```csharp
// Load input JPG image file
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// Read Height of input image
int h = srcImage.Height;

// Read Height of input image
int w = srcImage.Width;

// Initialize a new PDF document
Document doc = new Document();

// Add an empty page
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Set page dimensions and margins
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Save output PDF file
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```

