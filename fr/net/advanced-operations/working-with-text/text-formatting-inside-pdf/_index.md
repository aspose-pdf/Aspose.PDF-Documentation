---
title: Formatage de texte dans un PDF en utilisant C#
linktitle: Formatage de texte dans un PDF
type: docs
weight: 30
url: /fr/net/text-formatting-inside-pdf/
description: Cette page explique comment formater du texte dans votre fichier PDF. Il y a l'ajout d'indentation de ligne, l'ajout de bordure de texte, l'ajout de texte souligné, et etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatage de texte dans un PDF en utilisant C#",
    "alternativeHeadline": "Comment formater du texte dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, formater du texte dans un pdf",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette page explique comment formater du texte dans votre fichier PDF. Il y a l'ajout d'indentation de ligne, l'ajout de bordure de texte, l'ajout de texte souligné, et etc."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Comment ajouter un retrait de ligne à un PDF

Aspose.PDF pour .NET propose la propriété SubsequentLinesIndent dans la classe [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Elle peut être utilisée pour spécifier le retrait de ligne dans les scénarios de génération de PDF avec TextFragment et la collection de Paragraphes.

Veuillez utiliser le code suivant pour utiliser la propriété :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer un nouvel objet document
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("Un renard brun rapide a sauté par-dessus le chien paresseux. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Initialiser TextFormattingOptions pour le fragment de texte et spécifier la valeur SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Ligne2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Ligne3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Ligne4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Ligne5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## Comment ajouter une bordure de texte

Le code suivant montre comment ajouter une bordure à un texte en utilisant TextBuilder et en définissant la propriété DrawTextRectangleBorder de TextState :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer un nouvel objet document
Document pdfDocument = new Document();
// Obtenir une page spécifique
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Créer un fragment de texte
TextFragment textFragment = new TextFragment("texte principal");
textFragment.Position = new Position(100, 600);
// Définir les propriétés du texte
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Définir la propriété StrokingColor pour dessiner une bordure (contour) autour du rectangle de texte
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Définir la valeur de la propriété DrawTextRectangleBorder à true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Sauvegarder le document
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## Comment ajouter du texte souligné

Le code suivant vous montre comment ajouter du texte souligné lors de la création d'un nouveau fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer un objet document
Document pdfDocument = new Document();
// Ajouter une page au document PDF
pdfDocument.Pages.Add();
// Créer un TextBuilder pour la première page
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment avec un texte d'exemple
TextFragment fragment = new TextFragment("Test message");
// Définir la police pour TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Définir le formatage du texte en souligné
fragment.TextState.Underline = true;
// Spécifier la position où TextFragment doit être placé
fragment.Position = new Position(10, 800);
// Ajouter TextFragment au fichier PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
## Comment ajouter une bordure autour du texte ajouté

Vous avez le contrôle sur l'apparence du texte que vous ajoutez. L'exemple ci-dessous montre comment ajouter une bordure autour d'un morceau de texte que vous avez ajouté en dessinant un rectangle autour de celui-ci. Découvrez en plus sur la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Enregistrer le document PDF résultant.
editor.Save(dataDir);
```

## Comment ajouter un saut de ligne
## Comment ajouter un saut de ligne

TextFragment ne prend pas en charge le saut de ligne à l'intérieur du texte. Cependant, pour ajouter du texte avec un saut de ligne, veuillez utiliser TextFragment avec TextParagraph :

- utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu de "\n" simple ;
- créez un objet TextParagraph. Cela ajoutera du texte avec un saut de ligne ;
- ajoutez le TextFragment avec TextParagraph.AppendLine ;
- ajoutez le TextParagraph avec TextBuilder.AppendParagraph.
Veuillez utiliser le fragment de code ci-dessous.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Initialisez un nouveau TextFragment avec du texte contenant les marqueurs de nouvelle ligne requis
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nom du candidat: " + Environment.NewLine + " Joe Smoe");

// Définissez les propriétés du fragment de texte si nécessaire
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Créez un objet TextParagraph
TextParagraph par = new TextParagraph();

// Ajoutez un nouveau TextFragment au paragraphe
par.AppendLine(textFragment);

// Définissez la position du paragraphe
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Créez un objet TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Ajoutez le TextParagraph en utilisant TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Enregistrez le document PDF résultant.
pdfApplicationDoc.Save(dataDir);
```
## Comment ajouter du texte barré

La classe TextState offre les capacités de définir le formatage pour les TextFragments placés dans un document PDF. Vous pouvez utiliser cette classe pour définir le formatage du texte comme Gras, Italique, Souligné et, à partir de cette version, l'API a fourni les capacités de marquer le formatage du texte comme barré. Veuillez essayer d'utiliser le fragment de code suivant pour ajouter un TextFragment avec un formatage barré.

Veuillez utiliser le fragment de code complet :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Ouvrir le document
Document pdfDocument = new Document();
// Obtenir une page spécifique
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Créer un fragment de texte
TextFragment textFragment = new TextFragment("texte principal");
textFragment.Position = new Position(100, 600);

// Définir les propriétés du texte
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Définir la propriété StrikeOut
textFragment.TextState.StrikeOut = true;
// Marquer le texte comme Gras
textFragment.TextState.FontStyle = FontStyles.Bold;

// Créer un objet TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Ajouter le fragment de texte à la page PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
## Appliquer un ombrage dégradé au texte

La mise en forme du texte a été améliorée dans l'API pour les scénarios d'édition de texte et maintenant vous pouvez ajouter du texte avec un espace colorimétrique de motif à l'intérieur d'un document PDF. La classe Aspose.Pdf.Color a été améliorée en introduisant une nouvelle propriété de PatternColorSpace, qui peut être utilisée pour spécifier des couleurs d'ombrage pour le texte. Cette nouvelle propriété ajoute différents ombrages dégradés au texte, par exemple l'ombrage axial, l'ombrage radial (Type 3) comme le montre le code suivant :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Créer une nouvelle couleur avec espace colorimétrique de motif
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>Pour appliquer un dégradé radial, vous pouvez définir la propriété 'PatternColorSpace' égale à 'Aspose.Pdf.Drawing.GradientRadialShading(couleurDeDépart, couleurFinale)' dans l'extrait de code ci-dessus.

## Comment aligner le texte pour flotter le contenu

Aspose.PDF permet de définir l'alignement du texte pour les contenus à l'intérieur d'un élément Boîte Flottante. Les propriétés d'alignement de l'instance Aspose.Pdf.FloatingBox peuvent être utilisées pour cela comme montré dans l'exemple de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organisation",
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
                "@type": "Point de contact",
                "telephone": "+1 903 306 1676",
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "Point de contact",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "Point de contact",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offre",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "Évaluation globale",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

