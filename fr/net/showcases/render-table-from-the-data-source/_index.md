---
title: Rendre un tableau à partir de la source de données
linktitle: Rendre un tableau à partir de la source de données
type: docs
weight: 30
url: fr/net/render-table-from-the-data-source/
description: Cette page explique comment rendre un tableau à partir de la source de données en utilisant la bibliothèque Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF permet de créer un tableau avec DataSource provenant de DataSet, DataTable, tableaux et objets IEnumerable en utilisant la classe PdfLightTable.

La [classe Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) est utilisée pour traiter les tableaux. Cette classe nous donne la capacité de créer des tableaux et de les placer dans le document, en utilisant [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) et [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Ainsi, pour créer le tableau, vous devez ajouter le nombre requis de lignes et les remplir avec le nombre approprié de cellules.

L'exemple suivant crée un tableau de 4x10.

```csharp
var table = new Table
    {
        // Définir les largeurs automatiques des colonnes du tableau
        ColumnWidths = "25% 25% 25% 25%",
        // Définir le padding des cellules
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Gauche Bas Droite Haut
        // Définir la couleur de la bordure du tableau en Vert
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Définir la bordure des cellules du tableau en Noir
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Ajouter une ligne au tableau
        var row = table.Rows.Add();
        // Ajouter des cellules au tableau
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cellule ({i+1}, {rowCount +1})");
        }
    }
    // Ajouter l'objet tableau à la première page du document d'entrée
    document.Pages[1].Paragraphs.Add(table);
```
Lors de l'initialisation de l'objet Table, les paramètres d'apparence minimaux ont été utilisés :

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - largeur des colonnes (par défaut) ;
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - les champs par défaut pour la cellule du tableau ;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - attributs du cadre du tableau (style, épaisseur, couleur) ;
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - attributs du cadre de la cellule (style, épaisseur, couleur).

## Exportation de données à partir d'un tableau d'objets

La classe Table fournit des méthodes pour interagir avec les sources de données ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) et [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

Étant donné que ces objets ne sont pas très pratiques pour travailler dans le modèle MVC, nous nous limiterons à un exemple bref. Dans cet exemple (ligne 50), la méthode ImportDataTable est appelée et reçoit en paramètres une instance de DataTable et des paramètres supplémentaires comme le drapeau d'en-tête et la position initiale (lignes/colonnes) pour la sortie des données.

```csharp
// Créer un nouveau document PDF
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Initialise une nouvelle instance de TextFragment pour le titre du rapport
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Définir les largeurs des colonnes de la table
    ColumnWidths = "25% 25% 25% 25%",
    // Définir le padding des cellules
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Gauche Bas Droite Haut
    // Définir la couleur de la bordure de la table en Vert
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Définir la bordure des cellules de la table en Noir
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Pas de chaîne de connexion dans config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// Ajouter l'objet table à la première page du document d'entrée
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```

