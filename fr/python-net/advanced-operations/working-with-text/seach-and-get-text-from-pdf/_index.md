---
title: Rechercher et Obtenir du Texte à partir des Pages d'un PDF
linktitle: Rechercher et Obtenir du Texte
type: docs
weight: 60
url: /fr/python-net/search-and-get-text-from-pdf/
description: Cet article explique comment utiliser divers outils pour rechercher et obtenir du texte à partir d'Aspose.PDF pour .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rechercher et Obtenir du Texte à partir des Pages d'un PDF",
    "alternativeHeadline": "Outils pour rechercher et obtenir du texte à partir des Pages d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, rechercher du texte, obtenir du texte à partir de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Cet article explique comment utiliser divers outils pour rechercher et obtenir du texte à partir d'Aspose.PDF pour .NET."
}
</script>


## Rechercher et obtenir du texte à partir de toutes les pages d'un document PDF

La classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) vous permet de trouver du texte, correspondant à une phrase particulière, à partir de toutes les pages d'un document PDF. Afin de rechercher du texte dans tout le document, vous devez appeler la méthode Accept de la collection Pages. La méthode [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) prend un objet TextFragmentAbsorber comme paramètre, qui renvoie une collection d'objets TextFragment. Vous pouvez parcourir tous les fragments et obtenir leurs propriétés comme Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

L'extrait de code suivant montre comment rechercher du texte à partir de toutes les pages.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Parcourir les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Texte : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Police - Nom : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Police - Est accessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Police - Est intégrée : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Police - Est un sous-ensemble : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Taille de la police : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Couleur de premier plan : {0} ", textFragment.TextState.ForegroundColor);
}
```


Au cas où vous auriez besoin de rechercher du texte à l'intérieur d'une page PDF particulière, veuillez spécifier le numéro de la page dans la collection de pages de l'instance Document et appeler la méthode Accept pour cette page (comme montré dans la ligne de code ci-dessous).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Accepter l'absorbeur pour une page particulière
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Rechercher et Obtenir des Segments de Texte de Toutes les Pages du Document PDF

Afin de rechercher des segments de texte de toutes les pages, vous devez d'abord obtenir les objets TextFragment du document.
 TextFragmentAbsorber vous permet de trouver du texte, correspondant à une phrase particulière, à partir de toutes les pages d'un document PDF. Afin de rechercher du texte dans l'ensemble du document, vous devez appeler la méthode Accept de la collection Pages. La méthode Accept prend l'objet TextFragmentAbsorber comme paramètre, qui renvoie une collection d'objets TextFragment. Une fois que la TextFragmentCollection est récupérée du document, vous devez parcourir cette collection et obtenir TextSegmentCollection de chaque objet TextFragment. Après cela, vous pouvez obtenir toutes les propriétés de l'objet TextSegment individuel. Le snippet de code suivant vous montre comment rechercher des segments de texte à partir de toutes les pages.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Obtenez les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Parcourir les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Texte : {0} ", textSegment.Text);
        Console.WriteLine("Position : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Police - Nom : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Police - Est accessible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Police - Est incorporée : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Police - Est un sous-ensemble : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Taille de la police : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Couleur de premier plan : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

Pour rechercher et obtenir des TextSegments à partir d'une page particulière d'un PDF, vous devez spécifier l'index de la page particulière lors de l'appel de la méthode Accept(..). Veuillez jeter un œil aux lignes de code suivantes.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Rechercher et obtenir du texte de toutes les pages à l'aide d'une expression régulière

TextFragmentAbsorber vous aide à rechercher et à récupérer du texte, de toutes les pages, basé sur une expression régulière.
 Tout d'abord, vous devez passer une expression régulière au constructeur de TextFragmentAbsorber en tant que phrase. Après cela, vous devez définir la propriété TextSearchOptions de l'objet TextFragmentAbsorber. Cette propriété nécessite un objet TextSearchOptions et vous devez passer true en tant que paramètre à son constructeur lors de la création de nouveaux objets. Comme vous souhaitez récupérer le texte correspondant de toutes les pages, vous devez appeler la méthode Accept de la collection Pages. TextFragmentAbsorber renvoie une TextFragmentCollection contenant tous les fragments correspondant aux critères spécifiés par l'expression régulière. L'extrait de code suivant vous montre comment rechercher et obtenir du texte de toutes les pages en fonction d'une expression régulière.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Comme 1999-2000

// Définir l'option de recherche de texte pour spécifier l'utilisation de l'expression régulière
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Boucle à travers les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texte : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Police - Nom : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Police - EstAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Police - EstIntégrée : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Police - EstSous-ensemble : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Taille de la police : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Couleur de premier plan : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Afin de rechercher une correspondance exacte d'un mot, vous pouvez envisager d'utiliser une expression régulière.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Afin de rechercher une chaîne en majuscules ou minuscules, vous pouvez envisager d'utiliser une expression régulière.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Afin de rechercher toutes les chaînes (analyser toutes les chaînes) à l'intérieur du document PDF, veuillez essayer d'utiliser l'expression régulière suivante.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Trouver la correspondance de la chaîne de recherche et obtenir tout ce qui suit la chaîne jusqu'à la rupture de ligne.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Veuillez utiliser l'expression régulière suivante pour trouver le texte suivant la correspondance regex.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Afin de rechercher des Hyperliens/URL's à l'intérieur du document PDF, veuillez essayer d'utiliser l'expression régulière suivante.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## Rechercher du Texte basé sur une Expression Régulière et Ajouter un Hyperlien

Si vous souhaitez ajouter un hyperlien sur une phrase de texte basée sur une expression régulière, commencez par trouver toutes les phrases correspondant à cette expression régulière particulière en utilisant TextFragmentAbsorber et ajoutez un hyperlien sur ces phrases.

Pour trouver une phrase et ajouter un hyperlien sur celle-ci :

1. Passez l'expression régulière en tant que paramètre au constructeur TextFragmentAbsorber.
2. Créez un objet TextSearchOptions qui spécifie si l'expression régulière est utilisée ou non.
3. Obtenez les phrases correspondantes dans TextFragments.
4. Parcourez les correspondances pour obtenir leurs dimensions rectangulaires, changez la couleur de premier plan en bleu (optionnel - pour qu'il apparaisse comme un hyperlien et créez un lien en utilisant la méthode CreateWebLink(..) de la classe PdfContentEditor.
5. Enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.
Le code suivant vous montre comment rechercher du texte à l'intérieur d'un fichier PDF en utilisant une expression régulière et ajouter des hyperliens sur les correspondances.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Créer un objet absorbeur pour trouver toutes les instances de la phrase de recherche entrée
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Activer la recherche par expression régulière
absorber.TextSearchOptions = new TextSearchOptions(true);
// Ouvrir le document
PdfContentEditor editor = new PdfContentEditor();
// Lier le fichier PDF source
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Accepter l'absorbeur pour la page
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Parcourir les fragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```


