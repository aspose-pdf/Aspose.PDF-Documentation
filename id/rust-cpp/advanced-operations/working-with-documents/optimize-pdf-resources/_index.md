---
title: Optimalkan Sumber Daya PDF menggunakan Rust melalui C++
linktitle: Optimalkan Sumber Daya PDF
type: docs
weight: 15
url: /id/rust-cpp/optimize-pdf-resources/
description: Optimalkan Sumber Daya file PDF menggunakan alat Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimalkan Sumber Daya PDF menggunakan Aspose.PDF untuk Rust
Abstract: Aspose.PDF for Rust via C++ menyediakan kemampuan lanjutan untuk mengoptimalkan sumber daya PDF, meningkatkan efisiensi dokumen dan mengurangi ukuran file. Perpustakaan ini memungkinkan pengembang mengoptimalkan font, gambar, dan metadata dengan menghapus data berlebih dan mengompresi sumber daya tanpa mengorbankan kualitas dokumen. Teknik optimasi ini meningkatkan kinerja dokumen, menjadikan PDF lebih cocok untuk berbagi dan penyimpanan. Dokumentasi menyediakan panduan terperinci dan contoh kode untuk membantu pengembang mengimplementasikan optimasi sumber daya secara efektif dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Optimalkan Sumber Daya PDF

Optimalkan sumber daya dalam dokumen:

  1. Sumber daya yang tidak digunakan pada halaman dokumen dihapus.
  1. Sumber daya yang sama digabungkan menjadi satu objek.
  1. Objek yang tidak terpakai dihapus.

Optimisasi dapat mencakup kompresi gambar, menghapus objek yang tidak terpakai, dan mengoptimalkan font untuk mengurangi ukuran file serta meningkatkan kinerja. Setiap kesalahan selama operasi ini dicatat dan menghentikan program.  
 
1. The [buka](https://reference.aspose.com/pdf/rust-cpp/core/open/) metode memuat file PDF yang ditentukan (sample.pdf) ke memori.
1. Mengoptimalkan sumber daya dalam PDF untuk efisiensi menggunakan [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) metode.
1. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) metode menyimpan PDF yang dioptimalkan ke file baru.

Potongan kode berikut menunjukkan cara mengoptimalkan dokumen PDF.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_open.pdf")?;

      Ok(())
  }
```