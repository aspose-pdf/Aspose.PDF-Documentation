---
title: تصدير بيانات Excel لملء نموذج PDF
type: docs
weight: 10
url: /net/export-excel-worksheet-data-to-fill-pdf-form/
description: تشرح هذه القسم كيف يمكنك تصدير بيانات ورقة العمل Excel لملء نموذج PDF باستخدام فئة AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

يوفر [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF لـ .NET](/pdf/net/) طرقًا متنوعة لملء نماذج Pdf. يمكنك استيراد البيانات من ملف XML أو DFD أو XFDF، استخدام API وحتى يمكنك استخدام البيانات من ورقة عمل Excel. سنستخدم طريقة [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) لفئة [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) من [Aspose.Cells](https://docs.aspose.com//cells/net) لتصدير البيانات من ورقة Excel إلى كائن DataTable. ثم نحتاج إلى استيراد هذه البيانات إلى نموذج Pdf باستخدام طريقة [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) من فئة [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). تأكد من أن اسم العمود في DataTable هو نفس اسم الحقل في نموذج PDF.

{{% /alert %}}

## تفاصيل التنفيذ

في السيناريو التالي، سنقوم باستخدام نموذج PDF يحتوي على ثلاثة حقول نموذجية تحمل الأسماء ID، Name و Gender.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

في النموذج المحدد أعلاه، يحتوي على صفحة واحدة، مع ثلاثة حقول مسماة "ID"، "Name" و "Gender" بالتتابع. سنقوم باستخراج البيانات من ورقة إكسل التالية إلى كائن DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

نحتاج إلى إنشاء كائن من فئة [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) وربط نموذج Pdf الموجود في الصور أعلاه واستخدام طريقة [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) لملء حقول النموذج باستخدام البيانات الموجودة في كائن DataTable.
بمجرد استدعاء الطريقة يتم إنشاء ملف نموذج Pdf جديد، يحتوي على خمس صفحات يتم ملؤها بناءً على البيانات من ورقة Excel. كان نموذج Pdf المدخل صفحة واحدة والنتيجة هي خمس صفحات، لأن عدد صفوف البيانات في ورقة Excel هو 5. توفر فئة DataTable القدرة على استخدام الصف الأول من الورقة كاسم عمود.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// Creating a file stream containing the Excel file to be opened
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Opening the Excel file through the file stream
workbook.Open(fstream);
// Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.Worksheets[0];
// Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Closing the file stream to free all resources
fstream.Close();
// Create an object of AutoFiller class
AutoFiller autoFiller = new AutoFiller();
// The input pdf file that contains form fields
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// The resultant pdf, that will contain the form fields filled with information from DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Call the method to import the data from DataTable object into Pdf form fields.
autoFiller.ImportDataTable(dataTable);
// Call the save method to generate the pdf file
autoFiller.Save();
```
```

للملء من XLSX يُرجى استخدام مقطع الكود التالي:

```csharp
internal static void FillFromXLSX()
        {
            // إنشاء كائن من فئة AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // ملف pdf المدخل الذي يحتوي على حقول النموذج
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // استدعاء الطريقة لاستيراد البيانات من كائن DataTable إلى حقول النموذج في Pdf.
            autoFiller.ImportDataTable(dataTable);

            // ملف pdf الناتج، الذي سيحتوي على حقول النموذج المملوءة بالمعلومات من DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF لـ .NET يسمح لك بإنشاء جدول بيانات في مستند PDF:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // إنشاء جدول بيانات جديد.
            System.Data.DataTable table = new DataTable("Students");
            // إعلان المتغيرات لكائنات DataColumn و DataRow.
            DataColumn column;
            DataRow row;

            // إنشاء DataColumn جديد، تعيين DataType،
            // ColumnName وإضافته إلى DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // إضافة العمود إلى مجموعة DataColumnCollection.
            table.Columns.Add(column);

            // إنشاء العمود الثاني.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // إضافة العمود إلى الجدول.
            table.Columns.Add(column);

            // جعل عمود ID هو العمود الأساسي.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // إنشاء ثلاثة كائنات DataRow جديدة وإضافتها
            // إلى DataTable
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

## الخاتمة

{{% alert color="primary" %}}  
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) يوفر أيضًا القدرة على ملء نموذج PDF باستخدام بيانات من قاعدة البيانات، لكن هذه الميزة مدعومة حاليًا في إصدار .Net.  
{{% /alert %}}