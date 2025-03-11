---
title: Ajouter des tampons de texte dans PDF C#
linktitle: Tampons de texte dans le fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/text-stamps-in-the-pdf-file/
description: Ajouter un tampon de texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF for .NET.
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
    "abstract": "La nouvelle fonctionnalité TextStamp dans Aspose.PDF for .NET permet aux utilisateurs d'ajouter facilement des tampons de texte personnalisables aux documents PDF. Avec des propriétés pour la taille de police, le style et la couleur, ainsi que des options d'alignement, cette fonctionnalité améliore l'annotation des documents en permettant un placement et une apparence précis du texte dans les fichiers PDF.",
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
    "description": "Ajouter un tampon de texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF for .NET."
}
</script>

## Ajouter un tampon de texte

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) pour ajouter un tampon de texte dans un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le tampon dans le PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

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

## Définir l'alignement pour l'objet TextStamp

Ajouter des filigranes aux documents PDF est l'une des fonctionnalités les plus demandées et Aspose.PDF for .NET est entièrement capable d'ajouter des filigranes d'image ainsi que des filigranes de texte. Nous avons une classe nommée [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) qui fournit la fonctionnalité d'ajouter des tampons de texte sur le fichier PDF. Récemment, il y a eu une demande pour prendre en charge la fonctionnalité de spécifier l'alignement du texte lors de l'utilisation de l'objet TextStamp. Ainsi, pour répondre à cette exigence, nous avons introduit la propriété TextAlignment dans la classe TextStamp. En utilisant cette propriété, nous pouvons spécifier l'alignement horizontal du texte.

Le code suivant montre un exemple de la façon de charger un document PDF existant et d'ajouter un TextStamp dessus.

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

## Remplir le texte de contour en tant que tampon dans le fichier PDF

Nous avons mis en œuvre le réglage du mode de rendu pour les scénarios d'ajout et d'édition de texte. Pour rendre le texte de contour, veuillez créer un objet TextState et définir RenderingMode sur TextRenderingMode.StrokeText et sélectionner également une couleur pour la propriété StrokingColor. Ensuite, liez TextState au tampon en utilisant la méthode BindTextState().

Le code suivant démontre l'ajout de texte de contour rempli :

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

## Ajouter un tampon de texte et ajuster automatiquement la taille de la police

Le code suivant démontre comment ajouter un tampon de texte à un fichier PDF et ajuster automatiquement la taille de la police pour s'adapter au rectangle du tampon.

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
Le code suivant démontre comment ajouter un tampon de texte à un fichier PDF et ajuster automatiquement la taille de la police pour s'adapter au rectangle du tampon. Le rectangle du tampon par défaut correspond à la taille de la page.

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