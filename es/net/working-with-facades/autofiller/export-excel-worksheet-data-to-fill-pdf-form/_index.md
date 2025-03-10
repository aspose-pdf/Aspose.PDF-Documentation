---
title: Exportar datos de Excel para llenar un formulario PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Esta sección explica cómo puedes exportar datos de una hoja de cálculo de Excel para llenar un formulario PDF utilizando la clase AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "La función en Aspose.PDF for .NET permite a los usuarios exportar sin problemas datos de hojas de cálculo de Excel a formularios PDF utilizando la clase AutoFiller. Al aprovechar el método ExportDataTable, los usuarios pueden transformar datos de Excel en un DataTable y completar eficientemente formularios PDF, agilizando el proceso de entrada de datos y aumentando la productividad. Esta funcionalidad asegura que los formularios PDF se completen de manera precisa y automática según la estructura de datos en Excel.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

{{% alert color="primary" %}}

[El espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/net/) ofrece varias formas de llenar los formularios PDF. Puedes importar datos de un archivo XML, DFD, XFDF, usar la API e incluso usar los datos de una hoja de cálculo de Excel.
Usaremos el método [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) de la clase [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) de [Aspose.Cells](https://docs.aspose.com//cells/net) para exportar los datos de la hoja de Excel a un objeto DataTable. Luego, necesitaremos importar estos datos en el formulario PDF utilizando el método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) de la clase [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Asegúrate de que el nombre de la columna del DataTable sea el mismo que el nombre del campo en el formulario PDF.

{{% /alert %}}

## Detalles de implementación

En el siguiente escenario, vamos a utilizar un formulario PDF que contiene tres campos de formulario llamados ID, Nombre y Género.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

En el formulario especificado anteriormente hay una página, con tres campos llamados "ID", "Nombre" y "Género" respectivamente. Extraeremos los datos de la siguiente hoja de Excel en un objeto DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Necesitamos crear un objeto de la clase [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) y vincular el formulario PDF presente en las imágenes anteriores y usar el método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) para llenar los campos del formulario utilizando los datos presentes en el objeto DataTable.
Una vez que se llama al método, se genera un nuevo archivo de formulario PDF, que contiene cinco páginas con el formulario completado basado en los datos de la hoja de Excel. El formulario PDF de entrada era de una sola página y el resultado es de cinco páginas, porque el número de filas de datos en la hoja de Excel es 5. La clase DataTable ofrece la capacidad de usar la primera fila de la hoja como ColumnName.

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

Para llenar desde XLSX, por favor usa el siguiente fragmento de código:

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

Aspose.PDF for .NET te permite generar una tabla de datos en un documento PDF:

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

## Conclusión

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) también ofrece la capacidad de llenar formularios PDF utilizando datos de bases de datos, pero esta función actualmente solo es compatible en la versión .NET.
{{% /alert %}}