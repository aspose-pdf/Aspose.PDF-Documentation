---
title: Dapatkan dan Atur Properti Halaman
type: docs
weight: 30
url: /id/java/get-and-set-page-properties/
description: Topik ini menjelaskan cara mendapatkan nomor dalam file PDF, mendapatkan properti halaman dan menentukan warna halaman menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
---

Aspose.PDF untuk Java memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi Java Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini memerlukan tidak lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Kemudian gunakan properti Count dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (dari objek Document) untuk mendapatkan jumlah total halaman dalam dokumen.

Cuplikan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Dapatkan jumlah halaman
        System.out.println("Jumlah Halaman : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Kecuali file PDF disimpan dan semua elemen benar-benar ditempatkan di dalam file PDF, kita tidak dapat mendapatkan jumlah halaman untuk dokumen tertentu (karena kita tidak dapat memastikan jumlah halaman di mana semua elemen akan ditempatkan).
 Namun, mulai dengan rilis Aspose.PDF untuk Java 10.1.0, kami telah memperkenalkan metode bernama [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) yang menyediakan fitur untuk mendapatkan jumlah halaman untuk dokumen PDF, tanpa menyimpan file. Jadi kita dapat memperoleh informasi jumlah halaman secara langsung. Silakan coba gunakan potongan kode berikut untuk memenuhi persyaratan ini.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // Untuk contoh lengkap dan file data, silakan kunjungi
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // instansiasi instance Document
        Document doc = new Document();
        // tambahkan halaman ke koleksi halaman file PDF
        Page page = doc.getPages().add();
        // buat loop untuk menambahkan 300 instance TextFragment
        for (int i = 0; i < 300; i++)
            // tambahkan TextFragment ke koleksi paragraf halaman pertama PDF
            page.getParagraphs().add(new TextFragment("Uji jumlah halaman"));
        // proses paragraf untuk mendapatkan informasi jumlah halaman
        doc.processParagraphs();
        System.out.println("Jumlah Halaman dalam PDF = " + doc.getPages().size());
    }
```

## Mendapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti-properti ini.

### **Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox, dan Properti Rect**

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF tersebut juga akan memiliki bleed box.
 Bleed adalah jumlah warna (atau karya seni) yang meluas melewati tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("dipangkas"), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman salah dipangkas - dipotong sedikit melenceng dari tanda pangkas - tidak akan ada tepi putih yang muncul di halaman.
- **Kotak trim**: Kotak trim menunjukkan ukuran akhir dokumen setelah dicetak dan dipangkas.
- **Kotak seni**: Kotak seni adalah kotak yang digambar di sekitar isi sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Kotak potong**: Kotak potong adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya isi dari kotak potong yang ditampilkan di Adobe Acrobat.  
  Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Batas Halaman.
- **Page.Rect**: perpotongan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah mengilustrasikan properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Mengakses Properti Halaman

Kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) menyediakan semua properti terkait dengan halaman PDF tertentu. Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Dari sana, dimungkinkan untuk mengakses objek Page individual menggunakan indeks mereka, atau melalui koleksi, menggunakan loop foreach, untuk mendapatkan semua halaman. Setelah halaman individual diakses, kita dapat mendapatkan propertinya. Cuplikan kode berikut menunjukkan cara mendapatkan properti halaman.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Dapatkan koleksi halaman
        PageCollection pageCollection = pdfDocument.getPages();

        // Dapatkan halaman tertentu
        Page pdfPage = pageCollection.get_Item(1);

        // Dapatkan properti halaman
        System.out.printf("\n ArtBox : Tinggi = " + pdfPage.getArtBox().getHeight() + ", Lebar = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Tinggi = " + pdfPage.getBleedBox().getHeight() + ", Lebar = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Tinggi = " + pdfPage.getCropBox().getHeight() + ", Lebar = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Tinggi = " + pdfPage.getMediaBox().getHeight() + ", Lebar = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Tinggi = " + pdfPage.getTrimBox().getHeight() + ", Lebar = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Tinggi = " + pdfPage.getRect().getHeight() + ", Lebar = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Nomor Halaman :- " + pdfPage.getNumber());
        System.out.printf("\n Rotasi :-" + pdfPage.getRotate());
    }
```

## Menentukan Warna Halaman

Kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) menyediakan properti terkait halaman tertentu dalam dokumen PDF, termasuk jenis warna apa - RGB, hitam putih, grayscale, atau tidak terdefinisi - yang digunakan halaman.

Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Properti [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) menentukan warna elemen pada halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) dari objek kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Cuplikan kode berikut menunjukkan cara mengiterasi melalui halaman individu dari file PDF untuk mendapatkan informasi warna.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Iterasi melalui semua halaman dari file PDF
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Dapatkan informasi jenis warna untuk halaman PDF tertentu
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Halaman # -" + pageCount + " adalah Hitam dan putih..");
                break;
            case 1:
                System.out.println("Halaman # -" + pageCount + " adalah Skala Abu-abu...");
                break;
            case 0:
                System.out.println("Halaman # -" + pageCount + " adalah RGB..");
                break;
            case 3:
                System.out.println("Halaman # -" + pageCount + " Warna tidak terdefinisi..");
                break;
            }
        }
    }
}
```