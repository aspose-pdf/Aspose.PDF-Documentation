---
title: Extract Images from PDF File
type: docs
weight: 20
url: /net/extract-images/
description: This section explains how to extract Images with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-05"
draft: false
---

## Extract Images from the Whole PDF to Files (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extract all the images
            pdfExtractor.ExtractImage();

            // Get all the extracted images
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```

## Extract Images from the Whole PDF to Streams (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file into streams. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to stream, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes Stream as argument. The following code snippet shows you how to extract images from the whole PDF to streams.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extract images
            pdfExtractor.ExtractImage();
            // Get all the extracted images
            while (pdfExtractor.HasNextImage())
            {
                // Read image into memory stream
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Write to disk, if you like, or use it otherwise.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
```

## Extract Images from a Particular Page of a PDF (Facades)

You can extract images from a particular page of a PDF file. In order to do that, you need to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the particular page you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a particular page of PDF to streams.

```csharp
     public static void ExtractImagesParticularPage()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Set StartPage and EndPage properties to the page number to
            // You want to extract images from
            pdfExtractor.StartPage = 2;
            pdfExtractor.EndPage = 2;

            // Extract images
            pdfExtractor.ExtractImage();
            // Get extracted images
            while (pdfExtractor.HasNextImage())
            {
                // Read image into memory stream
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Write to disk, if you like, or use it otherwise.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```

## Extract Images from a Range of Pages of a PDF (Facades)

You can extract images from a range of pages of a PDF file. In order to do that, you need to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the range of pages you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a range of pages of PDF to streams.

```csharp
      public static void ExtractImagesRangePages()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Set StartPage and EndPage properties to the page number to
            // You want to extract images from
            pdfExtractor.StartPage = 2;
            pdfExtractor.EndPage = 2;

            // Extract images
            pdfExtractor.ExtractImage();
            // Get extracted images
            while (pdfExtractor.HasNextImage())
            {
                // Read image into memory stream
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Write to disk, if you like, or use it otherwise.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```

## Extract Images using Image Extraction Mode (Facades)

[PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. Aspose.PDF supports two extraction modes; first is ActuallyUsedImage which extract the images actually used in the PDF document. Second mode is [DefinedInResources](https://apireference.aspose.com/pdf/net/aspose.pdf/extractimagemode) which extract the images defined in the resources of the PDF document (default extraction mode). First, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, specify the image extraction mode using [PdfExtractor.ExtractImageMode](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) property. Then call [ExtractImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory depending on the mode you specified. Once the images are extracted, you can get those images with the help of [HasNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument.

The following code snippet shows you how to extract images from PDF file using ExtractImageMode option.

```csharp
     public static void ExtractImagesImageExtractionMode()
        {
            // Open input PDF
            PdfExtractor extractor = new PdfExtractor();
            extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Specify Image Extraction Mode
            // extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
            extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

            // Extract Images based on Image Extraction Mode
            extractor.ExtractImage();

            // Get all the extracted images
            while (extractor.HasNextImage())
            {
                extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
```



