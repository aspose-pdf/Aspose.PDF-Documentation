---
title: 导出 Excel 数据以填写 PDF 表单
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/export-excel-worksheet-data-to-fill-pdf-form/
description: 本节解释了如何使用 AutoFiller 类导出 Excel 工作表数据以填写 PDF 表单。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "Aspose.PDF for .NET 中的功能允许用户无缝地将 Excel 工作表中的数据导出到 PDF 表单中，使用 AutoFiller 类。通过利用 ExportDataTable 方法，用户可以将 Excel 数据转换为 DataTable，并高效地填写 PDF 表单，从而简化数据输入过程并提高生产力。此功能确保 PDF 表单根据 Excel 中的数据结构准确且自动地填充。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/zh/net/) 中提供了多种填写 PDF 表单的方法。您可以从 XML 文件、DFD、XFDF 导入数据，使用 API，甚至可以使用 Excel 工作表中的数据。
我们将使用 [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) 方法从 [Aspose.Cells](https://docs.aspose.com//cells/net) 的 [Cells](https://reference.aspose.com/pdf/zh/net/aspose.pdf/cells) 类中将数据导出到 DataTable 对象中。然后，我们需要使用 [AutoFiller](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/autofiller) 类的 [ImportDataTable](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/autofiller/methods/importdatatable) 方法将这些数据导入 PDF 表单。确保 DataTable 的列名与 PDF 表单上的字段名相同。

{{% /alert %}}

## 实现细节

在以下场景中，我们将使用一个 PDF 表单，其中包含三个表单字段，分别命名为 ID、Name 和 Gender。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

上述表单有一页，包含三个字段，分别命名为“ID”、“Name”和“Gender”。我们将从以下 Excel 工作表中提取数据到 DataTable 对象中。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

我们需要创建一个 [AutoFiller](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/autofiller) 类的对象，并绑定上述图片中的 PDF 表单，并使用 [ImportDataTable](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/autofiller/methods/importdatatable) 方法使用 DataTable 对象中的数据填写表单字段。
一旦调用该方法，将生成一个新的 PDF 表单文件，其中包含五页，表单根据 Excel 工作表中的数据填写。输入的 PDF 表单是单页的，而结果是五页，因为 Excel 工作表中的数据行数为 5。DataTable 类提供了使用工作表的第一行作为列名的能力。

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

要从 XLSX 填充，请使用以下代码片段：

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

Aspose.PDF for .NET 允许您在 PDF 文档中生成数据表：

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

## 结论

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades) 还提供了使用数据库中的数据填写 PDF 表单的能力，但此功能目前仅在 .NET 版本中支持。
{{% /alert %}}