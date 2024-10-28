---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: Bagian ini menjelaskan cara mengonversi File PDF dengan Aspose.PDF Facades menggunakan kelas PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convert PDF Pages to Different Image Formats (Facades)

Untuk mengonversi halaman PDF ke format gambar yang berbeda, Anda perlu membuat objek [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) dan membuka file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) untuk tugas inisialisasi. Kemudian, Anda dapat melakukan loop melalui semua halaman menggunakan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). Metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) memungkinkan Anda membuat gambar dari halaman tertentu. Anda juga perlu melewatkan ImageFormat ke metode ini untuk membuat gambar dengan jenis tertentu yaitu JPEG, GIF, atau PNG, dll. Terakhir, panggil metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) dari kelas [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). Cuplikan kode berikut menunjukkan kepada Anda cara mengonversi halaman PDF menjadi gambar.

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // Buat objek PdfConverter
            PdfConverter converter = new PdfConverter();

            // Ikat file pdf input
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Inisialisasi proses konversi
            converter.DoConvert();

            // Periksa apakah halaman ada dan kemudian konversi ke gambar satu per satu
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Tutup objek PdfConverter
            converter.Close();
        }
```
Dalam cuplikan kode berikut, kami akan menunjukkan bagaimana Anda dapat mengubah beberapa parameter. Dengan [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) kami mengatur bingkai 'CropBox'. Juga, kita dapat mengubah [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) dengan menentukan jumlah titik per inci. Yang berikutnya [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - mode presentasi formulir. Kemudian kami menunjukkan [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) dengan nomor halaman yang ditetapkan sebagai awal konversi. Kami juga dapat menentukan halaman terakhir dengan mengatur rentang.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // Membuat objek PdfConverter
            PdfConverter converter = new PdfConverter();

            // Mengikat file pdf input
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Memulai proses konversi
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // Memeriksa apakah halaman ada dan kemudian mengonversi ke gambar satu per satu
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Menutup objek PdfConverter
            converter.Close();
        }
```

## See also

Aspose.PDF untuk .NET memungkinkan konversi dokumen PDF ke berbagai format dan juga konversi dari format lain ke PDF. Selain itu, Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online dengan aplikasi konverter Aspose.PDF. Pelajari bagian [Converting](/pdf/net/converting/) untuk menyelesaikan tugas Anda.