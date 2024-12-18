---
title: Integrasikan Tabel dengan Sumber Data PDF
linktitle: Integrasikan Tabel
type: docs
weight: 30
url: /id/net/integrate-table/
description: Artikel ini menunjukkan cara mengintegrasikan tabel PDF. Integrasikan Tabel dengan Database dan tentukan apakah tabel akan terpecah di halaman saat ini.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrasikan Tabel dengan Sumber Data PDF",
    "alternativeHeadline": "Cara mengintegrasikan Tabel dengan Sumber Data PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, c#, integrate table",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menunjukkan cara mengintegrasikan tabel PDF. Integrasikan Tabel dengan Database dan tentukan apakah tabel akan terpecah di halaman saat ini."
}
</script>
Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengintegrasikan Tabel dengan Basis Data

Basis data dibangun untuk menyimpan dan mengelola data. Sudah menjadi praktik umum bagi pemrogram untuk mengisi berbagai objek dengan data dari basis data. Artikel ini membahas tentang menambahkan data dari basis data ke dalam tabel. Dimungkinkan untuk mengisi objek [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) dengan data dari sumber data apa pun menggunakan Aspose.PDF untuk .NET. Dan tidak hanya mungkin, tetapi sangat mudah.

[Aspose.PDF untuk .NET](https://docs.aspose.com/pdf/net/) memungkinkan pengembang untuk mengimpor data dari:

- Array Objek
- DataTable
- DataView

Topik ini memberikan informasi tentang pengambilan data dari DataTable atau DataView.

Semua pengembang yang bekerja di bawah platform .NET harus familiar dengan konsep-konsep ADO.NET dasar yang diperkenalkan oleh .NET Framework.
Semua pengembang yang bekerja di bawah platform .NET harus mengenal konsep dasar ADO.NET yang diperkenalkan oleh .NET Framework.

Metode ImportDataTable(..) dan ImportDataView(..) dari kelas Table digunakan untuk mengimpor data dari basis data.

Contoh di bawah ini menunjukkan penggunaan metode ImportDataTable. Dalam contoh ini, objek DataTable dibuat dari awal dan catatan ditambahkan secara terprogram bukan mengisi DataTable dengan data dari basis data. Pengembang dapat mengisi DataTable dari basis data juga sesuai dengan keinginan mereka.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// Tambahkan 2 baris ke dalam objek DataTable secara terprogram
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// Buat instance Dokumen
Document doc = new Document();
doc.Pages.Add();
// Inisialisasi instance baru dari Tabel
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Atur lebar kolom tabel
table.ColumnWidths = "40 100 100 100";
// Atur warna batas tabel sebagai LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Atur batas untuk sel tabel
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Tambahkan objek tabel ke halaman pertama dokumen masukan
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Simpan dokumen yang diperbarui berisi objek tabel
doc.Save(dataDir);
```
## Bagaimana menentukan jika tabel akan terputus di halaman saat ini

Tabel secara default ditambahkan dari posisi kiri atas dan jika tabel mencapai akhir halaman, secara otomatis terputus. Anda dapat secara programatik mendapatkan informasi apakah Tabel akan muat di halaman saat ini atau akan terputus di bagian bawah halaman. Untuk itu, pertama, Anda perlu mendapatkan informasi ukuran dokumen, kemudian Anda perlu mendapatkan informasi margin atas dan bawah halaman, informasi margin atas tabel dan tinggi tabel. Jika Anda menambahkan margin Atas Halaman + margin Bawah Halaman + margin Atas Tabel + tinggi Tabel dan menguranginya dari tinggi dokumen, Anda dapat memperoleh jumlah ruang yang tersisa di atas dokumen. Tergantung pada tinggi baris tertentu (yang telah Anda tentukan), Anda dapat menghitung apakah semua baris dari sebuah tabel dapat diakomodasi dalam ruang yang tersisa di atas halaman atau tidak. Silakan lihat potongan kode berikut. Dalam kode berikut, tinggi rata-rata baris adalah 23.002 Poin.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instansiasi objek kelas PDF
Document pdf = new Document();
// Tambahkan bagian ke koleksi bagian dokumen PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// Instansiasi objek tabel
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Tambahkan tabel ke koleksi paragraf bagian yang diinginkan
page.Paragraphs.Add(table1);
// Setel lebar kolom tabel
table1.ColumnWidths = "100 100 100";
// Setel batas sel default menggunakan objek BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Setel batas tabel menggunakan objek BorderInfo yang disesuaikan lainnya
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Buat objek MarginInfo dan setel margin kiri, bawah, kanan, dan atasnya
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Setel bantalan sel default ke objek MarginInfo
table1.DefaultCellPadding = margin;
// Jika Anda meningkatkan counter menjadi 17, tabel akan terputus
// Karena tidak dapat lagi diakomodasi di halaman ini
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Buat baris di tabel dan kemudian sel di baris
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 3");
}
// Dapatkan informasi Tinggi Halaman
float PageHeight = (float)pdf.PageInfo.Height;
// Dapatkan informasi tinggi total margin Atas & Bawah halaman,
// Margin Atas tabel dan tinggi tabel.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Tampilkan Tinggi Halaman, Tinggi Tabel, informasi margin Atas tabel dan Atas
// Dan informasi margin Bawah halaman
Console.WriteLine("Tinggi dokumen PDF = " + pdf.PageInfo.Height.ToString() + "\nInfo Margin Atas = " + page.PageInfo.Margin.Top.ToString() + "\nInfo Margin Bawah = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nInfo Margin Atas Tabel = " + table1.Margin.Top.ToString() + "\nTinggi Rata-rata Baris = " + table1.Rows[0].MinRowHeight.ToString() + " \nTinggi tabel " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTinggi Halaman Total =" + PageHeight.ToString() + "\nTinggi Kumulatif termasuk Tabel =" + TotalObjectsHeight.ToString());

// Periksa jika kita mengurangi jumlah margin Atas Halaman + margin Bawah Halaman
// + Margin Atas Tabel dan tinggi tabel dari tinggi Halaman dan kurang
// Dari 10 (rata-rata baris bisa lebih dari 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // Jika nilai kurang dari 10, maka tampilkan pesan.
    // Yang menunjukkan bahwa baris lain tidak dapat ditempatkan dan jika kita menambahkan baru
    // Baris, tabel akan terputus. Ini tergantung pada nilai tinggi baris.
    Console.WriteLine("Tinggi Halaman - Tinggi Objek < 10, jadi tabel akan terputus");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Simpan dokumen pdf
pdf.Save(dataDir);
```
## Menambahkan Kolom Berulang dalam Tabel

Dalam kelas Aspose.Pdf.Table, Anda dapat mengatur RepeatingRowsCount yang akan mengulang baris jika tabel terlalu panjang secara vertikal dan meluap ke halaman berikutnya. Namun, dalam beberapa kasus, tabel terlalu lebar untuk muat dalam satu halaman dan perlu dilanjutkan ke halaman berikutnya. Untuk tujuan ini, kami telah mengimplementasikan properti RepeatingColumnsCount di kelas Aspose.Pdf.Table. Mengatur properti ini akan menyebabkan tabel patah ke halaman berikutnya berdasarkan kolom dan mengulang jumlah kolom yang diberikan di awal halaman berikutnya. Cuplikan kode berikut menunjukkan penggunaan properti RepeatingColumnsCount:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Buat dokumen baru
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Instansiasi tabel luar yang menempati seluruh halaman
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Instansiasi objek tabel yang akan ditempatkan di dalam outerTable yang akan patah di dalam halaman yang sama
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Tambahkan outerTable ke paragraf halaman
// Tambahkan mytable ke outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Tambahkan Baris Header
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("header 1");
row.Cells.Add("header 2");
row.Cells.Add("header 3");
row.Cells.Add("header 4");
row.Cells.Add("header 5");
row.Cells.Add("header 6");
row.Cells.Add("header 7");
row.Cells.Add("header 11");
row.Cells.Add("header 12");
row.Cells.Add("header 13");
row.Cells.Add("header 14");
row.Cells.Add("header 15");
row.Cells.Add("header 16");
row.Cells.Add("header 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Buat baris dalam tabel dan kemudian sel dalam baris
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("kol " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## Integrasikan Tabel dengan Sumber Entity Framework

Lebih relevan untuk .NET modern adalah impor data dari kerangka kerja ORM. Dalam hal ini, ide yang baik adalah memperluas kelas Tabel dengan metode ekstensi untuk mengimpor data dari daftar sederhana atau dari data yang dikelompokkan. Mari kita berikan contoh untuk salah satu ORM yang paling populer - Entity Framework.

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
Atribut Data Annotations sering digunakan untuk mendeskripsikan model dan membantu kita membuat tabel. Oleh karena itu, algoritma pembuatan tabel berikut dipilih untuk ImportEntityList:

- baris 12-18: membangun baris header dan menambahkan sel header sesuai dengan aturan "Jika DisplayAttribute ada, maka ambil nilainya, jika tidak ambil nama properti"
- baris 50-53: membangun baris data dan menambahkan sel baris sesuai dengan aturan "Jika atribut DataTypeAttribute didefinisikan, maka kita periksa apakah kita perlu membuat pengaturan desain tambahan untuk itu, dan jika tidak, hanya konversikan data menjadi string dan tambahkan ke sel;"

Dalam contoh ini, penyesuaian khusus dibuat untuk DataType.Currency (baris 32-34) dan DataType.Date (baris 35-43), tetapi Anda dapat menambahkan lainnya jika perlu.
Algoritma dari metode ImportGroupedData hampir sama dengan yang sebelumnya. Kelas GroupViewModel tambahan digunakan untuk menyimpan data yang dikelompokkan.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Karena kami memproses grup, pertama kami membuat baris untuk nilai kunci (baris 66-71), dan setelah itu - baris-baris dari grup ini.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

