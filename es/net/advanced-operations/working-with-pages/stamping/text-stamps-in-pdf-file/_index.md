---
title: Agregar sellos de texto en PDF C#
linktitle: Sellos de texto en archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/text-stamps-in-the-pdf-file/
description: Agregar un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF for .NET.
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
    "abstract": "La nueva función TextStamp en Aspose.PDF for .NET permite a los usuarios agregar sellos de texto personalizables a documentos PDF sin esfuerzo. Con propiedades para tamaño de fuente, estilo y color, junto con opciones de alineación, esta funcionalidad mejora la anotación de documentos al permitir la colocación y apariencia precisas del texto dentro de los archivos PDF.",
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
    "description": "Agregar un sello de texto a un documento PDF utilizando la clase TextStamp con la biblioteca Aspose.PDF for .NET."
}
</script>

## Agregar sello de texto

Puede usar la clase [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) para agregar un sello de texto en un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar un sello de texto, necesita crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puede llamar al método AddStamp de la página para agregar el sello en el PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código le muestra cómo agregar un sello de texto en el archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

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

## Definir alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características más solicitadas y Aspose.PDF for .NET es totalmente capaz de agregar marcas de agua de imagen así como de texto. Tenemos una clase llamada [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) que proporciona la función para agregar sellos de texto sobre el archivo PDF. Recientemente ha habido una necesidad de soportar la función de especificar la alineación del texto al usar el objeto TextStamp. Por lo tanto, para cumplir con este requisito, hemos introducido la propiedad TextAlignment en la clase TextStamp. Usando esta propiedad, podemos especificar la alineación horizontal del texto.

El siguiente fragmento de código muestra un ejemplo de cómo cargar un documento PDF existente y agregar un TextStamp sobre él.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DefineAlignmentForTextStampObject()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

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

## Rellenar texto de trazo como sello en archivo PDF

Hemos implementado la configuración del modo de renderizado para escenarios de adición y edición de texto. Para renderizar texto de trazo, por favor cree un objeto TextState y establezca RenderingMode en TextRenderingMode.StrokeText y también seleccione un color para la propiedad StrokingColor. Luego, vincule TextState al sello usando el método BindTextState().

El siguiente fragmento de código demuestra cómo agregar texto de trazo relleno:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillStrokeTextAsStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
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
        // Save PDF document
        fileStamp.Save(dataDir + "FillStrokeTextAsStampInPdfFile_out.pdf");
        fileStamp.Close();
    }
}
```

## Agregar sello de texto y ajustar automáticamente el tamaño de fuente

El siguiente fragmento de código demuestra cómo agregar un sello de texto a un archivo PDF y ajustar automáticamente el tamaño de fuente para que se ajuste al rectángulo del sello.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

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
El siguiente fragmento de código demuestra cómo agregar un sello de texto a un archivo PDF y ajustar automáticamente el tamaño de fuente para que se ajuste al rectángulo del sello. El rectángulo del sello tiene como tamaño predeterminado el tamaño de la página.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
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