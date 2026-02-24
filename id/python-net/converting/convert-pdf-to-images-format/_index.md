---
title: Konversi PDF ke Berbagai Format Gambar dalam Python
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /id/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Jelajahi cara mengonversi halaman PDF menjadi gambar seperti PNG, JPEG, atau TIFF menggunakan Aspose.PDF dalam Python melalui .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke Format Gambar dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi file PDF ke berbagai format gambar menggunakan Python, khususnya memanfaatkan pustaka Aspose.PDF untuk Python. Dokumen ini menjelaskan metode konversi PDF ke format gambar termasuk TIFF, BMP, EMF, JPG, PNG, GIF, dan SVG. Dua pendekatan konversi utama dibahas - menggunakan pendekatan Device dan SaveOption. Pendekatan Device melibatkan penggunaan kelas seperti `DocumentDevice` dan `ImageDevice` untuk konversi seluruh dokumen atau konversi per halaman. Langkah-langkah terperinci dan contoh kode Python disediakan untuk mengonversi halaman PDF ke berbagai format seperti TIFF menggunakan `TiffDevice`, serta BMP, EMF, JPEG, PNG, dan GIF menggunakan kelas perangkat masing-masing (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Untuk konversi SVG, kelas `SvgSaveOptions` diperkenalkan. Artikel ini juga menyoroti alat daring untuk mencoba konversi tersebut.
---

## Python Mengonversi PDF ke Gambar

**Aspose.PDF for Python** menggunakan beberapa pendekatan untuk mengonversi PDF ke gambar. Secara umum, kami menggunakan dua pendekatan: konversi dengan pendekatan Device dan konversi dengan SaveOption. Bagian ini akan menunjukkan cara mengonversi dokumen PDF ke format gambar seperti BMP, JPEG, GIF, PNG, EMF, TIFF, dan format SVG menggunakan salah satu pendekatan tersebut.

Ada beberapa kelas dalam pustaka yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. DocumentDevice ditujukan untuk mengonversi seluruh dokumen, sedangkan ImageDevice - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF for Python** memungkinkan mengonversi Halaman PDF ke gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (berbasis DocumentDevice) memungkinkan Anda mengonversi halaman PDF ke gambar TIFF. Kelas ini menyediakan metode bernama [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) yang memungkinkan Anda mengonversi semua halaman dalam file PDF ke satu gambar TIFF.

{{% alert color="success" %}}
**Coba mengonversi PDF ke TIFF secara daring**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi daring gratis ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), dimana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Mengonversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk Python menjelaskan cara mengonversi semua halaman dalam file PDF ke satu gambar TIFF:

Langkah: Konversi PDF ke TIFF dalam Python

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat objek [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) dan [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Panggil metode [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) untuk mengonversi dokumen PDF ke TIFF.
1. Untuk mengatur properti file output, gunakan kelas [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Potongan kode berikut menunjukkan cara mengonversi semua halaman PDF ke satu gambar TIFF.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## Mengonversi PDF menggunakan kelas ImageDevice

`ImageDevice` adalah kelas induk untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Enhanced Meta File">EMF</abbr>.
- Kelas [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) memungkinkan Anda mengonversi halaman PDF menjadi gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Portable Network Graphics">PNG</abbr>.
- Kelas [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) memungkinkan Anda mengonversi halaman PDF menjadi gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat cara mengonversi halaman PDF ke gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) menyediakan metode bernama [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) yang memungkinkan Anda mengonversi halaman tertentu dari file PDF ke format gambar BMP. Kelas lain memiliki metode yang sama. Jadi, jika kita perlu mengonversi halaman PDF ke gambar, cukup buat instance kelas yang diperlukan.

Langkah-langkah berikut dan potongan kode dalam Python menunjukkan kemungkinan ini:

- [Konversi PDF ke BMP dalam Python](#python-pdf-to-image)
- [Konversi PDF ke EMF dalam Python](#python-pdf-to-image)
- [Konversi PDF ke JPG dalam Python](#python-pdf-to-image)
- [Konversi PDF ke PNG dalam Python](#python-pdf-to-image)
- [Konversi PDF ke GIF dalam Python](#python-pdf-to-image)

Langkah: PDF ke Gambar (BMP, EMF, JPG, PNG, GIF) dalam Python

1. Muat file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat instance dari subclass [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) yaitu.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (untuk mengonversi PDF ke BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (untuk mengonversi PDF ke Emf)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (untuk mengonversi PDF ke JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (untuk mengonversi PDF ke PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (untuk mengonversi PDF ke GIF)
1. Panggil metode [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) untuk melakukan konversi PDF ke Gambar.

### Mengonversi PDF ke BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Mengonversi PDF ke JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### Mengonversi PDF ke PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke PNG dengan font default

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke PNG secara daring**

Sebagai contoh cara kerja aplikasi gratis kami, silakan periksa fitur berikut.

Aspose.PDF for Python mempersembahkan aplikasi gratis daring ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Mengonversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan Python dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba mengonversi PDF ke SVG secara daring**

Aspose.PDF for Python via .NET mempersembahkan aplikasi gratis daring ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diprogram, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman membuatnya dengan program menggambar seperti Inkscape.

Aspose.PDF for Python mendukung fitur untuk mengonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengonversi file PDF ke format SVG. Untuk memenuhi kebutuhan ini, kelas [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) telah diperkenalkan ke dalam namespace Aspose.PDF. Buat instance objek SvgSaveOptions dan berikan sebagai argumen kedua ke metode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Potongan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG dengan Python.

Langkah: Mengonversi PDF ke SVG dalam Python

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) dengan pengaturan yang diperlukan.
1. Panggil metode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan berikan objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) untuk mengonversi dokumen PDF ke SVG.

### Mengonversi PDF ke SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

