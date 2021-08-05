---
title: Convert PDF to JPG 
linktitle: Convert PDF to JPG
type: docs
weight: 10
url: /androidjava/convert-pdf-to-jpg/
description:  This page describes how to convert PDF Pages to JPEG image, convert all and single pages to JPEG images with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convert PDF Pages to JPG Images

The JpegDevice class allows you to convert PDF pages to JPEG images. This class provides a method named process(..) which allows you to convert a particular page of the PDF file to JPEG image.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Convert single PDF page to JPG image

Aspose.PDF for Java allows you to convert a single page to Jpeg format.

To convert just one page to a JPEG image:

1. Create an object of the Document class to get the page you want to convert.
1. Call the process(..) method to convert the page to a JPEG image.

The following code snippet shows the steps to convert the first page of PDF to Jpeg format.

```java
public static void ConvertPDFtoJpegSinglePage() throws IOException {
        // Open document
        String inputFileName = Paths.get(_dataDir.toString(), "input.pdf").toString();
        Document pdfDocument = new Document(inputFileName);
        // Create stream object to save the output image

        java.io.OutputStream imageStream = new java.io.FileOutputStream(
                Paths.get(_dataDir.toString(), "Converted_Image.Jpeg").toString());

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create JpegDevice object with particular resolution
        JpegDevice JpegDevice = new JpegDevice(resolution);

        // Convert a particular page and save the image to stream
        JpegDevice.process(pdfDocument.getPages().get_Item(1), imageStream);

        // Close the stream
        imageStream.close();
    }
```
## Convert all PDF pages to JPG image

Aspose.PDF for Java allows you to convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    - Create an object of the Document class to load the PDF document.
    - Get the page you want to convert.
    - Call the Process method to convert the page to Jpeg.

The following code snippet shows you how to convert all PDF pages to Jpeg images.

```java
    public static void ConvertPDFtoJpegAllPages() throws IOException {
        // Open document
        String inputFileName = Paths.get(_dataDir.toString(), "input.pdf").toString();
        Document pdfDocument = new Document(inputFileName);

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            java.io.OutputStream imageStream = new java.io.FileOutputStream("Converted_Image" + pageCount + ".Jpeg");

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            imageStream.close();
        }
    }
```
## Convert particular PDF page to JPG image

```java
    public static void ConvertParticularPageRegionPDFtoJpegAllPages() throws IOException {
        // open document
        Document document = new Document("Input.pdf");
        
        // Get rectangle of particular page region
        Rectangle pageRect = new Rectangle(20, 671, 693, 1125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);
        
        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        
        // Create Jpeg device with specified attributes
        JpegDevice JpegDevice = new JpegDevice(resolution);
        
        // Convert a particular page and save the image to stream
        JpegDevice.process(document.getPages().get_Item(1), "Output.Jpeg");

    }
}
```