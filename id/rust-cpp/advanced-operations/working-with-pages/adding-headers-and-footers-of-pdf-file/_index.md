---
title: Menambahkan Header dan Footer ke PDF menggunakan Rust
linktitle: Menambahkan Header dan Footer ke PDF
type: docs
weight: 90
url: /id/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Header dan Footer ke PDF menggunakan Rust
Abstract: Artikel ini menunjukkan cara menambahkan header dan footer teks ke dokumen PDF menggunakan pustaka asposepdf Rust. Ini menjelaskan cara membuka PDF yang ada, menyisipkan teks konsisten ke header atau footer setiap halaman, dan menyimpan dokumen yang dimodifikasi sebagai file baru. Contoh-contoh menampilkan alur kerja sederhana yang aman dari kesalahan yang dapat digunakan untuk tugas seperti menambahkan nomor halaman, judul, atau branding secara programatis dalam aplikasi Rust.
SoftwareApplication: rust-cpp
---

## Menambahkan Header dan Footer sebagai Fragmen Teks

### Tambahkan teks di Footer PDF-document

Alat kami memungkinkan Anda membuka PDF yang sudah ada, menambahkan footer teks ke semua halaman, dan menyimpan PDF yang telah dimodifikasi sebagai file baru menggunakan pustaka asposepdf Rust. Ini menangani kesalahan dengan baik menggunakan tipe Result milik Rust.

1. Buka dokumen PDF yang sudah ada.
1. Tambahkan teks ke footer dengan [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Simpan PDF yang telah dimodifikasi.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Tambahkan teks di Header dokumen PDF

Potongan kode ini menunjukkan cara membuka file PDF yang ada, menambahkan header teks ke semua halaman, dan menyimpan dokumen yang telah dimodifikasi sebagai file baru menggunakan pustaka asposepdf. Ini menyediakan cara sederhana dan otomatis untuk menyisipkan header yang konsisten ke dalam PDF.

1. Buka PDF yang ada.
1. Tambahkan teks ke Header dengan bantuan [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Simpan PDF yang telah dimodifikasi.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```