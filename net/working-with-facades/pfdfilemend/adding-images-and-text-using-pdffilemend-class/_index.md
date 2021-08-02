---
title: Adding Images and Text using PdfFileMend class
type: docs
weight: 10
url: /net/adding-images-and-text-using-pdffilemend-class/
description: This section explains how to Add Images and Text using PdfFileMend class.
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend) class can help you add images and text in an existing PDF document, at a specified location. It provides two methods with the names [AddImage](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend/methods/addimage/index) method allows you to add images of type JPG, GIF, PNG, and BMP. [AddText](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend/methods/addtext/index) method takes an argument of type [FormattedText](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/formattedtext) class and adds it in the existing PDF file. The images and text can be added in a rectangle region specified by the coordinates of lower left and upper right points. While adding images you can specify either image file path or a stream of an image file. In order to specify the page number at which the image or text needs to be added, both of these methods provide an argument of page number. So, you can not only add the images and text at the specified location but also on a specified page as well.

Images are an important part of the contents of a PDF document. Manipulating images in an existing PDF file is a common requirement of the people working with PDF files. In this article, we’ll explore how the images can be manipulated, in an existing PDF file, with the help of [Aspose.Pdf.Facades namespace](https://apireference.aspose.com/pdf/net/aspose.pdf.facades) of [Aspose.PDF for .NET](/pdf/net/). All the image related operations of [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) have been consolidated in this article.

## Implementation details

[Aspose.Pdf.Facades namespace](https://apireference.aspose.com/pdf/net/aspose.pdf.facades) allows you to add new images in an existing PDF file. You can also replace or remove an existing image. A PDF file can also be converted to images. You can either convert each individual page into a single image or a complete PDF file into one image. It allows you to formats i.e. JPEG, BMP, PNG and TIFF etc. You can extract the images from a PDF file as well. You can use four classes of [Aspose.Pdf.Facades namespace](https://apireference.aspose.com/pdf/net/aspose.pdf.facades) to implement these operations i.e. [PdfFileMend](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend), [PdfContentEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdfextractor) and [PdfConverter](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdfconverter).

## Image Operations

In this section, we’ll have a detailed look into these image operations. We’ll also see the code snippets to show the use of the related classes and methods. First of all, let’s have a look at adding an image in an existing PDF file. We can use [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method of [PdfFileMend](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffilemend) class to add a new image. Using this method, you can not only specify the page number on which you want to add the image, but also the location of the image can be specified.

## Add Image in an Existing PDF File (Facades)

You can use [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method of the [PdfFileMend](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class. The [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) method. The following code snippet shows you how to add image in an existing PDF file.

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Add Image in an Existing PDF File (Facades)

You can use [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method of the [PdfFileMend](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class. The [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) method. The following code snippet shows you how to add image in an existing PDF file.
