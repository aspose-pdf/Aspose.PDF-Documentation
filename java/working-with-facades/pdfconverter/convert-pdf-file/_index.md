---
title: Convert PDF File
type: docs
weight: 20
url: /java/convert-pdf-file/
description: This section explains how to convert PDF File with Aspose.PDF Facades using PdfConverter class.
lastmod: "2021-06-05"
draft: false
---

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) object and open the PDF file using [bindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-) method. 

After that, you need to call [doConvert](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) method for initialization tasks. Then, you can loop through all the pages using [hasNextImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) and [getNextImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-) methods. The getNextImage method allows you to create image of a particular page. You also need to pass ImageType to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. 

Finally, call the close method of the [PdfConverter](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfConverter) class.

The following code snippet shows you how to convert PDF pages to images.

```java
public static void ConvertPdfPagesToImages01() {
        // Create PdfConverter object
        PdfConverter converter = new PdfConverter();

        // Bind input pdf file
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Initialize the converting process
        converter.doConvert();
        
        int count=0;

        // Check if pages exist and then convert to image one by one
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Close the PdfConverter object
        converter.close();
    }
```

In the next code snippet, we will show how you can change some parameters. With [setCoordinateType](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) we set the frame [CropBox](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). Also, we can change [setResolution](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) specifying the number of dots per inch. The next one [setFormPresentationMode](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - form presentation mode. Then we indicate the [setStartPage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) with which the page number of the beginning of the conversion is set. We can also specify the last page by setting a range.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Create PdfConverter object
        PdfConverter converter = new PdfConverter();

        // Bind input pdf file
        converter.bindPdf(_dataDir + "sample.pdf");

        // Initialize the converting process
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Check if pages exist and then convert to image one by one
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Close the PdfConverter object
        converter.close();
    }
```