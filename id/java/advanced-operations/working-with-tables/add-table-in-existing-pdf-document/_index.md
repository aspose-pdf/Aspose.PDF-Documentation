---
title: Membuat atau Menambahkan Tabel Dalam PDF 
linktitle: Membuat atau Menambahkan Tabel
type: docs
weight: 10
url: id/java/add-table-in-existing-pdf-document/
description: Pelajari cara membuat atau menambahkan tabel ke dokumen PDF, menerapkan gaya sel, membagi tabel di halaman, dan menyesuaikan baris dan kolom, dll.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Membuat Tabel

Namespace Aspose.PDF berisi kelas bernama [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), dan [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) yang menyediakan fungsionalitas untuk membuat tabel saat menghasilkan dokumen PDF dari awal.

Tabel dapat dibuat dengan membuat objek dari Kelas Table.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Menambahkan Tabel ke Dokumen PDF yang Ada

Untuk menambahkan tabel ke file PDF yang sudah ada dengan Aspose.PDF untuk Java, ikuti langkah-langkah berikut:

1. Muat file sumber.

1. Inisialisasi tabel dan atur kolom serta barisnya.
1. Atur pengaturan tabel (kami telah mengatur batas-batasnya).
1. Isi tabel.
1. Tambahkan tabel ke halaman.
1. Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan teks ke dalam file PDF yang sudah ada.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Menginisialisasi instance baru dari Tabel
        Table table = new Table();
        // Atur warna batas tabel sebagai LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // atur batas untuk sel tabel
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // buat loop untuk menambahkan 10 baris
        for (int row_count = 1; row_count < 10; row_count++) {
            // tambahkan baris ke tabel
            Row row = table.getRows().add();
            // tambahkan sel tabel
            row.getCells().add("Kolom (" + row_count + ", 1)");
            row.getCells().add("Kolom (" + row_count + ", 2)");
            row.getCells().add("Kolom (" + row_count + ", 3)");
        }
        // Tambahkan objek tabel ke halaman pertama dokumen input
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Simpan dokumen yang diperbarui yang mengandung objek tabel
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan dan RowSpan dalam Tabel Aspose.PDF menggunakan Java

Aspose.PDF untuk Java menyediakan metode [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) untuk menggabungkan kolom dalam tabel dan metode [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) untuk menggabungkan baris.

Kami menggunakan metode [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) atau [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) pada objek [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) yang membuat sel tabel. Setelah menerapkan properti yang diperlukan, sel yang dibuat dapat ditambahkan ke dalam tabel.

