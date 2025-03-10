---
title: تصدير بيانات Excel لملء نموذج PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/export-excel-worksheet-data-to-fill-pdf-form/
description: يشرح هذا القسم كيفية تصدير بيانات ورقة عمل Excel لملء نموذج PDF باستخدام فئة AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "تتيح الميزة في Aspose.PDF for .NET للمستخدمين تصدير البيانات من أوراق عمل Excel إلى نماذج PDF بسلاسة باستخدام فئة AutoFiller. من خلال الاستفادة من طريقة ExportDataTable، يمكن للمستخدمين تحويل بيانات Excel إلى DataTable وملء نماذج PDF بكفاءة، مما يسهل عملية إدخال البيانات وزيادة الإنتاجية. تضمن هذه الوظيفة أن يتم ملء نماذج PDF بدقة وبشكل تلقائي بناءً على هيكل البيانات في Excel.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

[مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/ar/net/) تقدم طرقًا متنوعة لملء نماذج PDF. يمكنك استيراد البيانات من ملف XML، DFD، XFDF، استخدام API وحتى استخدام البيانات من ورقة عمل Excel.
سنستخدم طريقة [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) من فئة [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) من [Aspose.Cells](https://docs.aspose.com//cells/net) لتصدير البيانات من ورقة Excel إلى كائن DataTable. ثم سنقوم باستيراد هذه البيانات إلى نموذج PDF باستخدام طريقة [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) من فئة [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). تأكد من أن اسم العمود في DataTable هو نفسه اسم الحقل في نموذج PDF.

{{% /alert %}}

## تفاصيل التنفيذ

في السيناريو التالي، سنستخدم نموذج PDF يحتوي على ثلاثة حقول نموذجية تُسمى ID وName وGender.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

في النموذج المحدد أعلاه، يوجد صفحة واحدة، مع ثلاثة حقول تُسمى "ID" و"Name" و"Gender" على التوالي. سنقوم باستخراج البيانات من ورقة Excel التالية إلى كائن DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

نحتاج إلى إنشاء كائن من فئة [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) وربط نموذج PDF الموجود في الصور أعلاه واستخدام طريقة [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) لملء حقول النموذج باستخدام البيانات الموجودة في كائن DataTable.
بمجرد استدعاء الطريقة، يتم إنشاء ملف نموذج PDF جديد يحتوي على خمس صفحات مع نموذج مملوء بناءً على البيانات من ورقة Excel. كان نموذج PDF المدخل صفحة واحدة والنتيجة هي خمس صفحات، لأن عدد صفوف البيانات في ورقة Excel هو 5. توفر فئة DataTable القدرة على استخدام الصف الأول من الورقة كاسم العمود.

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

لملء من XLSX، يرجى استخدام مقتطف الشيفرة التالي:

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

Aspose.PDF for .NET يتيح لك إنشاء جدول بيانات في مستند PDF:

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

## الخاتمة

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) تقدم أيضًا القدرة على ملء نموذج PDF باستخدام البيانات من قاعدة البيانات، ولكن هذه الميزة مدعومة حاليًا في إصدار .NET فقط.
{{% /alert %}}