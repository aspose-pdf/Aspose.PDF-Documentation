---
title: Convert PDF to BMP 
linktitle: Convert PDF to BMP
type: docs
weight: 40
url: /androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
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
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Convert All PDF Pages to BMP Images

To convert all page of PDF file to BMP format, you need to iterate through to get each individual page and convert it to BMP format. The following code snippet shows you how to traverse through all the pages of a PDF file and convert it to BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convert a particular page region to Image (DOM)

We can convert PDF documents to different Image formats using image devices objects of Aspose.PDF. However sometimes there is a requirement to convert particular page region into Image format. We can fulfill this requirement in two steps. Initially crop the PDF page to desired region and later convert it to image using desired Image device object.

The following code snippet shows you how to convert PDF pages to images.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
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
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```