---
title: Экспорт данных Excel для заполнения формы PDF
type: docs
weight: 10
url: /ru/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Этот раздел объясняет, как экспортировать данные рабочего листа Excel для заполнения формы PDF с использованием класса AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF для .NET](/pdf/ru/net/) предлагает различные способы заполнения форм PDF. Вы можете импортировать данные из XML файла, DFD, XFDF, использовать API и даже использовать данные из рабочего листа Excel. Мы будем использовать метод [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) класса [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) из [Aspose.Cells](https://docs.aspose.com//cells/net) для экспорта данных из листа Excel в объект DataTable. Затем нам нужно импортировать эти данные в форму PDF, используя метод [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) класса [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Убедитесь, что имя столбца в DataTable совпадает с именем поля в форме PDF.

{{% /alert %}}

## Детали реализации

В следующем сценарии мы собираемся использовать форму PDF, которая содержит три поля формы с именами ID, Name и Gender.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

В указанной выше форме имеется одна страница с тремя полями, именуемыми "ID", "Name" и "Gender" соответственно. Мы будем извлекать данные из следующего листа Excel в объект DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Нам нужно создать объект класса [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) и связать форму PDF, представленную на изображениях выше, и использовать метод [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) для заполнения полей формы, используя данные, представленные в объекте DataTable.```csharp
Как только метод вызывается, создается новый файл Pdf формы, который содержит пять страниц с заполненными формами на основе данных из Excel листа. Входная Pdf форма была одностраничной, а результат является пятистраничным, потому что количество строк данных в excel листе равно 5. Класс DataTable предлагает возможность использовать первую строку листа в качестве ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

Workbook workbook = new Workbook();
// Создание файлового потока, содержащего Excel файл для открытия
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Открытие Excel файла через файловый поток
workbook.Open(fstream);
// Доступ к первому листу в Excel файле
Worksheet worksheet = workbook.Worksheets[0];
// Экспортирование содержимого 7 строк и 2 колонок, начиная с первой ячейки, в DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Закрытие файлового потока для освобождения всех ресурсов
fstream.Close();
// Создание объекта класса AutoFiller
AutoFiller autoFiller = new AutoFiller();
// Входной pdf файл, содержащий поля формы
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// Итоговый pdf, который будет содержать поля формы, заполненные информацией из DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Вызов метода для импорта данных из объекта DataTable в поля формы Pdf.
autoFiller.ImportDataTable(dataTable);
// Вызов метода сохранения для генерации pdf файла
autoFiller.Save();
```

Для заполнения из XLSX, пожалуйста, используйте следующий код:

```csharp
internal static void FillFromXLSX()
        {
            // Создать объект класса AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // Входной PDF файл, содержащий поля формы
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // Вызов метода для импорта данных из объекта DataTable в поля формы Pdf.
            autoFiller.ImportDataTable(dataTable);

            // Результирующий PDF, который будет содержать поля формы, заполненные информацией из DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF для .NET позволяет создавать таблицу данных в PDF документе:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // Создать новую таблицу данных.
            System.Data.DataTable table = new DataTable("Students");
            // Объявить переменные для объектов DataColumn и DataRow.
            DataColumn column;
            DataRow row;

            // Создать новый DataColumn, установить DataType,
            // ColumnName и добавить в DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // Добавить колонку в DataColumnCollection.
            table.Columns.Add(column);

            // Создать вторую колонку.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // Добавить колонку в таблицу.
            table.Columns.Add(column);

            // Сделать колонку ID первичным ключом.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // Создать три новых объекта DataRow и добавить
            // их в DataTable
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
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) также предлагает возможность заполнять PDF-формы, используя данные из базы данных, но эта функция в настоящее время поддерживается в версии .Net.
{{% /alert %}}