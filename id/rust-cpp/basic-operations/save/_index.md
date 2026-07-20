---
title: Simpan dokumen PDF secara programatik
linktitle: Simpan PDF
type: docs
weight: 30
url: /id/rust-cpp/save-pdf-document/
description: Pelajari cara menyimpan file PDF dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Simpan dokumen PDF dengan Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ menawarkan fungsionalitas komprehensif untuk menyimpan dokumen PDF dalam berbagai format dan lokasi dengan efisiensi serta fleksibilitas tinggi. Perpustakaan ini memungkinkan pengembang menyimpan PDF ke sistem berkas, aliran memori, atau mengeluarkannya dalam format alternatif seperti DOCX, XLSX, dan gambar. Ini menyediakan opsi untuk menyesuaikan parameter penyimpanan, mengoptimalkan ukuran file, dan memastikan integritas data. Dokumentasi mencakup instruksi terperinci dan contoh kode untuk membantu pengembang mengimplementasikan kemampuan penyimpanan PDF secara efisien dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Simpan dokumen PDF ke sistem berkas

Contoh ini menunjukkan [baru](https://reference.aspose.com/pdf/rust-cpp/core/new/) metode untuk membuat dokumen PDF baru, yang merupakan fitur dasar untuk menghasilkan dokumen secara dinamis, seperti laporan atau faktur.

Kode ini sederhana dan dapat berfungsi sebagai templat untuk fitur yang lebih maju seperti menambahkan teks, gambar, atau anotasi ke PDF.

Contoh ini menunjukkan penggunaan langsung perpustakaan Aspose.PDF Rust, menampilkan potensinya untuk membuat, memodifikasi, dan menyimpan dokumen.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
