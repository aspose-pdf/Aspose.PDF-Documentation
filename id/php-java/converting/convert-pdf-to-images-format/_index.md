---
title: Mengonversi PDF ke Format Gambar
linktitle: Mengonversi PDF ke Gambar
type: docs
weight: 70
url: id/php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan konversi PDF ke berbagai format gambar. Konversi halaman PDF ke gambar PNG, JPEG, BMP dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF untuk PHP** memungkinkan Anda mengonversi dokumen PDF ke format gambar seperti BMP, JPEG, GIF, PNG, EMF, TIFF, dan SVG menggunakan dua pendekatan. Konversi dilakukan menggunakan `Device` dan menggunakan `SaveOption`.

Ada beberapa kelas dalam pustaka yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. `DocumentDevice` berorientasi untuk mengonversi seluruh dokumen, tetapi `ImageDevice` - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF untuk PHP** memungkinkan konversi Halaman PDF ke gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) memungkinkan Anda mengonversi halaman PDF ke gambar TIFF.
 Kelas ini menyediakan metode bernama Process yang memungkinkan Anda untuk mengubah semua halaman dalam file PDF menjadi satu gambar TIFF.

### Mengonversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk PHP menjelaskan cara mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Panggil metode [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) untuk mengonversi dokumen.
3. Untuk mengatur properti file keluaran, gunakan kelas [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Cuplikan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```php
// Memuat dokumen PDF
$document = new Document($inputFile);

// Membuat objek TiffSettings baru
$tiffSettings = new devices_TiffSettings();

// Batalkan komentar pada baris berikut untuk menyesuaikan pengaturan TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Mengatur resolusi untuk gambar TIFF
$resolution = new devices_Resolution(300);

// Membuat objek TiffDevice baru dengan resolusi dan pengaturan yang ditentukan
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Mengonversi dokumen PDF ke TIFF menggunakan TiffDevice
$tiffDevice->process($document, $outputFile);
```

### Mengonversi Halaman Tunggal ke Gambar TIFF

Aspose.PDF untuk PHP memungkinkan untuk mengonversi halaman tertentu dalam file PDF ke gambar TIFF, gunakan versi yang di-overload dari metode Process(..) yang mengambil nomor halaman sebagai argumen untuk konversi. Cuplikan kode berikut menunjukkan cara mengonversi halaman pertama dari PDF ke format TIFF.

```php
// Memuat dokumen PDF
$document = new Document($inputFile);

// Membuat objek TiffSettings baru
$tiffSettings = new devices_TiffSettings();

// Hapus komentar pada baris berikut untuk menyesuaikan pengaturan TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Mengatur resolusi untuk gambar TIFF
$resolution = new devices_Resolution(300);

// Membuat objek TiffDevice baru dengan resolusi dan pengaturan yang ditentukan
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Mengonversi dokumen PDF ke TIFF menggunakan TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### Gunakan algoritma Bradley selama konversi

Aspose.PDF untuk PHP telah mendukung fitur untuk mengkonversi PDF ke TIFF menggunakan kompresi LZW dan kemudian dengan menggunakan AForge, Binarisasi dapat diterapkan. Namun salah satu pelanggan meminta bahwa untuk beberapa gambar, mereka perlu mendapatkan Threshold menggunakan Otsu, jadi mereka juga ingin menggunakan Bradley.

```php
// Buat objek TiffSettings baru
$tiffSettings = new devices_TiffSettings();

// Hapus komentar baris berikut untuk menyesuaikan pengaturan TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Atur resolusi untuk gambar TIFF
$resolution = new devices_Resolution(300);

// Buat objek TiffDevice baru dengan resolusi dan pengaturan yang ditentukan
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Konversi dokumen PDF ke TIFF menggunakan TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Buat objek stream untuk menyimpan gambar keluaran
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### Mengonversi Halaman PDF ke Gambar TIFF Berpiksel

Untuk mengonversi semua halaman dalam file PDF ke format TIFF Berpiksel, gunakan opsi Piksel dari IndexedConversionType

```php
// Buat objek TiffSettings baru
$tiffSettings = new devices_TiffSettings();

// Hapus komentar baris berikut untuk menyesuaikan pengaturan TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// atur kecerahan gambar
$tiffSettings->setBrightness(0.5f);
// atur IndexedConversion Type, nilai default adalah simple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Atur resolusi untuk gambar TIFF
$resolution = new devices_Resolution(300);

// Buat objek TiffDevice baru dengan resolusi dan pengaturan yang ditentukan
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Konversi dokumen PDF ke TIFF menggunakan TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Buat objek stream untuk menyimpan gambar keluaran
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**Coba konversi PDF ke TIFF online**

Aspose.PDF untuk PHP menghadirkan aplikasi online gratis ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya.

[![Aspose.PDF konversi PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF menggunakan kelas ImageDevice

`ImageDevice` adalah nenek moyang untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Enhanced Meta File">EMF</abbr>.

- Kelas [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Portable Network Graphics">PNG</abbr>.
- Kelas [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat bagaimana cara mengonversi halaman PDF ke gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) menyediakan metode bernama [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) yang memungkinkan Anda untuk mengonversi halaman tertentu dari file PDF ke format gambar BMP. Kelas lainnya memiliki metode yang sama. Jadi, jika kita perlu mengonversi halaman PDF ke gambar, kita hanya perlu membuat instans dari kelas yang diperlukan.

Cuplikan kode berikut menunjukkan kemungkinan ini:

```php
// Muat dokumen PDF
$document = new Document($inputFile);

// Dapatkan koleksi halaman dalam dokumen
$pages = $document->getPages();

// Dapatkan jumlah total halaman dalam dokumen
$count = $pages->size();

// Atur resolusi untuk gambar PNG
$resolution = new devices_Resolution(300);

// Buat perangkat PNG baru dengan resolusi yang ditentukan
$imageDevice = new devices_PngDevice($resolution);

// Loop melalui setiap halaman dalam dokumen
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // Atur nama file gambar keluaran untuk halaman saat ini
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // Dapatkan halaman saat ini dari koleksi
    $page = $document->getPages()->get_Item($pageCount);

    // Proses halaman saat ini dan simpan sebagai gambar PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerja.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan kepada Anda bagaimana mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan Java dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF untuk PHP menghadirkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerja.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah sekumpulan spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskrip, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman untuk membuatnya dengan program gambar seperti Inkscape.

### Mengonversi halaman PDF ke gambar SVG

Aspose.PDF untuk PHP mendukung fitur untuk mengonversi file PDF ke format SVG.
 Untuk memenuhi persyaratan ini, kelas [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) telah diperkenalkan ke dalam paket com.aspose.pdf. Buat sebuah objek dari [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) dan berikan sebagai argumen kedua ke metode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG.

```php
// Memuat dokumen PDF
$document = new Document($inputFile);

// Membuat instance dari kelas SvgSaveOptions
$saveOption = new SvgSaveOptions();

// Menyimpan dokumen PDF sebagai SVG
$document->save($outputFile, $saveOption);
```