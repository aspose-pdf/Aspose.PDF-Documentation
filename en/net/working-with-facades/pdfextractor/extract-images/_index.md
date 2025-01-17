---
title: Extract Images using PdfExtractor
type: docs
weight: 20
url: /net/extract-images/
description: This section explains how to extract Images with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "The PdfExtractor feature from Aspose.PDF enables users to efficiently extract images from PDF documents, offering multiple options such as extracting images from the entire document, specific pages, or specified ranges. It supports saving images directly to files or memory streams, enhancing flexibility for developers working with PDF assets. This powerful functionality allows precise control over image extraction modes, making it easier to handle different PDF content types",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Extract Images from the Whole PDF to Files (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## Extract Images from the Whole PDF to Streams (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file into streams. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, call [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to stream, you can call the overload of the [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes Stream as argument. The following code snippet shows you how to extract images from the whole PDF to streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extract Images from a Particular Page of a PDF (Facades)

You can extract images from a particular page of a PDF file. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the particular page you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a particular page of PDF to streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extract Images from a Range of Pages of a PDF (Facades)

You can extract images from a range of pages of a PDF file. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the range of pages you want to extract images from. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties. After that, call [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. You can either save the images to disk or stream. You only need to call the appropriate overload of [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method. The following code snippet shows you how to extract images from a range of pages of PDF to streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extract Images using Image Extraction Mode (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class allows you to extract images from a PDF file. Aspose.PDF supports two extraction modes; first is ActuallyUsedImage which extract the images actually used in the PDF document. Second mode is [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) which extract the images defined in the resources of the PDF document (default extraction mode). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, specify the image extraction mode using [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) property. Then call [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) method to extract all the images into memory depending on the mode you specified. Once the images are extracted, you can get those images with the help of [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) method which takes file path as argument.

The following code snippet shows you how to extract images from PDF file using ExtractImageMode option.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

For checking if Pdf contains Text Or Images use next code snippet:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```