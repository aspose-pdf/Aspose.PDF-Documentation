---
title: Konversi PDF ke Format Gambar di Rust
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /id/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: Topik ini menunjukkan cara menggunakan Aspose.PDF for Rust untuk mengonversi PDF ke berbagai format gambar mis. TIFF, BMP, JPEG, PNG, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Alat untuk mengonversi PDF ke format gambar dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ memungkinkan konversi mulus dokumen PDF ke berbagai format gambar, termasuk JPEG, PNG, BMP, dan TIFF. Fitur ini memungkinkan pengembang untuk merender gambar berkualitas tinggi sambil mempertahankan konten, tata letak, dan resolusi dokumen asli. Perpustakaan ini menyediakan opsi fleksibel untuk pengaturan output seperti resolusi, kualitas gambar, dan kedalaman warna. Dokumentasi menyediakan petunjuk langkah demi langkah serta contoh kode untuk membantu pengembang mengintegrasikan konversi PDF ke gambar secara efisien ke dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Konversi PDF ke Gambar

Dalam artikel ini, kami akan menunjukkan kepada Anda opsi-opsi untuk mengonversi PDF ke format gambar.

Dokumen yang dipindai sebelumnya sering disimpan dalam format file PDF. Namun, apakah Anda perlu mengeditnya di editor grafis atau mengirimnya lebih lanjut dalam format gambar? Kami memiliki alat universal untuk Anda mengonversi PDF ke gambar menggunakan **Aspose.PDF for Rust via C++**.
Tugas paling umum adalah ketika Anda perlu menyimpan seluruh dokumen PDF atau beberapa halaman tertentu dari dokumen sebagai sekumpulan gambar. **Aspose.PDF for Rust via C++** memungkinkan Anda mengonversi PDF ke format JPG dan PNG untuk menyederhanakan langkah-langkah yang diperlukan agar mendapatkan gambar Anda dari file PDF tertentu.

**Aspose.PDF for Rust via C++** mendukung berbagai konversi format PDF ke gambar. Harap periksa bagian tersebut [Format File yang Didukung Aspose.PDF](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### Konversi PDF ke JPEG

Potongan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar JPEG menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke JPEG menggunakan [page_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke JPEG secara online**

Aspose.PDF for Rust mempersembahkan aplikasi gratis online kepada Anda ["PDF ke JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya saat beroperasi.

[![Konversi PDF ke JPEG dengan Aplikasi Gratis Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### Konversi PDF ke TIFF

Cuplikan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar TIFF menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke TIFF menggunakan [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke TIFF secara daring**

Aspose.PDF for Rust mempersembahkan aplikasi gratis online kepada Anda ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya saat beroperasi.

[![Aspose.PDF konversi PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Konversi PDF ke PNG

Potongan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar PNG menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi sebuah Halaman ke PNG menggunakan [page_to_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke PNG secara daring**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikutnya.

Aspose.PDF for Rust mempersembahkan aplikasi gratis online kepada Anda ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya saat beroperasi.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah sebuah keluarga spesifikasi format file berbasis XML untuk grafik vektor dua dimensi, baik yang statis maupun dinamis (interaktif atau beranimasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

### Konversi PDF ke SVG

Potongan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari sebuah dokumen PDF menjadi gambar SVG menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke SVG menggunakan [page_to_svg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke SVG secara daring**

Aspose.PDF for Rust mempersembahkan aplikasi gratis online kepada Anda ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya saat beroperasi.

[![Konversi PDF ke SVG dengan Aplikasi Gratis Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### Konversi PDF ke arsip ZIP SVG

Contoh berikut mengonversi dokumen PDF menjadi arsip SVG, di mana setiap halaman disimpan sebagai file SVG terpisah di dalam wadah ZIP.

1. Buka dokumen PDF sumber.
1. Simpan dokumen sebagai arsip ZIP yang berisi file SVG.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### Konversi PDF ke DICOM

Potongan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar DICOM menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke DICOM menggunakan [halaman_ke_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### Konversi PDF ke BMP

Cuplikan kode Rust yang disediakan menunjukkan cara mengonversi halaman pertama dari dokumen PDF menjadi gambar BMP menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi Halaman ke BMP menggunakan [page_to_bmp](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) fungsi.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```