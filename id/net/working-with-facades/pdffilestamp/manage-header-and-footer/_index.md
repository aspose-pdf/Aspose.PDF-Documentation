---
title: Manage Header and Footer
type: docs
weight: 40
url: /id/net/manage-header-and-footer/
description: Bagian ini menjelaskan cara mengelola Header dan Footer dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Header dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) memungkinkan Anda menambahkan header dalam file PDF. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Untuk menambahkan header, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Anda dapat memformat teks header menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Setelah Anda siap untuk menambahkan header dalam file, Anda perlu memanggil metode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). Anda juga perlu menentukan setidaknya margin atas dalam metode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). Cuplikan kode berikut menunjukkan cara menambahkan header dalam file PDF.

```csharp
 public static void AddHeader()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat teks terformat untuk nomor halaman
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Tambahkan header
            fileStamp.AddHeader(formattedText, 10);

            // Simpan file PDF yang diperbarui
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```
## Add Footer in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class memungkinkan Anda untuk menambahkan footer dalam file PDF. Untuk menambahkan footer, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Anda dapat memformat teks footer menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Setelah Anda siap untuk menambahkan footer dalam file, Anda perlu memanggil metode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Anda juga perlu menentukan setidaknya margin bawah dalam metode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Potongan kode berikut menunjukkan kepada Anda bagaimana menambahkan footer dalam file PDF.

```csharp
 public static void AddFooter()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Buat teks terformat untuk nomor halaman
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Tambahkan footer
            fileStamp.AddFooter(formattedText, 10);

            // Simpan file PDF yang telah diperbarui
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Tutup fileStamp
            fileStamp.Close();
        }
```
## Tambahkan Gambar di Header File PDF yang Ada

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) memungkinkan Anda menambahkan gambar di header file PDF. Untuk menambahkan gambar di header, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Setelah itu, Anda perlu memanggil metode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Anda dapat mengoper gambar ke metode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Akhirnya, simpan file PDF output menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Cuplikan kode berikut menunjukkan cara menambahkan gambar di header file PDF.

```csharp
public static void AddImageHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add Header
                fileStamp.AddHeader(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Close fileStamp
                fileStamp.Close();
            }
        }
```
## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class memungkinkan Anda untuk menambahkan gambar di footer file PDF. Untuk menambahkan gambar di footer, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Setelah itu, Anda perlu memanggil metode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Anda dapat mengoper gambar ke metode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Terakhir, simpan file PDF keluaran menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Potongan kode berikut menunjukkan cara menambahkan gambar di footer file PDF.

```csharp
public static void AddImageFooter()
        {
            // Buat objek PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Buka Dokumen
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Tambahkan footer
                fileStamp.AddFooter(fs, 10);

                // Simpan file PDF yang diperbarui
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Tutup fileStamp
                fileStamp.Close();
            }
        }
```