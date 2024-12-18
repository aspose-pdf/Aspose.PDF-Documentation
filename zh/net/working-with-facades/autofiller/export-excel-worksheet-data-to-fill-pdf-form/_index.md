---
title: 将Excel数据导出以填写PDF表单
type: docs
weight: 10
url: /zh/net/export-excel-worksheet-data-to-fill-pdf-form/
description: 本节解释了如何使用AutoFiller类将Excel工作表数据导出以填写PDF表单。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/zh/net/) 中提供了多种填写Pdf表单的方法。您可以从XML文件、DFD、XFDF导入数据，可以使用API，甚至可以使用Excel工作表中的数据。
我们将使用 [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) 方法，该方法属于 [Aspose.Cells](https://docs.aspose.com//cells/net) 的 [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) 类，将Excel表中的数据导出到DataTable对象中。 然后，我们需要使用 [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 类的 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 方法将这些数据导入到 PDF 表单中。确保 DataTable 的列名称与 PDF 表单上的字段名称相同。
{{% /alert %}}

## 实施细节

在以下场景中，我们将使用一个 PDF 表单，其中包含三个名为 ID、Name 和 Gender 的表单字段。

在上面指定的表单中有一页，包含 "ID"、"Name" 和 "Gender" 三个字段。我们将从以下 Excel 表中提取数据到 DataTable 对象。

我们需要创建一个 [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 类的对象，并绑定上图中的 PDF 表单，并使用 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 方法使用 DataTable 对象中的数据填充表单字段。一旦调用该方法，就会生成一个新的 Pdf 表单文件，其中包含根据 Excel 表中的数据填写的五页表单。输入的 Pdf 表单是单页的，而结果是五页的，因为 Excel 表中的数据行数为 5。DataTable 类提供了使用工作表第一行作为 ColumnName 的功能。

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// 创建一个包含要打开的 Excel 文件的文件流
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// 通过文件流打开 Excel 文件
workbook.Open(fstream);
// 访问 Excel 文件中的第一个工作表
Worksheet worksheet = workbook.Worksheets[0];
// 从第一个单元格开始导出 7 行 2 列的内容到 DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// 关闭文件流以释放所有资源
fstream.Close();
// 创建 AutoFiller 类的对象
AutoFiller autoFiller = new AutoFiller();
// 包含表单字段的输入 pdf 文件
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// 结果 pdf 文件，将包含用 DataTable 信息填充的表单字段
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// 调用方法将 DataTable 对象中的数据导入 Pdf 表单字段。
autoFiller.ImportDataTable(dataTable);
// 调用保存方法生成 pdf 文件
autoFiller.Save();
```

要从 XLSX 填充，请使用以下代码段：

```csharp
internal static void FillFromXLSX()
        {
            // 创建 AutoFiller 类的对象
            AutoFiller autoFiller = new AutoFiller();
            // 包含表单字段的输入 pdf 文件
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // 调用方法将数据从 DataTable 对象导入到 Pdf 表单字段中。
            autoFiller.ImportDataTable(dataTable);

            // 生成的 pdf，将包含用 DataTable 信息填充的表单字段
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF for .NET 允许您在 PDF 文档中生成数据表：

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // 创建一个新的 DataTable。
            System.Data.DataTable table = new DataTable("Students");
            // 声明 DataColumn 和 DataRow 对象的变量。
            DataColumn column;
            DataRow row;

            // 创建新的 DataColumn，设置 DataType，
            // ColumnName 并添加到 DataTable。
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // 将列添加到 DataColumnCollection。
            table.Columns.Add(column);

            // 创建第二列。
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // 将列添加到表中。
            table.Columns.Add(column);

            // 使 ID 列成为主键列。
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // 创建三个新的 DataRow 对象并添加
            // 它们到 DataTable 中
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

## 结论

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 还提供了使用数据库中的数据填写 PDF 表单的功能，但此功能目前仅在 .Net 版本中支持。
{{% /alert %}}