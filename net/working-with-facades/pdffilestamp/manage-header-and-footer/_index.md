---
title: Manage Header and Footer
type: docs
weight: 40
url: /net/manage-header-and-footer/
description: Explore how to manipulate headers and footers in PDF files in .NET with Aspose.PDF for improved document structuring.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "The Manage Header and Footer features in Aspose.PDF for .NET allows users to easily add, customize, and format both headers and footers in PDF documents using the PdfFileStamp class. This functionality supports the inclusion of text and images, providing flexibility in document presentation while ensuring professional formatting. Users can seamlessly integrate this feature into their applications to enhance the visual appeal and organization of PDF files",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Add Header in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add header in a PDF file. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can format the header text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add header in the file, you need to call [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You also need to specify at least the top margin in the [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add header in a PDF file.

```csharp
public static void AddHeader()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create formatted text for page number
    FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
        System.Drawing.Color.Yellow,
        System.Drawing.Color.Black,
        FontStyle.Courier,
        EncodingType.Winansi, false, 14);

    // Add header
    fileStamp.AddHeader(formattedText, 10);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddHeader_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Footer in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add footer in a PDF file. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can format the footer text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add footer in the file, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You also need to specify at least the bottom margin in the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add footer in a PDF file.

```csharp
public static void AddFooter()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create formatted text for page number
    FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
        System.Drawing.Color.Blue,
        System.Drawing.Color.Gray,
        FontStyle.Courier,
        EncodingType.Winansi, false, 14);

    // Add footer
    fileStamp.AddFooter(formattedText, 10);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddFooter_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Image in Header of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add image in the header of a PDF file. In order to add image in header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. After that, you need to call [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can pass the image to the [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add image in header of PDF file.

```csharp
public static void AddImageHeader()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");
    using (var fs = new FileStream(dataDir + "aspose-logo.png", FileMode.Open))
    {
        // Add Header
        fileStamp.AddHeader(fs, 10);

        // Save updated PDF file
        fileStamp.Save(dataDir + "AddImage-Header_out.pdf");
        // Close fileStamp
        fileStamp.Close();
    }
}
```

## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add image in the footer of a PDF file. In order to add image in footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. After that, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can pass the image to the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add image in the footer of PDF file.

```csharp
public static void AddImageFooter()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");
    using (var fs = new FileStream(dataDir + "aspose-logo.png", FileMode.Open))
    {
        // Add footer
        fileStamp.AddFooter(fs, 10);

        // Save updated PDF file
        fileStamp.Save(dataDir + "AddImage-Footer_out.pdf");

        // Close fileStamp
        fileStamp.Close();
    }
}
```
