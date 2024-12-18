---
title: Render table with Entity Framework 
linktitle: Render table with Entity Framework
type: docs
weight: 40
url: /fr/net/render-table-using-entity-framework-model-as-data-source/
description: Cet article vous montrera comment afficher un tableau en utilisant le modèle Entity Framework comme source de données avec Aspose.PDF pour .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Il existe un certain nombre de tâches pour lesquelles, pour une raison ou une autre, il est plus pratique d'exporter des données de bases de données vers un document PDF sans utiliser le schéma de conversion HTML en PDF récemment populaire.

Cet article vous montrera comment générer un document PDF en utilisant Aspose.PDF pour .NET.

## Principes de base de la génération de PDF avec Aspose.PDF

L'une des classes les plus importantes dans Aspose.PDF est la [classe Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Cette classe est un moteur de rendu PDF. Pour présenter une structure PDF, la bibliothèque Aspose.PDF utilise le modèle Document-Page, où :

* Document - contient les propriétés du document PDF, y compris la collection de pages;
* Document - contient les propriétés du document PDF incluant la collection de pages;
* Page - contient les propriétés d'une page spécifique et diverses collections d'éléments associés à cette page.

Par conséquent, pour créer un document PDF avec Aspose.PDF, vous devriez suivre ces étapes :

1. Créer l'objet Document;
1. Ajouter la page (l'objet Page) à l'objet Document;
1. Créer des objets qui sont placés sur la page (par exemple, fragment de texte, tableau, etc.)
1. Ajouter les éléments créés à la collection correspondante sur la page (dans notre cas, ce sera une collection de paragraphes);
1. Enregistrer le document en tant que fichier PDF.

```csharp
// Étape 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Étape 2
var pdfPage = document.Pages.Add();

// Étape 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Étape 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Étape 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
Le problème le plus courant est l'affichage des données dans un format de tableau. La [classe Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) est utilisée pour traiter les tableaux. Cette classe nous permet de créer des tableaux et de les placer dans le document, en utilisant les [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) et les [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Ainsi, pour créer le tableau, vous devez ajouter le nombre requis de lignes et les remplir avec le nombre approprié de cellules.

L'exemple suivant crée le tableau 4x10.

```csharp
var table = new Table
    {
        // Définir les largeurs de colonne automatiques du tableau
        ColumnWidths = "25% 25% 25% 25%",
        // Définir le remplissage des cellules
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Gauche Bas Droite Haut
        // Définir la couleur de la bordure du tableau en Vert
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Définir la bordure pour les cellules du tableau en Noir
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
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - les champs par défaut pour la cellule de table ;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - attributs du cadre de la table (style, épaisseur, couleur) ;
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - attributs du cadre de la cellule (style, épaisseur, couleur).

En résultat, nous obtenons une table de 4x10 avec des colonnes de largeur égale.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Exportation des données depuis les objets ADO.NET

La classe Table fournit des méthodes pour interagir avec les sources de données ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf/table/importdatatable/methods/1) et [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
La classe Table fournit des méthodes pour interagir avec les sources de données ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) et [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Étant donné que ces objets ne sont pas très pratiques pour travailler dans le modèle MVC, nous nous limiterons à un exemple succinct. Dans cet exemple (ligne 50), la méthode ImportDataTable est appelée et reçoit comme paramètres une instance de DataTable et des paramètres supplémentaires comme le drapeau d'en-tête et la position initiale (lignes/colonnes) pour la sortie des données.

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
    throw new ArgumentException("Aucune chaîne de connexion dans config.json");

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
## Exportation de données à partir de Entity Framework

Plus pertinent pour le .NET moderne est l'importation de données à partir de cadres ORM. Dans ce cas, il est judicieux d'étendre la classe Table avec des méthodes d'extension pour importer des données à partir d'une liste simple ou de données groupées. Prenons un exemple pour l'un des ORMs les plus populaires - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Ajoute une ligne au tableau
                var row = table.Rows.Add();
                // Ajoute des cellules au tableau
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Ajoute une ligne de groupe au tableau
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Ajoute une ligne de données au tableau
                    var dataRow = table.Rows.Add();
                    // Ajoute des cellules
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```
Les attributs Data Annotations sont souvent utilisés pour décrire les modèles et nous aider à créer la table. Par conséquent, l'algorithme de génération de table suivant a été choisi pour ImportEntityList :

* lignes 12-18 : construire une ligne d'en-tête et ajouter des cellules d'en-tête selon la règle "Si l'attribut DisplayAttribute est présent, alors prendre sa valeur sinon prendre le nom de la propriété"
* lignes 50-53 : construire les lignes de données et ajouter des cellules de ligne selon la règle "Si l'attribut DataTypeAttribute est défini, alors nous vérifions si nous devons faire des paramètres de conception supplémentaires pour celui-ci, et sinon juste convertir les données en chaîne et ajouter à la cellule;"

Dans cet exemple, des personnalisations supplémentaires ont été faites pour DataType.Currency (lignes 32-34) et DataType.Date (lignes 35-43), mais vous pouvez en ajouter d'autres si nécessaire.
L'algorithme de la méthode ImportGroupedData est presque le même que le précédent. Une classe supplémentaire GroupViewModel est utilisée, pour stocker les données groupées.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Puisque nous traitons des groupes, nous générons d'abord une ligne pour la clé valeur (lignes 66-71), et après cela - les lignes de ce groupe.
