---
title: Exporter les données Excel pour remplir le formulaire PDF
type: docs
weight: 10
url: /net/export-excel-worksheet-data-to-fill-pdf-form/
description: Cette section explique comment vous pouvez exporter les données de la feuille de calcul Excel pour remplir le formulaire PDF en utilisant la classe AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) offre diverses façons de remplir les formulaires Pdf. Vous pouvez importer des données à partir d'un fichier XML, DFD, XFDF, utiliser l'API et même utiliser les données de la feuille de calcul Excel. Nous utiliserions la méthode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) de la classe [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) de [Aspose.Cells](https://docs.aspose.com//cells/net) pour exporter les données de la feuille Excel dans un objet DataTable. Ensuite, nous devons importer ces données sous forme de Pdf en utilisant la méthode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) de la classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Assurez-vous que le nom de colonne de DataTable est identique au nom du champ sur le formulaire PDF.

{{% /alert %}}

## Détails de l'implémentation

Dans le scénario suivant, nous allons utiliser un formulaire PDF, qui contient trois champs de formulaire nommés ID, Nom et Sexe.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

Dans le formulaire spécifié ci-dessus, il y a une page, avec trois champs nommés respectivement "ID", "Nom" et "Sexe". Nous extrairons les données de la feuille Excel suivante dans l'objet DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Nous devons créer un objet de la classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) et lier le formulaire PDF présent dans les images ci-dessus et utiliser la méthode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) pour remplir les champs du formulaire en utilisant les données présentes dans l'objet DataTable.Une fois la méthode appelée, un nouveau fichier de formulaire Pdf est généré, qui contient cinq pages avec le formulaire rempli basé sur les données de la feuille Excel. Le formulaire Pdf d'entrée était d'une seule page et le résultat est de cinq pages, parce que le nombre de lignes de données dans la feuille Excel est de 5. La classe DataTable offre la capacité d'utiliser la première ligne de la feuille comme ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// Création d'un flux de fichiers contenant le fichier Excel à ouvrir
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Ouverture du fichier Excel via le flux de fichiers
workbook.Open(fstream);
// Accès à la première feuille de calcul dans le fichier Excel
Worksheet worksheet = workbook.Worksheets[0];
// Exportation du contenu de 7 lignes et 2 colonnes à partir de la 1ère cellule vers DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Fermeture du flux de fichiers pour libérer toutes les ressources
fstream.Close();
// Créer un objet de la classe AutoFiller
AutoFiller autoFiller = new AutoFiller();
// Le fichier pdf d'entrée qui contient les champs de formulaire
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// Le pdf résultant, qui contiendra les champs de formulaire remplis avec les informations de DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Appeler la méthode pour importer les données de l'objet DataTable dans les champs de formulaire Pdf.
autoFiller.ImportDataTable(dataTable);
// Appeler la méthode de sauvegarde pour générer le fichier pdf
autoFiller.Save();
```

Pour remplir depuis XLSX, veuillez utiliser l'extrait de code suivant :

```csharp
internal static void FillFromXLSX()
        {
            // Créer un objet de la classe AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // Le fichier PDF d'entrée qui contient les champs de formulaire
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // Appeler la méthode pour importer les données de l'objet DataTable dans les champs de formulaire PDF.
            autoFiller.ImportDataTable(dataTable);

            // Le PDF résultant, qui contiendra les champs de formulaire remplis avec les informations de DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF pour .NET vous permet de générer une table de données dans un document PDF :

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // Créer un nouveau DataTable.
            System.Data.DataTable table = new DataTable("Students");
            // Déclarer des variables pour les objets DataColumn et DataRow.
            DataColumn column;
            DataRow row;

            // Créer un nouveau DataColumn, définir le DataType,
            // ColumnName et ajouter à DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // Ajouter la colonne à DataColumnCollection.
            table.Columns.Add(column);

            // Créer la deuxième colonne.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // Ajouter la colonne au tableau.
            table.Columns.Add(column);

            // Faire de la colonne ID la colonne clé primaire.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // Créer trois nouveaux objets DataRow et les ajouter
            // au DataTable
            var rand = new Random();
            for (int i = 1; i <= 4; i++)
            {
                row = table.NewRow();
                row["id"] = i;
                row["First Name"] = names[rand.Next(names.Length)];
                table.Rows.Add(row);
            }
            return table;
        }
```

## Conclusion

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre également la capacité de remplir un formulaire PDF en utilisant des données provenant d'une base de données, mais cette fonctionnalité est actuellement prise en charge dans la version .Net.
{{% /alert %}}