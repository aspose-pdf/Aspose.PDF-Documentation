---
title: Merender tabel dengan Entity Framework
linktitle: Merender tabel dengan Entity Framework
type: docs
weight: 40
url: /net/render-table-using-entity-framework-model-as-data-source/
description: Artikel ini akan menunjukkan cara merender tabel menggunakan model Entity Framework sebagai sumber data menggunakan Aspose.PDF untuk .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Terdapat sejumlah tugas ketika untuk beberapa alasan lebih nyaman untuk mengekspor data dari basis data ke dokumen PDF tanpa menggunakan skema konversi HTML ke PDF yang baru-baru ini populer.

Artikel ini akan menunjukkan cara menghasilkan dokumen PDF menggunakan Aspose.PDF untuk .NET.

## Dasar-dasar pembuatan PDF dengan Aspose.PDF

Salah satu kelas paling penting dalam Aspose.PDF adalah [kelas Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document). Kelas ini adalah mesin rendering PDF. Untuk menggambarkan struktur PDF, pustaka Aspose.PDF menggunakan model Dokumen-Halaman, di mana:

* Dokumen - berisi properti dari dokumen PDF termasuk koleksi halaman;
* Dokumen - berisi properti dokumen PDF termasuk koleksi halaman;
* Halaman - berisi properti halaman tertentu dan berbagai koleksi elemen yang terkait dengan halaman ini.

Oleh karena itu, untuk membuat dokumen PDF dengan Aspose.PDF, Anda harus mengikuti langkah-langkah berikut:

1. Buat objek Dokumen;
1. Tambahkan halaman (objek Halaman) untuk objek Dokumen;
1. Buat objek yang ditempatkan di halaman (misalnya fragmen teks, tabel, dll.)
1. Tambahkan item yang dibuat ke koleksi yang sesuai di halaman (dalam kasus kita akan menjadi koleksi paragraf);
1. Simpan dokumen sebagai file PDF.

```csharp
// Langkah 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Langkah 2
var pdfPage = document.Pages.Add();

// Langkah 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Langkah 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Langkah 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
Masalah yang paling umum adalah output data dalam format tabel. [Kelas Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) digunakan untuk memproses tabel. Kelas ini memberi kita kemampuan untuk membuat tabel dan menempatkannya dalam dokumen, menggunakan [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) dan [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Jadi, untuk membuat tabel, Anda perlu menambahkan jumlah baris yang diperlukan dan mengisi mereka dengan jumlah sel yang sesuai.

Contoh berikut ini membuat tabel 4x10.

```csharp
var table = new Table
    {
        // Atur lebar kolom otomatis dari tabel
        ColumnWidths = "25% 25% 25% 25%",
        // Atur padding sel
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Kiri Bawah Kanan Atas
        // Atur warna batas tabel sebagai Hijau
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Atur batas untuk sel tabel sebagai Hitam
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Tambahkan baris ke tabel
        var row = table.Rows.Add();
        // Tambahkan sel tabel
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Tambahkan objek tabel ke halaman pertama dokumen masukan
    document.Pages[1].Paragraphs.Add(table);
```
Saat menginisialisasi objek Tabel, pengaturan skin minimal digunakan:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - lebar kolom (secara default);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - padding sel default untuk sel tabel;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atribut bingkai tabel (gaya, ketebalan, warna);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atribut bingkai sel (gaya, ketebalan, warna).

Sebagai hasilnya, kita mendapatkan tabel 4x10 dengan kolom berukuran sama lebar.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Mengekspor Data dari Objek ADO.NET

Kelas Tabel menyediakan metode untuk berinteraksi dengan sumber data ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) dan [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Kelas Table menyediakan metode untuk berinteraksi dengan sumber data ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) dan [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Mengingat bahwa objek-objek ini tidak sangat nyaman untuk digunakan dalam template MVC, kita akan membatasi diri pada contoh singkat. Dalam contoh ini (baris 50), metode ImportDataTable dipanggil dan menerima sebagai parameter sebuah instansi DataTable dan pengaturan tambahan seperti bendera header dan posisi awal (baris/kolom) untuk output data.

```csharp
// Buat dokumen PDF baru
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Inisialisasi instansi baru dari TextFragment untuk judul laporan
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Atur lebar kolom dari tabel
    ColumnWidths = "25% 25% 25% 25%",
    // Atur padding sel
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Kiri Bawah Kanan Atas
    // Atur warna batas tabel menjadi Hijau
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Atur batas untuk sel tabel menjadi Hitam
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Tidak ada string koneksi di config.json");

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

// Tambahkan objek tabel ke halaman pertama dari dokumen masukan
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
## Mengekspor Data dari Entity Framework

Lebih relevan untuk .NET modern adalah impor data dari kerangka kerja ORM. Dalam kasus ini, ide yang baik adalah memperluas kelas Table dengan metode ekstensi untuk mengimpor data dari daftar sederhana atau dari data yang dikelompokkan. Mari kita berikan contoh untuk salah satu ORM yang paling populer - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Tambahkan baris ke tabel
                var row = table.Rows.Add();
                // Tambahkan sel tabel
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Tambahkan baris grup ke tabel
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Tambahkan baris data ke tabel
                    var dataRow = table.Rows.Add();
                    // Tambahkan sel
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```
Atribut Data Annotations sering digunakan untuk mendeskripsikan model dan membantu kita untuk membuat tabel. Oleh karena itu, algoritma pembuatan tabel berikut dipilih untuk ImportEntityList:

* baris 12-18: membangun baris header dan menambahkan sel header sesuai dengan aturan "Jika DisplayAttribute ada, maka ambil nilainya jika tidak ambil nama properti"
* baris 50-53: membangun baris data dan menambahkan sel baris sesuai dengan aturan "Jika atribut DataTypeAttribute didefinisikan, maka kita periksa apakah kita perlu membuat pengaturan desain tambahan untuk itu, dan jika tidak, hanya mengonversi data menjadi string dan menambahkannya ke sel;"

Dalam contoh ini, penyesuaian kustom tambahan dibuat untuk DataType.Currency (baris 32-34) dan DataType.Date (baris 35-43), tetapi Anda dapat menambahkan yang lain jika diperlukan.
Algoritma metode ImportGroupedData hampir sama dengan yang sebelumnya. Kelas GroupViewModel tambahan digunakan, untuk menyimpan data yang dikelompokkan.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Karena kami memproses grup, pertama kami membuat baris untuk nilai kunci (baris 66-71), dan setelah itu - baris dari grup ini.
