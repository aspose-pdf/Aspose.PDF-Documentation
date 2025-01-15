---
title: Add Text stamps in PDF C#
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /net/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF document using the TextStamp class with  Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text stamps in PDF C#",
    "alternativeHeadline": "Effortlessly Add Text Stamps in PDF Documents with C#",
    "abstract": "The new TextStamp feature in Aspose.PDF for .NET enables users to effortlessly add customizable text stamps to PDF documents. With properties for font size, style, and color, along with alignment options, this functionality enhances document annotation by allowing precise placement and appearance of text within PDF files",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "765",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Add a text stamp to a PDF document using the TextStamp class with  Aspose.PDF for .NET library."
}
</script>

## Add Text Stamp

You can use [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) class to add a text stamp in a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text stamp, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the stamp in the PDF. 

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following code snippet shows you how to add text stamp in the PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text stamp
        var textStamp = new Aspose.Pdf.TextStamp("Sample Stamp");
        // Set whether stamp is background
        textStamp.Background = true;
        // Set origin
        textStamp.XIndent = 100;
        textStamp.YIndent = 100;
        // Rotate stamp
        textStamp.Rotate = Rotation.on90;
        // Set text properties
        textStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        textStamp.TextState.FontSize = 14.0F;
        textStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        textStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(textStamp);
        // Save PDF document
        document.Save(dataDir + "AddTextStamp_out.pdf");  
    }
}
```

## Define alignment for TextStamp object

Adding watermarks to PDF documents is one of the frequent demanded features and Aspose.PDF for .NET is fully capable of adding Image as well as Text watermarks. We have a class named [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) which provides the feature to add text stamps over the PDF file. Recently there has been a requirement to support the feature to specify the alignment of text when using TextStamp object. So in order to fulfill this requirement, we have introduced TextAlignment property in TextStamp class. Using this property, we can specify the Horizontal text alignment.

The following code snippets shows an example on how to load an existing PDF document and add TextStamp over it.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DefineAlignmentForTextStampObject()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Instantiate FormattedText object with sample string
        var text = new Aspose.Pdf.Facades.FormattedText("This");
        // Add new text line to FormattedText
        text.AddNewLineText("is sample");
        text.AddNewLineText("Center Aligned");
        text.AddNewLineText("TextStamp");
        text.AddNewLineText("Object");
        // Create TextStamp object using FormattedText
        var stamp = new Aspose.Pdf.TextStamp(text);
        // Specify the Horizontal Alignment of text stamp as Center aligned
        stamp.HorizontalAlignment = HorizontalAlignment.Center;
        // Specify the Vertical Alignment of text stamp as Center aligned
        stamp.VerticalAlignment = VerticalAlignment.Center;
        // Specify the Text Horizontal Alignment of TextStamp as Center aligned
        stamp.TextAlignment = HorizontalAlignment.Center;
        // Set top margin for stamp object
        stamp.TopMargin = 20;
        // Add the stamp object over first page of document
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "StampedPDF_out.pdf");
    }
}
```

## Fill Stroke Text as Stamp in PDF File

We have implemented setting of rendering mode for text adding and editing scenarios. To render stroke text please create TextState object and set RenderingMode to TextRenderingMode.StrokeText and also select color for StrokingColor property. Later, bind TextState to the stamp using BindTextState() method.

Following code snippet demonstrates adding Fill Stroke Text:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillStrokeTextAsStampInPdfFile()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    // Create TextState object to transfer advanced properties
    var textState = new Aspose.Pdf.Text.TextState();
    // Set color for stroke
    textState.StrokingColor = Color.Gray;
    // Set text rendering mode
    textState.RenderingMode = Aspose.Pdf.Text.TextRenderingMode.StrokeText;
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create PdfFileStamp
        var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp(document);
        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Aspose.Pdf.Facades.EncodingType.Winansi, true, 78));
        // Bind TextState
        stamp.BindTextState(textState);
        // Set X,Y origin
        stamp.SetOrigin(100, 100);
        stamp.Opacity = 5;
        stamp.BlendingSpace = Aspose.Pdf.Facades.BlendingColorSpace.DeviceRGB;
        stamp.Rotation = 45.0F;
        stamp.IsBackground = false;
        // Add Stamp
        fileStamp.AddStamp(stamp);
        fileStamp.Save(dataDir + "FillStrokeTextAsStampInPdfFile_out.pdf");
        fileStamp.Close();
    }
}
```

## Add text stamp and automatically adjust the font size

The following code snippet demonstrates how to add a text stamp to a PDF file and automatically adjust the font size to fit the stamp rectangle.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```
The following code snippet demonstrates how to add a text stamp to a PDF file and automatically adjust the font size to fit the stamp rectangle. The stamp rectangle defaults to the page size.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextStampInput.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);
        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
