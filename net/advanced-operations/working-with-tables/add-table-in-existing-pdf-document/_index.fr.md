---
titre: Créer ou Ajouter un Tableau dans un PDF en utilisant C#
linktitle: Créer ou Ajouter un Tableau
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF pour .NET est une bibliothèque utilisée pour créer, lire et modifier des tableaux PDF. Consultez d'autres fonctions avancées dans ce sujet.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Créer ou Ajouter un Tableau dans un PDF en utilisant C#",
    "alternativeHeadline": "Comment ajouter un Tableau dans un PDF avec .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, créer un tableau dans pdf, ajouter un tableau",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET est une bibliothèque utilisée pour créer, lire et modifier des tableaux PDF. Consultez d'autres fonctions avancées dans ce sujet."
}
</script>
## Création de table en utilisant C\#

Les tables sont importantes lorsqu'on travaille avec des documents PDF. Elles offrent d'excellentes fonctionnalités pour afficher les informations de manière systématique. L'espace de noms Aspose.PDF contient des classes nommées [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), et [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) qui fournissent des fonctionnalités pour créer des tables lors de la génération de documents PDF à partir de zéro.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

La table peut être créée en créant un objet de la classe Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Ajout d'une table dans un document PDF existant

Pour ajouter une table à un fichier PDF existant avec Aspose.PDF pour .NET, suivez les étapes suivantes :

1. Chargez le fichier source.
1. Initialisez une table et définissez ses colonnes et lignes.
1. Définissez les paramètres de la table (nous avons défini les bordures).
1. Peuplez la table.
1. Ajoutez la table à une page.
1.
1.

Les extraits de code suivants montrent comment ajouter du texte dans un fichier PDF existant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Charger le document PDF source
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Initialise une nouvelle instance de la Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Définir la couleur de la bordure de la table en gris clair
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Définir la bordure pour les cellules de la table
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Créer une boucle pour ajouter 10 lignes
for (int row_count = 1; row_count < 10; row_count++)
{
    // Ajouter une ligne à la table
    Aspose.Pdf.Row row = table.Rows.Add();
    // Ajouter des cellules à la table
    row.Cells.Add("Colonne (" + row_count + ", 1)");
    row.Cells.Add("Colonne (" + row_count + ", 2)");
    row.Cells.Add("Colonne (" + row_count + ", 3)");
}
// Ajouter l'objet table à la première page du document d'entrée
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// Sauvegarder le document mis à jour contenant l'objet table
doc.Save(dataDir);
```
### ColSpan et RowSpan dans les tables

Aspose.PDF pour .NET fournit la propriété [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) pour fusionner les colonnes dans un tableau et la propriété [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) pour fusionner les lignes.

Nous utilisons la propriété `ColSpan` ou `RowSpan` sur l'objet `Cell` qui crée la cellule de tableau. Après avoir appliqué les propriétés requises, la cellule créée peut être ajoutée au tableau.

```csharp
public static void AddTable_RowColSpan()
{
    // Charger le document PDF source
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Initialise une nouvelle instance de Table
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Définir la couleur de bordure de la table comme gris clair
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Définir la bordure pour les cellules de table
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Ajouter la 1ère rangée à la table
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Ajouter des cellules de table
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // Ajouter la 2ème rangée à la table
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // Ajouter la 3ème rangée à la table
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // Ajouter la 4ème rangée à la table
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // Ajouter la 5ème rangée à la table
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // Ajouter l'objet table à la première page du document d'entrée
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Enregistrer le document mis à jour contenant l'objet table
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
Le résultat du code d'exécution ci-dessous est la table représentée sur l'image suivante :

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Travailler avec les Bordures, Marges et Rembourrages

Veuillez noter qu'il prend également en charge la fonctionnalité de définir le style de bordure, les marges et le rembourrage des cellules pour les tables. Avant de plonger dans des détails techniques plus précis, il est important de comprendre les concepts de bordure, de marges et de rembourrage qui sont présentés ci-dessous dans un diagramme :

![Bordures, marges et rembourrages](set-border-style-margins-and-padding-of-table_1.png)

Dans la figure ci-dessus, vous pouvez voir que les bordures de la table, de la ligne et de la cellule se chevauchent. En utilisant Aspose.PDF, une table peut avoir des marges et les cellules peuvent avoir des rembourrages. Pour définir les marges des cellules, nous devons définir le rembourrage des cellules.

### Bordures

Pour définir les bordures des objets Table, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) et [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), utilisez les propriétés Table.Border, Row.Border et Cell.Border.
Pour définir les bordures des objets Table, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) et [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), utilisez les propriétés Table.Border, Row.Border et Cell.Border.

### Marges ou Rembourrage

Le rembourrage des cellules peut être géré en utilisant la propriété [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) de la classe Table. Toutes les propriétés liées au rembourrage sont attribuées à une instance de la classe [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) qui prend des informations sur les paramètres `Left`, `Right`, `Top` et `Bottom` pour créer des marges personnalisées.

