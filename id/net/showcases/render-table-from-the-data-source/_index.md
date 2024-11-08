---
title: Render table dari sumber data
linktitle: Render table dari sumber data
type: docs
weight: 30
url: /id/net/render-table-from-the-data-source/
description: Halaman ini menjelaskan bagaimana mungkin merender tabel dari sumber data menggunakan perpustakaan Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF memungkinkan Anda untuk membuat tabel dengan DataSource dari DataSet, Data Table, array dan objek IEnumerable menggunakan kelas PdfLightTable

[Kelas Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) digunakan untuk memproses tabel. Kelas ini memberi kita kemampuan untuk membuat tabel dan menempatkannya di dalam dokumen, menggunakan [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) dan [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Jadi, untuk membuat tabel, Anda perlu menambahkan jumlah baris yang diperlukan dan mengisinya dengan jumlah sel yang sesuai.

Contoh berikut membuat tabel 4x10.

```csharp
var table = new Table
    {
        // Set lebar kolom otomatis dari tabel
        ColumnWidths = "25% 25% 25% 25%",
        // Set padding sel
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Kiri Bawah Kanan Atas
        // Set warna border tabel sebagai Hijau
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Set border untuk sel tabel sebagai Hitam
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Tambahkan baris ke tabel
        var row = table.Rows.Add();
        // Tambahkan sel tabel
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Sel ({i+1}, {rowCount +1})");
        }
    }
    // Tambahkan objek tabel ke halaman pertama dokumen masukan
    document.Pages[1].Paragraphs.Add(table);
```

Saat menginisialisasi objek Table, pengaturan skin minimal digunakan:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - lebar kolom (secara default);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - padding sel tabel default;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atribut bingkai tabel (gaya, ketebalan, warna);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atribut bingkai sel (gaya, ketebalan, warna).

## Mengekspor data dari array objek

Kelas Table menyediakan metode untuk berinteraksi dengan sumber data ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) dan [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

Mengingat bahwa objek-objek ini tidak sangat nyaman untuk digunakan dalam template MVC, kita akan membatasi diri pada contoh singkat. Dalam contoh ini (baris 50), metode ImportDataTable dipanggil dan menerima sebagai parameter sebuah instansi DataTable dan pengaturan tambahan seperti bendera header dan posisi awal (baris/kolom) untuk output data.

```csharp
// Membuat dokumen PDF baru
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Menginisialisasi instansi baru dari TextFragment untuk judul laporan
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Mengatur lebar kolom dari tabel
    ColumnWidths = "25% 25% 25% 25%",
    // Mengatur padding sel
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Kiri Bawah Kanan Atas
    // Mengatur warna border tabel menjadi Hijau
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Mengatur border untuk sel tabel menjadi Hitam
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Tidak ada string koneksi dalam config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// Menambahkan objek tabel ke halaman pertama dokumen masukan
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```

