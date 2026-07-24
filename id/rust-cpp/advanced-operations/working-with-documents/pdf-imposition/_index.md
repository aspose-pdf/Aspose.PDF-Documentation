---
title: PDF Imposition menggunakan Aspose.PDF for Rust via C++
linktitle: PDF Imposition
type: docs
weight: 30
url: /id/rust-cpp/pdf-imposition/
description: Artikel ini menjelaskan cara menyusun ulang halaman PDF untuk tata letak yang dioptimalkan untuk cetak menggunakan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara membuat Booklet atau N-Up dari file PDF
Abstract: Aspose.PDF for Rust via C++ menyediakan alat yang kuat untuk merestrukturisasi dokumen PDF guna memenuhi kebutuhan pencetakan dan tata letak. Artikel ini menunjukkan cara mengubah PDF standar menjadi sebuah booklet, memastikan urutan halaman yang benar untuk dilipat, dan cara membuat PDF N-Up yang menggabungkan beberapa halaman menjadi satu lembar. Dengan contoh kode Rust yang singkat, pengembang dapat dengan cepat menerapkan transformasi PDF siap cetak untuk dokumentasi, penerbitan, dan alur kerja arsip.
SoftwareApplication: rust-cpp
---

## Buat N-Up dari PDF

PDF N-Up menempatkan beberapa halaman sumber ke dalam satu halaman output. Dalam contoh ini, tata letak 2 × 2 digunakan, sehingga empat halaman asli digabungkan menjadi setiap halaman dokumen output.

1. Buka dokumen PDF sumber.
1. Simpan dokumen menggunakan tata letak N-Up dengan jumlah baris dan kolom yang ditentukan.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## Buat Booklet PDF

Aspose.PDF for Rust via C++ menjelaskan cara mengonversi dokumen PDF standar menjadi PDF bergaya buklet.
Format buklet menyusun ulang halaman sehingga, ketika dicetak dan dilipat, dokumen membentuk buklet yang tepat dengan halaman dalam urutan yang benar.

1. Buka dokumen PDF sumber.
1. Simpan dokumen sebagai PDF buklet.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**Harap dicatat bahwa Lisensi Uji Coba Gratis diperlukan untuk fungsionalitas penuh.**

Jelajahi hasil membuat booklet 4 halaman.

![Contoh booklet 4 halaman](sample_4.png)

Jelajahi hasil membuat booklet 3 halaman.

![Contoh booklet 3 halaman](sample_3.png)