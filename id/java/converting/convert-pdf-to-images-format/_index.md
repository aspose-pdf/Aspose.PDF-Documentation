---
title: Mengonversi PDF ke Format Gambar 
linktitle: Mengonversi PDF ke Gambar
type: docs
weight: 70
url: id/java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan mengonversi PDF ke berbagai format gambar. Konversi halaman PDF ke gambar PNG, JPEG, BMP dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** memungkinkan Anda untuk mengonversi dokumen PDF ke format gambar seperti BMP, JPEG, GIF, PNG, EMF, TIFF, dan SVG menggunakan dua pendekatan. Konversi dilakukan menggunakan Device dan menggunakan SaveOption.

Ada beberapa kelas dalam pustaka yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. DocumentDevice berorientasi untuk konversi seluruh dokumen, tetapi ImageDevice - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF for Java** memungkinkan mengonversi Halaman PDF ke gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) memungkinkan Anda mengonversi halaman PDF ke gambar TIFF.
 Kelas ini menyediakan metode bernama Process yang memungkinkan Anda untuk mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF.

### Mengonversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF for Java menjelaskan bagaimana mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Panggil metode [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) untuk mengonversi dokumen.
1. Untuk mengatur properti file keluaran, gunakan kelas [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Cuplikan kode berikut menunjukkan bagaimana mengonversi semua halaman PDF menjadi satu gambar TIFF.

```java
// Buka dokumen
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Buat objek Resolution
Resolution resolution = new Resolution(300);

// Buat objek TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// Buat perangkat TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Konversi halaman tertentu dan simpan gambar ke stream
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### Mengonversi Halaman Tunggal ke Gambar TIFF

Aspose.PDF untuk Java memungkinkan untuk mengonversi halaman tertentu dalam file PDF ke gambar TIFF, gunakan versi berlebihan dari metode Process(..) yang mengambil nomor halaman sebagai argumen untuk konversi. Cuplikan kode berikut menunjukkan cara mengonversi halaman pertama dari PDF ke format TIFF.

```java
// Buka dokumen
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// Buat objek Resolution
Resolution resolution = new Resolution(300);

// Buat objek TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// Buat perangkat TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Konversi halaman tertentu dan simpan gambar ke stream
tiffDevice.process(document, 1, 1, tiffFileName);
```


### Gunakan algoritma Bradley selama konversi

Aspose.PDF untuk Java telah mendukung fitur untuk mengonversi PDF ke TIFF menggunakan kompresi LZW dan kemudian dengan menggunakan AForge, Binarisasi dapat diterapkan. Namun salah satu pelanggan meminta bahwa untuk beberapa gambar, mereka perlu mendapatkan Threshold menggunakan Otsu, jadi mereka juga ingin menggunakan Bradley.

```java
// Buka dokumen
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Buat objek Resolusi
Resolution resolution = new Resolution(300);
// Buat objek TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// Buat perangkat TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// Konversi halaman tertentu dan simpan gambar ke stream
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// Buat objek stream untuk menyimpan gambar keluaran
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### Ubah Halaman PDF ke Gambar TIFF Berpiksel

Untuk mengubah semua halaman dalam file PDF ke format TIFF Berpiksel, gunakan opsi Pixelated dari IndexedConversionType

```java
// Ubah Halaman PDF ke Gambar TIFF Berpiksel
// Untuk mengubah semua halaman dalam file PDF ke format TIFF Berpiksel, gunakan
// opsi Pixelated dari IndexedConversionType.

// Buka dokumen
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Buat objek stream untuk menyimpan gambar keluaran
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// Buat objek Resolution
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// instansiasi objek TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// atur kompresi dari gambar TIFF yang dihasilkan
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// atur kedalaman warna untuk gambar yang dihasilkan
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// lewati halaman kosong saat me-render PDF ke TIFF
tiffSettings.setSkipBlankPages(true);
// atur kecerahan gambar
tiffSettings.setBrightness(.5f);

// atur IndexedConversion Type, nilai default adalah sederhana
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// Buat TiffDevice dengan resolusi tertentu
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// Konversi halaman tertentu (Halaman 1) dan simpan gambar ke stream
tiffDevice.process(document, 1, 1, imageStream);

// Tutup stream
imageStream.close();
```


{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke TIFF secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF konversi PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF menggunakan kelas ImageDevice

`ImageDevice` adalah nenek moyang dari `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Enhanced Meta File">EMF</abbr>.

- Kelas [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Portable Network Graphics">PNG</abbr>.
- Kelas [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat bagaimana cara mengonversi halaman PDF ke gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) menyediakan metode bernama [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) yang memungkinkan Anda untuk mengonversi halaman tertentu dari file PDF ke format gambar BMP. Kelas lainnya memiliki metode yang sama. Jadi, jika kita perlu mengonversi halaman PDF ke gambar, kita cukup menginstansiasi kelas yang diperlukan.

Cuplikan kode berikut menunjukkan kemungkinan ini:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Konversi PDF ke Gambar.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Buat objek Resolution
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // Konversi halaman tertentu dan simpan gambar ke stream
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Tutup stream
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan cek fitur berikut.

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan kepada Anda bagaimana mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan Java dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

Gambar SVG dan perilaku mereka didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskrip, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apapun, tetapi sering lebih nyaman untuk membuatnya dengan program menggambar seperti Inkscape.

### Konversi halaman PDF ke gambar SVG

Aspose.PDF untuk Java mendukung fitur untuk mengonversi file PDF ke format SVG.
 Untuk memenuhi persyaratan ini, kelas [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) telah diperkenalkan ke dalam paket com.aspose.pdf. Buat sebuah objek dari [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) dan berikan sebagai argumen kedua ke metode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Mengonversi PDF ke SVG.
 */
public class ConvertPDFtoSVG {
    // Jalur ke direktori dokumen.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // Muat dokumen PDF
        Document document = new Document(pdfFileName);

        // Buat sebuah objek dari SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // Jangan kompres gambar SVG ke arsip Zip
        saveOptions.setCompressOutputToZipArchive(false);

        // Simpan keluaran dalam file SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```