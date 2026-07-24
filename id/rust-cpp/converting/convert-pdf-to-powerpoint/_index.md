---
title: Konversi PDF ke PPTX dalam Rust
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF memungkinkan Anda mengonversi PDF ke format PPTX menggunakan Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alat Rust untuk Mengonversi PDF ke PowerPoint
Abstract: Aspose.PDF untuk Rust via C++ menyediakan solusi andal untuk mengonversi dokumen PDF ke format PowerPoint (PPTX) sambil mempertahankan tata letak, pemformatan, dan struktur konten asli. Fungsionalitas ini memungkinkan pengembang untuk secara mulus mengubah file PDF statis menjadi presentasi yang dinamis dan dapat diedit. Perpustakaan ini menawarkan opsi penyesuaian untuk mengontrol proses konversi, memastikan output berkualitas tinggi yang cocok untuk penggunaan bisnis dan profesional. Dokumentasi menyediakan petunjuk langkah demi langkah serta contoh kode untuk membantu pengembang mengintegrasikan konversi PDF-ke-PowerPoint dengan efisien ke dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Konversi PDF ke PPTX

Potongan kode Rust yang diberikan menunjukkan cara mengonversi dokumen PDF menjadi PPTX menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke PPTX menggunakan [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) fungsi.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Coba konversi PDF ke PowerPoint secara online**

Aspose.PDF for Rust menyajikan Anda aplikasi online gratis ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}