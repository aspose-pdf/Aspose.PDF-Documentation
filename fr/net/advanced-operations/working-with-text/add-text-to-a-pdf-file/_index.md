---
title: Add Text to PDF using C#
linktitle: Add Text to PDF
type: docs
weight: 10
url: /fr/net/add-text-to-pdf-file/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez à ajouter du texte à un PDF, à ajouter des fragments HTML ou à utiliser des polices OTF personnalisées.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "How to add Text to PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, add text to pdf",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez à ajouter du texte à un PDF, à ajouter des fragments HTML ou à utiliser des polices OTF personnalisées."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrez le PDF d'entrée en utilisant l'objet Document.
2. Obtenez la page particulière à laquelle vous voulez ajouter le texte.
3. Créez un objet TextFragment avec le texte d'entrée ainsi que d'autres propriétés de texte. L'objet TextBuilder créé à partir de cette page particulière – à laquelle vous souhaitez ajouter le texte – vous permet d'ajouter l'objet TextFragment à la page en utilisant la méthode AppendText.
4. Appelez la méthode Save de l'objet Document et enregistrez le fichier PDF de sortie.

## Ajout de Texte

Le code suivant vous montre comment ajouter du texte dans un fichier PDF existant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "input.pdf");

// Obtenir la page particulière
Page pdfPage = (Page)pdfDocument.Pages[1];

// Créer un fragment de texte
TextFragment textFragment = new TextFragment("texte principal");
textFragment.Position = new Position(100, 600);

// Définir les propriétés du texte
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Créer un objet TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Ajouter le fragment de texte à la page PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Enregistrer le document PDF résultant.
pdfDocument.Save(dataDir);
```
## Chargement de police à partir d'un flux

Le fragment de code suivant montre comment charger une police à partir d'un objet Stream lors de l'ajout de texte à un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Charger le fichier PDF d'entrée
Document doc = new Document( dataDir + "input.pdf");
// Créer un objet constructeur de texte pour la première page du document
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Créer un fragment de texte avec une chaîne d'exemple
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Charger la police TrueType dans un objet de flux
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Définir le nom de la police pour la chaîne de texte
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Spécifier la position pour le fragment de texte
        textFragment.Position = new Position(10, 10);
        // Ajouter le texte au TextBuilder pour qu'il puisse être placé sur le fichier PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Sauvegarder le document PDF résultant.
    doc.Save(dataDir);
}
```
## Ajouter du texte avec TextParagraph

