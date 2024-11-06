---
title: Tambahkan Cap Halaman PDF
type: docs
weight: 10
url: id/net/add-pdf-page-stamp/
description: Bagian ini menjelaskan cara bekerja dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Cap Halaman PDF pada Semua Halaman di File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda menambahkan cap halaman PDF pada semua halaman dari file PDF. Untuk menambahkan stempel halaman PDF, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda juga perlu membuat stempel halaman PDF menggunakan metode [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan stempel dalam file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan stempel halaman PDF pada semua halaman dalam file PDF.

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
## Tambahkan Stempel Halaman PDF pada Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan stempel halaman PDF pada halaman tertentu dari file PDF. 
Untuk menambahkan stempel halaman PDF, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` 
Anda juga perlu membuat cap halaman PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` You can set other attributes like origin, rotation, background etc.  
Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang dll. 
menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga.
``` As Anda ingin menambahkan cap halaman PDF pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman yang ingin Anda tambahkan capnya. Kemudian Anda dapat menambahkan cap pada file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan cap halaman PDF pada halaman tertentu dalam file PDF.

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
## Tambahkan Nomor Halaman dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda menambahkan nomor halaman dalam file PDF. ```
Untuk menambahkan nomor halaman, Anda perlu terlebih dahulu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp).
``` If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

Jika Anda ingin menampilkan nomor halaman seperti "Halaman X dari N" di mana X adalah nomor halaman saat ini dan N adalah jumlah total halaman dalam file PDF, maka Anda perlu mendapatkan jumlah halaman menggunakan properti [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Untuk mendapatkan nomor halaman saat ini, Anda dapat menggunakan tanda **#** di teks Anda di mana saja Anda suka. Anda dapat memformat teks nomor halaman menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Jika Anda ingin memulai penomoran halaman dari nomor tertentu, Anda dapat mengatur properti [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Setelah Anda siap untuk menambahkan nomor halaman ke dalam file, Anda perlu memanggil metode [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). Akhirnya, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). Kode berikut menunjukkan kepada Anda cara menambahkan nomor halaman dalam file PDF.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Membuat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Dapatkan total jumlah halaman
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Membuat teks yang diformat untuk nomor halaman
            FormattedText formattedText = new FormattedText($"Halaman # dari {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Tetapkan nomor awal untuk halaman pertama; Anda mungkin ingin memulai dari 2 atau lebih
            fileStamp.StartingNumber = 1;

            // Tambahkan nomor halaman
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```
### Gaya Penomoran Kustom

Kelas PdfFileStamp menawarkan fitur untuk menambahkan informasi Nomor Halaman sebagai objek stempel di dalam dokumen PDF. Sebelum rilis ini, kelas hanya mendukung 1,2,3,4 sebagai gaya penomoran halaman. Namun, ada permintaan dari beberapa pelanggan untuk menggunakan gaya penomoran kustom saat menempatkan stempel nomor halaman di dalam dokumen PDF. Untuk memenuhi persyaratan ini, properti [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) telah diperkenalkan, yang menerima nilai dari enumerasi [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Di bawah ini adalah nilai-nilai yang ditawarkan dalam enumerasi ini.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Dapatkan jumlah total halaman
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Buat teks yang diformat untuk nomor halaman
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Tentukan gaya penomoran sebagai Numerals Roman UpperCase
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // Tetapkan nomor awal untuk halaman pertama; Anda mungkin ingin memulai dari 2 atau lebih
            fileStamp.StartingNumber = 1;

            // Tambahkan nomor halaman
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```