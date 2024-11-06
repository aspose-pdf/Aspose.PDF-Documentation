---
title: Remplacer le texte dans un PDF
linktitle: Remplacer le texte dans un PDF
type: docs
weight: 40
url: fr/net/replace-text-in-pdf/
description: Apprenez-en plus sur les différentes manières de remplacer et de supprimer du texte à partir de la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remplacer le texte dans un PDF",
    "alternativeHeadline": "Remplacement et suppression de texte dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, remplacer texte, supprimer texte",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Apprenez-en plus sur les différentes manières de remplacer et de supprimer du texte à partir de la bibliothèque Aspose.PDF pour .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Remplacer le texte dans toutes les pages d'un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de trouver et remplacer le texte dans le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Pour remplacer le texte dans toutes les pages d'un document PDF, vous devez d'abord utiliser TextFragmentAbsorber pour trouver la phrase particulière que vous souhaitez remplacer. Ensuite, vous devez parcourir tous les TextFragments pour remplacer le texte et modifier d'autres attributs. Une fois cela fait, il ne vous reste plus qu'à sauvegarder le PDF de sortie en utilisant la méthode Save de l'objet Document. Le code suivant vous montre comment remplacer le texte dans toutes les pages d'un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("texte");

// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Parcourir les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Mettre à jour le texte et autres propriétés
    textFragment.Text = "TEXTE";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// Sauvegarder le document PDF résultant.
pdfDocument.Save(dataDir);
```
## Remplacer le texte dans une région spécifique de la page

Pour remplacer le texte dans une région spécifique de la page, nous devons d'abord instancier un objet TextFragmentAbsorber, spécifier la région de la page en utilisant la propriété TextSearchOptions.Rectangle, puis itérer à travers tous les TextFragments pour remplacer le texte. Une fois ces opérations terminées, il ne reste plus qu'à sauvegarder le PDF de sortie en utilisant la méthode Save de l'objet Document. Le code suivant vous montre comment remplacer le texte dans toutes les pages d'un document PDF.

```csharp
// charger le fichier PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instancier l'objet TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// rechercher du texte dans les limites de la page
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// spécifier la région de la page pour les options de recherche de texte
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// rechercher du texte à partir de la première page du fichier PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// itérer à travers chaque TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // mettre à jour le texte en caractères vides
    tf.Text = "";
}

// sauvegarder le fichier PDF mis à jour après remplacement du texte
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## Remplacer le texte basé sur une expression régulière

Si vous souhaitez remplacer certaines phrases basées sur une expression régulière, vous devez d'abord trouver toutes les phrases correspondant à cette expression régulière en utilisant TextFragmentAbsorber. Vous devrez passer l'expression régulière comme paramètre au constructeur de TextFragmentAbsorber. Vous devez également créer un objet TextSearchOptions qui spécifie si l'expression régulière est utilisée ou non. Une fois que vous obtenez les phrases correspondantes dans TextFragments, vous devez les parcourir toutes et les mettre à jour comme nécessaire. Enfin, vous devez enregistrer le PDF mis à jour en utilisant la méthode Save de l'objet Document. Le fragment de code suivant vous montre comment remplacer le texte basé sur une expression régulière.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Comme 1999-2000

// Définir l'option de recherche de texte pour spécifier l'utilisation de l'expression régulière
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Accepter l'absorbeur pour une seule page
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Parcourir les fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Mettre à jour le texte et d'autres propriétés
    textFragment.Text = "Nouvelle Phrase";
    // Défini à une instance d'un objet.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## Remplacer les polices dans un fichier PDF existant

