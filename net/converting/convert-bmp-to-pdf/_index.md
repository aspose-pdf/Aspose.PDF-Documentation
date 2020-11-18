---
title: Convert BMP to PDF
type: docs
weight: 110
url: /net/convert-bmp-to-pdf/
---
# Convert BMP to PDF

BMP images are Files having extension .BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format. 
You can convert BMP to PDF with Aspose.PDF for .NET API. Therefore, you can follow the following steps to convert BMP images:

1. Initialize a new Document
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
    image.File = dataDir + @"Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Save output PDF document
    pdfDocument.Save(dataDir + @"BMPtoPDF.pdf");
}
```
