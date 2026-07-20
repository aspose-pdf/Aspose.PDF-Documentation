---
title: Optimalkan PDF menggunakan Aspose.PDF untuk Rust via C++
linktitle: Optimalkan File PDF
type: docs
weight: 10
url: /id/rust-cpp/optimize-pdf/
description: Optimalkan dan kompres file PDF menggunakan alat Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimalkan dan kompres file PDF menggunakan Aspose.PDF untuk Rust
Abstract: Aspose.PDF for Rust via C++ menawarkan fitur optimasi yang kuat untuk mengurangi ukuran dan meningkatkan kinerja dokumen PDF. Perpustakaan menyediakan berbagai opsi optimasi, termasuk mengompresi gambar, menghapus objek yang tidak terpakai, mengurangi ukuran font, dan mengoptimalkan aliran konten. Fitur-fitur ini membantu meningkatkan efisiensi penyimpanan dokumen dan memastikan waktu pemrosesan serta pemuatan yang lebih cepat. Dokumentasi menyediakan instruksi langkah demi langkah dan contoh kode untuk membantu pengembang dalam mengimplementasikan optimasi PDF secara efektif dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Optimalkan Dokumen PDF

Toolkit dengan Aspose.PDF for Rust via C\u002B\u002B memungkinkan Anda mengoptimalkan dokumen PDF.

Potongan kode ini berguna untuk aplikasi di mana pengurangan ukuran atau peningkatan efisiensi file PDF sangat penting, seperti untuk unggahan web, pengarsipan, atau berbagi melalui bandwidth terbatas.

1. The [buka](https://reference.aspose.com/pdf/rust-cpp/core/open/) metode memuat file PDF yang ditentukan (sample.pdf) ke memori.
1. The [optimalkan](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) mengurangi ukuran file dengan melakukan optimasi seperti menghapus objek yang tidak terpakai, mengompres gambar, meratakan anotasi, membatalkan embed font, dan memungkinkan penggunaan ulang konten. Langkah-langkah ini membantu mengurangi kebutuhan penyimpanan dan meningkatkan kecepatan pemrosesan untuk dokumen PDF.
1. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) metode menyimpan PDF yang dioptimalkan ke file baru.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```