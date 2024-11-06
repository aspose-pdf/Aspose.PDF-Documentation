```
---
title: Menambahkan Gambar dan Teks 
type: docs
weight: 10
url: id/net/adding-images-and-text-using-pdffilemend-class/
description: Bagian ini menjelaskan cara Menambahkan Gambar dan Teks menggunakan kelas PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

[Kelas PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) dapat membantu Anda menambahkan gambar dan teks ke dalam dokumen PDF yang sudah ada, pada lokasi yang ditentukan.
``` It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) dan [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). method [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) memungkinkan Anda menambahkan gambar dengan tipe JPG, GIF, PNG, dan BMP. method [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) mengambil argumen dari tipe kelas [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) dan menambahkannya ke dalam file PDF yang ada. Gambar dan teks dapat ditambahkan dalam wilayah persegi panjang yang ditentukan oleh koordinat titik kiri bawah dan kanan atas. Saat menambahkan gambar, Anda dapat menentukan jalur file gambar atau aliran file gambar. Untuk menentukan nomor halaman di mana gambar atau teks perlu ditambahkan, kedua metode ini menyediakan argumen nomor halaman. Jadi, Anda tidak hanya dapat menambahkan gambar dan teks di lokasi yang ditentukan tetapi juga di halaman yang ditentukan.

Gambar adalah bagian penting dari isi dokumen PDF. Manipulasi gambar dalam file PDF yang ada adalah kebutuhan umum bagi orang-orang yang bekerja dengan file PDF. Dalam artikel ini, kita akan mempelajari bagaimana gambar dapat dimanipulasi dalam file PDF yang ada dengan bantuan [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dari [Aspose.PDF untuk .NET](/pdf/net/). Semua operasi terkait gambar dari [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) telah dikonsolidasikan dalam artikel ini.

## Detail implementasi

[Ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memungkinkan Anda untuk menambahkan gambar baru dalam file PDF yang ada. Anda juga dapat mengganti atau menghapus gambar yang ada. File PDF juga dapat diubah menjadi gambar. Anda dapat mengubah setiap halaman individu menjadi satu gambar atau seluruh file PDF menjadi satu gambar. Ini memungkinkan Anda memformat i.e. JPEG, BMP, PNG dan TIFF dll. Anda juga dapat mengekstrak gambar dari file PDF. Anda dapat menggunakan empat kelas dari [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) untuk melaksanakan operasi ini i.e. [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Operasi Gambar

Dalam bagian ini, kita akan melihat dengan detail operasi gambar ini. Kita juga akan melihat potongan kode untuk menunjukkan penggunaan kelas dan metode terkait. Pertama-tama, mari kita lihat cara menambahkan gambar dalam file PDF yang sudah ada. Kita dapat menggunakan metode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) dari kelas [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) untuk menambahkan gambar baru. Dengan menggunakan metode ini, Anda tidak hanya dapat menentukan nomor halaman tempat Anda ingin menambahkan gambar, tetapi juga lokasi gambar dapat ditentukan.

## Tambah Gambar dalam File PDF yang Ada (Facades)

Anda dapat menggunakan metode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) dari kelas [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method memerlukan gambar untuk ditambahkan, nomor halaman di mana gambar perlu ditambahkan, dan informasi koordinat. Setelah itu, simpan file PDF yang diperbarui menggunakan metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

Dalam contoh berikut, kita menambahkan gambar ke halaman menggunakan imageStream:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image1.png)

Dengan bantuan [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), kita dapat menumpangkan satu gambar di atas gambar lainnya:
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Muat gambar ke dalam stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // simpan file keluaran
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image2.png)

Ada beberapa cara untuk menyimpan gambar dalam file PDF. Kami akan mendemonstrasikan salah satu dari mereka dalam contoh berikut:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Muat gambar ke dalam stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // simpan file keluaran
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Muat gambar ke dalam stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // simpan file keluaran
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Menambahkan Teks dalam File PDF yang Ada (fasad)

Kita dapat menambahkan teks dengan beberapa cara. Pertimbangkan yang pertama. Kami mengambil [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) dan menambahkannya ke Halaman. Setelah itu, kami menunjukkan koordinat sudut kiri bawah, dan kemudian kami menambahkan teks kami ke Halaman.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Periksa bagaimana tampilannya:

![Add Text](/pdf/net/images/add_text.png)

Cara kedua untuk menambahkan [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Selain itu, kami menunjukkan sebuah persegi panjang di mana teks kami harus sesuai.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
Contoh ketiga memberikan kemampuan untuk Menambahkan Teks ke halaman yang ditentukan. Dalam contoh kita, mari tambahkan keterangan pada halaman 1 dan 3 dari dokumen.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // simpan file keluaran
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```