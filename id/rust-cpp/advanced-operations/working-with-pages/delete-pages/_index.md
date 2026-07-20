---
title: Hapus Halaman PDF dengan Rust melalui C++
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: /id/rust-cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Halaman PDF dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ menawarkan fungsionalitas yang efisien untuk menghapus halaman dari dokumen PDF, memungkinkan pengembang menghapus halaman yang tidak diinginkan atau tidak diperlukan dengan mudah. Perpustakaan ini memungkinkan penghapusan satu atau beberapa halaman dengan menentukan nomor halaman atau rentang, memastikan modifikasi dokumen yang tepat. Fitur ini membantu menyederhanakan file PDF dengan menghilangkan konten yang berlebih dan mengoptimalkan struktur dokumen. Dokumentasi menyediakan petunjuk langkah demi langkah serta contoh kode untuk membantu pengembang mengimplementasikan fungsi penghapusan halaman secara efektif dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

Anda dapat menghapus halaman dari file PDF menggunakan **Aspose.PDF for Rust via C++**. Potongan kode berikut menunjukkan cara memanipulasi dokumen PDF dengan menghapus halaman tertentu. Metode ini efisien untuk tugas manipulasi dokumen PDF, khususnya untuk menghapus halaman, menyimpan dokumen yang telah dimodifikasi, dan memastikan manajemen sumber daya yang tepat.

1. Membuka File PDF.
1. Menghapus Halaman Tertentu dengan [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) fungsi.
1. Menyimpan Dokumen menggunakan [simpan](https://reference.aspose.com/pdf/rust-cpp/core/save/) metode.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
