---
title: Buka dokumen PDF secara programatik
linktitle: Buka PDF
type: docs
weight: 20
url: /id/rust-cpp/open-pdf-document/
description: Pelajari cara membuka file PDF dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buka dokumen PDF dengan Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ menyediakan fungsionalitas kuat untuk membuka dan memuat dokumen PDF secara programatik, memungkinkan pengembang mengakses dan memanipulasi konten PDF dengan mudah. Perpustakaan ini mendukung pembukaan file PDF dari berbagai sumber, seperti jalur file dan aliran memori, sambil memastikan pemrosesan yang efisien dan manajemen sumber daya. Ini menawarkan fitur untuk memeriksa properti dokumen, mengekstrak teks dan gambar, serta melakukan operasi lainnya pada PDF yang dimuat. Dokumentasi mencakup instruksi detail dan contoh kode untuk membantu pengembang mengintegrasikan kemampuan membuka PDF ke dalam aplikasi mereka secara mulus.
SoftwareApplication: rust-cpp
---

## Buka dokumen PDF yang ada

Cuplikan kode menunjukkan operasi penting untuk bekerja dengan PDF menggunakan Aspose.PDF for Rust. Ini meliputi membuka file, menyimpan perubahan, dan menutup sumber daya dengan benar. Hal ini menjadikannya contoh dasar bagi pengembang yang menangani dokumen PDF.

Contohnya sederhana, sehingga mudah dipahami dan dimodifikasi. Ini ideal untuk pemula atau sebagai kerangka kerja untuk aplikasi yang lebih kompleks.

Kemampuan untuk membuka dan menyimpan dokumen PDF merupakan kebutuhan inti dalam banyak skenario, seperti menghasilkan laporan, memodifikasi dokumen, atau membuat alur kerja otomatis.

Contoh ini menampilkan kemudahan penggunaan API untuk manipulasi PDF sederhana, yang dapat diperluas untuk mencakup fitur-fitur lanjutan seperti ekstraksi teks, anotasi, atau pengisian formulir.

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
