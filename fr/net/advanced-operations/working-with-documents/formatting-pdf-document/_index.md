---
title: Mise en forme d'un document PDF en C#
linktitle: Mise en forme d'un document PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/formatting-pdf-document/
description: Créez et mettez en forme le document PDF avec Aspose.PDF for .NET. Utilisez le code suivant pour résoudre vos tâches.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "Découvrez la nouvelle fonctionnalité puissante de Aspose.PDF for .NET qui permet aux utilisateurs de créer et de mettre en forme des documents PDF sans effort. Avec un contrôle complet sur les propriétés du document telles que les paramètres d'affichage de la fenêtre, les options d'incorporation de polices et les facteurs de zoom personnalisables, les développeurs peuvent améliorer l'expérience utilisateur et maintenir l'intégrité du document sur différentes plateformes. Optimisez vos tâches de manipulation PDF avec cette fonctionnalité robuste qui améliore considérablement l'efficacité de vos applications .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Créez et mettez en forme le document PDF avec Aspose.PDF for .NET. Utilisez le code suivant pour résoudre vos tâches."
}
</script>

## Mise en forme d'un document PDF

### Obtenir les propriétés d'affichage de la fenêtre du document et de la page

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation et comment les pages sont affichées. Pour définir ces propriétés :

Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Maintenant, vous pouvez définir les propriétés de l'objet Document, telles que

