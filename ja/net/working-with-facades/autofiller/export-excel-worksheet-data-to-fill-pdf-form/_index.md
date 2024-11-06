---
title: ExcelデータをエクスポートしてPDFフォームに入力
type: docs
weight: 10
url: ja/net/export-excel-worksheet-data-to-fill-pdf-form/
description: このセクションでは、AutoFillerクラスを使用してExcelワークシートデータをエクスポートし、PDFフォームに入力する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) は、PDFフォームを入力するためのさまざまな方法を提供します。XMLファイル、DFD、XFDFからデータをインポートしたり、APIを使用したり、Excelワークシートのデータを使用することもできます。ExcelシートからデータをDataTableオブジェクトにエクスポートするために、[Aspose.Cells](https://docs.aspose.com//cells/net)の[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells)クラスの[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index)メソッドを使用します。
``` その後、このデータを [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) クラスの [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) メソッドを使用して PDF フォームにインポートする必要があります。DataTable の列名が PDF フォーム上のフィールド名と同じであることを確認してください。

{{% /alert %}}

## 実装の詳細

次のシナリオでは、ID、Name、Gender という名前の 3 つのフォーム フィールドを含む PDF フォームを使用します。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

上記のフォームには 1 ページがあり、「ID」、「Name」、「Gender」という 3 つのフィールドがあります。以下のエクセルシートからデータを DataTable オブジェクトに抽出します。

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

[AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) クラスのオブジェクトを作成し、上記の画像にある Pdf フォームをバインドして、DataTable オブジェクトにあるデータを使用してフォーム フィールドを埋めるために [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) メソッドを使用する必要があります。メソッドが呼び出されると、新しいPdfフォームファイルが生成され、Excelシートのデータに基づいてフォームが埋め込まれた5ページが含まれます。入力されたPdfフォームは1ページであり、結果は5ページです。これは、Excelシートのデータ行数が5だからです。DataTableクラスは、シートの最初の行をColumnNameとして使用する機能を提供します。

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// 開くためのExcelファイルを含むファイルストリームの作成
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// ファイルストリームを通してExcelファイルを開く
workbook.Open(fstream);
// Excelファイル内の最初のワークシートにアクセス
Worksheet worksheet = workbook.Worksheets[0];
// 最初のセルから始まる7行と2列の内容をDataTableにエクスポート
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// リソースをすべて解放するためにファイルストリームを閉じる
fstream.Close();
// AutoFillerクラスのオブジェクトを作成
AutoFiller autoFiller = new AutoFiller();
// フォームフィールドを含む入力pdfファイル
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// DataTableから情報が入力されたフォームフィールドを含む結果のpdf
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// PdfフォームフィールドにDataTableオブジェクトからデータをインポートするメソッドを呼び出す
autoFiller.ImportDataTable(dataTable);
// pdfファイルを生成するためのセーブメソッドを呼び出す
autoFiller.Save();
```

XLSXから入力するには、次のコードスニペットを使用してください:

```csharp
internal static void FillFromXLSX()
        {
            // AutoFillerクラスのオブジェクトを作成
            AutoFiller autoFiller = new AutoFiller();
            // フォームフィールドを含む入力pdfファイル
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // DataTableオブジェクトからPdfフォームフィールドにデータをインポートするメソッドを呼び出します。
            autoFiller.ImportDataTable(dataTable);

            // DataTableからの情報でフォームフィールドが埋められた結果のpdf
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF for .NETは、PDFドキュメントでデータテーブルを生成することを可能にします:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // 新しいDataTableを作成。
            System.Data.DataTable table = new DataTable("Students");
            // DataColumnおよびDataRowオブジェクトの変数を宣言。
            DataColumn column;
            DataRow row;

            // 新しいDataColumnを作成し、DataType、ColumnNameを設定し、DataTableに追加します。
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // ColumnをDataColumnCollectionに追加します。
            table.Columns.Add(column);

            // 2番目のColumnを作成。
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // テーブルにColumnを追加します。
            table.Columns.Add(column);

            // IDカラムを主キーカラムにします。
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // 3つの新しいDataRowオブジェクトを作成し、それらをDataTableに追加します。
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

## 結論

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) には、データベースからのデータを使用して PDF フォームを記入する機能もありますが、この機能は現在 .Net バージョンでサポートされています。
{{% /alert %}}