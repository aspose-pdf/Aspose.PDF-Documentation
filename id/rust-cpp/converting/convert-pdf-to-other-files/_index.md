---
title: Konversi PDF ke EPUB, TeX, Text, XPS dalam Rust
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Alat Rust untuk Mengonversi PDF ke EPUB, TeX, Teks, dan XPS
Abstract: Aspose.PDF for Rust via C++ menawarkan kemampuan kuat untuk mengonversi dokumen PDF ke berbagai format file, termasuk DOCX, PPTX, HTML, EPUB, SVG, dan lainnya. Fungsionalitas ini memungkinkan pengembang mengekstrak dan menggunakan kembali konten PDF secara mulus sambil mempertahankan format, struktur, dan kualitas di berbagai format output. Pustaka menyediakan opsi fleksibel untuk menyesuaikan proses konversi sesuai dengan kebutuhan spesifik. Dokumentasi mencakup panduan komprehensif dan contoh kode untuk membantu pengembang dalam mengimplementasikan konversi PDF-ke-file secara efisien dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Ubah PDF menjadi EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat mengalir kembali, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Format ini menggantikan standar Open eBook.

Potongan kode Rust yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi EPUB menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke EPUB menggunakan [simpan_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke EPUB secara online**

Aspose.PDF for Rust mempersembahkan Anda aplikasi gratis online ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Convertion PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Konversi PDF ke TeX

**Aspose.PDF for Rust** mendukung mengkonversi PDF ke TeX.
Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penataan huruf berkualitas tinggi.

Cuplikan kode Rust yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi TeX menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke TeX menggunakan [simpan_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara daring**

Aspose.PDF for Rust mempersembahkan Anda aplikasi gratis online ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Ubah PDF menjadi TXT

Potongan kode Rust yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi TXT menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke TXT menggunakan [save_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke Teks secara online**

Aspose.PDF for Rust mempersembahkan Anda aplikasi gratis online ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke XPS

Tipe file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya bernama kode Metro dan menggabungkan konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penampilan dokumen ke dalam sistem operasi Windows.

**Aspose.PDF for Rust** memberikan kemungkinan untuk mengonversi file PDF menjadi <abbr title="XML Paper Specification">XPS</abbr> format. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Rust.

Potongan kode Rust yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi XPS menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke XPS menggunakan [simpan_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke XPS secara online**

Aspose.PDF for Rust mempersembahkan Anda aplikasi gratis online ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Ubah PDF menjadi PDF Grayscale

Potongan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi PDF Grayscale menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman PDF menjadi PDF Grayscale menggunakan [halaman_skala_abu-abu](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) fungsi.

Contoh ini mengonversi halaman tertentu dari PDF Anda ke Grayscale:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## Konversi PDF ke Markdawn

Potongan kode Rust yang diberikan menunjukkan cara mengonversi dokumen PDF menjadi file Markdown (.md) menggunakan Aspose.PDF untuk Rust.

1. Buka file PDF sumber.
1. Konversi PDF ke Markdown.
1. Simpan dokumen PDF yang dibuka sebagai file Markdown.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba konversi PDF ke MD secara online**

Aspose.PDF for Rust mempersembahkan Anda aplikasi gratis online ["PDF ke MD"](https://products.aspose.app/pdf/conversion/md), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke MD dengan Aplikasi Gratis](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}
