---
title: Ekstrak Teks dari PDF menggunakan Rust
linktitle: Ekstrak Teks dari PDF
type: docs
weight: 30
url: /id/rust-cpp/extract-text-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak Teks dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ menyediakan cara yang kuat dan efisien untuk mengekstrak teks dari dokumen PDF. Perpustakaan ini mendukung berbagai teknik ekstraksi, memungkinkan pengguna untuk mengambil teks dari seluruh dokumen, halaman tertentu, atau area yang telah ditentukan dalam PDF.
SoftwareApplication: rust-cpp
---

## Ekstrak Teks dari Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah tugas yang sangat umum dan berguna. PDF sering berisi informasi penting yang perlu diakses, dianalisis, atau diproses untuk berbagai keperluan. Mengekstrak teks memungkinkan penggunaan kembali yang lebih mudah dalam basis data, laporan, atau dokumen lain.

Mengekstrak teks membuat konten PDF dapat dicari, memungkinkan pengguna menemukan informasi spesifik dengan cepat tanpa harus meninjau seluruh dokumen secara manual.

Jika Anda ingin mengekstrak teks dari dokumen PDF, Anda dapat menggunakan [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) fungsi.
Silakan periksa potongan kode berikut untuk mengekstrak teks dari file PDF menggunakan Rust.

1. Buka dokumen PDF dengan nama file yang diberikan.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) mengekstrak konten teks dari dokumen PDF.
1. Cetak teks yang diekstrak ke konsol.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```