Dans l'exemple suivant, la largeur de la bordure de la cellule est définie à 0.1 point, la largeur de la bordure de la table est définie à 1 point et le rembourrage de la cellule est défini à 5 points.

![Marge et Bordure dans un Tableau PDF](margin-border.png)

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancie l'objet Document en appelant son constructeur vide
Document doc = new Document();
Page page = doc.Pages.Add();
// Instancie un objet table
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Ajoute la table dans la collection de paragraphes de la section souhaitée
page.Paragraphs.Add(tab1);
// Définit les largeurs de colonnes de la table
tab1.ColumnWidths = "50 50 50";
// Définit la bordure par défaut des cellules en utilisant l'objet BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Définit la bordure de la table en utilisant un autre objet BorderInfo personnalisé
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crée un objet MarginInfo et définit ses marges gauche, bas, droite et haut
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Définit le rembourrage par défaut des cellules à l'objet MarginInfo
tab1.DefaultCellPadding = margin;
// Crée des lignes dans la table puis des cellules dans les lignes
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 avec une longue chaîne de texte");
// row1.Cells.Add("col3 avec une longue chaîne de texte à placer dans la cellule");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Sauvegarde le Pdf
doc.Save(dataDir);
```
Pour créer une table avec des coins arrondis, utilisez la valeur `RoundedBorderRadius` de la classe BorderInfo et réglez le style des coins de la table sur arrondi.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Créez un objet BorderInfo vide
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Définissez la bordure avec un bord arrondi où le rayon est de 15
bInfo.RoundedBorderRadius = 15;
// Réglez le style des coins de la table sur Arrondi.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Définissez les informations de bordure de la table
tab1.Border = bInfo;
```

## Appliquer Différents Paramètres AutoFit à une Table

Lorsque vous créez une table en utilisant un agent visuel tel que Microsoft Word, vous vous retrouvez souvent à utiliser l'une des options AutoFit pour dimensionner automatiquement la table à la largeur souhaitée.
Lors de la création d'une table à l'aide d'un agent visuel tel que Microsoft Word, vous vous retrouvez souvent à utiliser l'une des options AutoFit pour dimensionner automatiquement la table à la largeur souhaitée.

Par défaut, Aspose.Pdf insère une nouvelle table en utilisant `ColumnAdjustment` avec la valeur `Customized`. La table s'adaptera à la largeur disponible sur la page. Pour modifier le comportement de dimensionnement sur une telle table ou une table existante, vous pouvez appeler la méthode Table.autoFit(int). Cette méthode accepte une énumération AutoFitBehavior qui définit quel type d'ajustement automatique est appliqué à la table.

Comme dans Microsoft Word, une méthode d'ajustement automatique est en fait un raccourci qui applique différentes propriétés à la table en une seule fois. Ces propriétés sont en fait ce qui donne à la table le comportement observé. Nous discuterons de ces propriétés pour chaque option d'ajustement automatique. Nous utiliserons la table suivante et appliquerons les différents paramètres d'ajustement automatique comme démonstration :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciez l'objet Pdf en appelant son constructeur vide
Document doc = new Document();
// Créez la section dans l'objet Pdf
Page sec1 = doc.Pages.Add();

// Instanciez un objet table
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Ajoutez la table dans la collection de paragraphes de la section désirée
sec1.Paragraphs.Add(tab1);

// Définissez les largeurs des colonnes de la table
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Définissez la bordure de cellule par défaut à l'aide de l'objet BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Définissez la bordure de la table à l'aide d'un autre objet BorderInfo personnalisé
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Créez un objet MarginInfo et définissez ses marges gauche, bas, droite et haut
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Définissez le rembourrage de cellule par défaut à l'objet MarginInfo
tab1.DefaultCellPadding = margin;

// Créez des rangées dans la table puis des cellules dans les rangées
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Sauvegardez le document mis à jour contenant l'objet table
doc.Save(dataDir);
```
### Obtenir la largeur de la table

Parfois, il est nécessaire d'obtenir dynamiquement la largeur d'une table. La classe Aspose.PDF.Table dispose d'une méthode [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) à cet effet. Par exemple, vous n'avez pas défini explicitement la largeur des colonnes de la table et avez réglé [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) sur AutoFitToContent. Dans ce cas, vous pouvez obtenir la largeur de la table comme suit.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Créer un nouveau document
Document doc = new Document();
// Ajouter une page au document
Page page = doc.Pages.Add();
// Initialiser une nouvelle table
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Ajouter une ligne à la table
Row row = table.Rows.Add();
// Ajouter une cellule à la table
Cell cell = row.Cells.Add("Texte de la cellule 1");
cell = row.Cells.Add("Texte de la cellule 2");
// Obtenir la largeur de la table
Console.WriteLine(table.GetWidth());
```