Le code suivant vous montre comment ajouter du texte dans un document PDF en utilisant la classe [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Ouvrir le document
Document doc = new Document();
// Ajouter une page à la collection de pages de l'objet Document
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Créer un paragraphe de texte
TextParagraph paragraph = new TextParagraph();
// Définir le retrait des lignes suivantes
paragraph.SubsequentLinesIndent = 20;
// Spécifier l'emplacement pour ajouter TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Spécifier le mode d'enveloppement des mots
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Créer un fragment de texte
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Ajouter le fragment au paragraphe
paragraph.AppendLine(fragment1);
// Ajouter le paragraphe
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Sauvegarder le document PDF résultant.
doc.Save(dataDir);
```
## Ajouter un Hyperlien à TextSegment

Une page PDF peut comprendre un ou plusieurs objets TextFragment, où chaque objet TextFragment peut avoir une ou plusieurs instances de TextSegment. Pour définir un hyperlien pour TextSegment, la propriété Hyperlink de la classe [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) peut être utilisée en fournissant l'objet de l'instance Aspose.Pdf.WebHyperlink. Veuillez essayer d'utiliser le fragment de code suivant pour réaliser cette exigence.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer une instance de document
Document doc = new Document();
// Ajouter une page à la collection de pages du fichier PDF
Page page1 = doc.Pages.Add();
// Créer une instance de TextFragment
TextFragment tf = new TextFragment("Fragment de texte exemple");
// Définir l'alignement horizontal pour TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Créer un textsegment avec du texte exemple
TextSegment segment = new TextSegment(" ... Segment de texte 1...");
// Ajouter le segment à la collection de segments de TextFragment
tf.Segments.Add(segment);
// Créer un nouveau TextSegment
segment = new TextSegment("Lien vers Google");
// Ajouter le segment à la collection de segments de TextFragment
tf.Segments.Add(segment);
// Définir un hyperlien pour TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Définir la couleur de premier plan pour le segment de texte
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Définir la mise en forme du texte en italique
segment.TextState.FontStyle = FontStyles.Italic;
// Créer un autre objet TextSegment
segment = new TextSegment("TextSegment sans hyperlien");
// Ajouter le segment à la collection de segments de TextFragment
tf.Segments.Add(segment);
// Ajouter TextFragment à la collection de paragraphes de l'objet page
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Sauvegarder le document PDF résultant.
doc.Save(dataDir);
```
## Utiliser une police OTF

Aspose.PDF pour .NET offre la fonctionnalité d'utiliser des polices Custom/TrueType lors de la création/manipulation de contenus de fichiers PDF afin que les contenus du fichier soient affichés en utilisant des polices autres que les polices système par défaut. Depuis la version d'Aspose.PDF pour .NET 10.3.0, nous avons fourni le support pour les polices de type Open.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer une nouvelle instance de document
Document pdfDocument = new Document();
// Ajouter une page à la collection de pages du fichier PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Créer une instance de TextFragment avec un texte d'exemple
TextFragment fragment = new TextFragment("Texte d'exemple en police OTF");
// Trouver la police dans le répertoire des polices système
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// Ou vous pouvez même spécifier le chemin de la police OTF dans le répertoire système
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Spécifier pour intégrer la police dans le fichier PDF, afin qu'elle soit affichée correctement,
// Même si la police spécifique n'est pas installée/présente sur la machine cible
fragment.TextState.Font.IsEmbedded = true;
// Ajouter TextFragment à la collection de paragraphes de l'instance de Page
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
## Ajouter une chaîne HTML en utilisant DOM

La classe Aspose.Pdf.Generator.Text contient une propriété appelée IsHtmlTagSupported qui permet d'ajouter des balises/contenus HTML dans des fichiers PDF. Le contenu ajouté est rendu dans des balises HTML natives au lieu d'apparaître comme une simple chaîne de texte. Pour supporter une fonctionnalité similaire dans le nouveau Modèle d'Objet Document (DOM) de l'espace de noms Aspose.Pdf, la classe HtmlFragment a été introduite.

L'instance [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) peut être utilisée pour spécifier les contenus HTML qui doivent être placés à l'intérieur du fichier PDF. Semblable à TextFragment, HtmlFragment est un objet de niveau paragraphe et peut être ajouté à la collection de paragraphes de l'objet Page. Les extraits de code suivants montrent les étapes pour placer des contenus HTML à l'intérieur d'un fichier PDF en utilisant l'approche DOM.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Instancier l'objet Document
Document doc = new Document();
// Ajouter une page à la collection de pages du fichier PDF
Page page = doc.Pages.Add();
// Instancier HtmlFragment avec des contenus HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Tableau</i></b></fontsize>");
// Définir les informations de marge inférieure
title.Margin.Bottom = 10;
// Définir les informations de marge supérieure
title.Margin.Top = 200;
// Ajouter le Fragment HTML à la collection de paragraphes de la page
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Sauvegarder le fichier PDF
doc.Save(dataDir);
```
Le code suivant montre les étapes pour ajouter des listes ordonnées HTML dans le document :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Le chemin vers le document de sortie.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Instancier l'objet Document
Document doc = new Document();
// Instancier l'objet HtmlFragment avec le fragment HTML correspondant
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>Premier</li><li>Deuxième</li><li>Troisième</li><li>Quatrième</li><li>Cinquième</li></ul>Texte après la liste.<br/>Ligne suivante<br/>Dernière ligne</body>`");
// Ajouter une page dans la collection de pages
Page page = doc.Pages.Add();
// Ajouter HtmlFragment dans la page
page.Paragraphs.Add(t);
// Enregistrer le fichier PDF résultant
doc.Save(outFile);
```

Vous pouvez également définir le formatage de chaîne HTML en utilisant l'objet TextState comme suit :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("du texte");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
Dans le cas où vous définiriez des valeurs d'attributs de texte via le balisage HTML, puis fourniriez les mêmes valeurs dans les propriétés TextState, elles écraseront les paramètres HTML par les propriétés de l'instance TextState. Les extraits de code suivants montrent le comportement décrit.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instancier l'objet Document
Document doc = new Document();
// Ajouter une page à la collection de pages du fichier PDF
Page page = doc.Pages.Add();
// Instancier HtmlFragment avec des contenus HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
// La famille de polices 'Verdana' sera réinitialisée à 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Définir les informations de marge inférieure
title.Margin.Bottom = 10;
// Définir les informations de marge supérieure
title.Margin.Top = 400;
// Ajouter le Fragment HTML à la collection de paragraphes de la page
page.Paragraphs.Add(title);
// Enregistrer le fichier PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Enregistrer le fichier PDF
doc.Save(dataDir);
```
## Notes de bas de page et notes de fin (DOM)

Les notes de bas de page indiquent des notes dans le texte de votre document en utilisant des numéros en exposant consécutifs. La note elle-même est indentée et peut apparaître comme une note de bas de page au bas de la page.

### Ajouter une note de bas de page

Dans un système de référencement par note de bas de page, indiquez une référence en :

- plaçant un petit numéro au-dessus de la ligne de texte juste après le matériel source. Ce numéro est appelé un identifiant de note. Il se situe légèrement au-dessus de la ligne de texte.
- plaçant le même numéro, suivi d'une citation de votre source, au bas de la page. La numérotation des notes de bas de page doit être numérique et chronologique : la première référence est 1, la seconde est 2, et ainsi de suite.

L'avantage de la notation par notes de bas de page est que le lecteur peut simplement baisser les yeux vers le bas de la page pour découvrir la source d'une référence qui l'intéresse.

Veuillez suivre les étapes spécifiées ci-dessous pour créer une note de bas de page :

- Créez une instance de Document
- Créez un objet Page
- Créez un objet TextFragment
- Créez une instance de Note et passez sa valeur à la propriété TextFragment.FootNote
- Créer une instance de Note et passer sa valeur à la propriété TextFragment.FootNote
- Ajouter TextFragment à la collection de paragraphes d'une instance de page

### Style de ligne personnalisé pour FootNote

L'exemple suivant montre comment ajouter des notes de bas de page au bas de la page PDF et définir un style de ligne personnalisé.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer une instance de Document
Document doc = new Document();
// Ajouter une page à la collection de pages du PDF
Page page = doc.Pages.Add();
// Créer un objet GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Définir la largeur de ligne à 2
graph.LineWidth = 2;
// Définir la couleur pour l'objet graphique
graph.Color = Aspose.Pdf.Color.Red;
// Définir la valeur du tableau de pointillés à 3
graph.DashArray = new int[] { 3 };
// Définir la valeur de phase de pointillés à 1
graph.DashPhase = 1;
// Définir le style de ligne de note de bas de page pour la page comme graphique
page.NoteLineStyle = graph;
// Créer une instance de TextFragment
TextFragment text = new TextFragment("Hello World");
// Définir la valeur de FootNote pour TextFragment
text.FootNote = new Note("note de bas de page pour le texte de test 1");
// Ajouter TextFragment à la collection de paragraphes de la première page du document
page.Paragraphs.Add(text);
// Créer un second TextFragment
text = new TextFragment("Aspose.Pdf for .NET");
// Définir FootNote pour le second fragment de texte
text.FootNote = new Note("note de bas de page pour le texte de test 2");
// Ajouter le second fragment de texte à la collection de paragraphes du fichier PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Sauvegarder le document PDF résultant.
doc.Save(dataDir);
```
Nous pouvons définir le formatage de l'étiquette de note de bas de page (identifiant de note) en utilisant l'objet TextState comme suit :

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Personnaliser l'étiquette de la note de bas de page

Par défaut, le numéro de FootNote est incrémental à partir de 1. Cependant, nous pouvons avoir besoin de définir une étiquette de FootNote personnalisée. Pour accomplir cette exigence, veuillez essayer d'utiliser le fragment de code suivant

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer une instance Document
Document doc = new Document();
// Ajouter une page à la collection de pages du PDF
Page page = doc.Pages.Add();
// Créer un objet GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Définir la largeur de ligne à 2
graph.LineWidth = 2;
// Définir la couleur pour l'objet graphique
graph.Color = Aspose.Pdf.Color.Red;
// Définir la valeur du tableau de tirets à 3
graph.DashArray = new int[] { 3 };
// Définir la valeur de phase de tirets à 1
graph.DashPhase = 1;
// Définir le style de ligne de la note de bas de page pour la page comme graphique
page.NoteLineStyle = graph;
// Créer une instance de TextFragment
TextFragment text = new TextFragment("Hello World");
// Définir la valeur de FootNote pour TextFragment
text.FootNote = new Note("foot note for test text 1");
// Spécifier une étiquette personnalisée pour FootNote
text.FootNote.Text = " Aspose(2015)";
// Ajouter TextFragment à la collection de paragraphes de la première page du document
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## Ajout d'une image et d'un tableau en note de bas de page

Dans les versions antérieures, le support des notes de bas de page était fourni mais il était uniquement applicable à l'objet TextFragment. Cependant, à partir de la version Aspose.PDF pour .NET 10.7.0, vous pouvez également ajouter des notes de bas de page à d'autres objets dans le document PDF tels que Table, Cellules, etc. Le fragment de code suivant montre les étapes pour ajouter une note de bas de page à l'objet TextFragment puis ajouter un objet Image et un objet Tableau à la collection de paragraphes de la section de la note de bas de page.

```csharp

// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("du texte");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("texte de note de bas de page");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Ligne 1 Cellule 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Sauvegarder le document PDF résultant.
doc.Save(dataDir);
```
## Comment créer des notes de fin

Une note de fin est une citation de source qui renvoie les lecteurs à un endroit spécifique à la fin du document où ils peuvent trouver la source de l'information ou des mots cités ou mentionnés dans le document. Lors de l'utilisation de notes de fin, votre phrase citée ou paraphrasée ou votre matériel résumé est suivi d'un numéro en exposant.

L'exemple suivant montre comment ajouter une note de fin dans une page PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer une instance de Document
Document doc = new Document();
// Ajouter une page à la collection de pages du PDF
Page page = doc.Pages.Add();
// Créer une instance de TextFragment
TextFragment text = new TextFragment("Bonjour le monde");
// Définir la valeur FootNote pour TextFragment
text.EndNote = new Note("note de fin d'exemple");
// Spécifier une étiquette personnalisée pour FootNote
text.EndNote.Text = " Aspose(2015)";
// Ajouter TextFragment à la collection de paragraphes de la première page du document
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Sauvegarder le document PDF résultant.
doc.Save(dataDir);
```
## Texte et Image en Paragraphe en Ligne

La disposition par défaut du fichier PDF est la disposition en flux (De haut à gauche à bas à droite). Par conséquent, chaque nouvel élément ajouté au fichier PDF est ajouté dans le flux en bas à droite. Cependant, nous pouvons avoir besoin d'afficher divers éléments de page, c'est-à-dire Image et Texte, au même niveau (l'un après l'autre). Une approche peut être de créer une instance de Table et d'ajouter les deux éléments à des cellules individuelles. Cependant, une autre approche peut être le paragraphe en ligne. En définissant la propriété IsInLineParagraph de l'Image et du Texte sur true, ces paragraphes apparaîtront en ligne par rapport aux autres éléments de la page.

Le code suivant vous montre comment ajouter du texte et une Image en paragraphes en ligne dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instancier un document
Document doc = new Document();
// Ajouter une page à la collection de pages du document
Page page = doc.Pages.Add();
// Créer un fragment de texte
TextFragment text = new TextFragment("Bonjour le monde.. ");
// Ajouter le fragment de texte à la collection de paragraphes de l'objet Page
page.Paragraphs.Add(text);
// Créer une instance d'image
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Définir l'image comme paragraphe en ligne pour qu'elle apparaisse juste après
// l'objet de paragraphe précédent (TextFragment)
image.IsInLineParagraph = true;
// Spécifier le chemin du fichier image
image.File = dataDir + "aspose-logo.jpg";
// Définir la hauteur de l'image (optionnel)
image.FixHeight = 30;
// Définir la largeur de l'image (optionnel)
image.FixWidth = 100;
// Ajouter l'image à la collection de paragraphes de l'objet page
page.Paragraphs.Add(image);
// Réinitialiser l'objet TextFragment avec un contenu différent
text = new TextFragment(" Bonjour encore..");
// Définir TextFragment comme paragraphe en ligne
text.IsInLineParagraph = true;
// Ajouter le TextFragment nouvellement créé à la collection de paragraphes de la page
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## Spécifier l'espacement des caractères lors de l'ajout de texte

Un texte peut être ajouté à la collection de paragraphes de fichiers PDF en utilisant une instance de TextFragment ou en utilisant l'objet TextParagraph et même vous pouvez tamponner le texte à l'intérieur du PDF en utilisant la classe TextStamp. Lors de l'ajout du texte, nous pouvons avoir besoin de spécifier l'espacement des caractères pour les objets texte. Afin de répondre à cette exigence, une nouvelle propriété nommée propriété CharacterSpacing a été introduite. Veuillez examiner les approches suivantes pour répondre à cette exigence.

Les approches suivantes montrent les étapes pour spécifier l'espacement des caractères lors de l'ajout de texte à l'intérieur d'un document PDF.

### Utilisation de TextBuilder et TextFragment

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer une instance de Document
Document pdfDocument = new Document();
// Ajouter une page à la collection de pages de Document
Page page = pdfDocument.Pages.Add();
// Créer une instance de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Créer une instance de fragment de texte avec des contenus d'exemple
TextFragment wideFragment = new TextFragment("Texte avec un espacement des caractères augmenté");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Spécifier l'espacement des caractères pour TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Spécifier la position de TextFragment
wideFragment.Position = new Position(100, 650);
// Ajouter TextFragment à l'instance de TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
### Utilisation de TextParagraph

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer une instance de Document
Document pdfDocument = new Document();
// Ajouter une page à la collection de pages de Document
Page page = pdfDocument.Pages.Add();
// Créer une instance de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Instancier TextParagraph
TextParagraph paragraph = new TextParagraph();
// Créer une instance de TextState pour spécifier le nom de la police et la taille
TextState state = new TextState("Arial", 12);
// Spécifier l'espacement des caractères
state.CharacterSpacing = 1.5f;
// Ajouter du texte à l'objet TextParagraph
paragraph.AppendLine("Ceci est un paragraphe avec espacement des caractères", state);
// Spécifier la position pour TextParagraph
paragraph.Position = new Position(100, 550);
// Ajouter TextParagraph à l'instance de TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
### Utilisation de TextStamp

```csharp
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer une instance de Document
Document pdfDocument = new Document();
// Ajouter une page à la collection de pages du Document
Page page = pdfDocument.Pages.Add();
// Instancier TextStamp avec du texte d'exemple
TextStamp stamp = new TextStamp("Ceci est un tampon de texte avec un espacement des caractères");
// Spécifier le nom de la police pour l'objet Stamp
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Spécifier la taille de la police pour TextStamp
stamp.TextState.FontSize = 12;
// Spécifier l'espacement des caractères comme 1f
stamp.TextState.CharacterSpacing = 1f;
// Définir l'XIndent pour le Stamp
stamp.XIndent = 100;
// Définir l'YIndent pour le Stamp
stamp.YIndent = 500;
// Ajouter le tampon textuel à l'instance de page
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Enregistrer le document PDF résultant.
pdfDocument.Save(dataDir);
```

## Créer un document PDF multi-colonnes

Dans les magazines et les journaux, nous voyons principalement que les nouvelles sont affichées en plusieurs colonnes sur les pages uniques au lieu des livres où les paragraphes de texte sont principalement imprimés sur toute la page de gauche à droite. De nombreuses applications de traitement de documents comme Microsoft Word et Adobe Acrobat Writer permettent aux utilisateurs de créer plusieurs colonnes sur une seule page, puis d'ajouter des données.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) offre également la fonctionnalité de créer plusieurs colonnes à l'intérieur des pages des documents PDF.
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) offre également la possibilité de créer plusieurs colonnes à l'intérieur des pages des documents PDF.

