---
title: Formatage du texte dans un PDF en utilisant C#
linktitle: Formatage du texte dans un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/text-formatting-inside-pdf/
description: Apprenez à formater le texte dans un document PDF en .NET en utilisant Aspose.PDF pour améliorer la présentation visuelle du document.
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
    "abstract": "Découvrez les puissantes capacités de formatage de texte de Aspose.PDF for .NET, vous permettant d'ajouter des retraits de ligne, des bordures de texte, des effets de soulignement, et plus encore à vos documents PDF. Cette fonctionnalité permet un contrôle précis sur l'esthétique et la mise en page du texte, améliorant la présentation globale de vos fichiers PDF. Optimisez vos flux de génération de PDF avec des options de formatage polyvalentes adaptées aux développeurs.",
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
    "description": "Cette page explique comment formater le texte à l'intérieur de votre fichier PDF. Il y a l'ajout de retrait de ligne, l'ajout de bordure de texte, l'ajout de texte souligné, etc."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Comment ajouter un retrait de ligne à un PDF

Aspose.PDF for .NET offre la propriété SubsequentLinesIndent dans la classe [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Elle peut être utilisée pour spécifier le retrait de ligne dans les scénarios de génération de PDF avec TextFragment et la collection de Paragraphes.

Veuillez utiliser le code suivant pour utiliser la propriété :

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

## Comment ajouter une bordure de texte

Le code suivant montre comment ajouter une bordure à un texte en utilisant TextBuilder et en définissant la propriété DrawTextRectangleBorder de TextState :

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

## Comment ajouter du texte souligné

Le code suivant vous montre comment ajouter du texte souligné lors de la création d'un nouveau fichier PDF.

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

## Comment ajouter une bordure autour du texte ajouté

Vous avez le contrôle sur l'apparence du texte que vous ajoutez. L'exemple ci-dessous montre comment ajouter une bordure autour d'un morceau de texte que vous avez ajouté en traçant un rectangle autour. Découvrez-en plus sur la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

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

## Comment ajouter un saut de ligne

TextFragment ne prend pas en charge le saut de ligne à l'intérieur du texte. Cependant, pour ajouter du texte avec un saut de ligne, veuillez utiliser TextFragment avec TextParagraph :

- Utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu d'un simple "\n".
- Créez un objet TextParagraph. Cela ajoutera du texte avec des coupures de ligne.
- Ajoutez le TextFragment avec TextParagraph.AppendLine.
- Ajoutez le TextParagraph avec TextBuilder.AppendParagraph.

Veuillez utiliser le code ci-dessous.

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

## Comment ajouter du texte barré

La classe TextState fournit les capacités pour définir le formatage des TextFragments placés à l'intérieur d'un document PDF. Vous pouvez utiliser cette classe pour définir le formatage du texte en Gras, Italique, Souligné et à partir de cette version, l'API a fourni les capacités de marquer le formatage du texte comme Barré. Veuillez essayer d'utiliser le code suivant pour ajouter un TextFragment avec un formatage barré.

Veuillez utiliser le code complet :

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

## Appliquer un dégradé de couleur au texte

Le formatage du texte a été encore amélioré dans l'API pour les scénarios d'édition de texte et vous pouvez maintenant ajouter du texte avec un espace coloré à motifs à l'intérieur d'un document PDF. La classe Aspose.Pdf.Color a été améliorée en introduisant une nouvelle propriété de PatternColorSpace, qui peut être utilisée pour spécifier les couleurs d'ombrage pour le texte. Cette nouvelle propriété ajoute différents dégradés de couleur au texte, par exemple, un ombrage axial, un ombrage radial (Type 3) comme montré dans le code suivant :

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

>Pour appliquer un dégradé radial, vous pouvez définir la propriété ‘PatternColorSpace’ égale à ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ dans le code ci-dessus.

## Comment aligner le texte avec le contenu flottant

Aspose.PDF prend en charge la définition de l'alignement du texte pour les contenus à l'intérieur d'un élément Floating Box. Les propriétés d'alignement de l'instance Aspose.Pdf.FloatingBox peuvent être utilisées pour y parvenir comme montré dans l'exemple de code suivant.

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

## Comment supprimer le texte caché d'un fichier PDF

Tout d'abord, le code crée un objet Document à partir d'un fichier. Ensuite, il ajoute un TextFragmentAbsorber pour trouver et éditer le texte. Il vérifie ensuite les textes cachés et les supprime. Enfin, il enregistre le document mis à jour.

Cette méthode garde le texte visible intact et préserve la mise en page.

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