---
title: Mengonversi PDF ke Berbagai Format Gambar dalam C#
linktitle: Mengonversi PDF ke Gambar
type: docs
weight: 70
url: id/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, EMF, JPEG, PNG, GIF, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Overview

Artikel ini menjelaskan cara mengonversi PDF ke berbagai format gambar menggunakan C#. Ini mencakup topik berikut.

_Format Gambar_: **TIFF**
- [C# PDF ke TIFF](#csharp-pdf-to-tiff)
- [C# Mengonversi PDF ke TIFF](#csharp-pdf-to-tiff)
- [C# Mengonversi Satu atau Halaman Tertentu dari PDF ke TIFF](#csharp-pdf-to-tiff-pages)

_Format Gambar_: **BMP**
- [C# PDF ke BMP](#csharp-pdf-to-bmp)
- [C# Mengonversi PDF ke BMP](#csharp-pdf-to-bmp)
- [C# Konverter PDF ke BMP](#csharp-pdf-to-bmp)

_Format Gambar_: **EMF**
- [C# PDF ke EMF](#csharp-pdf-to-emf)
- [C# Mengonversi PDF ke EMF](#csharp-pdf-to-emf)
- [C# Konverter PDF ke EMF](#csharp-pdf-to-emf)
- [C# PDF ke EMF Converter](#csharp-pdf-to-emf)


_Format Gambar_: **JPG**
- [C# PDF ke JPG](#csharp-pdf-to-jpg)
- [C# Konversi PDF ke JPG](#csharp-pdf-to-jpg)
- [C# PDF ke JPG Converter](#csharp-pdf-to-jpg)


_Format Gambar_: **PNG**
- [C# PDF ke PNG](#csharp-pdf-to-png)
- [C# Konversi PDF ke PNG](#csharp-pdf-to-png)
- [C# PDF ke PNG Converter](#csharp-pdf-to-png)


_Format Gambar_: **GIF**
- [C# PDF ke GIF](#csharp-pdf-to-gif)
- [C# Konversi PDF ke GIF](#csharp-pdf-to-gif)
- [C# PDF ke GIF Converter](#csharp-pdf-to-gif)

_Format Gambar_: **SVG**
- [C# PDF ke SVG](#csharp-pdf-to-svg)
- [C# Konversi PDF ke SVG](#csharp-pdf-to-svg)
- [C# PDF ke SVG Converter](#csharp-pdf-to-svg)

## C# Konversi PDF ke Gambar

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF untuk .NET** menggunakan beberapa pendekatan untuk mengkonversi PDF ke gambar.
**Aspose.PDF for .NET** menggunakan beberapa pendekatan untuk mengonversi PDF menjadi gambar.

Ada beberapa kelas di perpustakaan yang memungkinkan Anda menggunakan perangkat virtual untuk mentransformasi gambar. DocumentDevice ditujukan untuk konversi seluruh dokumen, tetapi ImageDevice - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF for .NET** memungkinkan untuk mengonversi Halaman PDF menjadi gambar TIFF.

Kelas TiffDevice (berbasis DocumentDevice) memungkinkan Anda untuk mengonversi halaman PDF menjadi gambar TIFF. Kelas ini menyediakan metode yang bernama `Process` yang memungkinkan Anda untuk mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF.

{{% alert color="success" %}}
**Coba konversi PDF ke TIFF secara online**

Aspose.PDF for .NET menyajikan aplikasi gratis online ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Mengonversi Halaman PDF menjadi Satu Gambar TIFF

Aspose.PDF for .NET menjelaskan cara mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

<a name="csharp-pdf-to-tiff"><strong>Langkah-langkah: Mengonversi PDF ke TIFF dalam C#</strong></a>

1. Buat objek dari kelas **Document**.
2. Buat objek **TiffSettings** dan **TiffDevice**
3. Panggil metode **TiffDevice.Process()** untuk mengonversi dokumen PDF menjadi TIFF.
4. Untuk mengatur properti file keluaran, gunakan kelas **TiffSettings**.

Potongan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Buat objek Resolusi
    Resolution resolution = new Resolution(300);

    // Buat objek TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Buat perangkat TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### Konversi Satu Halaman ke Gambar TIFF

Aspose.PDF untuk .NET memungkinkan untuk mengonversi halaman tertentu dalam file PDF menjadi gambar TIFF, gunakan versi yang dimuat lebih dari metode Process(..) yang mengambil nomor halaman sebagai argumen untuk konversi. Potongan kode berikut menunjukkan cara mengonversi halaman pertama dari PDF ke format TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Langkah: Mengonversi Halaman Tunggal atau Tertentu dari PDF ke TIFF dalam C#</strong></a>

1. Buat objek dari kelas **Document**.
2. Buat objek **TiffSettings** dan **TiffDevice**
3. Panggil metode **TiffDevice.Process()** yang dimuat lebih dengan parameter **fromPage** dan **toPage** untuk mengonversi halaman dokumen PDF menjadi TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Buat objek Resolusi
    Resolution resolution = new Resolution(300);

    // Buat objek TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Buat perangkat TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Gunakan algoritma Bradley selama konversi

Aspose.PDF untuk .NET telah mendukung fitur untuk mengonversi PDF ke TIF menggunakan kompresi LZW dan kemudian dengan menggunakan AForge, Binarisasi dapat diterapkan. Namun, salah satu pelanggan meminta bahwa untuk beberapa gambar, mereka perlu mendapatkan Ambang menggunakan Otsu, sehingga mereka juga ingin menggunakan Bradley.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // Buka dokumen
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Buat objek Resolusi
    Resolution resolution = new Resolution(300);
    // Buat objek TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Buat perangkat TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## Mengonversi PDF menggunakan kelas ImageDevice

`ImageDevice` adalah leluhur untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Enhanced Meta File">EMF</abbr>.
- Kelas [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Portable Network Graphics">PNG</abbr>.
- Kelas [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat cara mengonversi halaman PDF menjadi gambar.
Mari kita lihat cara mengonversi halaman PDF menjadi gambar.

Kelas `BmpDevice` menyediakan metode yang bernama [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) yang memungkinkan Anda untuk mengonversi halaman tertentu dari file PDF menjadi format gambar BMP. Kelas lain memiliki metode yang sama. Jadi, jika kita perlu mengonversi halaman PDF menjadi gambar, kita hanya perlu menginstansiasi kelas yang dibutuhkan.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Langkah berikut dan cuplikan kode dalam C# menunjukkan kemungkinan ini
 
 - [Konversi PDF ke BMP dalam C#](#csharp-pdf-to-image)
 - [Konversi PDF ke EMF dalam C#](#csharp-pdf-to-image)
 - [Konversi PDF ke JPG dalam C#](#csharp-pdf-to-image)
 - [Konversi PDF ke PNG dalam C#](#csharp-pdf-to-image)
 - [Konversi PDF ke GIF dalam C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Langkah: PDF ke Gambar (BMP, EMF, JPG, PNG, GIF) dalam C#</strong></a>

1.
1.
2. Buat instance dari subclass **ImageDevice** yaitu:
   * **BmpDevice** (untuk mengubah PDF menjadi BMP)
   * **EmfDevice** (untuk mengubah PDF menjadi Emf)
   * **JpegDevice** (untuk mengubah PDF menjadi JPG)
   * **PngDevice** (untuk mengubah PDF menjadi PNG)
   * **GifDevice** (untuk mengubah PDF menjadi GIF)
3. Panggil method **ImageDevice.Process()** untuk melakukan konversi PDF ke Gambar.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Create Resolution object            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // Convert a particular page and save the image to stream
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Close stream
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk .NET memperkenalkan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Mengonversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan C# dan kelas SaveOptions.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke SVG secara online**

Aspose.PDF untuk .NET memperkenalkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.
{{% /alert %}}

[![Konversi Aspose.PDF PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
**Grafik Vektor Skalabel (SVG)** adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh Konsorsium World Wide Web (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, di-script, dan jika diperlukan, dikompres. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi sering kali lebih mudah untuk membuatnya dengan program gambar seperti Inkscape.

Aspose.PDF untuk .NET mendukung fitur untuk mengonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengonversi file PDF ke format SVG.
Aspose.PDF untuk .NET mendukung fitur untuk mengonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengonversi file PDF ke format SVG.

Potongan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG dengan .NET.

<a name="csharp-pdf-to-svg"><strong>Langkah: Mengonversi PDF ke SVG dalam C#</strong></a>

1. Buat objek dari kelas **Document**.
2. Buat objek **SvgSaveOptions** dengan pengaturan yang diperlukan.
3. Panggil metode **Document.Save()** dan berikan objek **SvgSaveOptions** untuk mengonversi dokumen PDF ke SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // Muat dokumen PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // Instansiasi objek SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // Jangan kompres gambar SVG ke arsip Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Simpan output dalam file SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

