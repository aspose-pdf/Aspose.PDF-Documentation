---
title: Mengonversi PDF ke Berbagai Format Gambar dalam Python
linktitle: Mengonversi PDF ke Gambar
type: docs
weight: 70
url: id/python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: Topik ini menunjukkan kepada Anda bagaimana menggunakan Aspose.PDF untuk Python untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, EMF, JPEG, PNG, GIF, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Ikhtisar

Artikel ini menjelaskan cara mengonversi PDF ke berbagai format gambar menggunakan Python. Ini mencakup topik-topik berikut.

_Format Gambar_: **TIFF**
- [Python PDF ke TIFF](#python-pdf-to-tiff)
- [Python Mengonversi PDF ke TIFF](#python-pdf-to-tiff)
- [Python Mengonversi Halaman Tunggal atau Tertentu dari PDF ke TIFF](#python-pdf-to-tiff-pages)

_Format Gambar_: **BMP**
- [Python PDF ke BMP](#python-pdf-to-bmp)
- [Python Mengonversi PDF ke BMP](#python-pdf-to-bmp)
- [Python PDF ke Konverter BMP](#python-pdf-to-bmp)

_Format Gambar_: **EMF**
- [Python PDF ke EMF](#python-pdf-to-emf)

- [Python Mengonversi PDF ke EMF](#python-pdf-to-emf)
 - [Python PDF to EMF Converter](#python-pdf-to-emf)


_Format Gambar_: **JPG**
- [Python PDF ke JPG](#python-pdf-to-jpg)
- [Python Konversi PDF ke JPG](#python-pdf-to-jpg)
- [Pengonversi Python PDF ke JPG](#python-pdf-to-jpg)


_Format Gambar_: **PNG**
- [Python PDF ke PNG](#python-pdf-to-png)
- [Python Konversi PDF ke PNG](#python-pdf-to-png)
- [Pengonversi Python PDF ke PNG](#python-pdf-to-png)


_Format Gambar_: **GIF**
- [Python PDF ke GIF](#python-pdf-to-gif)
- [Python Konversi PDF ke GIF](#python-pdf-to-gif)
- [Pengonversi Python PDF ke GIF](#python-pdf-to-gif)

_Format Gambar_: **SVG**
- [Python PDF ke SVG](#python-pdf-to-svg)
- [Python Konversi PDF ke SVG](#python-pdf-to-svg)
- [Pengonversi Python PDF ke SVG](#python-pdf-to-svg)

## Python Konversi PDF ke Gambar

**Aspose.PDF untuk Python** menggunakan beberapa pendekatan untuk mengonversi PDF ke gambar.
 Umumnya, kami menggunakan dua pendekatan: konversi menggunakan pendekatan Device dan konversi menggunakan SaveOption. Bagian ini akan menunjukkan kepada Anda bagaimana mengkonversi dokumen PDF ke format gambar seperti BMP, JPEG, GIF, PNG, EMF, TIFF, dan SVG menggunakan salah satu pendekatan tersebut.

Ada beberapa kelas dalam perpustakaan yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. DocumentDevice berorientasi untuk konversi seluruh dokumen, tetapi ImageDevice - untuk halaman tertentu.

## Konversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF untuk Python** memungkinkan konversi Halaman PDF ke gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (berdasarkan DocumentDevice) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar TIFF. Kelas ini menyediakan metode bernama [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) yang memungkinkan Anda untuk mengkonversi semua halaman dalam file PDF ke satu gambar TIFF.

{{% alert color="success" %}}

**Cobalah untuk mengkonversi PDF ke TIFF secara online**
Aspose.PDF untuk Python via .NET menyajikan aplikasi online gratis ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Konversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk Python menjelaskan cara mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

<a name="csharp-pdf-to-tiff"><strong>Langkah-langkah: Konversi PDF ke TIFF dalam Python</strong></a>

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat objek [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) dan [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/)

3. Panggil metode [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) untuk mengkonversi dokumen PDF ke TIFF.
4. Untuk mengatur properti file keluaran, gunakan kelas [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Cuplikan kode berikut menunjukkan cara mengkonversi semua halaman PDF menjadi satu gambar TIFF.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolusi
    resolution = ap.devices.Resolution(300)

    # Buat objek TiffSettings
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # Buat perangkat TIFF
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice.process(document, output_pdf)
```


## Convert PDF menggunakan kelas ImageDevice

`ImageDevice` adalah nenek moyang untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Enhanced Meta File">EMF</abbr>.
- Kelas [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Portable Network Graphics">PNG</abbr>.

- Kelas [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat bagaimana cara mengubah halaman PDF menjadi gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) menyediakan metode bernama [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) yang memungkinkan Anda untuk mengubah halaman tertentu dari file PDF menjadi format gambar BMP. Kelas lainnya memiliki metode yang sama. Jadi, jika kita perlu mengubah halaman PDF menjadi gambar, kita hanya perlu membuat instance dari kelas yang dibutuhkan.

Langkah-langkah berikut dan cuplikan kode dalam Python menunjukkan kemungkinan ini

 - [Ubah PDF ke BMP dalam Python](#python-pdf-to-image)
 - [Ubah PDF ke EMF dalam Python](#python-pdf-to-image)
 - [Ubah PDF ke JPG dalam Python](#python-pdf-to-image)
 - [Ubah PDF ke PNG dalam Python](#python-pdf-to-image)
 - [Ubah PDF ke GIF dalam Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Langkah-langkah: PDF ke Gambar (BMP, EMF, JPG, PNG, GIF) dalam Python</strong></a>

1. Muat file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat instance dari subclass [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) yaitu
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (untuk mengonversi PDF ke BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (untuk mengonversi PDF ke Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (untuk mengonversi PDF ke JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (untuk mengonversi PDF ke PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (untuk mengonversi PDF ke GIF)
3. Panggil metode [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) untuk melakukan konversi PDF ke Gambar.

### Konversi PDF ke BMP

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # Buat file untuk menyimpan
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # Konversi halaman tertentu dan simpan gambar ke stream
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### Konversi PDF ke EMF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolusi
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # Buat file untuk menyimpan
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # Konversi halaman tertentu dan simpan gambar ke stream
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### Konversi PDF ke JPEG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolusi
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # Buat file untuk menyimpan
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # Konversi halaman tertentu dan simpan gambar ke stream
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### Konversi PDF ke PNG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolusi
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # Buat file untuk menyimpan
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # Konversi halaman tertentu dan simpan gambar ke stream
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
``` 

### Konversi PDF ke GIF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat objek Resolusi
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # Buat file untuk menyimpan
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # Konversi halaman tertentu dan simpan gambar ke stream
        device.process(document.pages[i + 1], imageStream)
        # Tutup stream
        imageStream.close()  
``` 


{{% alert color="success" %}}
**Coba konversi PDF ke PNG online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk Python mempersembahkan aplikasi gratis online ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan kepada Anda cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan Python dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba konversi PDF ke SVG online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah sebuah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskrip, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman untuk membuatnya dengan program gambar seperti Inkscape.

Aspose.PDF untuk Python mendukung fitur untuk mengkonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengkonversi file PDF ke format SVG.
 Untuk memenuhi persyaratan ini, kelas [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) telah diperkenalkan ke dalam namespace Aspose.PDF. Instansiasi objek SvgSaveOptions dan berikan sebagai argumen kedua ke metode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG dengan Python.

<a name="csharp-pdf-to-svg"><strong>Langkah-langkah: Mengonversi PDF ke SVG dalam Python</strong></a>

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) dengan pengaturan yang diperlukan.
3. Panggil metode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan lewati objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) untuk mengonversi dokumen PDF ke SVG.

### Konversi PDF ke SVG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Membuat sebuah objek dari SvgSaveOptions
    saveOptions = ap.SvgSaveOptions()

    # Jangan kompres gambar SVG ke arsip Zip
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # Simpan output dalam file SVG
    document.save(output_pdf, saveOptions)
```