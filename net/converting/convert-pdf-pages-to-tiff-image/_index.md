---
title: Convert PDF Pages to TIFF Image 
type: docs
weight: 260
url: /net/convert-pdf-pages-to-tiff-image/
---
# Convert PDF Pages to TIFF Image

The TiffDevice class allows you to convert PDF pages to TIFF images. This class provides a method named Process which allows you to convert all the pages in a PDF file to a single TIFF image.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convert All Pages to One TIFF Image
To convert all pages in a PDF file to a single TIFF image:

1. Create an object of the Document class.
1. Call the Process method to convert the document.
1. To set the output file's properties, use the TiffSettings class.

The following code snippet shows how to convert all the PDF pages to a single TIFF image.

To convert all pages in a PDF file to a single TIFF image:

Create an object of the Document class.
Call the Process method to convert the document.
To set the output file's properties, use the TiffSettings class.
The following code snippet shows how to convert all the PDF pages to a single TIFF image.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Create Resolution object
    Resolution resolution = new Resolution(300);

    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convert a particular page and save the image to stream
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```

## Convert One Page to TIFF Image
To convert a particular page in a PDF file to a TIFF image, use an overloaded version of the Process(..) method which takes a page number as an argument for conversion. The following code snippet shows how to convert the first page of a PDF to TIFF format.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Create Resolution object
    Resolution resolution = new Resolution(300);

    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convert a particular page and save the image to stream
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```

## Use Bradley algorithm during conversion
Aspose.PDF for .NET has been supporting the feature to convert PDF to TIF using LZW compression and then with the use of AForge, Binarization can be applied. However one of the customers requested that for some images, they need to get the Threshold using Otsu, so they also would like to use Bradley.

```csharp
public static void ConvertPDFtoTiffBradleyBinarization()
{

    // Open document
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Create Resolution object
    Resolution resolution = new Resolution(300);
    // Create TiffSettings object
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Create TIFF device
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Convert a particular page and save the image to stream
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
}
```