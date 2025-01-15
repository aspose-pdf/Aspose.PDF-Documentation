---
title: Add Text and Image Stamp
type: docs
weight: 20
url: /net/add-text-and-image-stamp/
description: This section explains how to add Text and Image Stamp with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "The Add Text and Image Stamp features in Aspose.PDF for .NET enables users to seamlessly apply customized text and image stamps across all or specific pages of PDF documents. This functionality enhances document personalization, allowing for detailed control over stamp attributes such as position, rotation, and quality, ultimately improving the presentation and branding of your PDF files",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Add Text Stamp on All Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on all the pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on all pages in a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Add Text Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on particular pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add text stamp on particular pages of the PDF file, you also need to set the  [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on particular pages in a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Add Image Stamp on All Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on all the pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on all pages in a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Control image quality when adding as stamp

When adding Image as stamp object, you can also control the quality of image. In order to accomplish this requirement, Quality property is added for [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. It indicates the quality of image in percents (valid values are 0..100).

## Add Image Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on particular pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add image stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on particular pages in a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object using 'using' block to ensure proper disposal
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```
