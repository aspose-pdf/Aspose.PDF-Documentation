---
title: Formatting PDF Document using C#
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: Créez et formatez le document PDF avec Aspose.PDF pour .NET. Utilisez le prochain extrait de code pour résoudre vos tâches.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting PDF Document using C#",
    "alternativeHeadline": "How to format PDF Document in .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, dotnet, format pdf document",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "Créez et formatez le document PDF avec Aspose.PDF pour .NET. Utilisez le prochain extrait de code pour résoudre vos tâches."
}
</script>

## Formatage du document PDF

### Obtenir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application visualisatrice et comment les pages sont affichées. Pour définir ces propriétés :

Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Maintenant, vous pouvez définir les propriétés de l'objet Document, telles que :

- CenterWindow – Centrer la fenêtre du document sur l'écran. Par défaut : false.
- Direction – Ordre de lecture. Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Afficher le titre du document dans la barre de titre de la fenêtre du document. Par défaut : false (le titre est affiché).
- HideMenuBar – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : false (la barre de menu est affichée).
- HideToolBar – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : false (la barre d'outils est affichée).
- HideWindowUI – Masquer ou afficher les éléments de la fenêtre du document comme les barres de défilement. Par défaut : false (les éléments sont affichés).
- HideWindowUI – Masquer ou afficher les éléments de la fenêtre du document tels que les barres de défilement.
- NonFullScreenPageMode – Comment le document est affiché lorsqu'il n'est pas en mode plein écran.
- PageLayout – La disposition des pages.
- PageMode – Comment le document est affiché lorsqu'il est ouvert pour la première fois. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code suivant vous montre comment obtenir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Obtenir différentes propriétés du document
// Position de la fenêtre du document - Par défaut : false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// Ordre de lecture prédominant; détermine la position de la page
// Lorsqu'affichées côte à côte - Par défaut : L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// Si la barre de titre de la fenêtre doit afficher le titre du document
// Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// Si la fenêtre du document doit être redimensionnée pour s'adapter à la taille de
// La première page affichée - Par défaut : false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// Si la barre de menu de l'application de visualisation doit être masquée - Par défaut : false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// Si la barre d'outils de l'application de visualisation doit être masquée - Par défaut : false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// Si les éléments de l'interface utilisateur comme les barres de défilement doivent être masqués
// Et ne laisser afficher que le contenu de la page - Par défaut : false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// Mode de page du document. Comment afficher le document en quittant le mode plein écran.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// La disposition de la page, c'est-à-dire page unique, une colonne
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// Comment le document doit s'afficher lorsqu'ouvert
// c'est-à-dire afficher les vignettes, plein écran, afficher le panneau des pièces jointes
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Définir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage des pages. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Définissez les propriétés de l'objet Document.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

Les propriétés disponibles sont :

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Chacune est utilisée et décrite dans le code ci-dessous. Le - code suivant vous montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Définir différentes propriétés du document
// Spécifier pour positionner la fenêtre du document - Par défaut : false
pdfDocument.CenterWindow = true;

// Ordre de lecture prédominant ; détermine la position de la page
// Lorsqu'affichées côte à côte - Par défaut : L2R
pdfDocument.Direction = Direction.R2L;

// Spécifier si la barre de titre de la fenêtre doit afficher le titre du document
// Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
pdfDocument.DisplayDocTitle = true;

// Spécifier si redimensionner la fenêtre du document pour adapter la taille de
// La première page affichée - Par défaut : false
pdfDocument.FitWindow = true;

// Spécifier si masquer la barre de menu de l'application de visualisation - Par défaut : false
pdfDocument.HideMenubar = true;

// Spécifier si masquer la barre d'outils de l'application de visualisation - Par défaut : false
pdfDocument.HideToolBar = true;

// Spécifier si masquer les éléments de l'interface utilisateur comme les barres de défilement
// Et ne laisser que le contenu de la page affiché - Par défaut : false
pdfDocument.HideWindowUI = true;

// Mode de page du document. spécifier comment afficher le document en quittant le mode plein écran.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// Spécifier la disposition des pages, c'est-à-dire une seule page, une colonne
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// Spécifier comment le document doit s'afficher lorsqu'il est ouvert
// C'est-à-dire montrer les vignettes, en plein écran, montrer le panneau de pièces jointes
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Enregistrer le fichier PDF mis à jour
pdfDocument.Save(dataDir);
```
### Incorporation de polices dans un fichier PDF existant

Les lecteurs de PDF prennent en charge [un noyau de 14 polices](https://en.wikipedia.org/wiki/PDF#Text) afin que les documents puissent être affichés de la même manière, quelle que soit la plateforme sur laquelle le document est affiché. Lorsqu'un PDF contient une police qui n'est pas l'une des 14 polices de base, intégrez la police au fichier PDF pour éviter la substitution de polices.

Aspose.PDF pour .NET prend en charge l'incorporation de polices dans les fichiers PDF existants. Vous pouvez incorporer une police complète ou un sous-ensemble de la police. Pour incorporer la police, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Utilisez ensuite la classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) pour incorporer la police dans le fichier PDF. Pour incorporer la police complète, utilisez la propriété IsEmbeded de la classe Font ; pour utiliser un sous-ensemble de la police, utilisez la propriété IsSubset.

{{% alert color="primary" %}}

Un sous-ensemble de police n'incorpore que les caractères utilisés et est utile lorsque les polices sont utilisées pour des phrases courtes ou des slogans, par exemple lorsque une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal.
Un sous-ensemble de polices intègre uniquement les caractères utilisés et est utile là où les polices sont utilisées pour des phrases courtes ou des slogans, par exemple là où une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal.

{{% /alert %}}

Le code suivant montre comment intégrer une police dans un fichier PDF.

### Intégration des polices Standard Type 1

Certains documents PDF utilisent des polices d'un ensemble spécial de polices Adobe. Les polices de cet ensemble sont appelées "Polices Standard Type 1". Cet ensemble comprend 14 polices et l'intégration de ce type de polices nécessite l'utilisation de drapeaux spéciaux, par exemple [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Voici le fragment de code qui peut être utilisé pour obtenir un document avec toutes les polices intégrées, y compris les Polices Standard Type 1 :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Charger un document PDF existant
Document pdfDocument = new Document(dataDir + "input.pdf");
// Définir la propriété EmbedStandardFonts du document
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// Vérifier si la police est déjà intégrée
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Intégration de polices lors de la création de PDF

Si vous devez utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez intégrer la description de la police lors de la génération du fichier Pdf. Si les informations sur la police ne sont pas intégrées, Adobe Reader les prendra à partir du système d'exploitation si elles y sont installées, ou il construira une police de substitution en fonction du descripteur de police dans le Pdf.

>Veuillez noter que la police intégrée doit être installée sur la machine hôte, c'est-à-dire dans le cas du code suivant, la police ‘Univers Condensed’ est installée sur le système.

Nous utilisons la propriété IsEmbedded de la classe Font pour intégrer les informations de police dans le fichier Pdf. Définir la valeur de cette propriété sur ‘True’ intégrera le fichier de police complet dans le Pdf, sachant que cela augmentera la taille du fichier Pdf. Voici le fragment de code qui peut être utilisé pour intégrer les informations de police dans le Pdf.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciez l'objet Pdf en appelant son constructeur vide
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Créez une section dans l'objet Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" Ceci est un texte exemple utilisant une police personnalisée.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Sauvegardez le document PDF
doc.Save(dataDir);
```
### Définir le nom de la police par défaut lors de l'enregistrement en PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui-même ni sur l'appareil, l'API remplace ces polices par la police par défaut. Lorsque la police est disponible (elle est installée sur l'appareil ou intégrée dans le document), le PDF de sortie doit conserver la même police (elle ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (et non le chemin vers les fichiers de police). Nous avons mis en place une fonctionnalité pour définir le nom de la police par défaut lors de l'enregistrement d'un document en tant que PDF. Le fragment de code suivant peut être utilisé pour définir la police par défaut :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Charger un document PDF existant avec une police manquante
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Spécifier le nom de la police par défaut
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### Obtenir toutes les polices d'un document PDF

Si vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode FontUtilities.GetAllFonts() fournie dans la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Veuillez vérifier le fragment de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### Obtenir des avertissements pour la substitution de polices

Aspose.PDF pour .NET fournit des méthodes pour obtenir des notifications concernant la substitution de polices pour gérer les cas de substitution de polices. Les extraits de code ci-dessous montrent comment utiliser la fonctionnalité correspondante.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
La méthode **OnFontSubstitution** est listée ci-dessous.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("La police '{0}' a été substituée par une autre police '{1}'",
oldFont.FontName, newFont.FontName));
```

### Améliorer l'incorporation des polices en utilisant FontSubsetStrategy

La fonctionnalité pour incorporer les polices en tant que sous-ensemble peut être accomplie en utilisant la propriété IsSubset, mais parfois vous souhaitez réduire un ensemble de polices entièrement incorporées aux seuls sous-ensembles utilisés dans le document. Aspose.Pdf.Document possède la propriété FontUtilities qui inclut la méthode SubsetFonts(FontSubsetStrategy subsetStrategy). Dans la méthode SubsetFonts(), le paramètre subsetStrategy aide à ajuster la stratégie de sous-ensemble. FontSubsetStrategy prend en charge les deux variantes suivantes de sous-ensemencement de polices.

- SubsetAllFonts - Cela va sous-ensembler toutes les polices, utilisées dans un document.
- SubsetEmbeddedFontsOnly - Cela va sous-ensembler uniquement les polices qui sont entièrement incorporées dans le document.

Le code suivant montre comment définir FontSubsetStrategy:
Suivant l'extrait de code montre comment configurer FontSubsetStrategy :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// Toutes les polices seront intégrées comme sous-ensemble dans le document en cas de SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// Le sous-ensemble de polices sera intégré pour les polices entièrement intégrées mais les polices qui ne sont pas intégrées dans le document ne seront pas affectées.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### Obtenir-Définir le facteur de zoom d'un fichier PDF

Parfois, vous souhaitez déterminer quel est le facteur de zoom actuel d'un document PDF. Avec Aspose.Pdf, vous pouvez découvrir la valeur actuelle ainsi que définir une.

La propriété Destination de la classe [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) vous permet d'obtenir la valeur de zoom associée à un fichier PDF.
#### Définir le facteur de zoom

Le code suivant montre comment définir le facteur de zoom d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instancier un nouvel objet Document
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Sauvegarder le document
doc.Save(dataDir);
```

#### Obtenir le facteur de zoom

Le code suivant montre comment obtenir le facteur de zoom d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instancier un nouvel objet Document
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Créer un objet GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// Obtenir le facteur de zoom du fichier PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Valeur de zoom du document;
```
### Définir les propriétés prédéfinies de la boîte de dialogue d'impression

Aspoose.PDF permet de définir les propriétés prédéfinies de la boîte de dialogue d'impression d'un document PDF. Il vous permet de modifier la propriété DuplexMode pour un document PDF qui est défini sur simplex par défaut. Cela peut être réalisé en utilisant deux méthodologies différentes comme indiqué ci-dessous.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### Définir les propriétés prédéfinies de la boîte de dialogue d'impression en utilisant l'éditeur de contenu PDF

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("Le fichier a le retournement duplex par le petit bord");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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
```

