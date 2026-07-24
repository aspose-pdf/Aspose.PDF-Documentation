---
title: Contoh Hello World menggunakan bahasa Rust
linktitle: Contoh Hello World
type: docs
weight: 40
url: /id/rust-cpp/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World melalui Aspose.PDF for Rust
Abstract: Panduan Memulai untuk Aspose.PDF for Rust via C++ memberikan pengantar tentang cara bekerja dengan pustaka ini, mencakup langkah-langkah dasar untuk membuat dan memanipulasi dokumen PDF. Panduan ini menyertakan contoh 'Hello World' yang menunjukkan cara menghasilkan file PDF sederhana dengan konten teks, membantu pengembang dengan cepat memahami fungsi inti API.
SoftwareApplication: rust-cpp
---

Contoh "Hello World" secara tradisional digunakan untuk memperkenalkan fitur-fitur suatu bahasa pemrograman atau perangkat lunak dengan kasus penggunaan yang sederhana.

**Aspose.PDF for Rust** adalah API PDF yang kaya fitur yang memungkinkan pengembang menyematkan pembuatan dokumen PDF, manipulasi, dan kemampuan konversi dengan Rust. Ia mendukung banyak format file populer, termasuk PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, format gambar, dll. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!" Setelah memasang Aspose.PDF for Rust di lingkungan Anda, Anda dapat menjalankan contoh kode untuk melihat cara kerja API Aspose.PDF.
Cuplikan kode di bawah ini mengikuti langkah-langkah berikut:

1. Buat sebuah instance dokumen PDF baru.
1. Tambahkan halaman baru ke dokumen PDF menggunakan [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) fungsi.
1. Atur ukuran halaman menggunakan [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Tambahkan teks "Hello World!" ke halaman pertama menggunakan [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Simpan dokumen PDF menggunakan [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) metode.

Potongan kode berikut adalah program Hello World untuk menunjukkan cara kerja Aspose.PDF for Rust API.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