L'espacement des colonnes désigne l'espace entre les colonnes et l'espacement par défaut entre les colonnes est de 1,25 cm. Si la largeur de la colonne n'est pas spécifiée, alors [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) calcule automatiquement la largeur de chaque colonne en fonction de la taille de la page et de l'espacement des colonnes.

Un exemple est donné ci-dessous pour démontrer la création de deux colonnes avec des objets Graphiques (Ligne) qui sont ajoutés à la collection de paragraphes de FloatingBox, qui est ensuite ajoutée à la collection de paragraphes de l'instance de Page.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Spécifier les informations de marge gauche pour le fichier PDF
doc.PageInfo.Margin.Left = 40;
// Spécifier les informations de marge droite pour le fichier PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Ajouter la ligne à la collection de paragraphes de l'objet section
page.Paragraphs.Add(graph1);

// Spécifier les coordonnées pour la ligne
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Créer des variables de chaîne avec du texte contenant des balises html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> Comment éviter les arnaques financières</<strong> "
+ "</font>";
// Créer des paragraphes de texte contenant du texte HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Ajouter quatre colonnes dans la section
box.ColumnInfo.ColumnCount = 2;
// Définir l'espacement entre les colonnes
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("Par A Googler (Le Blog Officiel de Google)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Créer un objet graphique pour dessiner une ligne
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Spécifier les coordonnées pour la ligne
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Ajouter la ligne à la collection de paragraphes de l'objet section
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Enregistrer le fichier PDF
doc.Save(dataDir);
```
## Travailler avec des tabulations personnalisées

Un arrêt de tabulation est un point d'arrêt pour la tabulation. Dans le traitement de texte, chaque ligne contient plusieurs arrêts de tabulation placés à intervalles réguliers (par exemple, tous les demi-pouces). Ils peuvent être modifiés, cependant, car la plupart des traitements de texte vous permettent de placer des arrêts de tabulation où vous le souhaitez. Lorsque vous appuyez sur la touche Tab, le curseur ou le point d'insertion saute au prochain arrêt de tabulation, qui est lui-même invisible. Bien que les arrêts de tabulation n'existent pas dans le fichier texte, le traitement de texte garde une trace d'eux afin de pouvoir réagir correctement à la touche Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permet aux développeurs d'utiliser des arrêts de tabulation personnalisés dans les documents PDF. La classe Aspose.Pdf.Text.TabStop est utilisée pour définir des arrêts TAB personnalisés dans la classe [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) offre également certains types de leaders de tabulation prédéfinis sous forme d'une énumération nommée TabLeaderType dont les valeurs prédéfinies et leurs descriptions sont données ci-dessous :
[Aspose.PDF pour .NET](https://docs.aspose.com/pdf/net/) propose également quelques types de tabulations prédéfinis sous forme d'une énumération appelée, TabLeaderType dont les valeurs prédéfinies et leurs descriptions sont données ci-dessous :

|**Type de Leader de Tabulation**|**Description**|
| :- | :- |
|None|Pas de leader de tabulation|
|Solid|Leader de tabulation plein|
|Dash|Leader de tabulation en tiret|
|Dot|Leader de tabulation en point|

Voici un exemple de comment définir des arrêts de TAB personnalisés.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("Ceci est un exemple de formation de tableau avec des arrêts de TAB", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## Comment ajouter du texte transparent dans un PDF

Un fichier PDF contient des objets Image, Texte, Graphique, pièce jointe, Annotations et lors de la création de TextFragment, vous pouvez définir les informations de couleur de premier plan, de fond ainsi que le formatage du texte. Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajout de texte avec canal de couleur Alpha. Le fragment de code suivant montre comment ajouter du texte avec une couleur transparente.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer une instance Document
Document doc = new Document();
// Créer une page à la collection de pages du fichier PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// Créer un objet Graph
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Créer une instance de rectangle avec certaines dimensions
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Créer un objet couleur à partir du canal de couleur Alpha
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Ajouter le rectangle à la collection de formes de l'objet Graph
canvas.Shapes.Add(rect);
// Ajouter l'objet graphique à la collection de paragraphes de l'objet page
page.Paragraphs.Add(canvas);
// Définir la valeur pour ne pas changer de position pour l'objet graphique
canvas.IsChangePosition = false;

// Créer une instance de TextFragment avec une valeur d'exemple
TextFragment text = new TextFragment("texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent ");
// Créer un objet couleur à partir du canal Alpha
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Définir les informations de couleur pour l'instance de texte
text.TextState.ForegroundColor = color;
// Ajouter le texte à la collection de paragraphes de l'instance de page
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## Spécifier l'interligne pour les polices

Chaque police possède un carré abstrait, dont la hauteur est la distance prévue entre les lignes de texte de la même taille de police.
Chaque police possède un carré abstrait, dont la hauteur est la distance prévue entre les lignes de texte de la même taille de caractère.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Charger le fichier PDF d'entrée
Document doc = new Document();
//Créer TextFormattingOptions avec LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Créer un objet constructeur de texte pour la première page du document
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Créer un fragment de texte avec une chaîne d'exemple
TextFragment textFragment = new TextFragment("Bonjour le monde");

if (fontFile != "")
{
    // Charger la police TrueType dans un objet stream
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Définir le nom de la police pour la chaîne de texte
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Spécifier la position pour le fragment de texte
        textFragment.Position = new Position(100, 600);
        //Définir les options de formatage de texte du fragment actuel sur celles prédéfinies (qui pointent vers LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Ajouter le texte au constructeur de texte pour qu'il puisse être placé sur le fichier PDF
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Sauvegarder le document PDF résultant
    doc.Save(dataDir);
}
```
## Obtenir dynamiquement la largeur du texte

Parfois, il est nécessaire d'obtenir la largeur du texte de manière dynamique. Aspose.PDF pour .NET comprend deux méthodes pour mesurer la largeur des chaînes de caractères. Vous pouvez invoquer la méthode [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) des classes Aspose.Pdf.Text.Font ou Aspose.Pdf.Text.TextState (ou les deux). Le fragment de code ci-dessous montre comment utiliser cette fonctionnalité.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("Mesure de chaîne de caractères de la police inattendue !");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("Mesure de chaîne de caractères de la police inattendue !");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("La mesure de la chaîne de caractères de la police et de l'état ne correspondent pas !");
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

