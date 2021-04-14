---
title: Convert PDF to EMF 
linktitle: Convert PDF to EMF 
type: docs
weight: 50
url: /java/convert-pdf-to-emf/
lastmod: "2021-02-04"
description: This page describes how to convert PDF Pages to EMF image, convert all and single pages to EMF images with Aspose.PDF for Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-emf](https://products.aspose.app/pdf/conversion/pdf-to-emf)

{{% /alert %}}

The EmfDevice class allows you to convert PDF pages to <abbr title="Enhanced Meta File">EMF</abbr> images. This class provides a method named Process which allows you to convert a particular page of the PDF file to EMF image format.


## Convert single PDF page to EMF image

Pass the page index as an argument to the Process(..) method.

The following code snippet shows the steps to convert single page of PDF to EMF format.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.EmfDevice;
import com.aspose.pdf.devices.Resolution;

public final class ConvertPDFtoEMF {

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        ConvertPDFtoEMFtoSinglePage();
        ConvertPDFtoEMFAllPages();
    }

    public static void ConvertPDFtoEMFtoSinglePage() throws IOException {
        // Open document
        String inputFileName = Paths.get(_dataDir.toString(), "input.pdf").toString();
        Document pdfDocument = new Document(inputFileName);
        // Create stream object to save the output image

        java.io.OutputStream imageStream = new java.io.FileOutputStream(
                Paths.get(_dataDir.toString(), "Converted_Image.emf").toString());

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create EmfDevice object with particular resolution
        EmfDevice emfDevice = new EmfDevice(resolution);

        // Convert a particular page and save the image to stream
        emfDevice.process(pdfDocument.getPages().get_Item(1), imageStream);

        // Close the stream
        imageStream.close();
    }
```
## Convert all PDF pages to EMF image

Aspose.PDF for Java allows you to convert all pages in a PDF file to images:

1. Loop through all pages in the file.
1. Convert each page individually:
    - Create an object of the Document class to load the PDF document.
    - Get the page you want to convert.
    - Call the Process method to convert the page to EMF.

The following code snippet shows you how to convert all PDF pages to EMF images with Java.

```java
    public static void ConvertPDFtoEMFAllPages() throws IOException {
        // Open document
        String inputFileName = Paths.get(_dataDir.toString(), "input.pdf").toString();
        Document pdfDocument = new Document(inputFileName);

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            java.io.OutputStream imageStream = new java.io.FileOutputStream("Converted_Image" + pageCount + ".emf");

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create EMFDevice object with particular resolution
            EmfDevice emfDevice = new EmfDevice(resolution);

            // Convert a particular page and save the image to stream
            emfDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            imageStream.close();
        }
    }
```
## Convert  particular page region of a PDF page to all EMF pages

```java
    public static void ConvertParticularPageRegionPDFtoEMFAllPages() throws IOException {
        // open document
        Document document = new Document("input.pdf");
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
        // Create EMF device with specified attributes
        EmfDevice emfDevice = new EmfDevice(resolution);
        // Convert a particular page and save the image to stream
        emfDevice.process(document.getPages().get_Item(1), "output.emf");

    }
}
```
