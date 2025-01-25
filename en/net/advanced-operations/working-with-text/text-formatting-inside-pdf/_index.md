---
title: Text Formatting inside PDF using C#
linktitle: Text Formatting inside PDF
type: docs
weight: 30
url: /net/text-formatting-inside-pdf/
description: Learn how to format text within a PDF document in .NET using Aspose.PDF to enhance the document's visual presentation.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Text Formatting inside PDF using C#",
    "alternativeHeadline": "Enhance PDF Text Formatting with New C# Features",
    "abstract": "Discover the powerful text formatting capabilities of Aspose.PDF for .NET, allowing you to add line indents, text borders, underline effects, and more to your PDF documents. This feature enables precise control over text aesthetics and layout, enhancing the overall presentation of your PDF files. Optimize your PDF generation workflows with versatile formatting options tailored for developers",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1642",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "This page explains how to format text inside your PDF file. There are adding line Indent, adding text border, adding underline text, and etc."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## How to add Line Indent to PDF

Aspose.PDF for .NET offers SubsequentLinesIndent property into [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) class. Which can be used to specify line indent in PDF generation scenarios with TextFragment and Paragraphs collection.

Please use the following code snippet to use the property:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFormattingInsidePdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

        Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

        // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value
        text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
        {
            SubsequentLinesIndent = 20
        };

        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line2");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line3");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line4");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line5");
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "SubsequentIndent_out.pdf");
    }
}
```

## How to add Text Border

The following code snippet shows, how to add a border to a text using TextBuilder and setting DrawTextRectangleBorder property of TextState:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrokingColor property for drawing border (stroking) around text rectangle
        textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
        // Set DrawTextRectangleBorder property value to true
        textFragment.TextState.DrawTextRectangleBorder = true;
        var tb = new Aspose.Pdf.Text.TextBuilder(page);
        tb.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "PDFWithTextBorder_out.pdf");
    }
}
```

## How to add Underline Text

The following code snippet shows you how to add Underline text while creating a new PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddUnderlineText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add age page to PDF document
        document.Pages.Add();
        // Create TextBuilder for first page
        var tb = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // TextFragment with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Test message");
        // Set the font for TextFragment
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment.TextState.FontSize = 10;
        // Set the formatting of text as Underline
        fragment.TextState.Underline = true;
        // Specify the position where TextFragment needs to be placed
        fragment.Position = new Aspose.Pdf.Text.Position(10, 800);
        // Append TextFragment to PDF file
        tb.AppendText(fragment);

        // Save PDF document
        document.Save(dataDir + "AddUnderlineText_out.pdf");
    }
}
```

## How to add Border Around Added Text

You have control over the look and feel of the text you add. The example below shows how to add a border around a piece of text that you have added by drawing a rectangle around it. Find out more about the [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Open PDF document
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "AddBorder.pdf");
        var lineInfo = new Aspose.Pdf.Facades.LineInfo();
        lineInfo.LineWidth = 2;
        lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
        lineInfo.Visibility = true;
        // Add border
        editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

        // Save PDF document
        editor.Save(dataDir + "AddingBorderAroundAddedText_out.pdf");
    }
}
```

## How to add NewLine feed

TextFragment doesn’t support line feed inside the text. However in order to add text with line feed, please use TextFragment with TextParagraph:

- Use "\r\n" or Environment.NewLine in TextFragment instead of single "\n".
- Create TextParagraph object. It will add text with line splitting.
- Add the TextFragment with TextParagraph.AppendLine.
- Add the TextParagraph with TextBuilder.AppendParagraph.

Please use below code snippet.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNewLine()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        var textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "AddNewLineFeed_out.pdf");
    }
}
```

## How to add StrikeOut Text

The TextState class provides the capabilities to set formatting for TextFragments being placed inside PDF document. You can use this class to set text formatting as Bold, Italic, Underline and starting this release, the API has provided the capabilities to mark text formatting as Strikeout. Please try using the following code snippet to add TextFragment with Strikeout formatting.

Please use complete code snippet:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStrikeoutText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrikeOut property
        textFragment.TextState.StrikeOut = true;
        // Mark text as Bold
        textFragment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddStrikeOutText_out.pdf");
    }
}
```

## Apply Gradient Shading to the Text

Text formatting has been further enhanced in the API for text editing scenarios and now you can add text with pattern colorspace inside PDF document. Aspose.Pdf.Color Class has further been enhanced by introducing new property of PatternColorSpace, which can be used to specify shading colors for the text. This new property adds different Gradient Shading to the text e.g. Axial Shading, Radial (Type 3) Shading as shown in the following code snippet:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyGradientShadingToText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "text_sample4.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Lorem ipsum");
        document.Pages.Accept(absorber);

        var textFragment = absorber.TextFragments[1];

        // Create new color with pattern colorspace
        textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
        {
            PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        };
        textFragment.TextState.Underline = true;

        // Save PDF document
        document.Save(dataDir +"ApplyGradientShadingToText_out.pdf");
    }
}
```

>In order to apply a Radial Gradient, you can set ‘PatternColorSpace’ property equal to ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ in the above code snippet.

## How to align text to float content

Aspose.PDF supports setting text alignment for contents inside a Floating Box element. The alignment properties of Aspose.Pdf.FloatingBox instance can be used to achieve this as shown in the following code sample.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AlignTextToFloat()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create float box
        Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;
        floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_bottom"));
        floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_center"));
        floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox1);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_top"));
        floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox2);

        // Save PDF document
        document.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
    }
}
```

## How to remove hidden text from a PDF file

First, the code snippet creates a Document object from a file. Then, it adds a TextFragmentAbsorber to find and edit text. It then checks for hidden text and deletes it. Finally, it saves the updated document.

This method keeps visible text intact and preserves the layout.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
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