## Ajouter une image SVG à une cellule de table
## Ajouter une image SVG à une cellule de tableau

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter une cellule de tableau dans un fichier PDF. Lors de la création d'un tableau, il est possible d'ajouter du texte ou des images dans les cellules. De plus, l'API offre également la fonctionnalité de convertir des fichiers SVG au format PDF. En utilisant une combinaison de ces fonctionnalités, il est possible de charger une image SVG et de l'ajouter dans une cellule de tableau.

Le fragment de code suivant montre les étapes pour créer une instance de tableau et ajouter une image SVG à l'intérieur d'une cellule de tableau.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancier l'objet Document
Document doc = new Document();
// Créer une instance d'image
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Définir le type d'image comme SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Chemin pour le fichier source
img.File = dataDir + "SVGToPDF.svg";
// Définir la largeur pour l'instance d'image
img.FixWidth = 50;
// Définir la hauteur pour l'instance d'image
img.FixHeight = 50;
// Créer une instance de tableau
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Définir la largeur pour les cellules du tableau
table.ColumnWidths = "100 100";
// Créer un objet de ligne et l'ajouter à l'instance de tableau
Aspose.Pdf.Row row = table.Rows.Add();
// Créer un objet de cellule et l'ajouter à l'instance de ligne
Aspose.Pdf.Cell cell = row.Cells.Add();
// Ajouter un textfragment à la collection de paragraphes de l'objet cellule
cell.Paragraphs.Add(new TextFragment("Première cellule"));
// Ajouter une autre cellule à l'objet ligne
cell = row.Cells.Add();
// Ajouter l'image SVG à la collection de paragraphes de l'instance de cellule récemment ajoutée
cell.Paragraphs.Add(img);
// Créer un objet de page et l'ajouter à la collection de pages de l'instance de document
Page page = doc.Pages.Add();
// Ajouter le tableau à la collection de paragraphes de l'objet de page
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Enregistrer le fichier PDF
doc.Save(dataDir);
```
## Utilisation de balises HTML dans un tableau

Parfois, vous pouvez avoir besoin d'importer des contenus de base de données qui contiennent certaines balises HTML, puis d'importer le contenu dans l'objet Tableau. Lors de l'importation du contenu, il doit être rendu les balises HTML en conséquence dans le document PDF. Nous avons amélioré la méthode ImprotDataTable(), afin de répondre à une telle exigence comme suit :

{{% alert color="primary" %}}

Veuillez prendre en compte que l'utilisation de balises HTML à l'intérieur d'un élément de tableau augmente le temps de génération du document, car l'API doit traiter les balises HTML en conséquence et les rendre dans le document PDF de sortie.

{{% /alert %}}

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employé");
dt.Columns.Add("donnée", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Service d'urgence : 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Service de Médecine d'Observation de Penn : 3400 Spruce Street Rez-de-chaussée Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dép. de Médecine d'Urgence : 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Initialise une nouvelle instance de Table
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// Définir les largeurs de colonnes du tableau
tableProvider.ColumnWidths = "400 50 ";
// Définir la couleur de bordure du tableau comme gris clair
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Définir la bordure pour les cellules du tableau
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## Insérer un saut de page entre les lignes d'un tableau

Par comportement par défaut, lors de la création d'un tableau dans un fichier PDF, le tableau continue sur les pages suivantes lorsqu'il atteint la marge inférieure du tableau. Cependant, nous pouvons avoir besoin d'insérer de force un saut de page lorsque un certain nombre de lignes sont ajoutées au tableau. Le fragment de code suivant montre les étapes pour insérer un saut de page lorsque 10 lignes sont ajoutées au tableau.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancier une instance de Document
Document doc = new Document();
// Ajouter une page à la collection de pages du fichier PDF
doc.Pages.Add();
// Créer une instance de tableau
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Définir le style de bordure pour le tableau
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Définir le style de bordure par défaut pour le tableau avec la couleur de bordure comme Rouge
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Spécifier la largeur des colonnes du tableau
tab.ColumnWidths = "100 100";
// Créer une boucle pour ajouter 200 lignes au tableau
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Cellule " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Cellule " + counter + ", 1"));
    row.Cells.Add(cell2);
    // Lorsque 10 lignes sont ajoutées, rendre la nouvelle ligne dans une nouvelle page
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Ajouter le tableau à la collection de paragraphes du fichier PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Sauvegarder le document PDF
doc.Save(dataDir);
```
## Afficher un tableau sur une nouvelle page

Par défaut, les paragraphes sont ajoutés à la collection Paragraphs d'un objet Page. Cependant, il est possible de rendre un tableau sur une nouvelle page au lieu de juste après l'objet de niveau paragraphe précédemment ajouté sur la page.

### Exemple : Comment afficher un tableau sur une nouvelle page en utilisant C\#

Pour afficher un tableau sur une nouvelle page, utilisez la propriété [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) dans la classe BaseParagraph. Le fragment de code suivant montre comment faire.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Page ajoutée.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Contenu 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// Je veux garder la table 1 pour la page suivante s'il vous plaît...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
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

