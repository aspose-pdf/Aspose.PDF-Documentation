---
title: Экспорт данных Excel для заполнения формы PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/export-excel-worksheet-data-to-fill-pdf-form/
description: В этом разделе объясняется, как можно экспортировать данные листа Excel для заполнения формы PDF с помощью класса AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "Функция Aspose.PDF для .NET позволяет пользователям легко экспортировать данные из листов Excel в формы PDF с помощью класса AutoFiller. Используя метод ExportDataTable, пользователи могут преобразовать данные Excel в DataTable и эффективно заполнить формы PDF, оптимизируя процесс ввода данных и повышая производительность. Эта функция обеспечивает точное и автоматическое заполнение форм PDF на основе структуры данных в Excel",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="основной" %}}

[Пространство имён Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF for .NET](/pdf/ru/net/) предлагает различные способы заполнения форм Pdf. Вы можете импортировать данные из XML-файла, DFD, XFDF, использовать API и даже можете использовать данные из листа Excel.
Мы будем использовать метод [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) класса [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) из [Aspose.Cells](https://docs.aspose.com//cells/net), чтобы экспортировать данные из таблицы Excel в объект DataTable. Затем нам нужно будет импортировать эти данные в форму Pdf с помощью метода [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) класса [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Убедитесь, что имя столбца DataTable совпадает с именем поля в форме PDF.

{{% /alert %}}

## Детали реализации

В следующем сценарии мы будем использовать форму PDF, которая содержит три поля формы с именами ID, Name и Gender.

|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)|
|:-- |:-- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png) |![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png) |

На указанной выше форме одна страница с тремя полями, названными «ID», «Name» и «Gender» соответственно. Мы извлечём данные из следующей таблицы Excel в объект DataTable.

Нам нужно создать объект класса [AutoFiller] (https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) и связать форму Pdf, представленную на рисунках выше, и использовать метод [ImportDataTable], чтобы заполнить поля формы данными, содержащимися в объекте DataTable. После вызова метода создаётся новый файл формы Pdf, который содержит пять страниц с заполненными формами на основе данных из таблицы Excel. Исходная форма Pdf была на одной странице, а итоговая — на пяти, потому что количество строк данных в таблице Excel равно 5. Класс DataTable позволяет использовать первую строку листа в качестве имени столбца.

| ![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)  | ![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png) |
|:-- | :-- |

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

Для заполнения из XLSX используйте следующий фрагмент кода:

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

Aspose.PDF for .NET позволяет создавать таблицу данных в документе PDF:

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

## Заключение

{{% alert color="основной" %}}
[Aspose.Pdf.Facades] (https://reference.aspose.com/pdf/net/aspose.pdf.facades) также позволяет заполнять формы PDF данными из базы данных, но эта функция в настоящее время поддерживается в версии .NET.
{{% /alert %}}