---
title: Ekspor data Excel untuk mengisi formulir PDF
type: docs
weight: 10
url: id/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Bagian ini menjelaskan bagaimana Anda dapat mengekspor data lembar kerja Excel untuk mengisi formulir PDF menggunakan Kelas AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF untuk .NET](/pdf/net/) menawarkan berbagai cara untuk mengisi formulir Pdf. Anda dapat mengimpor data dari file XML, DFD, XFDF, menggunakan API, dan bahkan dapat menggunakan data dari lembar kerja Excel. Kami akan menggunakan metode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) dari kelas [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) dari [Aspose.Cells](https://docs.aspose.com//cells/net) untuk mengekspor data dari lembar Excel ke dalam objek DataTable. Kemudian kita perlu mengimpor data ini ke dalam bentuk Pdf menggunakan metode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) dari kelas [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Pastikan bahwa nama Kolom dari DataTable sama dengan nama field pada formulir PDF.

{{% /alert %}}

## Rincian Implementasi

Dalam skenario berikut, kita akan menggunakan formulir PDF, yang berisi tiga field formulir bernama ID, Name, dan Gender.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

Dalam Formulir yang ditentukan di atas memiliki satu halaman, dengan tiga field bernama "ID", "Name", dan "Gender" secara berurutan. Kita akan mengekstrak data dari lembar excel berikut ke dalam objek DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Kita perlu membuat objek dari kelas [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) dan mengikat formulir Pdf yang ada di gambar di atas dan menggunakan metode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) untuk mengisi field formulir menggunakan data yang ada di objek DataTable.Setelah metode dipanggil, file formulir Pdf baru dihasilkan, yang berisi lima halaman dengan formulir yang diisi berdasarkan data dari lembar Excel. Formulir Pdf masukan adalah halaman tunggal dan hasilnya adalah lima halaman, karena jumlah baris data di lembar excel adalah 5. Kelas DataTable menawarkan kemampuan untuk menggunakan baris pertama dari lembar sebagai ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// Membuat aliran file yang berisi file Excel untuk dibuka
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Membuka file Excel melalui aliran file
workbook.Open(fstream);
// Mengakses lembar kerja pertama dalam file Excel
Worksheet worksheet = workbook.Worksheets[0];
// Mengekspor isi dari 7 baris dan 2 kolom mulai dari sel pertama ke DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Menutup aliran file untuk membebaskan semua sumber daya
fstream.Close();
// Membuat objek dari kelas AutoFiller
AutoFiller autoFiller = new AutoFiller();
// File pdf masukan yang berisi bidang formulir
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// File pdf hasil, yang akan berisi bidang formulir yang diisi dengan informasi dari DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Memanggil metode untuk mengimpor data dari objek DataTable ke bidang formulir Pdf.
autoFiller.ImportDataTable(dataTable);
// Memanggil metode simpan untuk menghasilkan file pdf
autoFiller.Save();
```

Untuk mengisi dari XLSX silakan gunakan potongan kode berikut:

```csharp
internal static void FillFromXLSX()
        {
            // Buat objek dari kelas AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // File pdf input yang berisi bidang formulir
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // Panggil metode untuk mengimpor data dari objek DataTable ke bidang formulir Pdf.
            autoFiller.ImportDataTable(dataTable);


            // Pdf hasil, yang akan berisi bidang formulir yang diisi dengan informasi dari DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF untuk .NET memungkinkan Anda untuk menghasilkan Tabel Data dalam dokumen PDF:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // Buat DataTable baru.
            System.Data.DataTable table = new DataTable("Students");
            // Deklarasikan variabel untuk objek DataColumn dan DataRow.
            DataColumn column;
            DataRow row;

            // Buat DataColumn baru, setel DataType,
            // ColumnName dan tambahkan ke DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // Tambahkan Kolom ke DataColumnCollection.
            table.Columns.Add(column);

            // Buat kolom kedua.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // Tambahkan kolom ke tabel.
            table.Columns.Add(column);

            // Jadikan kolom ID sebagai kolom kunci utama.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // Buat tiga objek DataRow baru dan tambahkan
            // mereka ke DataTable
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

## Kesimpulan

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) juga menawarkan kemampuan untuk mengisi formulir PDF menggunakan data dari basis data tetapi fitur ini saat ini didukung dalam versi .Net.
{{% /alert %}}