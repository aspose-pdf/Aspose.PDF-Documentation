---
title: Ajouter des tampons texte dans PDF C#
linktitle: Tampons texte dans un fichier PDF
type: docs
weight: 20
url: /fr/net/text-stamps-in-the-pdf-file/
description: Ajouter un tampon texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des tampons texte dans PDF C#",
    "alternativeHeadline": "Ajouter des tampons texte dans PDF C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, génération de document",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Ajouter un tampon texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF pour .NET."
}
</script>
## Ajouter un tampon de texte avec C#

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) pour ajouter un tampon de texte dans un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le tampon dans le PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// Créer un tampon de texte
TextStamp textStamp = new TextStamp("Sample Stamp");
// Définir si le tampon est en arrière-plan
textStamp.Background = true;
// Définir l'origine
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// Tourner le tampon
textStamp.Rotate = Rotation.on90;
// Définir les propriétés du texte
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// Ajouter le tampon à une page particulière
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// Sauvegarder le document de sortie
pdfDocument.Save(dataDir);
```
## Définir l'alignement pour l'objet TextStamp

L'ajout de filigranes aux documents PDF est l'une des fonctionnalités fréquemment demandées et Aspose.PDF pour .NET est entièrement capable d'ajouter des filigranes d'image ainsi que de texte. Nous avons une classe nommée [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) qui fournit la fonctionnalité d'ajouter des tampons textuels sur le fichier PDF. Récemment, il y a eu une exigence pour supporter la fonctionnalité de spécifier l'alignement du texte lors de l'utilisation de l'objet TextStamp. Afin de répondre à cette exigence, nous avons introduit la propriété TextAlignment dans la classe TextStamp. En utilisant cette propriété, nous pouvons spécifier l'alignement horizontal du texte.

Le code suivant montre un exemple sur comment charger un document PDF existant et ajouter un TextStamp dessus.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instancier l'objet Document avec le fichier d'entrée
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// Instancier l'objet FormattedText avec une chaîne d'exemple
FormattedText text = new FormattedText("Ceci");
// Ajouter une nouvelle ligne de texte à FormattedText
text.AddNewLineText("est un exemple");
text.AddNewLineText("Centré");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Objet");
// Créer l'objet TextStamp en utilisant FormattedText
TextStamp stamp = new TextStamp(text);
// Spécifier l'alignement horizontal du tampon texte comme centré
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// Spécifier l'alignement vertical du tampon texte comme centré
stamp.VerticalAlignment = VerticalAlignment.Center;
// Spécifier l'alignement horizontal du texte de TextStamp comme centré
stamp.TextAlignment = HorizontalAlignment.Center;
// Définir la marge supérieure pour l'objet tampon
stamp.TopMargin = 20;
// Ajouter l'objet tampon sur la première page du document
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```
## Remplir le texte en trait comme un tampon dans un fichier PDF

Nous avons mis en œuvre le paramétrage du mode de rendu pour les scénarios d'ajout et d'édition de texte. Pour rendre le texte en trait, veuillez créer un objet TextState et définir RenderingMode sur TextRenderingMode.StrokeText et sélectionner également une couleur pour la propriété StrokingColor. Ensuite, liez TextState au tampon en utilisant la méthode BindTextState().

Le fragment de code suivant démontre l'ajout de texte en remplissage et en trait :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// Créer un objet TextState pour transférer des propriétés avancées
TextState ts = new TextState();
// Définir la couleur pour le trait
ts.StrokingColor = Color.Gray;
// Définir le mode de rendu du texte
ts.RenderingMode = TextRenderingMode.StrokeText;
// Charger un document PDF d'entrée
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// Lier TextState
stamp.BindTextState(ts);
// Définir l'origine X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// Ajouter le tampon
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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

