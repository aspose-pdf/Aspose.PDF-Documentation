---
title: Convert PDF to TIFF 
linktitle: Convert PDF to TIFF  
type: docs
weight: 30
url: /java/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: This article describes how to convert pages in PDF document into TIFF image. You will learn how to convert all or single pages to TIFF images with Aspose.PDF for Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** makes a possible to convert PDF Pages to TIFF  images.

The [TiffDevice class](https://apireference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) allows you to convert PDF pages to TIFF images. This class provides a method named Process which allows you to convert all the pages in a PDF file to a single TIFF image.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convert PDF Pages to One TIFF Image

Aspose.PDF for Java explain how to convert all pages in a PDF file to a single TIFF image:

1. Create an object of the Document class.
1. Call the Process method to convert the document.
1. To set the output file's properties, use the TiffSettings class.

The following code snippet shows how to convert all the PDF pages to a single TIFF image.

```java
public static void ConvertPDFtoTiffAllPages() throws IOException {

        // Open document
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PageToTIFF.pdf").toString();
        Document pdfDocument = new Document(pdfDocumentFileName);

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
    }
```

## Convert Single Page to TIFF Image

Aspose.PDF for Java allows to convert a particular page in a PDF file to a TIFF image, use an overloaded version of the Process(..) method which takes a page number as an argument for conversion. The following code snippet shows how to convert the first page of a PDF to TIFF format.

```java
public static void ConvertPDFtoTiffSinglePage() throws IOException {

        // Open document
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PageToTIFF.pdf").toString();
        String tiffFileName = Paths.get(_dataDir.toString(), "PageToTIFF_out.tif").toString();
        Document pdfDocument = new Document(pdfDocumentFileName);

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.process(pdfDocument, 1, 1, tiffFileName);
    }
```

## Use Bradley algorithm during conversion

Aspose.PDF for Java has been supporting the feature to convert PDF to TIFF using LZW compression and then with the use of AForge, Binarization can be applied. However one of the customers requested that for some images, they need to get the Threshold using Otsu, so they also would like to use Bradley.

```java
    public static void ConvertPDFtoTiffBradleyBinarization() throws IOException {

        // Open document
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PageToTIFF.pdf").toString();
        Document pdfDocument = new Document(pdfDocumentFileName);

        String outputImageFileName = Paths.get(_dataDir.toString(), "resultant_out.tif").toString();
        String outputBinImageFileName = Paths.get(_dataDir.toString(), "37116-bin_out.tif").toString();

        java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
        java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Format1bpp);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        // Convert a particular page and save the image to stream
        tiffDevice.process(pdfDocument, outputImageFile);
        outputImageFile.close();

        // Create stream object to save the output image
        java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
        tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);

    }
```
## Convert PDF Pages to Pixelated TIFF Images

To convert all pages in a PDF file to Pixelated TIFF format, use Pixelated option of IndexedConversionType

```java
   public static void ConvertPDFtoTIFF_Pixelated() throws IOException {
        // Convert PDF Pages to Pixelated TIFF Images
        // To convert all pages in a PDF file to Pixelated TIFF format, use Pixelated
        // option of IndexedConversionType.

        // Open document
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PageToTIFF.pdf").toString();
        Document pdfDocument = new Document(pdfDocumentFileName);

        // Create stream object to save the output image
        java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

        // Create Resolution object
        com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

        // instantiate TiffSettings object
        com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

        // set the compression of resultant TIFF image
        tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
        // set the color depth for resultant image
        tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
        // skip blank pages while rendering PDF to TIFF
        tiffSettings.setSkipBlankPages(true);
        // set image brightness
        tiffSettings.setBrightness(.5f);

        // set IndexedConversion Type, default value is simple
        tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

        // Create TiffDevice object with particular resolution
        TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

        // Convert a particular page (Page 1) and save the image to stream
        tiffDevice.process(pdfDocument, 1, 1, imageStream);

        // Close the stream
        imageStream.close();
    }
}
```