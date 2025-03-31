---
title: Exportar dados do Excel para preencher formulário PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Esta seção explica como você pode exportar dados da planilha do Excel para preencher um formulário PDF usando a classe AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "O recurso em Aspose.PDF for .NET permite que os usuários exportem dados de planilhas do Excel para formulários PDF usando a classe AutoFiller. Ao aproveitar o método ExportDataTable, os usuários podem transformar dados do Excel em um DataTable e preencher formulários PDF de forma eficiente, agilizando o processo de entrada de dados e aumentando a produtividade. Essa funcionalidade garante que os formulários PDF sejam preenchidos com precisão e automaticamente com base na estrutura de dados do Excel.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) em [Aspose.PDF for .NET](/pdf/pt/net/) oferece várias maneiras de preencher os formulários PDF. Você pode importar dados de arquivo XML, DFD, XFDF, usar API e até mesmo usar os dados da planilha do Excel.
Usaremos o método [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) da classe [Cells](https://reference.aspose.com/pdf/pt/net/aspose.pdf/cells) de [Aspose.Cells](https://docs.aspose.com//cells/net) para exportar os dados da planilha do Excel para um objeto DataTable. Em seguida, precisaremos importar esses dados para o formulário PDF usando o método [ImportDataTable](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/autofiller/methods/importdatatable) da classe [AutoFiller](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/autofiller). Certifique-se de que o nome da coluna do DataTable seja o mesmo que o nome do campo no formulário PDF.

{{% /alert %}}

## Detalhes da implementação

No cenário a seguir, vamos usar um formulário PDF, que contém três campos de formulário chamados ID, Nome e Gênero.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

No formulário especificado acima, há uma página, com três campos chamados "ID", "Nome" e "Gênero", respectivamente. Extrairíamos os dados da seguinte planilha do Excel para um objeto DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Precisamos criar um objeto da classe [AutoFiller](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/autofiller) e vincular o formulário PDF presente nas imagens acima e usar o método [ImportDataTable](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/autofiller/methods/importdatatable) para preencher os campos do formulário usando os dados presentes no objeto DataTable.
Uma vez que o método é chamado, um novo arquivo de formulário PDF é gerado, que contém cinco páginas com o formulário preenchido com base nos dados da planilha do Excel. O formulário PDF de entrada era de uma única página e o resultado é de cinco páginas, porque o número de linhas de dados na planilha do Excel é 5. A classe DataTable oferece a capacidade de usar a primeira linha da planilha como Nome da Coluna.

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

Para preencher a partir de XLSX, por favor, use o próximo trecho de código:

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

Aspose.PDF for .NET permite que você gere uma Tabela de Dados em um documento PDF:

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

## Conclusão

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) também oferece a capacidade de preencher formulários PDF usando dados de banco de dados, mas esse recurso é atualmente suportado na versão .NET.
{{% /alert %}}