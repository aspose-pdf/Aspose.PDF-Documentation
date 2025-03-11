---
title: Rotar texto dentro de PDF usando C#
linktitle: Rotar texto dentro de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/rotate-text-inside-pdf/
description: Aprende cómo rotar texto dentro de archivos PDF en .NET usando Aspose.PDF para ajustar la alineación del texto y mejorar la presentación.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate Text Inside PDF using C#",
    "alternativeHeadline": "Rotate Text to Any Angle in PDF with C#",
    "abstract": "Aspose.PDF for .NET permite a los usuarios rotar fragmentos de texto y párrafos completos dentro de documentos PDF en varios ángulos. Esta función mejora la flexibilidad del documento al permitir ajustes precisos de orientación del texto, atendiendo a diversas necesidades de formato en aplicaciones profesionales y creativas. Los usuarios pueden implementar estas rotaciones sin esfuerzo utilizando las API proporcionadas, mejorando la experiencia de generación de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "860",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Aprende diferentes formas de rotar texto a PDF. Aspose.PDF te permite rotar texto a cualquier ángulo, rotar fragmento de texto o un párrafo completo."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Rotar texto dentro de PDF usando la propiedad de rotación

Al usar la propiedad de Rotación de la clase [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment), puedes rotar texto en varios ángulos. La rotación del texto se puede utilizar en diferentes escenarios de generación de documentos. Puedes especificar el ángulo de rotación en grados para rotar el texto según tus requisitos. Por favor, revisa los siguientes diferentes escenarios, en los que puedes implementar la rotación de texto.

## Implementar rotación usando TextFragment y TextBuilder

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment1.Position = new Aspose.Pdf.Text.Position(100, 600);
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create rotated text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("rotated text");
        textFragment2.Position = new Aspose.Pdf.Text.Position(200, 600);
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment2.TextState.Rotation = 45;
        // Create rotated text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("rotated text");
        textFragment3.Position = new Aspose.Pdf.Text.Position(300, 600);
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment3.TextState.Rotation = 90;
        // create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment1);
        textBuilder.AppendText(textFragment2);
        textBuilder.AppendText(textFragment3);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## Implementar rotación usando TextParagraph y TextBuilder (Fragmentos rotados)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.Position = new Aspose.Pdf.Text.Position(200, 600);
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment1.TextState.Rotation = 45;
        // Create text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("main text");
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("another rotated text");
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment3.TextState.Rotation = -45;
        // Append the text fragments to the paragraph
        paragraph.AppendLine(textFragment1);
        paragraph.AppendLine(textFragment2);
        paragraph.AppendLine(textFragment3);
        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text paragraph to the PDF page
        textBuilder.AppendParagraph(paragraph);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## Implementar rotación usando TextFragment y Page.Paragraphs

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("main text");
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment2.TextState.Rotation = 315;
        // Create text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment3.TextState.Rotation = 270;
        page.Paragraphs.Add(textFragment1);
        page.Paragraphs.Add(textFragment2);
        page.Paragraphs.Add(textFragment3);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## Implementar rotación usando TextParagraph y TextBuilder (Párrafo completo rotado)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        for (int i = 0; i < 4; i++)
        {
            var paragraph = new Aspose.Pdf.Text.TextParagraph();
            paragraph.Position = new Aspose.Pdf.Text.Position(200, 600);
            // Specify rotation
            paragraph.Rotation = i * 90 + 45;
            // Create text fragment
            var textFragment1 = new Aspose.Pdf.Text.TextFragment("Paragraph Text");
            // Create text fragment
            textFragment1.TextState.FontSize = 12;
            textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            // Create text fragment
            var textFragment2 = new Aspose.Pdf.Text.TextFragment("Second line of text");
            // Set text properties
            textFragment2.TextState.FontSize = 12;
            textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            // Create text fragment
            var textFragment3 = new Aspose.Pdf.Text.TextFragment("And some more text...");
            // Set text properties
            textFragment3.TextState.FontSize = 12;
            textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            textFragment3.TextState.Underline = true;
            paragraph.AppendLine(textFragment1);
            paragraph.AppendLine(textFragment2);
            paragraph.AppendLine(textFragment3);
            // Create TextBuilder object
            var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
            // Append the text fragment to the PDF page
            textBuilder.AppendParagraph(paragraph);
        }
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
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