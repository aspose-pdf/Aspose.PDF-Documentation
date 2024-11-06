---
title: Membuat atau Menambahkan Tabel Dalam PDF 
linktitle: Membuat atau Menambahkan Tabel
type: docs
weight: 10
url: id/cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF untuk C++ adalah sebuah pustaka yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Menggunakan pustaka ini, Anda dapat mempaginasi tabel pada halaman PDF menggunakan C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Membuat Tabel menggunakan C++

Tabel penting saat bekerja dengan dokumen PDF. Mereka menyediakan fitur hebat untuk menampilkan informasi secara sistematis.

Tabel dalam dokumen PDF mengatur data dalam baris dan kolom secara sistematis. API Aspose.PDF untuk C++ memungkinkan Anda menambahkan tabel ke dokumen PDF, dan menambahkan baris dan kolom ke dalamnya di aplikasi C++ Anda. Kelas [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) digunakan untuk menambahkan tabel ke dokumen. Langkah-langkah berikut dapat diikuti untuk menambahkan tabel ke dokumen PDF menggunakan C++.

### Menambahkan Tabel dalam Dokumen PDF yang Ada

Untuk menambahkan tabel ke file PDF yang sudah ada dengan Aspose.PDF untuk C++, lakukan langkah-langkah berikut:

1. Muat file sumber.
1. Inisialisasi tabel dan atur kolom serta barisnya.
1. Atur pengaturan tabel (kami telah mengatur batasan).
1. Isi tabel.
1. Tambahkan tabel ke halaman.
1. Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada.

>Headers

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Sample

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // Memuat dokumen PDF sumber
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Menginisialisasi instance baru dari Tabel
    auto table = MakeObject<Table>();
    
    // Mengatur warna batas tabel sebagai LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // Mengatur batas untuk sel tabel
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // Membuat loop untuk menambahkan 10 baris
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // Menambahkan baris ke tabel
        auto row = table->get_Rows()->Add();
        // Menambahkan sel tabel
        row->get_Cells()->Add(String::Format(u"Kolom ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Kolom ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Kolom ({0}, 3)", row_count));
    }

    // Menambahkan objek tabel ke halaman pertama dokumen input
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // Menyimpan dokumen yang diperbarui yang mengandung objek tabel
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan dan RowSpan dalam Tabel

Aspose.PDF untuk C++ menyajikan properti [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) untuk menggabungkan kolom dalam tabel dan properti [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) untuk menggabungkan baris.

Kami menggunakan properti [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) atau [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) pada objek [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) yang membuat sel tabel. Setelah menerapkan properti yang diperlukan, sel yang dibuat dapat ditambahkan ke tabel.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Muat dokumen PDF sumber
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Inisialisasi instance baru dari Tabel
    auto table = MakeObject<Table>();
    // Atur warna batas tabel sebagai LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // Atur batas untuk sel tabel
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Tambahkan baris 1 ke tabel
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Tambahkan sel tabel
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // Tambahkan baris 2 ke tabel
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // Tambahkan baris 3 ke tabel
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // Tambahkan baris 4 ke tabel
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");


    // Tambahkan baris 5 ke tabel
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // Tambahkan objek tabel ke halaman pertama dokumen input
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Simpan dokumen yang diperbarui yang berisi objek tabel
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

Hasil eksekusi kode di bawah ini adalah tabel yang digambarkan pada gambar berikut:

![Demo ColSpan dan RowSpan](colspan_rowspan.png)

## Bekerja dengan Borders, Margins dan Padding

Perhatikan bahwa ini juga mendukung fungsi pengaturan border, margins, dan padding sel untuk tabel, mari kita pahami terlebih dahulu konsep dari borders, margins, dan padding, yang disajikan dalam diagram di bawah ini:

![Borders, margins dan padding](set-border-style-margins-and-padding-of-table_1.png)

Periksa gambar secara detail. Ini menunjukkan bahwa borders dari tabel, baris, dan sel saling tumpang tindih. Menggunakan Aspose.PDF untuk C++ tabel dapat memiliki margins dan sel dapat memiliki indentasi. Untuk mengatur margins sel, kita harus mengatur padding sel.

## Borders

Untuk mengatur borders dari objek Table, [Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) dan [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), gunakan properti Table.Border, Row.Border dan Cell.Border. Perbatasan sel juga dapat diatur menggunakan properti DefaultCellBorder kelas [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) atau Row. Semua properti terkait perbatasan yang dibahas di atas diberikan pada instance kelas Row, yang dibuat dengan memanggil konstruktornya. Kelas Row memiliki banyak overload yang mengambil hampir semua parameter yang diperlukan untuk menyesuaikan perbatasan.

