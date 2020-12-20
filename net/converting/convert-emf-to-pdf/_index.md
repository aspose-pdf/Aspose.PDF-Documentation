---
title: Convert EMF to PDF
type: docs
weight: 120
url: /net/convert-emf-to-pdf/
lastmod: "2020-12-15"
description: Both bitmap as well as vector graphics can be files having an EMF extension. Convert EMF to PDF file simply with C#.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Enhanced metafile format (EMF)** stores graphical images device-independently. Metafiles of EMF comprises of variable-length records in chronological order that can render the stored image after parsing on any output device. Furthermore, you can convert EMF to PDF image using the below steps:
1. Firstly, initialize Document class object
1. Load EMF image file
1. Add the loaded EMF image to a Page
1. Save PDF document

Moreover, the following code snippet shows how to convert an EMF to PDF with C# in your .NET code snippet:
```csharp
// Initialize new PDF document
var doc = new Document();

// Spcify path of input EMF image file
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add(); 
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// Specify page dimesion properties
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

//Save output PDF document
doc.Save(dataDir + "EMFtoPDF.pdf");
```


