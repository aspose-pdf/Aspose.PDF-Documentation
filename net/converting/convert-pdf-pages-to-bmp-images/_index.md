---
title: Convert PDF Pages to BMP Image
type: docs
weight: 160
url: /net/convert-pdf-pages-to-bmp-image/
---
# Convert PDF Pages to BMP Image
The BmpDevice class allows you to convert PDF pages to Bmp images. This class provides a method named Process which allows you to convert a particular page of the PDF file to Bmp image format.

## Convert All Pages to Bmp Images
> Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

To convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    1. Create an object of the Document class to load the PDF document.
    1. Get the page you want to convert.
    1. Call the Process method to convert the page to BMP.

The following code snippet shows you how to convert all PDF pages to BMP images.

```csharp
public static void ConvertPDFtoBmpAllPages()
{
    Document pdfDocument = new Document(_dataDir + "ConvertAllPagesToBmp.pdf");

    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = new FileStream(_dataDir + "image" + pageCount + "_out" + ".bmp", FileMode.Create))
        {
            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create PNG device with specified attributes
            // Width, Height, Resolution
            BmpDevice BmpDevice = new BmpDevice(500, 700, resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Close stream
            imageStream.Close();

        }
    }
}
```

## Convert single PDF page to BMP image
To convert a particular page to Bmp format:

Pass the page index as an argument to the Process(..) method.
The following code snippet shows the steps to convert the first page of PDF to Bmp format.

```csharp
public static void ConvertPDFtoBmpSinglePage()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToBmp.pdf");

    using (FileStream imageStream = new FileStream(_dataDir + "image_out.Bmp", FileMode.Create))
    {
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Bmp device with specified attributes
        // Width, Height, Resolution
        BmpDevice BmpDevice = new BmpDevice(500, 700, resolution);

        // Convert a particular page and save the image to stream
        BmpDevice.Process(pdfDocument.Pages[1], imageStream);

        // Close stream
        imageStream.Close();
    }
}
```