## Margin atau Padding

Padding sel dapat diatur menggunakan properti [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) kelas Table. Semua properti terkait padding diberikan pada instance kelas [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) yang mengambil informasi tentang parameter `Left`, `Right`, `Top`, dan `Bottom` untuk membuat margin kustom.

![Margin dan Border dalam Tabel PDF](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // Instansiasi objek Document dengan memanggil konstruktor kosongnya
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Instansiasi objek tabel
    auto tab1 = MakeObject<Table>();
    // Tambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    page->get_Paragraphs()->Add(tab1);
    // Atur lebar kolom tabel
    tab1->set_ColumnWidths (u"50 50 50");
    // Atur perbatasan sel default menggunakan objek BorderInfo
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // Atur perbatasan tabel menggunakan objek BorderInfo yang disesuaikan lainnya
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // Buat objek MarginInfo dan atur margin kiri, bawah, kanan, dan atasnya
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // Atur padding sel default ke objek MarginInfo
    tab1->set_DefaultCellPadding (margin);
    // Buat baris dalam tabel dan kemudian sel dalam baris
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 dengan string teks besar");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Simpan Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
Untuk membuat tabel dengan sudut melengkung, gunakan kelas [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) nilai [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) dan atur gaya sudut tabel ke bulat.

```cpp
void AddTable_RoundedBorderRadius()
{
    // Jalur ke direktori dokumen.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // Buat objek BorderInfo kosong
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // Atur batas menjadi batas melengkung di mana radius lengkung adalah 15
    bInfo->set_RoundedBorderRadius(15);
    // Atur gaya Sudut tabel sebagai Bulat.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // Atur informasi batas tabel
    tab1->set_Border(bInfo);
}
```

### Properti AutoFitToWindow dalam enumerasi ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // Jalur ke direktori dokumen.
    String _dataDir("C:\\Samples\\");

    // Instansiasi objek Pdf dengan memanggil konstruktor kosongnya
    auto document = MakeObject<Document>();

    // Buat bagian dalam objek Pdf
    auto sec1 = document->get_Pages()->Add();

    // Instansiasi objek tabel
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // Tambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    sec1->get_Paragraphs()->Add(tab1);

    // Atur dengan lebar kolom tabel
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // Atur batas sel default menggunakan objek BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // Atur batas tabel menggunakan objek BorderInfo yang dikustomisasi lainnya
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // Buat objek MarginInfo dan atur margin kiri, bawah, kanan, dan atasnya
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // Atur padding sel default ke objek MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // Buat baris dalam tabel dan kemudian sel dalam baris
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Simpan dokumen yang diperbarui yang berisi objek tabel
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### Dapatkan Lebar Tabel

Ada tugas di mana Anda perlu mendapatkan lebar tabel secara dinamis. Kelas [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) memiliki metode [GetWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c) untuk tujuan ini. Sebagai contoh, Anda belum secara eksplisit menetapkan lebar kolom tabel, dan Anda belum menetapkan [ColumnAdjustment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) ke AutoFitToContent. Dalam hal ini, Anda dapat mendapatkan lebar tabel berikutnya.

```cpp
void GetTableWidth() {
    // Buat dokumen baru
    auto document = MakeObject<Document>();
    
    // Tambahkan halaman dalam dokumen
    auto page = document->get_Pages()->Add();

    // Inisialisasi tabel baru
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // Tambahkan baris dalam tabel
    auto row = table->get_Rows()->Add();

    // Tambahkan sel dalam tabel
    auto cell = row->get_Cells()->Add(u"Teks Sel 1");
    cell = row->get_Cells()->Add(u"Teks Sel 2");
    // Dapatkan lebar tabel
    Console::WriteLine(table->GetWidth());
}
```

## Tambahkan Gambar SVG ke Sel Tabel

Aspose.PDF untuk C++ memungkinkan Anda menambahkan sel tabel ke file PDF. Ketika Anda membuat tabel, Anda dapat menambahkan teks atau gambar ke sel. Selain itu, API juga menawarkan fitur untuk mengonversi file SVG ke PDF. Dengan menggunakan kombinasi fungsi-fungsi ini, dimungkinkan untuk memuat gambar SVG dan menambahkannya ke sel tabel.

Cuplikan kode berikut menunjukkan langkah-langkah untuk membuat tabel dan menambahkan gambar SVG ke sel tabel.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Membuat objek Dokumen
    auto document = MakeObject<Document>();
    // Membuat instance gambar
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Menetapkan tipe gambar sebagai SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Jalur untuk file sumber
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Menetapkan lebar untuk instance gambar
    img->set_FixWidth (50);
    // Menetapkan tinggi untuk instance gambar
    img->set_FixHeight(50);
    // Membuat instance tabel
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Menetapkan lebar untuk sel tabel
    table->set_ColumnWidths (u"100 100");
    // Membuat objek baris dan menambahkannya ke instance tabel
    auto row = table->get_Rows()->Add();
    // Membuat objek sel dan menambahkannya ke instance baris
    auto cell = row->get_Cells()->Add();
    // Menambahkan fragmen teks ke koleksi paragraf dari objek sel
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // Menambahkan sel lain ke objek baris
    cell = row->get_Cells()->Add();
    // Menambahkan gambar SVG ke koleksi paragraf dari instance sel yang baru ditambahkan
    cell->get_Paragraphs()->Add(img);
    // Membuat objek halaman dan menambahkannya ke koleksi halaman dari instance dokumen
    auto page = document->get_Pages()->Add();
    // Menambahkan tabel ke koleksi paragraf dari objek halaman
    page->get_Paragraphs()->Add(table);    
    // Menyimpan file PDF
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## Menggunakan Tag HTML di dalam Tabel

Untuk beberapa tugas, Anda perlu mengimpor konten basis data dengan beberapa tag HTML dan kemudian mengimpor konten tersebut ke dalam objek Tabel. Saat mengimpor konten, tag HTML harus ditampilkan di dalam dokumen PDF.

Dalam potongan kode berikut, Anda dapat mengatur warna batas tabel, menetapkan batas untuk sel tabel. Setelah itu, Anda akan membuat loop untuk menambahkan 10 baris. Tambahkan objek tabel ke halaman pertama dokumen input dan simpan dokumen yang diperbarui.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Menginisialisasi instance baru dari Tabel
    auto table = MakeObject<Table>();
    // Mengatur warna batas tabel sebagai LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // menetapkan batas untuk sel tabel
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // membuat loop untuk menambahkan 10 baris       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // menambahkan baris ke tabel
        auto row = table->get_Rows()->Add();
        // menambahkan sel tabel
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Kolom <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Kolom <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Kolom <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Menambahkan objek tabel ke halaman pertama dokumen input
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Menyimpan dokumen yang diperbarui yang berisi objek tabel
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## Sisipkan Pemisah Halaman antara baris tabel

Biasanya, ketika membuat tabel dalam PDF, tabel mengalir ke halaman berikutnya ketika mencapai batas bawah tabel. Tetapi kita mungkin memiliki kebutuhan untuk memaksa pemisah halaman dimasukkan ketika sejumlah baris tertentu ditambahkan ke tabel. Cuplikan kode berikut menunjukkan langkah-langkah untuk menyisipkan pemisah halaman saat menambahkan 10 baris ke tabel.

Cuplikan kode berikut menunjukkan langkah-langkah untuk menyisipkan pemisah halaman ketika 10 baris ditambahkan untuk tabel.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Membuat instance Dokumen
    auto document = MakeObject<Document>();
    
    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat instance tabel
    auto tab = MakeObject<Table>();

    // Atur gaya border untuk tabel
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Atur gaya border default untuk tabel dengan warna border Merah
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Tentukan lebar kolom tabel
    tab->set_ColumnWidths(u"100 100");

    // Buat loop untuk menambahkan 200 baris untuk tabel
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // Ketika 10 baris ditambahkan, render baris baru di halaman baru
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Tambahkan tabel ke koleksi paragraf file PDF
    page->get_Paragraphs()->Add(tab);

    // Simpan dokumen PDF
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## Render a Table on New Page

Secara default, paragraf ditambahkan ke koleksi Paragraphs dari objek Page. Namun, adalah mungkin untuk merender tabel di halaman baru, bukan langsung setelah objek level paragraf yang sebelumnya ditambahkan pada halaman.

### Contoh: Cara Merender Tabel di Halaman Baru menggunakan C++

Untuk merender tabel di halaman baru, gunakan properti [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) dalam kelas [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph).
Cuplikan kode berikut menunjukkan caranya.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Ditambahkan halaman.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // Saya ingin menjaga table 1 ke halaman berikutnya tolong...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```