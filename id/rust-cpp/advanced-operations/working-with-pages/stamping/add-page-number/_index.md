---
title: Menambahkan Nomor Halaman ke PDF dengan Rust
linktitle: Menambahkan Nomor Halaman
type: docs
weight: 10
url: /id/rust-cpp/add-page-number/
description: Artikel ini menunjukkan cara menambahkan nomor halaman ke dokumen PDF yang ada menggunakan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Nomor Halaman
Abstract: Aspose.PDF for Rust via C++ memungkinkan pengembang meningkatkan dokumen PDF yang ada dengan penomoran halaman otomatis hanya dalam beberapa baris kode. Contoh ini menunjukkan cara membuka file PDF, menyisipkan nomor halaman pada semua halaman, dan menyimpan dokumen yang diperbarui sebagai file baru. Mengotomatiskan penomoran halaman memastikan struktur dokumen yang konsisten dan sangat berguna untuk laporan, kontrak, manual, serta output multi‑halaman lainnya yang disiapkan untuk distribusi atau pencetakan.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ menyediakan fungsionalitas bawaan untuk memodifikasi dokumen PDF secara programatik. Pada contoh ini, aplikasi membuka file PDF yang ada, menerapkan penomoran halaman otomatis pada setiap halaman, dan menyimpan dokumen yang telah dimodifikasi dengan nama baru.

Pendekatan ini berguna saat membuat dokumen final untuk distribusi, pencetakan, atau tujuan arsip. Prosesnya hanya memerlukan beberapa baris kode dan tidak mengubah file asli kecuali secara eksplisit ditimpa.

Penomoran halaman adalah kebutuhan umum untuk laporan, faktur, kontrak, manual, dan dokumen multi‑halaman lainnya. The [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) metode secara otomatis menyisipkan nomor halaman ke semua halaman dokumen, memastikan pagination yang konsisten di seluruh file.

Setelah menambahkan nomor halaman, dokumen yang diperbarui disimpan sebagai file PDF baru.

1. Buka dokumen PDF yang ada.
1. Tambahkan nomor halaman dengan [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) metode.
1. Simpan dokumen yang diperbarui.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```