Aspose.PDF pour .NET prend en charge la capacité de remplacer le texte dans un document PDF. Cependant, parfois vous avez besoin de remplacer uniquement la police utilisée dans le document PDF. Ainsi, au lieu de remplacer le texte, seule la police utilisée est remplacée. L'un des surcharges du constructeur de TextFragmentAbsorber accepte l'objet TextEditOptions comme argument et nous pouvons utiliser la valeur RemoveUnusedFonts de l'énumération TextEditOptions.FontReplace pour accomplir nos exigences. Le fragment de code suivant montre comment remplacer la police à l'intérieur du document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Charger le fichier PDF source
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Rechercher des fragments de texte et définir l'option d'édition pour supprimer les polices inutilisées
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(absorber);
// Parcourir tous les TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Si le nom de la police est ArialMT, remplacer le nom de la police par Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```
## Le remplacement de texte doit automatiquement réorganiser le contenu de la page

Aspose.PDF pour .NET prend en charge la fonctionnalité de recherche et de remplacement de texte dans le fichier PDF. Cependant, récemment, certains clients ont rencontré des problèmes lors du remplacement de texte lorsque un TextFragment particulier est remplacé par un contenu plus petit et que des espaces supplémentaires sont affichés dans le PDF résultant ou dans le cas où le TextFragment est remplacé par une chaîne plus longue, les mots se chevauchent avec le contenu existant de la page. Ainsi, il était nécessaire d'introduire un mécanisme pour qu'une fois le texte dans un document PDF remplacé, le contenu soit réorganisé.

Afin de répondre aux scénarios mentionnés ci-dessus, Aspose.PDF pour .NET a été amélioré afin qu'aucun de ces problèmes n'apparaisse lors du remplacement de texte dans un fichier PDF. Le fragment de code suivant montre comment remplacer le texte dans un fichier PDF et le contenu de la page doit être réorganisé automatiquement.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Charger le fichier PDF source
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Créer un objet TextFragment Absorber avec expression régulière
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Remplacer chaque TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Définir la police du fragment de texte à remplacer
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Définir la taille de la police
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Remplacer le texte par une chaîne plus longue que l'espace réservé
    textFragment.Text = "Ceci est une chaîne plus longue pour le test de ce problème";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Sauvegarder le PDF résultant
