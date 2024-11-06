---
title: Mengonversi PDF ke Berbagai Format Gambar di Python
linktitle: Mengonversi PDF ke Gambar
type: docs
weight: 70
url: id/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF untuk Python untuk mengonversi PDF ke berbagai format gambar seperti TIFF, BMP, EMF, JPEG, PNG, GIF, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Gambaran Umum

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
 - [Python PDF ke EMF Converter](#python-pdf-to-emf)


_Format Gambar_: **JPG**
- [Python PDF ke JPG](#python-pdf-to-jpg)
- [Python Konversi PDF ke JPG](#python-pdf-to-jpg)
- [Python PDF ke JPG Converter](#python-pdf-to-jpg)


_Format Gambar_: **PNG**
- [Python PDF ke PNG](#python-pdf-to-png)
- [Python Konversi PDF ke PNG](#python-pdf-to-png)
- [Python PDF ke PNG Converter](#python-pdf-to-png)


_Format Gambar_: **GIF**
- [Python PDF ke GIF](#python-pdf-to-gif)
- [Python Konversi PDF ke GIF](#python-pdf-to-gif)
- [Python PDF ke GIF Converter](#python-pdf-to-gif)

_Format Gambar_: **SVG**
- [Python PDF ke SVG](#python-pdf-to-svg)
- [Python Konversi PDF ke SVG](#python-pdf-to-svg)
- [Python PDF ke SVG Converter](#python-pdf-to-svg)

## Python Konversi PDF ke Gambar

**Aspose.PDF untuk Python** menggunakan beberapa pendekatan untuk mengkonversi PDF ke gambar.
 Secara umum, kita menggunakan dua pendekatan: konversi menggunakan pendekatan Device dan konversi menggunakan SaveOption. Bagian ini akan menunjukkan cara mengonversi dokumen PDF ke format gambar seperti BMP, JPEG, GIF, PNG, EMF, TIFF, dan SVG menggunakan salah satu pendekatan tersebut.

Ada beberapa kelas dalam perpustakaan yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. DocumentDevice diorientasikan untuk konversi seluruh dokumen, tetapi ImageDevice - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF untuk Python** memungkinkan konversi Halaman PDF ke gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (berdasarkan DocumentDevice) memungkinkan Anda untuk mengonversi halaman PDF ke gambar TIFF. Kelas ini menyediakan metode bernama [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) yang memungkinkan Anda untuk mengonversi semua halaman dalam file PDF ke dalam satu gambar TIFF.

{{% alert color="success" %}}

**Cobalah mengonversi PDF ke TIFF secara online**
Aspose.PDF untuk Python via .NET menghadirkan aplikasi gratis online ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Konversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk Python menjelaskan cara mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

<a name="csharp-pdf-to-tiff"><strong>Langkah-langkah: Konversi PDF ke TIFF dalam Python</strong></a>

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Buat objek [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) dan [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/).

3. Panggil metode [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) untuk mengonversi dokumen PDF ke TIFF.
4. Untuk mengatur properti file keluaran, gunakan kelas [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).

Cuplikan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```python


from asposepdf import Api, Device

# inisialisasi lisensi
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Buka dokumen PDF
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# Buka dokumen PDF
document = Api.Document(input_pdf)
# Buat objek Resolution
resolution = Device.Resolution(300)

# Buat objek TiffSettings
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# Buat perangkat TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# Konversi halaman tertentu dan simpan gambar ke stream
tiffDevice.process(document, output_image)
```


## Mengonversi PDF menggunakan kelas ImageDevice

`ImageDevice` adalah nenek moyang untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) memungkinkan Anda mengonversi halaman PDF ke gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) memungkinkan Anda mengonversi halaman PDF ke gambar <abbr title="Enhanced Meta File">EMF</abbr>.
- Kelas [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) memungkinkan Anda mengonversi halaman PDF ke gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) memungkinkan Anda mengonversi halaman PDF ke gambar <abbr title="Portable Network Graphics">PNG</abbr>.

- Kelas [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) memungkinkan Anda mengonversi halaman PDF ke gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat bagaimana mengubah halaman PDF menjadi gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) menyediakan metode bernama [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) yang memungkinkan Anda mengubah halaman tertentu dari file PDF ke format gambar BMP. Kelas lainnya memiliki metode yang sama. Jadi, jika kita perlu mengonversi halaman PDF ke gambar, kita hanya perlu menginstansiasi kelas yang diperlukan.

Langkah-langkah berikut dan potongan kode di Python menunjukkan kemungkinan ini

 - [Mengonversi PDF ke BMP dalam Python](#python-pdf-to-image)
 - [Mengonversi PDF ke EMF dalam Python](#python-pdf-to-image)
 - [Mengonversi PDF ke JPG dalam Python](#python-pdf-to-image)
 - [Mengonversi PDF ke PNG dalam Python](#python-pdf-to-image)
 - [Mengonversi PDF ke GIF dalam Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Langkah-langkah: PDF ke Gambar (BMP, EMF, JPG, PNG, GIF) dalam Python</strong></a>

1. Muat file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Buat instance dari subclass [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/) yaitu.
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (untuk mengonversi PDF ke BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (untuk mengonversi PDF ke Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (untuk mengonversi PDF ke JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (untuk mengonversi PDF ke PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (untuk mengonversi PDF ke GIF)
3. Panggil metode [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) untuk melakukan konversi PDF ke Gambar.

### Mengonversi PDF ke BMP

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Buka dokumen PDF
document = Api.Document(input_pdf)

# Buat objek Resolusi
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # Buat nama file untuk disimpan
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # Konversi halaman tertentu dan simpan gambar ke file
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Mengubah PDF ke EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Buka dokumen PDF
document = Api.Document(input_pdf)

# Buat objek Resolusi
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # Buat nama file untuk disimpan
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # Konversi halaman tertentu dan simpan gambar ke file
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### Mengubah PDF ke JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Buka dokumen PDF
document = Api.Document(input_pdf)

# Buat objek Resolusi
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # Buat nama file untuk disimpan
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # Konversi halaman tertentu dan simpan gambar ke file
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Konversi PDF ke PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Buka dokumen PDF
document = Api.Document(input_pdf)

# Buat objek Resolusi
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # Buat nama file untuk disimpan
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # Konversi halaman tertentu dan simpan gambar ke file
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### Konversi PDF ke GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Buka dokumen PDF
document = Api.Document(input_pdf)

# Buat objek Resolusi
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # Buat nama file untuk disimpan
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # Konversi halaman tertentu dan simpan gambar ke file
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


{{% alert color="success" %}}
**Coba ubah PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan kepada Anda cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan Python dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba ubah PDF ke SVG secara online**

Aspose.PDF untuk Python melalui .NET menyajikan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskript, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman untuk membuatnya dengan program menggambar seperti Inkscape.

Aspose.PDF untuk Python mendukung fitur untuk mengonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengonversi file PDF ke format SVG.
 Untuk memenuhi persyaratan ini, kelas [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) telah diperkenalkan ke dalam namespace Aspose.PDF. Instansiasi objek dari SvgSaveOptions dan berikan sebagai argumen kedua ke metode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG dengan Python.

<a name="csharp-pdf-to-svg"><strong>Langkah-langkah: Mengonversi PDF ke SVG dalam Python</strong></a>

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Buat objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) dengan pengaturan yang diperlukan.
3. Panggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan berikan objek [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) untuk mengonversi dokumen PDF ke SVG.

### Mengonversi PDF ke SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```