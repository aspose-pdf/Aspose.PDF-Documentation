---
title: Konversi PDF ke EPUB, TeX, Teks, XPS di Go
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Text, XPS, dll menggunakan Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Alat Golang untuk Mengonversi PDF ke EPUB, TeX, Text, dan XPS
Abstract: Aspose.PDF for Go via C++ menawarkan kemampuan kuat untuk mengonversi dokumen PDF ke berbagai format file, termasuk DOCX, PPTX, HTML, EPUB, SVG, dan lainnya. Fungsionalitas ini memungkinkan pengembang mengekstrak dan menggunakan kembali konten PDF secara mulus sambil mempertahankan format, struktur, dan kualitas di berbagai format output. Perpustakaan menyediakan opsi fleksibel untuk menyesuaikan proses konversi sesuai dengan kebutuhan spesifik. Dokumentasi mencakup panduan komprehensif dan contoh kode untuk membantu pengembang dalam mengimplementasikan konversi PDF-ke-file secara efisien di dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Konversi PDF ke EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat mengalir ulang, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi EPUB menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke EPUB menggunakan [SimpanEpub]() fungsi.
1. Tutup dokumen PDF dan bebaskan semua sumber daya yang dialokasikan.

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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke EPUB secara daring**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis secara online ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya saat bekerja.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Konversi PDF ke TeX

**Aspose.PDF for Go** mendukung konversi PDF ke TeX.
Format file LaTeX adalah format file teks dengan penanda khusus dan digunakan dalam sistem penyusunan dokumen berbasis TeX untuk penataan huruf berkualitas tinggi.

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi TeX menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke TeX menggunakan [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) fungsi.
1. Tutup dokumen PDF dan bebaskan semua sumber daya yang dialokasikan.

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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis secara online ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya saat bekerja.

[![Konversi Aspose.PDF PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke TXT

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi TXT menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke TXT menggunakan [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) fungsi.
1. Tutup dokumen PDF dan bebaskan semua sumber daya yang dialokasikan.

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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba konversi PDF ke Teks secara online**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis secara online ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya saat bekerja.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Ubah PDF menjadi XPS

Tipe berkas XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), sebelumnya bernama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dokumen dan penayangannya ke dalam sistem operasi Windows.

**Aspose.PDF for Go** memberikan kemungkinan untuk mengonversi file PDF ke <abbr title="XML Paper Specification">XPS</abbr> format. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Go.

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi XPS menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke XPS menggunakan [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) fungsi.
1. Tutup dokumen PDF dan bebaskan semua sumber daya yang dialokasikan.

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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke XPS secara online**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis secara online ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya saat bekerja.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Ubah PDF menjadi PDF Grayscale

Potongan kode Go yang diberikan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi PDF Grayscale menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman PDF menjadi PDF Grayscale menggunakan [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) fungsi.
1. Tutup dokumen PDF dan bebaskan semua sumber daya yang dialokasikan.

Contoh ini mengonversi halaman tertentu dari PDF Anda ke Grayscale:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

Contoh ini akan mengonversi seluruh dokumen PDF menjadi Grayscale:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```