---
title: Konversi PDF ke Format Gambar dalam Go
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /id/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF for Go untuk mengonversi PDF ke berbagai format gambar, misalnya TIFF, BMP, JPEG, PNG, SVG, dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Alat untuk Mengonversi PDF ke format Gambar dengan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ memungkinkan konversi PDF dokumen secara mulus ke berbagai format gambar, termasuk JPEG, PNG, BMP, dan TIFF. Fitur ini memungkinkan pengembang merender gambar berkualitas tinggi sambil mempertahankan konten, tata letak, dan resolusi dokumen asli. Perpustakaan menyediakan opsi fleksibel untuk pengaturan output seperti resolusi, kualitas gambar, dan kedalaman warna. Dokumentasi menawarkan instruksi langkah demi langkah serta contoh kode untuk membantu pengembang mengintegrasikan konversi PDF ke gambar secara efisien ke dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Go Konversi PDF ke Gambar

Dalam artikel ini, kami akan menunjukkan Anda opsi untuk mengkonversi PDF ke format gambar.

Dokumen yang dipindai sebelumnya sering disimpan dalam format file PDF. Namun, apakah Anda perlu mengeditnya di editor grafis atau mengirimnya lebih lanjut dalam format gambar? Kami memiliki alat universal untuk Anda mengonversi PDF menjadi gambar menggunakan **Aspose.PDF for Go via C++**.
Tugas paling umum adalah ketika Anda perlu menyimpan seluruh dokumen PDF atau beberapa halaman tertentu dari dokumen sebagai sekumpulan gambar. **Aspose.PDF for Go via C++** memungkinkan Anda mengonversi PDF ke format JPG dan PNG untuk menyederhanakan langkah-langkah yang diperlukan untuk mendapatkan gambar Anda dari file PDF tertentu.

**Aspose.PDF for Go via C++** mendukung konversi berbagai format PDF ke gambar. Silakan periksa bagian tersebut. [Format File yang Didukung oleh Aspose.PDF](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## Konversi PDF ke JPEG

Potongan kode Go yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar JPEG menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke JPEG menggunakan [HalamanKeJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke JPEG secara daring**

Aspose.PDF for Go mempersembahkan aplikasi gratis online ["PDF ke JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF konversi PDF ke JPEG dengan Aplikasi Gratis](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Konversi PDF ke TIFF

Potongan kode Go yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar TIFF menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman menjadi TIFF menggunakan [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke TIFF secara online**

Aspose.PDF for Go mempersembahkan aplikasi gratis online ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Konversi PDF ke PNG

Potongan kode Go yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar PNG menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke PNG menggunakan [HalamanKePng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara daring**

Sebagai contoh cara kerja aplikasi gratis kami, silakan periksa fitur berikutnya.

Aspose.PDF for Go mempersembahkan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah sekumpulan spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG merupakan standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

## Ubah PDF ke SVG

Potongan kode Go yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar SVG menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke SVG menggunakan [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF for Go mempersembahkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## Konversi PDF ke DICOM

Potongan kode Go yang diberikan menunjukkan cara mengonversi halaman pertama dokumen PDF menjadi gambar DICOM menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke DICOM menggunakan [HalamanKeDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Konversi PDF ke BMP

Potongan kode Go yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar BMP menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke BMP menggunakan [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```