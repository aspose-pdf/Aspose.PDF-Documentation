---
title: Convert images to PDF 
type: docs
weight: 100
url: /net/convert-images-to-pdf/
---
# Convert images to PDF using Image class

For the most filetype we can use Image class to convert image into a PDF page. This technique is similar to add TextFragment (see "Convert text ..." section):

1. Create an object of the Image class.
1. Add the image to a page's Paragraphs collection.
1. Specify the file's path or source.
    - If an image is at a location on the hard drive, specify the path location using the Image.File property.
    - If an image is placed in a MemoryStream, pass the object holding the image to the Image.ImageStream property.

The following code snippet shows how to load an image object, get its dimensions, set the page dimensions according to image dimensions, place the image on a page in a PDF file and save the output as PDF.

```csharp
public static void ConvertImagetoPDF()
{
    // For complete examples and data files, please
    // go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Instantiate Document Object
    Document pdfDocument= new Document();
    // Add a page to pages collection of document
    Page page = pdfDocument.Pages.Add();
    // Load the source image file to Stream object
    FileStream fs = new FileStream(dataDir + "CCITT_8.TIF", FileMode.Open, FileAccess.Read);
    byte[] tmpBytes = new byte[fs.Length];
    fs.Read(tmpBytes, 0, int.Parse(fs.Length.ToString()));

    MemoryStream imageStream = new MemoryStream(tmpBytes);
    // Instantiate BitMap object with loaded image stream
    Bitmap b = new Bitmap(imageStream);

    // Set margins so image will fit, etc.
    page.PageInfo.Margin.Bottom = 0;
    page.PageInfo.Margin.Top = 0;
    page.PageInfo.Margin.Left = 0;
    page.PageInfo.Margin.Right = 0;

    page.CropBox = new Aspose.Pdf.Rectangle(0, 0, b.Width, b.Height);
    // Create an image object
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();
    // Add the image into paragraphs collection of the section
    page.Paragraphs.Add(image);
    // Set the image file stream
    image.ImageStream = imageStream;
    dataDir += "ImageToPDF_out.pdf";
    // Save resultant PDF file
    pdfDocument.Save(dataDir);

    // Close memoryStream object
    imageStream.Close();
}
```
