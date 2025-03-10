---
title: Exporter les données Excel pour remplir un formulaire PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Cette section explique comment vous pouvez exporter les données d'une feuille de calcul Excel pour remplir un formulaire PDF en utilisant la classe AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET permet aux utilisateurs d'exporter sans effort des données des feuilles de calcul Excel vers des formulaires PDF en utilisant la classe AutoFiller. En utilisant la méthode ExportDataTable, les utilisateurs peuvent transformer les données Excel en un DataTable et remplir efficacement les formulaires PDF, rationalisant ainsi le processus de saisie des données et augmentant la productivité. Cette fonctionnalité garantit que les formulaires PDF sont remplis avec précision et automatiquement en fonction de la structure des données dans Excel.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "908",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/export-excel-worksheet-data-to-fill-pdf-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/export-excel-worksheet-data-to-fill-pdf-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

[L'espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) offre diverses façons de remplir les formulaires PDF. Vous pouvez importer des données à partir d'un fichier XML, DFD, XFDF, utiliser l'API et même utiliser les données d'une feuille de calcul Excel.
Nous utiliserions la méthode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) de la classe [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) de [Aspose.Cells](https://docs.aspose.com//cells/net) pour exporter les données de la feuille Excel dans un objet DataTable. Ensuite, nous devrions importer ces données dans le formulaire PDF en utilisant la méthode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) de la classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Assurez-vous que le nom de la colonne du DataTable est le même que le nom du champ dans le formulaire PDF.

{{% /alert %}}

## Détails de mise en œuvre

Dans le scénario suivant, nous allons utiliser un formulaire PDF, qui contient trois champs de formulaire nommés ID, Nom et Genre.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

Le formulaire spécifié ci-dessus a une page, avec trois champs nommés "ID", "Nom" et "Genre" respectivement. Nous allons extraire les données de la feuille Excel suivante dans un objet DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Nous devons créer un objet de la classe [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) et lier le formulaire PDF présent dans les images ci-dessus et utiliser la méthode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) pour remplir les champs du formulaire en utilisant les données présentes dans l'objet DataTable.
Une fois la méthode appelée, un nouveau fichier de formulaire PDF est généré, qui contient cinq pages avec le formulaire rempli en fonction des données de la feuille Excel. Le formulaire PDF d'entrée était une seule page et le résultat est cinq pages, car le nombre de lignes de données dans la feuille Excel est de 5. La classe DataTable offre la capacité d'utiliser la première ligne de la feuille comme nom de colonne.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportExcelToPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    var workbook = new Workbook();
    // Creating a file stream containing the Excel file to be opened
    using (FileStream fstream = new FileStream(dataDir + "newBook1.xls", FileMode.Open))
    {
        // Opening the Excel file through the file stream
        workbook.Open(fstream);
        // Accessing the first worksheet in the Excel file
        var worksheet = workbook.Worksheets[0];
        // Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
        System.Data.DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
        // Create an object of AutoFiller class
        using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
        {
            // The input pdf file that contains form fields
            autoFiller.InputFileName = dataDir + "DataTableExample.pdf";
            // The resultant pdf, that will contain the form fields filled with information from DataTable
            autoFiller.OutputFileName = dataDir + "DataTableExample_out.pdf";
            // Call the method to import the data from DataTable object into Pdf form fields
            autoFiller.ImportDataTable(dataTable);
            // Save PDF document
            autoFiller.Save();
        }
    }
}
```

Pour remplir à partir de XLSX, veuillez utiliser le prochain extrait de code :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFromXLSX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    // Create an object of AutoFiller class
    using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
    {
        // Bind PDF document
        autoFiller.BindPdf(dataDir + "Sample-Form-01.pdf");

        System.Data.DataTable dataTable = GenerateDataTable();

        // Call the method to import the data from DataTable object into Pdf form fields
        autoFiller.ImportDataTable(dataTable);

        // Save PDF document
        autoFiller.Save(dataDir + "Sample-Form-01_out.pdf");
    }
}
```

Aspose.PDF for .NET vous permet de générer un tableau de données dans un document PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static System.Data.DataTable GenerateDataTable()
{
    string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
    // Create a new DataTable
    var table = new System.Data.DataTable("Students");

    // Create new DataColumn, set DataType,
    // ColumnName and add to DataTable
    var column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.Int32"),
        ColumnName = "id",
        ReadOnly = true,
        Unique = true
    };
    // Add the Column to the DataColumnCollection
    table.Columns.Add(column);

    // Create second column
    column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.String"),
        ColumnName = "First Name",
        AutoIncrement = false,
        Caption = "First Name",
        ReadOnly = false,
        Unique = false
    };
    // Add the column to the table
    table.Columns.Add(column);

    // Make the ID column the primary key column
    var primaryKeyColumns = new System.Data.DataColumn[1];
    primaryKeyColumns[0] = table.Columns["id"];
    table.PrimaryKey = primaryKeyColumns;

    // Create three new DataRow objects and add
    // them to the DataTable
    var rand = new Random();
    System.Data.DataRow row;
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
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre également la possibilité de remplir un formulaire PDF en utilisant des données provenant d'une base de données, mais cette fonctionnalité est actuellement prise en charge dans la version .NET.
{{% /alert %}}