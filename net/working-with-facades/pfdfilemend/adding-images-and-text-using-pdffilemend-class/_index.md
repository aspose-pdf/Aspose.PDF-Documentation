---
title: Adding Images and Text 
type: docs
weight: 10
url: /net/adding-images-and-text-using-pdffilemend-class/
description: This section explains how to Add Images and Text using PdfFileMend class.
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class can help you add images and text in an existing PDF document, at a specified location. It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method allows you to add images of type JPG, GIF, PNG, and BMP. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) method takes an argument of type [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class and adds it in the existing PDF file. The images and text can be added in a rectangle region specified by the coordinates of lower left and upper right points. While adding images you can specify either image file path or a stream of an image file. In order to specify the page number at which the image or text needs to be added, both of these methods provide an argument of page number. So, you can not only add the images and text at the specified location but also on a specified page as well.

Images are an important part of the contents of a PDF document. Manipulating images in an existing PDF file is a common requirement of the people working with PDF files. In this article, we’ll explore how the images can be manipulated, in an existing PDF file, with the help of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) of [Aspose.PDF for .NET](/pdf/net/). All the image related operations of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) have been consolidated in this article.

## Implementation details

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) allows you to add new images in an existing PDF file. You can also replace or remove an existing image. A PDF file can also be converted to images. You can either convert each individual page into a single image or a complete PDF file into one image. It allows you to formats i.e. JPEG, BMP, PNG and TIFF etc. You can extract the images from a PDF file as well. You can use four classes of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) to implement these operations i.e. [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) and [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Image Operations

In this section, we’ll have a detailed look into these image operations. We’ll also see the code snippets to show the use of the related classes and methods. First of all, let’s have a look at adding an image in an existing PDF file. We can use [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method of [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class to add a new image. Using this method, you can not only specify the page number on which you want to add the image, but also the location of the image can be specified.

## Add Image in an Existing PDF File (Facades)

You can use [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method of the [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class. The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) method.

In the following example, we add image to the page using imageStream:

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

![Add Image](/pdf/net/images/add_image1.png)

With the help of [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), we can superimpose one image on top of another:

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

![Add Image](/pdf/net/images/add_image2.png)

There are several ways to store an image in PDF file. We will demonstrate one of them in the following example:

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

## Add Text in an Existing PDF File (facades)

We can add text in several ways. Consider the first. We take the [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) and add it to the Page. After, we indicate the coordinates of the lower left corner, and then we add our text to the Page.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Check how it's looks:

![Add Text](/pdf/net/images/add_text.png)

The second way to add [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Additionally, we indicate a rectangle in which our text should fit.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```

The third example provides the ability to Add Text to specified pages. In our example, let's add a caption on pages 1 and 3 of the document.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```
