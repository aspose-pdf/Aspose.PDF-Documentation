---
title: Tambahkan Teks ke PDF menggunakan Rust
linktitle: Tambahkan Teks ke PDF
type: docs
weight: 10
url: /id/rust-cpp/add-text-to-pdf-file/
description: Pelajari cara menambahkan teks ke dokumen PDF dalam Rust menggunakan Aspose.PDF untuk peningkatan konten dan pengeditan dokumen.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Tambahkan Teks ke PDF menggunakan Aspose.PDF untuk Rust
Abstract: Bagian Tambahkan Teks ke File PDF dalam dokumentasi Aspose.PDF untuk C++ dan Rust menyediakan petunjuk langkah demi langkah tentang penyisipan teks ke dalam dokumen PDF secara programatis. Bagian ini mencakup berbagai metode untuk menambahkan teks, termasuk penempatan, kustomisasi Font, penyesuaian warna, dan opsi perataan teks. Panduan tersebut menunjukkan cara menambahkan teks ke halaman dan lokasi tertentu dalam PDF, memastikan penempatan konten yang tepat. Dengan contoh kode dan penjelasan yang rinci, pengembang dapat dengan mudah mengintegrasikan fitur penyisipan teks ke dalam aplikasi mereka untuk peningkatan manajemen dokumen PDF.
SoftwareApplication: rust-cpp
---

Untuk menambahkan teks ke file PDF yang ada:

1. Buka file PDF.
1. Tambahkan teks ke dokumen PDF dengan [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) fungsi.
1. Menyimpan modifikasi ke file yang sama.

## Menambahkan Teks

Potongan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang sudah ada.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
