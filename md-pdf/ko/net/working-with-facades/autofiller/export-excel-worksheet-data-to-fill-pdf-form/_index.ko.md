---
title: 엑셀 데이터 내보내기하여 PDF 양식 채우기
type: docs
weight: 10
url: /net/export-excel-worksheet-data-to-fill-pdf-form/
description: 이 섹션에서는 AutoFiller 클래스를 사용하여 엑셀 워크시트 데이터를 내보내어 PDF 양식을 채우는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/)의 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 PDF 양식을 채우는 다양한 방법을 제공합니다. XML 파일, DFD, XFDF에서 데이터를 가져오거나 API를 사용하고 엑셀 워크시트의 데이터를 사용할 수도 있습니다. 우리는 [Aspose.Cells](https://docs.aspose.com//cells/net)의 [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) 클래스의 [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) 메서드를 사용하여 엑셀 시트의 데이터를 DataTable 객체로 내보낼 것입니다. 그런 다음 [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 클래스의 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 메서드를 사용하여 이 데이터를 PDF 양식으로 가져와야 합니다. DataTable의 열 이름이 PDF 양식의 필드 이름과 동일한지 확인하십시오.

{{% /alert %}}

## 구현 세부 사항

다음 시나리오에서는 ID, Name 및 Gender라는 세 가지 양식 필드가 있는 PDF 양식을 사용합니다.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

위에 지정된 양식에는 "ID", "Name" 및 "Gender"라는 세 개의 필드가 있는 한 페이지가 있습니다. 다음 엑셀 시트의 데이터를 DataTable 객체로 추출합니다.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

[AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 클래스의 객체를 생성하고 위의 사진에 있는 PDF 양식을 바인딩한 다음 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 메서드를 사용하여 DataTable 객체에 있는 데이터를 사용하여 양식 필드를 채워야 합니다.Once the method is called a new Pdf form file is generated, which contains five pages with form filled based over the data from Excel sheet. Input Pdf form was single page and resultant is five pages, because the number of data rows in excel sheet is 5. The DataTable class offers the capability to use the first row of the sheet as ColumnName.

메서드가 호출되면 Excel 시트의 데이터를 기반으로 양식이 채워진 새 Pdf 양식 파일이 생성됩니다. 입력 Pdf 양식은 단일 페이지였고 결과는 Excel 시트의 데이터 행 수가 5개이기 때문에 5페이지입니다. DataTable 클래스는 시트의 첫 번째 행을 ColumnName으로 사용할 수 있는 기능을 제공합니다.

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

XLSX에서 채우려면 다음 코드 스니펫을 사용하세요:

```csharp
internal static void FillFromXLSX()
        {
            // AutoFiller 클래스의 객체 생성
            AutoFiller autoFiller = new AutoFiller();
            // 양식 필드가 포함된 입력 pdf 파일
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // DataTable 객체에서 Pdf 양식 필드로 데이터를 가져오는 메서드 호출
            autoFiller.ImportDataTable(dataTable);

            // DataTable의 정보로 채워진 양식 필드를 포함하는 결과 pdf
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF for .NET을 사용하면 PDF 문서에서 데이터 테이블을 생성할 수 있습니다:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // 새로운 DataTable 생성
            System.Data.DataTable table = new DataTable("Students");
            // DataColumn 및 DataRow 객체에 대한 변수 선언
            DataColumn column;
            DataRow row;

            // 새로운 DataColumn 생성, DataType 설정,
            // ColumnName 설정 및 DataTable에 추가
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // DataColumnCollection에 열 추가
            table.Columns.Add(column);

            // 두 번째 열 생성
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // 테이블에 열 추가
            table.Columns.Add(column);

            // ID 열을 기본 키 열로 설정
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // 세 개의 새로운 DataRow 객체 생성 및
            // DataTable에 추가
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

## 결론

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 또한 데이터베이스의 데이터를 사용하여 PDF 양식을 채우는 기능을 제공하지만 이 기능은 현재 .Net 버전에서 지원됩니다.
{{% /alert %}}