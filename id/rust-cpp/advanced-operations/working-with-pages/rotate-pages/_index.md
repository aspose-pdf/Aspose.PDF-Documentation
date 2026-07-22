---
title: Putar Halaman PDF dengan Rust via C++
linktitle: Putar Halaman PDF
type: docs
weight: 50
url: /id/rust-cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara programatis dengan Rust via C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Putar Halaman PDF dengan Aspose.PDF untuk Rust
Abstract: Aspose.PDF for Rust via C++ menyediakan fungsi yang kuat untuk memutar halaman dalam dokumen PDF, memungkinkan pengembang mengubah orientasi halaman sesuai kebutuhan. Perpustakaan mendukung memutar halaman sebesar 90, 180, atau 270 derajat, memungkinkan penyesuaian cepat dan efisien pada tata letak dokumen. Fitur ini berguna untuk memperbaiki halaman yang salah orientasi atau mengubah presentasi dokumen. Dokumentasi mencakup instruksi langkah demi langkah dan contoh kode untuk membantu pengembang mengintegrasikan kemampuan pemutaran halaman secara mulus ke dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

Bagian ini menjelaskan cara mengubah orientasi halaman dari lanskap ke potret dan sebaliknya dalam file PDF yang ada menggunakan Rust

Memutar halaman memastikan penyelarasan yang tepat untuk pencetakan atau penampilan PDF dalam lingkungan profesional

1. Buka Dokumen PDF.
1. Putar Halaman PDF. The [putar](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) fungsi menerapkan rotasi spesifik (dalam hal ini, 180 derajat) pada halaman tertentu.
1. Simpan Perubahan ke File Baru. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) fungsi membuat file PDF baru untuk mempertahankan yang asli sekaligus menyimpan versi yang diperbarui.

Pada contoh ini, Anda memutar halaman tertentu dalam dokumen PDF:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```