## Rechercher et dessiner un rectangle autour de chaque TextFragment

Aspose.PDF pour .NET prend en charge la fonctionnalité de recherche et d'obtention des coordonnées de chaque caractère ou fragment de texte. Donc, pour être certain des coordonnées retournées pour chaque caractère, nous pouvons envisager de surligner (ajouter un rectangle) autour de chaque caractère.

Dans le cas d'un paragraphe de texte, vous pouvez envisager d'utiliser une expression régulière pour déterminer la rupture de paragraphe et dessiner un rectangle autour de celle-ci. Veuillez jeter un œil au code suivant. Le code suivant obtient les coordonnées de chaque caractère et crée un rectangle autour de chaque caractère.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```


## Mettre en évidence chaque caractère dans un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de rechercher du texte dans un document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF pour .NET prend en charge la fonctionnalité de recherche et d'obtention des coordonnées de chaque caractère ou fragment de texte. Donc, pour être certain des coordonnées renvoyées pour chaque caractère, nous pouvons envisager de mettre en évidence (ajouter un rectangle) autour de chaque caractère. Le code suivant obtient les coordonnées de chaque caractère et crée un rectangle autour de chaque caractère.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Créer un objet TextAbsorber pour trouver tous les mots
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Boucle à travers les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```


## Ajouter et Rechercher du Texte Caché

Parfois, nous voulons ajouter du texte caché dans un document PDF, puis rechercher ce texte caché et utiliser sa position pour un post-traitement. Pour votre commodité, Aspose.PDF pour .NET offre ces capacités. Vous pouvez ajouter du texte caché lors de la génération du document. De plus, vous pouvez trouver du texte caché en utilisant TextFragmentAbsorber. Pour ajouter du texte caché, réglez TextState.Invisible à ‘true’ pour le texte ajouté. TextFragmentAbsorber trouve tout le texte qui correspond au modèle (si spécifié). C'est le comportement par défaut qui ne peut pas être modifié. Afin de vérifier si le texte trouvé est réellement invisible, la propriété TextState.Invisible peut être utilisée. Le fragment de code ci-dessous montre comment utiliser cette fonctionnalité.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Créer un document avec du texte caché
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Ceci est un texte commun.");
TextFragment frag2 = new TextFragment("Ceci est un texte invisible.");

//Définir la propriété du texte - invisible
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Rechercher du texte dans le document
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Faire quelque chose avec les fragments
    Console.WriteLine("Texte '{0}' à la position {1} invisibilité : {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## Recherche de texte avec .NET Regex

Aspose.PDF pour .NET permet de rechercher des documents en utilisant l'option standard .NET Regex. Le TextFragmentAbsorber peut être utilisé à cette fin comme montré dans l'exemple de code ci-dessous.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Créer un objet Regex pour trouver tous les mots
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Ouvrir le document
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Obtenir une page particulière
Page page = document.Pages[1];

// Créer un objet TextAbsorber pour trouver toutes les instances de l'expression régulière d'entrée
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Accepter l'absorbeur pour la page
page.Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Boucler à travers les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>