---
title: Intégrer Table avec des Sources de Données PDF
linktitle: Intégrer Table
type: docs
weight: 30
url: fr/net/integrate-table/
description: Cet article montre comment intégrer des tables PDF. Intégrer Table avec une base de données et déterminer si la table se divisera sur la page actuelle.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Intégrer Table avec des Sources de Données PDF",
    "alternativeHeadline": "Comment intégrer Table avec des Sources de Données PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, intégrer table",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de Documentation Aspose.PDF",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article montre comment intégrer des tables PDF. Intégrer Table avec une base de données et déterminer si la table se divisera sur la page actuelle."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Intégrer un tableau avec une base de données

Les bases de données sont conçues pour stocker et gérer des données. Il est courant pour les programmeurs de peupler différents objets avec des données provenant de bases de données. Cet article traite de l'ajout de données provenant d'une base de données dans un tableau. Il est possible de peupler un objet [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) avec des données de n'importe quelle source de données en utilisant Aspose.PDF pour .NET. Et ce n'est pas seulement possible, mais c'est très facile.

[Aspose.PDF pour .NET](https://docs.aspose.com/pdf/net/) permet aux développeurs d'importer des données à partir de :

- Tableau d'objets
- DataTable
- DataView

Ce sujet fournit des informations sur l'extraction de données à partir d'un DataTable ou d'un DataView.

Tous les développeurs travaillant sous la plateforme .NET doivent être familiers avec les concepts de base d'ADO.NET introduits par le .NET Framework.
Tous les développeurs travaillant sous la plateforme .NET doivent être familiers avec les concepts de base d'ADO.NET introduits par .NET Framework.

Les méthodes ImportDataTable(..) et ImportDataView(..) de la classe Table sont utilisées pour importer des données depuis des bases de données.

L'exemple ci-dessous démontre l'utilisation de la méthode ImportDataTable. Dans cet exemple, l'objet DataTable est créé à partir de zéro et des enregistrements sont ajoutés de manière programmatique au lieu de remplir le DataTable avec des données provenant de bases de données. Les développeurs peuvent également peupler le DataTable à partir de la base de données selon leur désir.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// Ajouter 2 lignes dans l'objet DataTable de manière programmatique
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// Créer une instance de Document
Document doc = new Document();
doc.Pages.Add();
// Initialiser une nouvelle instance de Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Définir les largeurs de colonnes de la table
table.ColumnWidths = "40 100 100 100";
// Définir la couleur de la bordure de la table en LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Définir la bordure pour les cellules de la table
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Ajouter l'objet table à la première page du document d'entrée
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Enregistrer le document mis à jour contenant l'objet table
doc.Save(dataDir);
```
## Comment déterminer si le tableau se cassera dans la page actuelle

Les tableaux sont par défaut ajoutés à partir de la position en haut à gauche et si le tableau atteint la fin de la page, il se casse automatiquement. Vous pouvez obtenir programmatiquement l'information que le tableau sera accommodé dans la page actuelle ou s'il se cassera en bas de la page. Pour cela, vous devez d'abord obtenir les informations sur la taille du document, puis vous avez besoin d'obtenir les informations sur la marge supérieure et la marge inférieure de la page, les informations sur la marge supérieure du tableau et la hauteur du tableau. Si vous ajoutez la marge supérieure de la page + la marge inférieure de la page + la marge supérieure du tableau + la hauteur du tableau et le soustrayez de la hauteur du document, vous pouvez obtenir la quantité d'espace restant sur le document. En fonction de la hauteur particulière de la ligne (que vous avez spécifiée), vous pouvez calculer si toutes les lignes d'un tableau peuvent être accommodées dans l'espace restant sur une page ou non. Veuillez jeter un coup d'œil au fragment de code suivant. Dans le code suivant, la hauteur moyenne d'une ligne est de 23.002 points.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciez un objet de classe PDF
Document pdf = new Document();
// Ajoutez la section à la collection de sections du document PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// Instanciez un objet tableau
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Ajoutez le tableau dans la collection de paragraphes de la section désirée
page.Paragraphs.Add(table1);
// Définissez les largeurs de colonnes du tableau
table1.ColumnWidths = "100 100 100";
// Définissez la bordure par défaut des cellules en utilisant l'objet BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Définissez la bordure du tableau en utilisant un autre objet BorderInfo personnalisé
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Créez un objet MarginInfo et définissez ses marges gauche, bas, droite et haut
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Définissez le rembourrage par défaut des cellules à l'objet MarginInfo
table1.DefaultCellPadding = margin;
// Si vous augmentez le compteur à 17, le tableau se cassera
// Car il ne peut plus être accommodé sur cette page
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Créez des rangées dans le tableau puis des cellules dans les rangées
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// Obtenez les informations sur la hauteur de la page
float PageHeight = (float)pdf.PageInfo.Height;
// Obtenez les informations totales sur la hauteur de la marge supérieure et inférieure de la page,
// la marge supérieure du tableau et la hauteur du tableau.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Affichez la hauteur du document PDF, la hauteur du tableau, la marge supérieure du tableau et les informations de marge supérieure et inférieure de la page
Console.WriteLine("Hauteur du document PDF = " + pdf.PageInfo.Height.ToString() + "\nInfo de marge supérieure = " + page.PageInfo.Margin.Top.ToString() + "\nInfo de marge inférieure = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nInfo de marge supérieure du tableau = " + table1.Margin.Top.ToString() + "\nHauteur moyenne de la rangée = " + table1.Rows[0].MinRowHeight.ToString() + " \nHauteur du tableau " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nHauteur totale de la page =" + PageHeight.ToString() + "\nHauteur cumulative incluant le tableau =" + TotalObjectsHeight.ToString());

// Vérifiez si nous soustrayons la somme de la marge supérieure de la page + la marge inférieure de la page
// + la marge supérieure du tableau et la hauteur du tableau de la hauteur de la page et c'est moins
// Que 10 (une rangée moyenne peut être supérieure à 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // Si la valeur est inférieure à 10, affichez alors le message.
    // Qui montre qu'une autre rangée ne peut pas être placée et si nous ajoutons une nouvelle
    // Rangée, le tableau se cassera. Cela dépend de la valeur de la hauteur de la rangée.
    Console.WriteLine("Hauteur de la page - Hauteur des objets < 10, donc le tableau se cassera");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Sauvegardez le document PDF
pdf.Save(dataDir);
```
## Ajouter une colonne répétitive dans le tableau

Dans la classe Aspose.Pdf.Table, vous pouvez définir un RepeatingRowsCount qui répétera les lignes si le tableau est trop long verticalement et déborde sur la page suivante. Cependant, dans certains cas, les tableaux sont trop larges pour tenir sur une seule page et doivent se poursuivre sur la page suivante. Pour répondre à ce besoin, nous avons implémenté la propriété RepeatingColumnsCount dans la classe Aspose.Pdf.Table. Définir cette propriété fera en sorte que le tableau se brise à la page suivante en colonnes et répète le nombre de colonnes spécifié au début de la page suivante. Le fragment de code suivant montre l'utilisation de la propriété RepeatingColumnsCount :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Créer un nouveau document
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Instancier une table externe qui occupe toute la page
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Instancier un objet table qui sera imbriqué dans outerTable et qui se cassera dans la même page
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Ajouter outerTable aux paragraphes de la page
// Ajouter mytable à outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Ajouter une ligne d'en-tête
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("en-tête 1");
row.Cells.Add("en-tête 2");
row.Cells.Add("en-tête 3");
row.Cells.Add("en-tête 4");
row.Cells.Add("en-tête 5");
row.Cells.Add("en-tête 6");
row.Cells.Add("en-tête 7");
row.Cells.Add("en-tête 11");
row.Cells.Add("en-tête 12");
row.Cells.Add("en-tête 13");
row.Cells.Add("en-tête 14");
row.Cells.Add("en-tête 15");
row.Cells.Add("en-tête 16");
row.Cells.Add("en-tête 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Créer des lignes dans le tableau puis des cellules dans les lignes
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## Intégration de Table avec la source Entity Framework

Plus pertinent pour le .NET moderne est l'importation de données à partir de frameworks ORM. Dans ce cas, il est judicieux de prolonger la classe Table avec des méthodes d'extension pour importer des données à partir d'une liste simple ou de données groupées. Prenons l'exemple d'un des ORM les plus populaires - Entity Framework.

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
                // Ajouter une ligne au tableau
                var row = table.Rows.Add();
                // Ajouter des cellules au tableau
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
                // Ajouter une ligne de groupe au tableau
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Ajouter une ligne de données au tableau
                    var dataRow = table.Rows.Add();
                    // Ajouter des cellules
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

- lignes 12-18 : construire une ligne d'en-tête et ajouter des cellules d'en-tête selon la règle "Si l'attribut DisplayAttribute est présent, alors prendre sa valeur sinon prendre le nom de la propriété"
- lignes 50-53 : construire les lignes de données et ajouter des cellules de ligne selon la règle "Si l'attribut DataTypeAttribute est défini, alors nous vérifions si nous devons faire des paramètres de conception supplémentaires pour cela, et sinon juste convertir les données en chaîne et ajouter à la cellule ;"

Dans cet exemple, des personnalisations supplémentaires ont été faites pour DataType.Currency (lignes 32-34) et DataType.Date (lignes 35-43), mais vous pouvez en ajouter d'autres si nécessaire.
L'algorithme de la méthode ImportGroupedData est presque le même que le précédent. Une classe supplémentaire GroupViewModel est utilisée, pour stocker les données groupées.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```

Étant donné que nous traitons des groupes, nous générons d'abord une ligne pour la clé (lignes 66-71), puis les lignes de ce groupe.

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