```java
public static void AddTable_RowColSpan() {
        // Memuat dokumen PDF sumber
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Menginisialisasi instance baru dari Table
        Table table = new Table();
        // Mengatur warna border tabel sebagai LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Mengatur border untuk sel tabel
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Menambahkan baris ke-1 ke tabel
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Menambahkan sel tabel
            row1.getCells().add("Test 1 " + cellCount);
        }

        // Menambahkan baris ke-2 ke tabel
        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        // Menambahkan baris ke-3 ke tabel
        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        // Menambahkan baris ke-4 ke tabel
        Row row4 = table.getRows().add();
        row3.getCells().add("Test 4 1");
        cell = row3.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Test 4 3");
        row3.getCells().add("Test 4 4");

        // Menambahkan baris ke-5 ke tabel
        row4 = table.getRows().add();
        row4.getCells().add("Test 5 1");
        row4.getCells().add("Test 5 3");
        row4.getCells().add("Test 5 4");

        // Menambahkan objek tabel ke halaman pertama dokumen input
        page.getParagraphs().add(table);

        // Menyimpan dokumen yang diperbarui yang mengandung objek tabel
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


Hasil dari eksekusi kode di bawah ini adalah tabel yang digambarkan pada gambar berikut:

![Demo ColSpan dan RowSpan](colspan_rowspan.png)

## Bekerja dengan Batas, Margin dan Padding

Aspose.PDF untuk Java memungkinkan pengembang untuk membuat tabel dalam dokumen PDF. Menurut Model Objek Dokumen Aspose.PDF, sebuah tabel adalah elemen tingkat paragraf.

Harap dicatat bahwa itu juga mendukung fitur untuk mengatur gaya batas, margin dan padding sel untuk tabel. Sebelum masuk ke detail teknis lebih lanjut, penting untuk memahami konsep batas, margin dan padding yang disajikan di bawah ini dalam diagram:

![Batas, margin dan padding](set-border-style-margins-and-padding-of-table_1.png)

Dalam gambar di atas, Anda dapat melihat bahwa batas dari tabel, baris dan sel saling tumpang tindih. Menggunakan Aspose.PDF, sebuah tabel dapat memiliki margin dan sel dapat memiliki padding. Untuk mengatur margin sel, kita harus mengatur padding sel.

## Batas

Untuk mengatur batas objek [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table), [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) dan [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), gunakan metode [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) dan [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 Batas sel juga dapat diatur menggunakan metode [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) dari kelas [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) atau [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row). Semua properti terkait batas yang dibahas di atas diberikan pada sebuah instance dari kelas Row, yang dibuat dengan memanggil konstruktornya. Kelas Row memiliki banyak overload yang mengambil hampir semua parameter yang diperlukan untuk menyesuaikan batas.

## Margin atau Padding

Padding sel dapat dikelola menggunakan metode [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) dari kelas Table. Semua properti terkait padding ditetapkan sebagai instance dari kelas [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) yang mengambil informasi tentang parameter `Left`, `Right`, `Top`, dan `Bottom` untuk membuat margin khusus.

Dalam contoh berikut, lebar batas sel diatur ke 0.1 poin, lebar batas tabel diatur ke 1 poin, dan padding sel diatur ke 5 poin.

![Margin dan Border dalam Tabel PDF](margin-border.png)

```java
public static void MargingPadding() {
        // Memulai objek Document dengan memanggil konstruktor kosongnya
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Memulai objek tabel
        Table tab1 = new Table();
        // Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
        page.getParagraphs().add(tab1);
        // Mengatur lebar kolom tabel
        tab1.setColumnWidths ("50 50 50");
        // Mengatur batas sel default menggunakan objek BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Mengatur batas tabel menggunakan objek BorderInfo yang disesuaikan
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // Membuat objek MarginInfo dan mengatur margin kiri, bawah, kanan, dan atasnya
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // Mengatur padding sel default ke objek MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Membuat baris dalam tabel dan kemudian sel dalam baris
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 dengan string teks yang besar");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Menyimpan PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Untuk membuat tabel dengan sudut membulat, gunakan nilai `RoundedBorderRadius` dari kelas [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) dan atur gaya sudut tabel menjadi bulat.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Memulai objek tabel
        Table tab1 = new Table();

        // Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Membuat objek BorderInfo kosong
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Mengatur border menjadi border bulat dengan radius bulat adalah 15
        bInfo.setRoundedBorderRadius(15);
        // Mengatur gaya sudut tabel sebagai Bulat.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Mengatur informasi border tabel
        tab1.setBorder(bInfo);
        // Membuat baris dalam tabel dan kemudian sel dalam baris
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 dengan string teks yang panjang");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Menyimpan PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### Properti AutoFitToWindow dalam enumerasi ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // Memperoleh objek Pdf dengan memanggil konstruktor kosongnya
        Document doc = new Document();
        // Membuat bagian dalam objek Pdf
        Page sec1 = doc.getPages().add();

        // Memperoleh objek tabel
        Table tab1 = new Table();
        // Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
        sec1.getParagraphs().add(tab1);

        // Mengatur lebar kolom dari tabel
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Mengatur batas sel default menggunakan objek BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Mengatur batas tabel menggunakan objek BorderInfo yang disesuaikan
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Membuat objek MarginInfo dan mengatur margin kiri, bawah, kanan, dan atasnya
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Mengatur padding sel default ke objek MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Membuat baris dalam tabel dan kemudian sel dalam baris
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Menyimpan dokumen yang diperbarui yang berisi objek tabel
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### Dapatkan Lebar Tabel

Kadang-kadang, diperlukan untuk mendapatkan lebar tabel secara dinamis. Kelas Aspose.PDF.Table memiliki metode [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) untuk tujuan ini. Misalnya, Anda belum menetapkan lebar kolom tabel secara eksplisit dan mengatur [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) ke AutoFitToContent. Dalam kasus ini, Anda dapat mendapatkan lebar tabel sebagai berikut.

```java
public static void GetTableWidth() {
        // Buat dokumen baru
        Document doc = new Document();
        // Tambahkan halaman dalam dokumen
        Page page = doc.getPages().add();

        // Inisialisasi tabel baru
        Table table = new Table();

        // Tambahkan tabel dalam koleksi paragraf di bagian yang diinginkan
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Tambahkan baris dalam tabel
        Row row = table.getRows().add();
        // Tambahkan sel dalam tabel
        row.getCells().add("Teks Sel 1");
        row.getCells().add("Teks Sel 2");
        // Dapatkan lebar tabel
        System.out.println(table.getWidth());
    }
```


## Tambahkan Objek SVG ke Sel Tabel

Aspose.PDF untuk Java mendukung fitur untuk menambahkan sel tabel ke dalam file PDF. Saat membuat tabel, dimungkinkan untuk menambahkan teks atau gambar ke dalam sel. Selain itu, API juga menawarkan fitur untuk mengonversi file SVG ke format PDF. Dengan menggunakan kombinasi fitur-fitur ini, dimungkinkan untuk memuat gambar SVG dan menambahkannya ke dalam sel tabel.

Cuplikan kode berikut menunjukkan langkah-langkah untuk membuat instance tabel dan menambahkan gambar SVG ke dalam sel tabel.

```java
 public static void AddSVGObjectToTableCell() {
        // Membuat objek Document
        Document doc = new Document();
        // Membuat instance gambar
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Mengatur jenis gambar sebagai SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Jalur untuk file sumber
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Mengatur lebar untuk instance gambar
        img.setFixWidth (50);
        // Mengatur tinggi untuk instance gambar
        img.setFixHeight (50);
        // Membuat instance tabel
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Mengatur lebar untuk sel tabel
        table.setColumnWidths ("100 100");
        // Membuat objek baris dan menambahkannya ke instance tabel
        com.aspose.pdf.Row row = table.getRows().add();
        // Membuat objek sel dan menambahkannya ke instance baris
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Menambahkan fragment teks ke koleksi paragraf dari objek sel
        cell.getParagraphs().add(new TextFragment("Sel pertama"));
        // Menambahkan sel lain ke objek baris
        cell = row.getCells().add();
        // Menambahkan gambar SVG ke koleksi paragraf dari instance sel yang baru saja ditambahkan
        cell.getParagraphs().add(img);
        // Membuat objek halaman dan menambahkannya ke koleksi halaman dari instance dokumen
        Page page = doc.getPages().add();
        // Menambahkan tabel ke koleksi paragraf dari objek halaman
        page.getParagraphs().add(table);
        // Menyimpan file PDF
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## Menambahkan Tag HTML di dalam Tabel

Aspose.PDF untuk Java memungkinkan menambahkan Fragmen HTML baru ke dalam Paragraf dari file PDF Anda.

{{% alert color="primary" %}}

Harap diperhatikan bahwa penggunaan Tag HTML di dalam elemen tabel meningkatkan waktu pembuatan dokumen, karena API perlu memproses Tag HTML sesuai dan merendernya dalam dokumen PDF keluaran.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Menginisialisasi instance baru dari Tabel
        Table table = new Table();
        // Mengatur warna batas tabel sebagai LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // mengatur batas untuk sel tabel
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // membuat loop untuk menambahkan 10 baris
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // menambahkan baris ke tabel
            Row row = table.getRows().add();
            // menambahkan sel tabel
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Kolom <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Kolom <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Kolom <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Menambahkan objek tabel ke halaman pertama dari dokumen input
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Menyimpan dokumen yang telah diperbarui yang mengandung objek tabel
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## Sisipkan Pemisah Halaman antara baris tabel

Sebagai perilaku default, ketika membuat tabel di dalam file PDF, tabel akan mengalir ke halaman berikutnya ketika mencapai margin bawah tabel. Namun, kita mungkin memiliki kebutuhan untuk memaksa menyisipkan pemisah halaman ketika sejumlah baris telah ditambahkan ke tabel. Cuplikan kode berikut menunjukkan langkah-langkah untuk menyisipkan pemisah halaman ketika 10 baris telah ditambahkan ke tabel.

```java
    public static void InsertPageBreak() {
        // Membuat instance Dokumen
        Document doc = new Document();
        // Menambahkan halaman ke koleksi halaman file PDF
        Page page = doc.getPages().add();
        // Membuat instance tabel
        Table tab = new Table();
        // Mengatur gaya border untuk tabel
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Mengatur gaya border default untuk tabel dengan warna border Merah
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Menentukan lebar kolom tabel
        tab.setColumnWidths ("100 100");
        // Membuat loop untuk menambahkan 200 baris ke tabel
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // Ketika 10 baris ditambahkan, render baris baru di halaman baru
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Menambahkan tabel ke koleksi paragraf file PDF
        page.getParagraphs().add(tab);

        // Menyimpan dokumen PDF
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## Sembunyikan Batas Sel yang Terbentang

Saat menambahkan sel ke tabel, batas sel yang terbentang mungkin muncul ketika mereka berpindah ke baris lain. Batas terbentang seperti itu dapat disembunyikan seperti yang ditunjukkan dalam contoh kode berikut.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Memulai objek tabel yang akan dinest dalam outerTable yang akan terpecah
//dalam halaman yang sama
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Tambahkan Baris header
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("header 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("header 3");
Cell cell2 = row.getCells().add("header 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("header 6");
Cell cell3 = row.getCells().add("header 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("header 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("header 12");
row.getCells().add("header 13");
row.getCells().add("header 14");
row.getCells().add("header 15");
row.getCells().add("header 16");
row.getCells().add("header 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Buat baris dalam tabel dan kemudian sel dalam baris
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("kol "+rowCounter+", 1");
  row1.getCells().add("kol "+rowCounter+", 2");
  row1.getCells().add("kol "+rowCounter+", 3");
  row1.getCells().add("kol "+rowCounter+", 4");
  row1.getCells().add("kol "+rowCounter+", 5");
  row1.getCells().add("kol "+rowCounter+", 6");
  row1.getCells().add("kol "+rowCounter+", 7");
  row1.getCells().add("kol "+rowCounter+", 8");
  row1.getCells().add("kol "+rowCounter+", 9");
  row1.getCells().add("kol "+rowCounter+", 10");
  row1.getCells().add("kol "+rowCounter+", 11");
  row1.getCells().add("kol "+rowCounter+", 12");
  row1.getCells().add("kol "+rowCounter+", 13");
  row1.getCells().add("kol "+rowCounter+", 14");
  row1.getCells().add("kol "+rowCounter+", 15");
  row1.getCells().add("kol "+rowCounter+", 16");
  row1.getCells().add("kol "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```