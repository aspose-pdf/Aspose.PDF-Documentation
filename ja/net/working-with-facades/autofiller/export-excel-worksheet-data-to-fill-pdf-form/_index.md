---
title: PDFフォームを埋めるためにExcelデータをエクスポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/export-excel-worksheet-data-to-fill-pdf-form/
description: このセクションでは、AutoFillerクラスを使用してPDFフォームを埋めるためにExcelワークシートデータをエクスポートする方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "Aspose.PDF for .NETの機能により、ユーザーはAutoFillerクラスを使用してExcelワークシートからPDFフォームにデータをシームレスにエクスポートできます。ExportDataTableメソッドを活用することで、ユーザーはExcelデータをDataTableに変換し、効率的にPDFフォームを記入することができ、データ入力のプロセスを合理化し、生産性を向上させます。この機能により、PDFフォームはExcelのデータ構造に基づいて正確かつ自動的に入力されます。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/net/aspose.pdf.facades)は、[Aspose.PDF for .NET](/pdf/ja/net/)でPDFフォームを埋めるためのさまざまな方法を提供します。XMLファイル、DFD、XFDFからデータをインポートしたり、APIを使用したり、Excelワークシートからデータを使用することもできます。
私たちは、ExcelシートからDataTableオブジェクトにデータをエクスポートするために、[Aspose.Cells](https://docs.aspose.com//cells/net)の[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells)クラスの[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index)メソッドを使用します。次に、[AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller)クラスの[ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable)メソッドを使用して、このデータをPDFフォームにインポートします。DataTableの列名がPDFフォームのフィールド名と同じであることを確認してください。

{{% /alert %}}

## 実装の詳細

次のシナリオでは、ID、名前、性別という3つのフォームフィールドを含むPDFフォームを使用します。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

上記のフォームには1ページがあり、「ID」、「名前」、「性別」という3つのフィールドがあります。次のExcelシートからDataTableオブジェクトにデータを抽出します。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

[AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller)クラスのオブジェクトを作成し、上記の画像にあるPDFフォームをバインドし、[ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable)メソッドを使用してDataTableオブジェクトにあるデータを使用してフォームフィールドを埋めます。
メソッドが呼び出されると、新しいPDFフォームファイルが生成され、Excelシートのデータに基づいてフォームが埋められた5ページが含まれます。入力PDFフォームは1ページで、結果は5ページです。これは、Excelシートのデータ行の数が5であるためです。DataTableクラスは、シートの最初の行をColumnNameとして使用する機能を提供します。

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

XLSXから埋めるには、次のコードスニペットを使用してください：

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

Aspose.PDF for .NETはPDFドキュメントにData Tableを生成することができます：

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

## 結論

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)は、データベースからのデータを使用してPDFフォームを埋める機能も提供していますが、この機能は現在.NETバージョンでのみサポートされています。
{{% /alert %}}