- CenterWindow – Centrer la fenêtre du document à l'écran. Par défaut : false.
- Direction – Ordre de lecture. Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Afficher le titre du document dans la barre de titre de la fenêtre du document. Par défaut : false (le titre est affiché).
- HideMenuBar – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : false (la barre de menu est affichée).
- HideToolBar – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : false (la barre d'outils est affichée).
- HideWindowUI – Masquer ou afficher les éléments de la fenêtre du document comme les barres de défilement. Par défaut : false (les éléments de l'interface utilisateur sont affichés).
- NonFullScreenPageMode – Comment le document est affiché lorsqu'il n'est pas affiché en mode plein écran.
- PageLayout – La mise en page de la page.
- PageMode – Comment le document est affiché lors de sa première ouverture. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code suivant vous montre comment obtenir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### Définir les propriétés d'affichage de la fenêtre du document et de la page

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage de la page. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

Les propriétés disponibles sont :

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

Chacune est utilisée et décrite dans le code ci-dessous. Le code suivant montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### Incorporation de polices dans un fichier PDF existant

Les lecteurs PDF prennent en charge [un noyau de 14 polices](https://en.wikipedia.org/wiki/PDF#Text) afin que les documents puissent être affichés de la même manière, quelle que soit la plateforme sur laquelle le document est affiché. Lorsqu'un PDF contient une police qui n'est pas l'une des 14 polices de base, incorporez la police dans le fichier PDF pour éviter la substitution de police.

Aspose.PDF for .NET prend en charge l'incorporation de polices dans des fichiers PDF existants. Vous pouvez incorporer une police complète ou un sous-ensemble de la police. Pour incorporer la police, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ensuite, utilisez la classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) pour incorporer la police dans le fichier PDF. Pour incorporer la police complète, utilisez la propriété IsEmbeded de la classe Font ; pour utiliser un sous-ensemble de la police, utilisez la propriété IsSubset.

{{% alert color="primary" %}}

Un sous-ensemble de police incorpore uniquement les caractères qui sont utilisés et est utile lorsque les polices sont utilisées pour de courtes phrases ou slogans, par exemple lorsque une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal. L'utilisation d'un sous-ensemble réduit la taille du fichier PDF de sortie. Cependant, si une police personnalisée est utilisée pour le texte principal, incorporez-la dans son intégralité.

{{% /alert %}}

Le code suivant montre comment incorporer une police dans un fichier PDF.

### Incorporation de polices standard de type 1

Certains documents PDF ont des polices d'un ensemble de polices Adobe spécial. Les polices de cet ensemble sont appelées "Polices standard de type 1". Cet ensemble comprend 14 polices et l'incorporation de ce type de polices nécessite l'utilisation de drapeaux spéciaux, c'est-à-dire [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Le code suivant peut être utilisé pour obtenir un document avec toutes les polices incorporées, y compris les polices standard de type 1 :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### Incorporation de polices lors de la création d'un PDF

Si vous devez utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez incorporer la description de la police lors de la génération du fichier PDF. Si les informations sur la police ne sont pas incorporées, Adobe Reader les prendra à partir du système d'exploitation si elles sont installées sur le système, ou il construira une police de substitution selon le descripteur de police dans le PDF.

>Veuillez noter que la police incorporée doit être installée sur la machine hôte, c'est-à-dire que dans le cas du code suivant, la police 'Univers Condensed' est installée sur le système.

Nous utilisons la propriété IsEmbedded de la classe Font pour incorporer les informations de police dans le fichier PDF. Définir la valeur de cette propriété sur 'True' incorporera le fichier de police complet dans le PDF, sachant que cela augmentera la taille du fichier PDF. Le code suivant peut être utilisé pour incorporer les informations de police dans le PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### Définir le nom de police par défaut lors de l'enregistrement du PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui-même et sur l'appareil, l'API remplace ces polices par la police par défaut. Lorsque la police est disponible (installée sur l'appareil ou incorporée dans le document), le PDF de sortie doit avoir la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (pas le chemin vers les fichiers de police). Nous avons mis en œuvre une fonctionnalité pour définir le nom de la police par défaut lors de l'enregistrement d'un document en tant que PDF. Le code suivant peut être utilisé pour définir la police par défaut :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### Obtenir toutes les polices d'un document PDF

Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode FontUtilities.GetAllFonts() fournie dans la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Veuillez consulter le code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### Obtenir des avertissements pour la substitution de police

Aspose.PDF for .NET fournit des méthodes pour obtenir des notifications concernant la substitution de police afin de gérer les cas de substitution de police. Les extraits de code ci-dessous montrent comment utiliser la fonctionnalité correspondante.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

La méthode **OnFontSubstitution** est listée ci-dessous.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### Améliorer l'incorporation de polices en utilisant FontSubsetStrategy

La fonctionnalité d'incorporation des polices en tant que sous-ensemble peut être réalisée en utilisant la propriété IsSubset, mais parfois vous souhaitez réduire un ensemble de polices entièrement incorporées à seulement des sous-ensembles qui sont utilisés dans le document. Aspose.Pdf.Document a une propriété FontUtilities qui inclut la méthode SubsetFonts(FontSubsetStrategy subsetStrategy). Dans la méthode SubsetFonts(), le paramètre subsetStrategy aide à affiner la stratégie de sous-ensemble. FontSubsetStrategy prend en charge deux variantes suivantes de sous-ensembles de polices.

- SubsetAllFonts - Cela sous-ensemencera toutes les polices utilisées dans un document.
- SubsetEmbeddedFontsOnly - Cela sous-ensemencera uniquement les polices qui sont entièrement incorporées dans le document.

Le code suivant montre comment définir FontSubsetStrategy :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### Obtenir-Définir le facteur de zoom d'un fichier PDF

Parfois, vous souhaitez déterminer quel est le facteur de zoom actuel d'un document PDF. Avec Aspose.Pdf, vous pouvez découvrir la valeur actuelle ainsi que définir une.

La propriété Destination de la classe [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) vous permet d'obtenir la valeur de zoom associée à un fichier PDF. De même, elle peut être utilisée pour définir le facteur de zoom d'un fichier.

#### Définir le facteur de zoom

Le code suivant montre comment définir le facteur de zoom d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### Obtenir le facteur de zoom

Le code suivant montre comment obtenir le facteur de zoom d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### Définir les propriétés prédéfinies de la boîte de dialogue d'impression

Aspose.PDF permet de définir les propriétés prédéfinies de la boîte de dialogue d'impression d'un document PDF. Il vous permet de changer la propriété DuplexMode pour un document PDF qui est définie sur simplex par défaut. Cela peut être réalisé en utilisant deux méthodologies différentes comme indiqué ci-dessous.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### Définir les propriétés prédéfinies de la boîte de dialogue d'impression en utilisant l'éditeur de contenu PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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