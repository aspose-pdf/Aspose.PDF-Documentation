---
title: Atur warna latar belakang untuk PDF dengan Rust via C++
linktitle: Atur warna latar belakang
type: docs
weight: 80
url: /id/rust-cpp/set-background-color/
description: Atur warna latar belakang untuk file PDF Anda dengan Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur warna latar belakang untuk PDF dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ menawarkan fungsionalitas untuk mengatur warna latar belakang halaman PDF, memungkinkan pengembang menyesuaikan tampilan dokumen. Fitur ini memungkinkan penerapan warna solid ke seluruh latar belakang halaman, meningkatkan presentasi visual dokumen. Pengembang dapat dengan mudah menentukan nilai warna menggunakan model warna standar seperti RGB atau CMYK. Dokumentasi menyediakan petunjuk terperinci dan contoh kode untuk membantu pengembang menerapkan penyesuaian warna latar belakang secara efektif dalam aplikasi C++ mereka.
SoftwareApplication: rust-cpp
---

1. Potongan kode yang disediakan menunjukkan cara mengatur warna latar belakang untuk file PDF menggunakan pustaka Aspose.PDF dalam Rust.
1. Itu [buka](https://reference.aspose.com/pdf/rust-cpp/core/open/) metode memuat file PDF yang ditentukan ke dalam memori, memungkinkan manipulasi lebih lanjut, seperti mengubah tampilan atau kontennya.
1. Itu [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) metode menerapkan warna latar belakang baru ke dokumen PDF. Nilai RGB memungkinkan pengguna menyesuaikan gaya visual dokumen.
1. Itu [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) metode menyimpan PDF yang diperbarui dengan nama baru.

Kode ini ideal untuk aplikasi yang perlu mengotomatisasi penyesuaian PDF, seperti membuat laporan bermerek, menambahkan watermark, atau meningkatkan konsistensi visual di beberapa dokumen.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```