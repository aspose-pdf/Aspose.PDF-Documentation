---
title: Membuat atau Menambahkan Tabel dalam PDF menggunakan C#
linktitle: Membuat atau Menambahkan Tabel
type: docs
weight: 10
url: /id/net/add-table-in-existing-pdf-document/
description: Aspose.PDF untuk .NET adalah perpustakaan yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Periksa fungsi lanjutan lainnya dalam topik ini.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat atau Menambahkan Tabel dalam PDF menggunakan C#",
    "alternativeHeadline": "Cara menambahkan Tabel dalam PDF dengan .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, membuat tabel dalam pdf, menambahkan tabel",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET adalah perpustakaan yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Periksa fungsi lanjutan lainnya dalam topik ini."
}
</script>
## Membuat Tabel menggunakan C\#

Tabel sangat penting ketika bekerja dengan dokumen PDF. Mereka menyediakan fitur yang baik untuk menampilkan informasi secara sistematis. Namespace Aspose.PDF mengandung kelas yang bernama [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), dan [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) yang menyediakan fungsionalitas untuk membuat tabel saat menghasilkan dokumen PDF dari awal.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Tabel dapat dibuat dengan membuat objek dari Kelas Tabel.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Menambahkan Tabel dalam Dokumen PDF yang Ada

Untuk menambahkan tabel ke dalam file PDF yang ada dengan Aspose.PDF untuk .NET, ikuti langkah-langkah berikut:

1. Muat file sumber.
1. Inisialisasi tabel dan atur kolom serta barisnya.
1. Atur pengaturan tabel (kita telah mengatur batasannya).
1. Isi tabel.
1. Tambahkan tabel ke halaman.
1.
Potongan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang sudah ada.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Muat dokumen PDF sumber
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Inisialisasi instance baru dari Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Atur warna batas tabel sebagai LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Atur batas untuk sel tabel
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Buat loop untuk menambahkan 10 baris
for (int row_count = 1; row_count < 10; row_count++)
{
    // Tambahkan baris ke tabel
    Aspose.Pdf.Row row = table.Rows.Add();
    // Tambahkan sel tabel
    row.Cells.Add("Kolom (" + row_count + ", 1)");
    row.Cells.Add("Kolom (" + row_count + ", 2)");
    row.Cells.Add("Kolom (" + row_count + ", 3)");
}
// Tambahkan objek tabel ke halaman pertama dokumen masukan
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// Simpan dokumen yang telah diperbarui yang mengandung objek tabel
doc.Save(dataDir);
```
### ColSpan dan RowSpan dalam Tabel

Aspose.PDF untuk .NET menyediakan properti [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) untuk menggabungkan kolom dalam sebuah tabel dan properti [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) untuk menggabungkan baris.

Kita menggunakan properti `ColSpan` atau `RowSpan` pada objek `Cell` yang menciptakan sel tabel. Setelah menerapkan properti yang diperlukan, sel yang dibuat dapat ditambahkan ke tabel.

```csharp
public static void AddTable_RowColSpan()
{
    // Memuat dokumen PDF sumber
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Menginisialisasi instance baru dari Tabel
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Mengatur warna border tabel sebagai LightGray
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Mengatur border untuk sel tabel
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Menambahkan baris pertama ke tabel
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Menambahkan sel tabel
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // Menambahkan baris kedua ke tabel
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // Menambahkan baris ketiga ke tabel
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // Menambahkan baris keempat ke tabel
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // Menambahkan baris kelima ke tabel
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // Menambahkan objek tabel ke halaman pertama dari dokumen masukan
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Menyimpan dokumen yang telah diperbarui yang mengandung objek tabel
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
Hasil eksekusi kode di bawah ini adalah tabel yang digambarkan pada gambar berikut:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Bekerja dengan Batas, Margin dan Padding

Harap dicatat bahwa ini juga mendukung fitur untuk mengatur gaya batas, margin, dan padding sel untuk tabel. Sebelum membahas lebih detail, penting untuk memahami konsep batas, margin, dan padding yang disajikan di bawah ini dalam diagram:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

Pada gambar di atas, Anda dapat melihat bahwa batas tabel, baris, dan sel tumpang tindih. Menggunakan Aspose.PDF, sebuah tabel dapat memiliki margin dan sel dapat memiliki padding. Untuk mengatur margin sel, kita harus mengatur padding sel.

### Batas

Untuk mengatur batas Tabel, objek [Baris](https://reference.aspose.com/pdf/net/aspose.pdf/row) dan [Sel](https://reference.aspose.com/pdf/net/aspose.pdf/cell), gunakan properti Table.Border, Row.Border, dan Cell.Border.
Untuk mengatur batas dari Tabel, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) dan [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), gunakan properti Table.Border, Row.Border dan Cell.Border.

### Margin atau Padding

Padding sel dapat dikelola menggunakan properti [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) dari kelas Table. Semua properti yang terkait dengan padding diberikan sebuah instance dari kelas [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) yang mengambil informasi tentang parameter `Left`, `Right`, `Top` dan `Bottom` untuk membuat margin khusus.

Pada contoh berikut, lebar batas sel diatur ke 0.1 poin, lebar batas tabel diatur ke 1 poin dan padding sel diatur ke 5 poin.

![Margin dan Batas dalam Tabel PDF](margin-border.png)

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Membuat instance objek Document dengan memanggil konstruktor kosongnya
Document doc = new Document();
Page page = doc.Pages.Add();
// Membuat instance objek tabel
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Menambahkan tabel ke koleksi paragraf bagian yang diinginkan
page.Paragraphs.Add(tab1);
// Mengatur lebar kolom tabel
tab1.ColumnWidths = "50 50 50";
// Mengatur batas sel default menggunakan objek BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Mengatur batas tabel menggunakan objek BorderInfo yang disesuaikan
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Membuat objek MarginInfo dan mengatur margin kiri, bawah, kanan, dan atasnya
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Mengatur padding sel default ke objek MarginInfo
tab1.DefaultCellPadding = margin;
// Membuat baris di tabel dan kemudian sel di baris tersebut
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 dengan teks panjang");
// Row1.Cells.Add("col3 dengan teks panjang yang akan ditempatkan di dalam sel");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Menyimpan Pdf
doc.Save(dataDir);
```
Untuk membuat tabel dengan sudut bulat, gunakan nilai `RoundedBorderRadius` dari kelas BorderInfo dan atur gaya sudut tabel menjadi bulat.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Buat objek BorderInfo kosong
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Atur batas menjadi batas bulat dengan radius 15
bInfo.RoundedBorderRadius = 15;
// Atur gaya sudut tabel menjadi Bulat.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Atur informasi batas tabel
tab1.Border = bInfo;
```

## Menerapkan Berbagai Pengaturan AutoFit pada Tabel

Ketika membuat tabel menggunakan agen visual seperti Microsoft Word, Anda seringkali akan menggunakan salah satu opsi AutoFit untuk secara otomatis mengatur ukuran tabel sesuai dengan lebar yang diinginkan.
Saat membuat tabel menggunakan agen visual seperti Microsoft Word, Anda sering kali akan menggunakan salah satu opsi AutoFit untuk secara otomatis menyesuaikan ukuran tabel sesuai dengan lebar yang diinginkan.

Secara default Aspose.Pdf memasukkan tabel baru menggunakan `ColumnAdjustment` dengan nilai `Customized`. Tabel akan disesuaikan dengan lebar yang tersedia di halaman. Untuk mengubah perilaku ukuran pada tabel tersebut atau tabel yang sudah ada, Anda dapat memanggil metode Table.autoFit(int). Metode ini menerima enumerasi AutoFitBehavior yang mendefinisikan jenis penyesuaian otomatis yang diterapkan pada tabel.

Seperti di Microsoft Word, metode autofit sebenarnya adalah jalan pintas yang menerapkan berbagai properti pada tabel sekaligus. Properti-properti inilah yang sebenarnya memberikan perilaku yang diamati pada tabel. Kami akan membahas properti-properti ini untuk setiap opsi autofit. Kami akan menggunakan tabel berikut dan menerapkan pengaturan autofit yang berbeda sebagai demonstrasi:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instansiasi objek Pdf dengan memanggil konstruktornya yang kosong
Document doc = new Document();
// Buat bagian di objek Pdf
Page sec1 = doc.Pages.Add();

// Instansiasi objek tabel
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Tambahkan tabel ke koleksi paragraf bagian yang diinginkan
sec1.Paragraphs.Add(tab1);

// Tetapkan lebar kolom tabel
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Tetapkan batas sel default menggunakan objek BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Tetapkan batas tabel menggunakan objek BorderInfo yang disesuaikan lainnya
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Buat objek MarginInfo dan tetapkan margin kiri, bawah, kanan, dan atasnya
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Tetapkan padding sel default ke objek MarginInfo
tab1.DefaultCellPadding = margin;

// Buat baris dalam tabel dan kemudian sel dalam baris
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Simpan dokumen yang telah diperbarui yang berisi objek tabel
doc.Save(dataDir);
```
### Dapatkan Lebar Tabel

Terkadang, diperlukan untuk mendapatkan lebar tabel secara dinamis. Kelas Aspose.PDF.Table memiliki metode [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) untuk tujuan tersebut. Misalnya, Anda belum menetapkan lebar kolom tabel secara eksplisit dan mengatur [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) ke AutoFitToContent. Dalam kasus ini, Anda dapat mendapatkan lebar tabel sebagai berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Buat dokumen baru
Document doc = new Document();
// Tambahkan halaman dalam dokumen
Page page = doc.Pages.Add();
// Inisialisasi tabel baru
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Tambahkan baris dalam tabel
Row row = table.Rows.Add();
// Tambahkan sel dalam tabel
Cell cell = row.Cells.Add("Teks Sel 1");
cell = row.Cells.Add("Teks Sel 2");
// Dapatkan lebar tabel
Console.WriteLine(table.GetWidth());
```

## Tambahkan Gambar SVG ke Sel Tabel
## Tambahkan Gambar SVG ke Sel Tabel

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan sel tabel ke dalam file PDF. Saat membuat tabel, dimungkinkan untuk menambahkan teks atau gambar ke dalam sel. Selain itu, API juga menawarkan fitur untuk mengonversi file SVG ke format PDF. Dengan kombinasi fitur ini, dimungkinkan untuk memuat gambar SVG dan menambahkannya ke dalam sel tabel.

Potongan kode berikut menunjukkan langkah-langkah untuk membuat instance tabel dan menambahkan gambar SVG di dalam sel tabel.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instansiasi objek Dokumen
Document doc = new Document();
// Buat instansi gambar
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Tetapkan tipe gambar sebagai SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Jalur untuk file sumber
img.File = dataDir + "SVGToPDF.svg";
// Tetapkan lebar untuk instansi gambar
img.FixWidth = 50;
// Tetapkan tinggi untuk instansi gambar
img.FixHeight = 50;
// Buat instansi tabel
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Tetapkan lebar untuk sel tabel
table.ColumnWidths = "100 100";
// Buat objek baris dan tambahkan ke instansi tabel
Aspose.Pdf.Row row = table.Rows.Add();
// Buat objek sel dan tambahkan ke instansi baris
Aspose.Pdf.Cell cell = row.Cells.Add();
// Tambahkan textfragment ke koleksi paragraf dari objek sel
cell.Paragraphs.Add(new TextFragment("Sel pertama"));
// Tambahkan sel lain ke objek baris
cell = row.Cells.Add();
// Tambahkan gambar SVG ke koleksi paragraf dari instansi sel yang baru ditambahkan
cell.Paragraphs.Add(img);
// Buat objek halaman dan tambahkan ke koleksi halaman dari instansi dokumen
Page page = doc.Pages.Add();
// Tambahkan tabel ke koleksi paragraf dari objek halaman
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Simpan file PDF
doc.Save(dataDir);
```
## Menggunakan Tag HTML dalam Tabel

Terkadang Anda dapat menemukan kebutuhan untuk mengimpor konten database yang memiliki beberapa tag HTML dan kemudian mengimpor konten ke objek Tabel. Saat mengimpor konten, tag HTML tersebut harus dirender sesuai dalam dokumen PDF. Kami telah meningkatkan metode ImprotDataTable(), untuk mencapai kebutuhan tersebut sebagai berikut:

{{% alert color="primary" %}}

Harap perhatikan bahwa penggunaan Tag HTML di dalam elemen tabel meningkatkan waktu pembuatan dokumen, karena API perlu memproses Tag HTML sesuai dan merendernya di dokumen PDF keluaran.

{{% /alert %}}

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Menginisialisasi instance baru dari Tabel
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// Mengatur lebar kolom tabel
tableProvider.ColumnWidths = "400 50 ";
// Mengatur warna batas tabel sebagai LightGray
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Mengatur batas untuk sel tabel
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## Memasukkan Pemisah Halaman antara baris tabel

Secara default, ketika membuat tabel di dalam file PDF, tabel akan mengalir ke halaman berikutnya ketika mencapai batas bawah tabel. Namun, kita mungkin memiliki kebutuhan untuk memaksa memasukkan pemisah halaman ketika sejumlah baris tertentu telah ditambahkan ke dalam tabel. Cuplikan kode berikut menunjukkan langkah-langkah untuk memasukkan pemisah halaman ketika 10 baris telah ditambahkan ke dalam tabel.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instansiasi instansi Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
doc.Pages.Add();
// Buat instansi tabel
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Atur gaya batas untuk tabel
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Atur gaya batas default untuk tabel dengan warna batas Merah
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Tentukan lebar kolom tabel
tab.ColumnWidths = "100 100";
// Buat loop untuk menambahkan 200 baris untuk tabel
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Sel " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Sel " + counter + ", 1"));
    row.Cells.Add(cell2);
    // Ketika 10 baris ditambahkan, render baris baru di halaman baru
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Tambahkan tabel ke koleksi paragraf file PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Simpan dokumen PDF
doc.Save(dataDir);
```
## Membuat Tabel di Halaman Baru

Secara default, paragraf ditambahkan ke koleksi Paragraphs dari objek Page. Namun, dimungkinkan untuk menampilkan tabel di halaman baru, bukan langsung setelah objek tingkat paragraf yang sebelumnya ditambahkan di halaman tersebut.

### Contoh: Cara Membuat Tabel di Halaman Baru menggunakan C\#

Untuk menampilkan tabel di halaman baru, gunakan properti [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) di kelas BaseParagraph. Berikut ini contoh kode yang menunjukkan cara tersebut.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Menambahkan halaman.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// Saya ingin menjaga tabel 1 di halaman berikutnya...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```

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
```

