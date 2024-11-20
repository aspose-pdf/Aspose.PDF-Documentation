---
title: Tambahkan Cap Teks dan Gambar
type: docs
weight: 20
url: /id/net/add-text-and-image-stamp/
description: Bagian ini menjelaskan cara menambahkan Cap Teks dan Gambar dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Cap Teks pada Semua Halaman di File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan cap teks pada semua halaman file PDF.
``` In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. Anda juga perlu membuat cap teks menggunakan metode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang, dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan cap tersebut ke dalam file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Kode berikut menunjukkan cara menambahkan cap teks pada semua halaman dalam file PDF.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat cap
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Tambahkan cap ke file PDF
            fileStamp.AddStamp(stamp);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```
## Tambahkan Cap Teks pada Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan cap teks pada halaman tertentu dari file PDF. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Untuk menambahkan cap teks, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). 
Anda juga perlu membuat cap teks menggunakan metode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` ```
Anda dapat mengatur atribut lain seperti origin, rotation, background, dll.
``` 
menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga.
``` Seperti yang Anda inginkan untuk menambahkan cap teks pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman tempat Anda ingin menambahkan cap tersebut. Kemudian Anda dapat menambahkan cap pada file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan cap teks pada halaman tertentu dalam file PDF.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat cap
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Atur halaman tertentu
            stamp.Pages = new int[] { 2 };

            // Tambahkan cap ke file PDF
            fileStamp.AddStamp(stamp);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```
## Add Image Stamp on All Pages in a PDF File

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda untuk menambahkan cap gambar pada semua halaman file PDF. 
Untuk menambahkan cap gambar, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` Anda juga perlu membuat cap gambar menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Kemudian Anda dapat menambahkan cap ke dalam file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Akhirnya, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan cap gambar pada semua halaman dalam file PDF.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Membuat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Membuat cap
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Menetapkan halaman tertentu
            stamp.Pages = new int[] { 2 };

            // Menambahkan cap ke file PDF
            fileStamp.AddStamp(stamp);

            // Menyimpan file PDF yang telah diperbarui
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Menutup fileStamp
            fileStamp.Close();
        }
```
### Mengontrol kualitas gambar saat menambahkan sebagai cap

Ketika menambahkan Gambar sebagai objek cap, Anda juga dapat mengontrol kualitas gambar. Untuk memenuhi persyaratan ini, properti Kualitas ditambahkan untuk kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ini menunjukkan kualitas gambar dalam persentase (nilai valid adalah 0..100).

## Menambahkan Cap Gambar pada Halaman Tertentu dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) memungkinkan Anda menambahkan cap gambar pada halaman tertentu dari file PDF. 
Untuk menambahkan cap gambar, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp).
``` Anda juga perlu membuat cap gambar menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Anda dapat mengatur atribut lain seperti asal, rotasi, latar belakang dll. menggunakan objek [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) juga. Karena Anda ingin menambahkan cap gambar pada halaman tertentu dari file PDF, Anda juga perlu mengatur properti [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) dari kelas [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Properti ini memerlukan array integer yang berisi nomor halaman di mana Anda ingin menambahkan cap. Kemudian Anda dapat menambahkan cap ke file PDF menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Akhirnya, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Cuplikan kode berikut menunjukkan cara menambahkan cap gambar pada halaman tertentu dalam file PDF.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Membuat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Membuat cap
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Tambahkan cap ke file PDF
            fileStamp.AddStamp(stamp);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```