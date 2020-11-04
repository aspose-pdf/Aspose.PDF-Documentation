---
title: Convert PNG to PDF
type: docs
weight: 140
url: /net/convert-png-to-pdf/
---
# Convert PNG to PDF

PNG, **Portable Network Graphics**, refers to a type of raster image file format that use loseless compression, that makes it popular among its users. 
You can convert PNG to PDF image using the below steps:
1. Load input PNG image
1. Read height and width values
1. Create new document and add Page
1. Set page dimensions
1. Save output file

Moreover, the code snippet below shows how to convert PNG to PDF with C# in your .NET applications:
```
// Load input PNG file
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// Initialize new Document
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Set page dimensions
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Save output PDF
doc.Save(dataDir + "ImagetoPDF.pdf");
```