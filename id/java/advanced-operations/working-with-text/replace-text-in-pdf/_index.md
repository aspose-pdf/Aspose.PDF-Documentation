---
title: Ganti Teks dalam PDF 
linktitle: Ganti Teks dalam PDF
type: docs
weight: 40
url: /id/java/replace-text-in-a-pdf-document/
description: Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari PDF. Aspose.PDF memungkinkan penggantian teks di wilayah tertentu atau dengan ekspresi reguler.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ganti Teks di semua halaman dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba menemukan dan mengganti teks dalam dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di [link ini](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Untuk mengganti teks di semua halaman dalam dokumen PDF menggunakan [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. Pertama gunakan [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) untuk menemukan frasa tertentu yang akan diganti.

1. Kemudian, periksa semua [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) untuk mengganti teks dan mengubah atribut lainnya.
1. Akhirnya, simpan output PDF menggunakan metode [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) dari kelas Document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Buat objek TextAbsorber untuk menemukan semua contoh dari frasa pencarian masukan
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Terima absorber untuk halaman pertama dokumen
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Lakukan loop melalui fragmen
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Perbarui teks dan properti lainnya
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Simpan file PDF yang telah diperbarui
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## Ganti Teks di wilayah halaman tertentu

Untuk mengganti teks di wilayah halaman tertentu, pertama kita perlu membuat objek TextFragmentAbsorber, menentukan wilayah halaman menggunakan [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) dan kemudian melakukan iterasi melalui semua TextFragment untuk mengganti teks. Setelah operasi ini selesai, kita hanya perlu menyimpan output PDF menggunakan metode simpan dari objek Document.

Cuplikan kode berikut menunjukkan cara mengganti teks di semua halaman dokumen PDF.

```java
 public static void ReplaceTextInParticularRegion(){
    // muat file PDF
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // membuat objek TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // cari teks dalam batas halaman
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // tentukan wilayah halaman untuk Opsi Pencarian Teks
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // cari teks dari halaman pertama file PDF
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // iterasi melalui TextFragment individu
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // ganti teks dengan "---"
        tf.setText("---");
    }

    // Simpan file PDF yang diperbarui
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## Mengganti Teks Berdasarkan Ekspresi Reguler

Jika Anda ingin mengganti beberapa frasa berdasarkan ekspresi reguler, pertama-tama Anda perlu menemukan semua frasa yang cocok dengan ekspresi reguler tersebut menggunakan TextFragmentAbsorber. Anda harus melewatkan ekspresi reguler sebagai parameter ke konstruktor TextFragmentAbsorber. Anda juga perlu membuat objek TextSearchOptions yang menentukan apakah ekspresi reguler sedang digunakan atau tidak. Setelah Anda mendapatkan frasa yang cocok di TextFragments, Anda perlu melakukan loop melalui semuanya dan memperbarui sesuai kebutuhan. Akhirnya, Anda perlu menyimpan PDF yang telah diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

```java
public static void ReplaceTextWithRegularExpression() {
    // memuat file PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Membuat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian yang dimasukkan
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // seperti 1999-2000

    // Mengatur opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Terima absorber untuk halaman pertama dokumen
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Melakukan loop melalui fragmen
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Memperbarui teks dan properti lainnya
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Simpan file PDF yang telah diperbarui
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## Mengganti font dalam file PDF yang ada

Aspose.PDF untuk Java mendukung kemampuan untuk mengganti teks dalam dokumen PDF. Namun, terkadang Anda memiliki persyaratan untuk hanya mengganti font yang digunakan di dalam dokumen PDF. Jadi, alih-alih mengganti teks, hanya font yang digunakan yang diganti. Salah satu overload dari konstruktor TextFragmentAbsorber menerima objek TextEditOptions sebagai argumen dan kita dapat menggunakan nilai RemoveUnusedFonts dari enumerasi TextEditOptions.FontReplace untuk memenuhi persyaratan kita.

Cuplikan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF.

```java
public static void ReplaceFonts() {
    // Membuat objek Dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Mencari fragmen teks dan setel opsi edit sebagai hapus font yang tidak terpakai
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Menerima absorber untuk semua halaman dokumen
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Melintasi semua TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // jika nama font adalah ArialMT, ganti nama font dengan Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Simpan file PDF yang telah diperbarui
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### Gunakan Font Non-Inggris (Jepang) Saat Mengganti Teks

Cuplikan kode berikut menunjukkan cara mengganti teks dengan karakter Jepang. Harap dicatat bahwa untuk menambahkan teks Jepang, Anda perlu menggunakan font yang mendukung karakter Jepang (misalnya MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Instansiasi objek Dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Mari kita ganti setiap kata "page" dengan beberapa teks Jepang dengan font tertentu
    // TakaoMincho yang mungkin terinstal di OS
    // Juga, mungkin font lain yang mendukung hieroglif
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Buat instance opsi Pencarian Teks
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Terima absorber untuk semua halaman dokumen
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Loop melalui fragmen-fragmen
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Perbarui teks dan properti lainnya
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Simpan dokumen yang telah diperbarui
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## Penggantian Teks harus secara otomatis mengatur ulang Konten Halaman

Aspose.PDF untuk Java mendukung fitur untuk mencari dan mengganti teks di dalam file PDF. Namun, baru-baru ini beberapa pelanggan mengalami masalah selama penggantian teks ketika TextFragment tertentu diganti dengan konten yang lebih kecil dan beberapa spasi ekstra ditampilkan dalam PDF hasil atau jika TextFragment diganti dengan string yang lebih panjang, maka kata-kata tumpang tindih dengan konten halaman yang ada. Jadi, ada kebutuhan untuk memperkenalkan mekanisme yang setelah teks di dalam dokumen PDF diganti, konten harus diatur ulang.

Untuk mengatasi skenario yang disebutkan di atas, Aspose.PDF untuk Java telah ditingkatkan sehingga tidak ada masalah seperti itu muncul ketika mengganti teks di dalam file PDF. Cuplikan kode berikut menunjukkan cara mengganti teks di dalam file PDF dan konten halaman harus diatur ulang secara otomatis.

```java
public static void RearrangeContent() {
    // Muat file PDF sumber
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Buat objek TextFragment Absorber dengan ekspresi reguler
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //Anda juga dapat menentukan opsi ReplaceAdjustment.WholeWordsHyphenation untuk membungkus teks pada baris berikutnya atau saat ini 
    //jika baris saat ini menjadi terlalu panjang atau pendek setelah penggantian:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Terima absorber untuk semua halaman dokumen
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Ganti setiap TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Setel font dari fragmen teks yang diganti
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Setel ukuran font
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Ganti teks dengan string yang lebih besar dari placeholder
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // Simpan PDF hasil
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## Merender Simbol yang Dapat Diganti selama Pembuatan PDF

Simbol yang dapat diganti adalah simbol khusus dalam string teks yang dapat digantikan dengan konten yang sesuai saat waktu berjalan. Simbol yang dapat diganti saat ini didukung oleh Model Objek Dokumen baru dari namespace Aspose.PDF adalah `$P`, `$p`, `\n`, `\r`. `$p` dan `$P` digunakan untuk menangani penomoran halaman saat waktu berjalan. `$p` digantikan dengan nomor halaman tempat kelas Paragraf saat ini berada. `$P` digantikan dengan jumlah total halaman dalam dokumen. Saat menambahkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) ke koleksi paragraf dokumen PDF, itu tidak mendukung pemindah baris di dalam teks. Namun untuk menambahkan teks dengan pemindah baris, silakan gunakan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) dengan [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- gunakan "\r\n" atau Environment.NewLine dalam TextFragment alih-alih menggunakan "\n" tunggal;
- buat objek TextParagraph.
 Itu akan menambahkan teks dengan pemisahan baris;
- tambahkan TextFragment dengan TextParagraph.AppendLine;
- tambahkan TextParagraph dengan TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // memuat file PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Inisialisasi TextFragment baru dengan teks yang mengandung penanda baris baru yang diperlukan
    TextFragment textFragment = new TextFragment("Nama Pelamar: " + System.lineSeparator() + " Joe Smoe");

    // Atur properti text fragment jika diperlukan
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // Buat objek TextParagraph
    TextParagraph par = new TextParagraph();

    // Tambahkan TextFragment baru ke paragraph
    par.appendLine(textFragment);

    // Atur posisi paragraph
    par.setPosition (new Position(100, 600));

    // Buat objek TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Tambahkan TextParagraph menggunakan TextBuilder
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Simbol yang Dapat Diganti di Area Header/Footer

Simbol yang dapat diganti juga dapat ditempatkan di dalam bagian Header/Footer dari file PDF. Silakan lihat cuplikan kode berikut untuk detail tentang cara menambahkan simbol yang dapat diganti di bagian footer.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Menetapkan instance marginInfo ke properti Margin dari sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Membuat paragraf Teks yang akan menyimpan isi untuk ditampilkan sebagai header
    TextFragment t1 = new TextFragment("judul laporan");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Nama_Laporan");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Membuat objek HeaderFooter untuk bagian tersebut
    HeaderFooter hfFoot = new HeaderFooter();

    // Mengatur objek HeaderFooter ke footer ganjil & genap
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Menambahkan paragraf teks yang berisi nomor halaman saat ini dari total jumlah halaman
    TextFragment t3 = new TextFragment("Dibuat pada tanggal uji");
    TextFragment t4 = new TextFragment("nama laporan ");
    TextFragment t5 = new TextFragment("Halaman $p dari $P");

    // Membuat objek tabel
    Table tab2 = new Table();

    // Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    hfFoot.getParagraphs().add(tab2);

    // Mengatur lebar kolom tabel
    tab2.setColumnWidths("165 172 165");

    // Membuat baris dalam tabel dan kemudian sel dalam baris
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Mengatur perataan vertikal teks sebagai perataan tengah
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    page.getParagraphs().add(table);

    // Mengatur batas sel default menggunakan objek BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Mengatur batas tabel menggunakan objek BorderInfo yang disesuaikan lainnya
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Membuat baris dalam tabel dan kemudian sel dalam baris
    Row row1 = table.getRows().add();

    row1.getCells().add("kol1");
    row1.getCells().add("kol2");
    row1.getCells().add("kol3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi setiap hari untuk memastikan berisi versi terbaru dari masing-masing komponen Java kami. "
                                + CRLF
                                + "basis harian untuk memastikan berisi versi terbaru dari masing-masing komponen Java kami. "
                                + CRLF
                                + "Menggunakan Aspose.Total untuk pengembang Java dapat membuat berbagai aplikasi.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## Hapus Semua Teks dari Dokumen PDF

### Hapus Semua Teks menggunakan Operator

Dalam beberapa operasi teks, Anda perlu menghapus semua teks dari dokumen PDF dan untuk itu, Anda perlu mengatur teks yang ditemukan sebagai nilai string kosong biasanya. Intinya adalah bahwa mengubah teks untuk banyak fragmen teks memicu sejumlah pemeriksaan dan operasi penyesuaian posisi teks. Mereka penting dalam skenario pengeditan teks. Kesulitannya adalah Anda tidak dapat menentukan berapa banyak fragmen teks yang akan dihapus dalam skenario di mana mereka diproses dalam sebuah loop.

Oleh karena itu, kami merekomendasikan menggunakan pendekatan lain untuk skenario menghapus semua teks dari halaman PDF. Silakan pertimbangkan potongan kode berikut yang bekerja sangat cepat.

```java
public static void RemoveAllTextUsingOperators() {
    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Loop melalui semua halaman Dokumen PDF
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Pilih semua teks di halaman
        page.getContents().accept(operatorSelector);
        // Hapus semua teks
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Simpan dokumen
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```