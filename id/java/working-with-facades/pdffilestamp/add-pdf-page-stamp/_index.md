---
title: Tambahkan Stempel Halaman PDF
type: docs
weight: 10
url: /id/java/add-pdf-page-stamp/
description: Bagian ini menjelaskan cara bekerja dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Stempel Halaman PDF pada Semua Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda menambahkan stempel halaman PDF pada semua halaman dari sebuah file PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. Anda juga perlu membuat stempel halaman PDF menggunakan metode [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Kemudian Anda dapat menambahkan stempel dalam file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Akhirnya, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan stempel halaman PDF pada semua halaman dalam file PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat stempel
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Tambahkan stempel ke file PDF
            fileStamp.AddStamp(stamp);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```

## Menambahkan Cap Halaman PDF pada Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan cap halaman PDF pada halaman tertentu dari file PDF.
 Untuk menambahkan stempel halaman PDF, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) dan [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda juga perlu membuat cap halaman PDF menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Anda dapat mengatur atribut lain seperti origin, rotasi, latar belakang dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) juga. Sebagaimana Anda ingin menambahkan cap halaman PDF pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) dari kelas [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan cap. Kemudian Anda dapat menambahkan cap dalam file PDF menggunakan metode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Akhirnya, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Contoh kode berikut menunjukkan kepada Anda bagaimana menambahkan cap halaman PDF pada halaman tertentu dalam sebuah file PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat cap
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Tambahkan cap ke file PDF
            fileStamp.AddStamp(stamp);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }

        // Tambahkan Nomor Halaman PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Tambahkan Nomor Halaman dalam File PDF (facades)

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda menambahkan nomor halaman dalam file PDF.
 Untuk menambahkan nomor halaman, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Jika Anda ingin menampilkan nomor halaman seperti "Halaman X dari N" di mana X adalah nomor halaman saat ini dan N adalah jumlah total halaman dalam file PDF, maka Anda perlu terlebih dahulu mendapatkan jumlah halaman menggunakan properti getNumberOfpages dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Untuk mendapatkan nomor halaman saat ini, Anda dapat menggunakan tanda **#** dalam teks Anda di mana pun Anda suka. Anda dapat memformat teks nomor halaman menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Jika Anda ingin memulai penomoran halaman dari nomor tertentu, Anda dapat mengatur properti setStartingNumber. Setelah Anda siap untuk menambahkan nomor halaman dalam file, Anda perlu memanggil metode addPageNumber dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Terakhir, simpan file PDF keluaran menggunakan metode Save dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

Cuplikan kode berikut menunjukkan cara menambahkan nomor halaman dalam file PDF.
```java
 public static void AddPageNumberInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Dapatkan total jumlah halaman
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Buat teks terformat untuk nomor halaman
        FormattedText formattedText = new FormattedText("Halaman # dari " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Tetapkan nomor awal untuk halaman pertama; Anda mungkin ingin memulai dari 2 atau lebih
        fileStamp.setStartingNumber(1);

        // Tambahkan nomor halaman
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```


### Gaya Penomoran Kustom

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) kelas menawarkan fitur untuk menambahkan informasi Nomor Halaman sebagai objek stempel di dalam dokumen PDF. Sebelum rilis ini, kelas tersebut hanya mendukung 1,2,3,4 sebagai gaya penomoran halaman. Namun, ada permintaan dari beberapa pelanggan untuk menggunakan gaya penomoran khusus saat menempatkan stempel nomor halaman di dalam dokumen PDF. Untuk memenuhi persyaratan ini, properti [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) telah diperkenalkan, yang menerima nilai dari enumerasi [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle). Ditentukan di bawah ini adalah nilai-nilai yang ditawarkan dalam enumerasi ini.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Dapatkan total jumlah halaman
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Buat teks terformat untuk nomor halaman
        FormattedText formattedText = new FormattedText("Halaman # dari " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Tentukan gaya penomoran sebagai Angka Romawi Huruf Besar
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Atur nomor mulai untuk halaman pertama; Anda mungkin ingin memulai dari 2 atau lebih
        fileStamp.setStartingNumber(1);

        // Tambahkan nomor halaman
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```