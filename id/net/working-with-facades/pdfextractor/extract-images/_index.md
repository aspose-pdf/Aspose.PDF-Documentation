---
title: Extract Images menggunakan PdfExtractor
type: docs
weight: 20
url: id/net/extract-images/
description: Bagian ini menjelaskan cara mengekstrak Gambar dengan Aspose.PDF Facades menggunakan Kelas PdfExtractor.
lastmod: "2021-07-15"
---

## Ekstrak Gambar dari Seluruh PDF ke Berkas (Facades)

Kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda mengekstrak gambar dari berkas PDF. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class dan mengikat file PDF masukan menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar-gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan iterasi melalui semua gambar yang diekstrak menggunakan perulangan while. Untuk menyimpan gambar ke disk, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang mengambil jalur file sebagai argumen. Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari seluruh PDF ke file.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Buka input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Ekstrak semua gambar
            pdfExtractor.ExtractImage();

            // Dapatkan semua gambar yang diekstrak
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Extract Images from the Whole PDF to Streams (Facades)

Kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF ke dalam stream. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Pertama, Anda perlu membuat objek dari kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar-gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan iterasi melalui semua gambar yang diekstrak menggunakan loop while. Untuk menyimpan gambar ke dalam stream, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang menerima Stream sebagai argumen. Cuplikan kode berikut menunjukkan bagaimana cara mengekstrak gambar dari seluruh PDF ke stream.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Buka PDF input
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Ekstrak gambar
            pdfExtractor.ExtractImage();
            // Dapatkan semua gambar yang diekstrak
            while (pdfExtractor.HasNextImage())
            {
                // Baca gambar ke dalam memory stream
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Tulis ke disk, jika Anda mau, atau gunakan dengan cara lain.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Extract Images from a Particular Page of a PDF (Facades)

Anda dapat mengekstrak gambar dari halaman tertentu dari file PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properti ke halaman tertentu yang Anda ingin ekstrak gambarnya.  First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

 Pertama-tama, Anda perlu membuat objek dari kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Kedua, Anda harus mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstrak, Anda dapat mendapatkan gambar-gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstrak menggunakan loop while. Anda dapat menyimpan gambar ke disk atau stream. Anda hanya perlu memanggil overload yang sesuai dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari halaman tertentu PDF ke stream.

```csharp
public static void ExtractImagesParticularPage()
{
    // Buka PDF input
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Setel properti StartPage dan EndPage ke nomor halaman yang
    // Anda inginkan untuk mengekstrak gambar
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Ekstrak gambar
    pdfExtractor.ExtractImage();
    // Dapatkan gambar yang diekstrak
    while (pdfExtractor.HasNextImage())
    {
        // Baca gambar ke dalam memory stream
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Tulis ke disk, jika Anda mau, atau gunakan dengan cara lain.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images from a Range of Pages of a PDF (Facades)

Anda dapat mengekstrak gambar dari rentang halaman file PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properti ke rentang halaman dari mana Anda ingin mengekstrak gambar. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Pertama-tama, Anda perlu membuat objek dari kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, Anda harus mengatur properti [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) dan [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). Setelah itu, panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstraksi, Anda dapat mendapatkan gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan iterasi melalui semua gambar yang diekstraksi menggunakan while loop. Anda dapat menyimpan gambar ke disk atau stream. Anda hanya perlu memanggil overload yang sesuai dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari rentang halaman PDF ke stream.

```csharp
public static void ExtractImagesRangePages()
{
    // Buka PDF input
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Atur properti StartPage dan EndPage ke nomor halaman untuk
    // Anda ingin mengekstrak gambar dari
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Ekstrak gambar
    pdfExtractor.ExtractImage();
    // Dapatkan gambar yang diekstraksi
    while (pdfExtractor.HasNextImage())
    {
        // Baca gambar ke dalam memory stream
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Tulis ke disk, jika Anda mau, atau gunakan dengan cara lain.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images using Image Extraction Mode (Facades)

Kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF. Aspose.PDF mendukung dua mode ekstraksi; yang pertama adalah ActuallyUsedImage yang mengekstraksi gambar yang benar-benar digunakan dalam dokumen PDF. ```
Mode kedua adalah [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) yang mengekstraksi gambar yang didefinisikan dalam sumber daya dokumen PDF (mode ekstraksi default).
``` First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Pertama, Anda perlu membuat objek dari kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, tentukan mode ekstraksi gambar menggunakan properti [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Kemudian panggil metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) untuk mengekstrak semua gambar ke dalam memori tergantung pada mode yang Anda tentukan. Setelah gambar diekstraksi, Anda dapat mendapatkan gambar-gambar tersebut dengan bantuan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Anda perlu melakukan loop melalui semua gambar yang diekstraksi menggunakan while loop. Untuk menyimpan gambar ke disk, Anda dapat memanggil overload dari metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) yang mengambil jalur file sebagai argumen.

Cuplikan kode berikut menunjukkan kepada Anda cara mengekstrak gambar dari file PDF menggunakan opsi ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // Buka PDF input
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Tentukan Mode Ekstraksi Gambar
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // Ekstrak Gambar berdasarkan Mode Ekstraksi Gambar
    extractor.ExtractImage();

    // Dapatkan semua gambar yang diekstraksi
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

Untuk memeriksa apakah PDF mengandung Teks atau Gambar gunakan potongan kode berikut:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // Buat objek memoryStream untuk menampung teks yang diekstrak dari Dokumen
            MemoryStream ms = new MemoryStream();
            // Buat objek PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // Hubungkan dokumen PDF input ke ekstraktor
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // Ekstrak teks dari dokumen PDF input
            extractor.ExtractText();
            // Simpan teks yang diekstrak ke file teks
            extractor.GetText(ms);
            // Periksa apakah panjang MemoryStream lebih besar atau sama dengan 1

            bool containsText = ms.Length >= 1;

            // Ekstrak gambar dari dokumen PDF input
            extractor.ExtractImage();

            // Memanggil metode HasNextImage dalam while loop. Ketika gambar habis, loop akan keluar
            bool containsImage = extractor.HasNextImage();

            // Sekarang cari tahu apakah PDF ini hanya teks atau hanya gambar

            if (containsText && !containsImage)
                Console.WriteLine("PDF hanya mengandung teks");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF hanya mengandung gambar");
            else if (containsText && containsImage)
                Console.WriteLine("PDF mengandung teks dan gambar");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF tidak mengandung teks maupun gambar");
        }

    }
```