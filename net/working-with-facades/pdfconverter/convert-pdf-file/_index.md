---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: Learn how to convert a PDF file to various formats in .NET using Aspose.PDF for flexible document handling.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "Unlock the power of Aspose.PDF for .NET Facades to effortlessly convert PDF pages into diverse image formats like JPEG, GIF, and PNG with the PdfConverter class. This feature enables detailed control over the conversion process, allowing you to specify parameters such as resolution, coordinate type, and page range for customized output. Enhance your document handling capabilities by integrating seamless PDF to image conversions into your applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) object and open the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you need to call [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) method for initialization tasks. Then, you can loop through all the pages using [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) and [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) methods. The [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) method of the [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) class. The following code snippet shows you how to convert PDF pages to images.

```csharp
public static void ConvertPdfPagesToImages01()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        converter.GetNextImage(dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
    }

    // Close the PdfConverter object
    converter.Close();
}
```

In the next code snippet, we will show how you can change some parameters. With [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) we set the frame 'CropBox'. Also, we can change [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) specifying the number of dots per inch. The next one [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - form presentation mode. Then we indicate the [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) with which the page number of the beginning of the conversion is set. We can also specify the last page by setting a range.

```csharp
public static void ConvertPdfPagesToImages02()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();
    converter.CoordinateType = PageCoordinateType.CropBox;
    converter.Resolution = new Devices.Resolution(600);
    converter.FormPresentationMode = Devices.FormPresentationMode.Production;
    converter.StartPage = 2;

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        converter.GetNextImage(dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
    }

    // Close the PdfConverter object
    converter.Close();
}
```

## See also

Aspose.PDF for .NET allows converting PDF documents to various formats and also converting from other formats to PDF. Also, you can check the quality of Aspose.PDF conversion and view the results online with Aspose.PDF converter app. Learn [Converting](/pdf/net/converting/) section for resolving your tasks.


