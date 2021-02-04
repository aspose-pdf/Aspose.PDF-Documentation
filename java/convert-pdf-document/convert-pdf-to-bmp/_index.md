---
title: Convert PDF to BMP 
linktitle: Convert PDF to BMP
type: docs
weight: 40
url: /net/convert-pdf-to-bmp/
lastmod: "2021-02-04"
description: This article describes how to convert PDF Pages to BMP image, convert all Pages to BMP images and convert single PDF page to BMP image with Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [BmpDevice](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) class allows you to convert PDF pages to <abbr title="Bitmap Image File">BMP</abbr> images. This class provides a method named [Process](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) which allows you to convert a particular page of the PDF file to Bmp image format.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}


The BmpDevice class allows you to convert PDF pages to BMP images. This class provides a method named process(..) which allows you to convert a particular page of the PDF file to BMP image.

## Convert a PDF Page to BMP Image

To convert a PDF page to a BMP image:

1. Create an object of the Document class, to get the particular page you want to convert.
1. Call the process(..) method to convert the page to BMP.

The following code snippet shows you how to convert particular page to BMP image.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.BmpDevice;
import com.aspose.pdf.devices.Resolution;

public final class ConvertPDFtoBMP {

    private ConvertPDFtoBMP() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        ConvertPDFtoBmpSinglePage();
    }

    public static void ConvertPDFtoBmpSinglePage() throws IOException
    {
        // Open document
        Document pdfDocument = new Document("input.pdf");
        // Create stream object to save the output image
        
        java.io.OutputStream imageStream = new java.io.FileOutputStream(Paths.get(_dataDir.toString(), "Converted_Image.bmp").toString());
        
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        
        //Create BmpDevice object with particular resolution
        BmpDevice bmpDevice = new BmpDevice(resolution);
        
        //Convert a particular page and save the image to stream
        bmpDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
        
        // Close the stream
        imageStream.close();
    }
}
```

## Convert All PDF Pages to BMP Images

To convert all page of PDF file to BMP format, you need to iterate through to get each individual page and convert it to BMP format. The following code snippet shows you how to traverse through all the pages of a PDF file and convert it to BMP.

```java
public static void ConvertPDFtoBmpAllPages() throws IOException {
    // Open document
    Document pdfDocument = new Document("input.pdf");

    // Loop through all the pages of PDF file
    for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
        // Create stream object to save the output image
        java.io.OutputStream imageStream = new java.io.FileOutputStream("Converted_Image" + pageCount + ".bmp");

        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create BmpDevice object with particular resolution
        BmpDevice bmpDevice = new BmpDevice(resolution);

        // Convert a particular page and save the image to stream
        bmpDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);

        // Close the stream
        imageStream.close();
    }
}
```

## Convert a particular page region to Image (DOM)

We can convert PDF documents to different Image formats using image devices objects of Aspose.PDF. However sometimes there is a requirement to convert particular page region into Image format. We can fulfill this requirement in two steps. Initially crop the PDF page to desired region and later convert it to image using desired Image device object.

The following code snippet shows you how to convert PDF pages to images.

```java
public static void ConvertParticularPageRegionPDFtoBmpAllPages() throws IOException {
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
    // Create BMP device with specified attributes
    BmpDevice bmpDevice = new BmpDevice(resolution);
    // Convert a particular page and save the image to stream
    bmpDevice.process(document.getPages().get_Item(1), "Output.bmp");

}
```