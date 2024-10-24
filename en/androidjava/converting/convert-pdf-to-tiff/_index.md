---
title: Convert PDF to TIFF 
linktitle: Convert PDF to TIFF  
type: docs
weight: 30
url: /androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: This article describes how to convert pages in PDF document into TIFF image. You will learn how to convert all or single pages to TIFF images with Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** makes a possible to convert PDF Pages to TIFF  images.

The [TiffDevice class](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) allows you to convert PDF pages to TIFF images. This class provides a method named Process which allows you to convert all the pages in a PDF file to a single TIFF image.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convert PDF Pages to One TIFF Image

Aspose.PDF for Android via Java explain how to convert all pages in a PDF file to a single TIFF image:

1. Create an object of the Document class.
1. Call the Process method to convert the document.
1. To set the output file's properties, use the TiffSettings class.

The following code snippet shows how to convert all the PDF pages to a single TIFF image.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convert Single Page to TIFF Image

Aspose.PDF for Android via Java allows to convert a particular page in a PDF file to a TIFF image, use an overloaded version of the Process(..) method which takes a page number as an argument for conversion. The following code snippet shows how to convert the first page of a PDF to TIFF format.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


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
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Use Bradley algorithm during conversion

Aspose.PDF for Android via Java has been supporting the feature to convert PDF to TIFF using LZW compression and then with the use of AForge, Binarization can be applied. However one of the customers requested that for some images, they need to get the Threshold using Otsu, so they also would like to use Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```