doc.Save(dataDir);
```
## Rendu des symboles remplaçables lors de la création de PDF

Les symboles remplaçables sont des symboles spéciaux dans une chaîne de texte qui peuvent être remplacés par un contenu correspondant au moment de l'exécution. Les symboles remplaçables actuellement pris en charge par le nouveau modèle d'objet document du namespace Aspose.PDF sont `$P`, `$p`, `\n`, `\r`. Les symboles `$p` et `$P` sont utilisés pour gérer la numérotation des pages en temps réel. `$p` est remplacé par le numéro de la page où se trouve la classe Paragraph actuelle. `$P` est remplacé par le nombre total de pages dans le document. Lors de l'ajout de `TextFragment` à la collection de paragraphes des documents PDF, il ne prend pas en charge le retour à la ligne à l'intérieur du texte. Cependant, pour ajouter du texte avec un retour à la ligne, veuillez utiliser `TextFragment` avec `TextParagraph` :

- utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu d'un simple "\n";
- créez un objet TextParagraph. Cela ajoutera du texte avec division de ligne;
- ajoutez le TextFragment avec TextParagraph.AppendLine;
- ajoutez le TextParagraph avec TextBuilder.AppendParagraph.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Initialiser un nouveau TextFragment avec du texte contenant les marqueurs de saut de ligne requis
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nom du demandeur : " + Environment.NewLine + " Joe Smoe");

// Définir les propriétés du fragment de texte si nécessaire
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Créer un objet TextParagraph
TextParagraph par = new TextParagraph();

// Ajouter un nouveau TextFragment au paragraphe
par.AppendLine(textFragment);

// Définir la position du paragraphe
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Créer un objet TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Ajouter le TextParagraph en utilisant TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## Symboles remplaçables dans la zone d'en-tête / pied de page

Les symboles remplaçables peuvent également être placés dans la section En-tête/Pied de page d'un fichier PDF. Veuillez consulter l'extrait de code suivant pour plus de détails sur la manière d'ajouter un symbole remplaçable dans la section pied de page.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Assignez l'instance marginInfo à la propriété Margin de sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instanciez un paragraphe de texte qui stockera le contenu à afficher en en-tête
TextFragment t1 = new TextFragment("titre du rapport");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nom_du_Rapport");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Créez un objet HeaderFooter pour la section
HeaderFooter hfFoot = new HeaderFooter();
// Définissez l'objet HeaderFooter pour les pieds de page impairs et pairs
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Ajoutez un paragraphe de texte contenant le numéro de page actuel sur le nombre total de pages
TextFragment t3 = new TextFragment("Généré le date de test");
TextFragment t4 = new TextFragment("nom du rapport ");
TextFragment t5 = new TextFragment("Page $p de $P");

// Instanciez un objet table
Table tab2 = new Table();

// Ajoutez la table dans la collection de paragraphes de la section souhaitée
hfFoot.Paragraphs.Add(tab2);

// Définissez les largeurs de colonne de la table
tab2.ColumnWidths = "165 172 165";

// Créez des rangées dans la table puis des cellules dans les rangées
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Définissez l'alignement vertical du texte comme centré
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Ajoutez la table dans la collection de paragraphes de la section souhaitée
page.Paragraphs.Add(table);

// Définissez la bordure de cellule par défaut à l'aide de l'objet BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Définissez la bordure de la table à l'aide d'un autre objet BorderInfo personnalisé
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Créez des rangées dans la table puis des cellules dans les rangées
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total pour Java est une compilation de chaque composant Java offert par Aspose. Il est compilé quotidiennement pour garantir qu'il contient les versions les plus à jour de chacun de nos composants Java. " + CRLF + "quotidiennement pour garantir qu'il contient les versions les plus à jour de chacun de nos composants Java. " + CRLF + "En utilisant Aspose.Total pour Java, les développeurs peuvent créer une large gamme d'applications.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## Supprimer les polices inutilisées d'un fichier PDF

Aspose.PDF pour .NET prend en charge la fonctionnalité d'incorporer des polices lors de la création d'un document PDF, ainsi que la capacité d'incorporer des polices dans des fichiers PDF existants. À partir d'Aspose.PDF pour .NET 7.3.0, il vous permet également de supprimer les polices dupliquées ou inutilisées des documents PDF.

Pour remplacer les polices, utilisez l'approche suivante :

1. Appelez la classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Appelez le paramètre TextEditOptions.FontReplace.RemoveUnusedFonts de la classe TextFragmentAbsorber. (Cela supprime les polices qui sont devenues inutilisées lors du remplacement de la police).
1. Définissez la police individuellement pour chaque fragment de texte.

Le fragment de code suivant remplace la police pour tous les fragments de texte de toutes les pages du document et supprime les polices inutilisées.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Charger le fichier PDF source
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Itérer à travers tous les TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```

## Supprimer tout le texte d'un document PDF

### Supprimer tout le texte en utilisant des opérateurs

Dans certaines opérations de texte, vous devez supprimer tout le texte d'un document PDF et pour cela, vous devez définir le texte trouvé comme une chaîne vide habituellement. Le point est que changer le texte pour de multiples fragments de texte invoque un certain nombre d'opérations de vérification et d'ajustement de position de texte. Elles sont essentielles dans les scénarios d'édition de texte. La difficulté est que vous ne pouvez pas déterminer combien de fragments de texte seront supprimés dans le scénario où ils sont traités en boucle.

Par conséquent, nous recommandons d'utiliser une autre approche pour le scénario de suppression de tout le texte des pages PDF. Veuillez considérer le fragment de code suivant qui fonctionne très rapidement.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Parcourir toutes les pages du document PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Sélectionner tout le texte sur la page
    page.Contents.Accept(operatorSelector);
    // Supprimer tout le texte
    page.Contents.Delete(operatorSelector.Selected);
}
// Enregistrer le document
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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

