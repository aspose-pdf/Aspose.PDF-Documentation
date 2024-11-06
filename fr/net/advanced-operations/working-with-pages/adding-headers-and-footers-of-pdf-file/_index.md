---
title: Ajouter un en-tête et un pied de page au PDF
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
weight: 70
url: fr/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un en-tête et un pied de page au PDF",
    "alternativeHeadline": "Comment ajouter un en-tête et un pied de page au fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, ajouter en-tête, ajouter pied de page dans pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp."
}
</script>

**Aspose.PDF pour .NET** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant. Vous pouvez ajouter des images ou du texte à un document PDF. Essayez également d'ajouter différents en-têtes dans un seul fichier PDF avec C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajout de texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) pour ajouter du texte dans l'en-tête d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez régler la propriété TopMargin de manière à ce qu'elle ajuste le texte dans la zone d'en-tête de votre PDF. Vous devez également définir l'HorizontalAlignment sur Center et le VerticalAlignment sur Top.

Le code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec C#.
Le code suivant montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// Créer un en-tête
TextStamp textStamp = new TextStamp("Texte de l'en-tête");
// Définir les propriétés du tampon
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Ajouter l'en-tête sur toutes les pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## Ajouter du texte dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF.
Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété Marge Inférieure de manière à ce qu'elle ajuste le texte dans la zone du pied de page de votre PDF. Vous devez également définir l'Alignement Horizontal à Centre et l'Alignement Vertical à Bas

{{% /alert %}}

Le code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Créer un pied de page
TextStamp textStamp = new TextStamp("Texte du pied de page");
// Définir les propriétés du tampon
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Ajouter le pied de page sur toutes les pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Sauvegarder le fichier de sortie
pdfDocument.Save(dataDir + "TextinFooter_out.pdf");
```
## Ajout d'une image dans l'en-tête d'un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) pour ajouter une image dans l'en-tête d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un timbre basé sur une image comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la Page pour ajouter l'image dans l'en-tête du PDF.

{{% alert color="primary" %}}

Vous devez régler la propriété TopMargin de manière à ce qu'elle ajuste l'image dans la zone de l'en-tête de votre PDF. Vous devez également régler HorizontalAlignment sur Center et VerticalAlignment sur Top.

{{% /alert %}}

Le code suivant montre comment ajouter une image dans l'en-tête d'un fichier PDF avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Créer l'en-tête
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Définir les propriétés du timbre
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Ajouter l'en-tête sur toutes les pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Sauvegarder le fichier de sortie
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## Ajout d'une image dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe Image Stamp pour ajouter une image dans le pied de page d'un fichier PDF. La classe Image Stamp offre les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter l'image dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez régler la propriété [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) de manière à ce qu'elle ajuste l'image dans la zone du pied de page de votre PDF. Vous devez également définir [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) à `Center` et [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) à `Bottom`.

{{% /alert %}}

Le code suivant montre comment ajouter une image dans le pied de page d'un fichier PDF avec C#.
Le code suivant montre comment ajouter une image dans le pied de page d'un fichier PDF avec C#.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Créer un pied de page
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Définir les propriétés du tampon
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Ajouter un pied de page sur toutes les pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Sauvegarder le fichier de sortie
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## Ajouter différents en-têtes dans un seul fichier PDF

Nous savons que nous pouvons ajouter TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés TopMargin ou Bottom Margin, mais parfois nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF.
Nous savons que nous pouvons ajouter TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés TopMargin ou Bottom Margin, mais parfois nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF.

Pour accomplir cette exigence, nous créerons des objets TextStamp individuels (le nombre d'objets dépend du nombre d'En-têtes/Pieds de page requis) et nous les ajouterons au document PDF. Nous pouvons également spécifier des informations de formatage différentes pour chaque objet de tampon. Dans l'exemple suivant, nous avons créé un objet Document et trois objets TextStamp, puis nous avons utilisé la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la Page pour ajouter le texte dans la section en-tête du PDF. Le fragment de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF pour .NET.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document source
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Créer trois tampons
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("En-tête 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("En-tête 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("En-tête 3");

// Définir l'alignement du tampon (placer le tampon en haut de la page, centré horizontalement)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Spécifier le style de police comme Gras
stamp1.TextState.FontStyle = FontStyles.Bold;
// Définir les informations de couleur de premier plan du texte en rouge
stamp1.TextState.ForegroundColor = Color.Red;
// Spécifier la taille de la police à 14
stamp1.TextState.FontSize = 14;

// Maintenant, nous devons définir l'alignement vertical du 2ème objet de tampon en Haut
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Définir les informations d'alignement horizontal pour le tampon comme centré
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Définir le facteur de zoom pour l'objet tampon
stamp2.Zoom = 10;

// Définir le formatage du 3ème objet de tampon
// Spécifier les informations d'alignement vertical pour l'objet de tampon en HAUT
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Définir les informations d'alignement horizontal pour l'objet de tampon comme centré
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Définir l'angle de rotation pour l'objet de tampon
stamp3.RotateAngle = 35;
// Définir le rose comme couleur de fond pour le tampon
stamp3.TextState.BackgroundColor = Color.Pink;
// Changer les informations de police pour le tampon en Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// Le premier tampon est ajouté à la première page;
doc.Pages[1].AddStamp(stamp1);
// Le deuxième tampon est ajouté à la deuxième page;
doc.Pages[2].AddStamp(stamp2);
// Le troisième tampon est ajouté à la troisième page.
doc.Pages[3].AddStamp(stamp3);
// Enregistrer le document mis à jour
doc.Save(dataDir + "MultiHeader_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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

