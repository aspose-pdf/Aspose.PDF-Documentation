---
title: Tambahkan Halaman ke PDF Document
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /id/rust-cpp/add-pages/
description: Jelajahi cara menambahkan halaman ke PDF yang sudah ada dalam Rust dengan Aspose.PDF untuk meningkatkan dan memperluas dokumen Anda.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan PDF Pages dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ menyediakan fungsionalitas yang kuat untuk menambahkan Page ke Document PDF, memungkinkan pengembang membuat Page baru secara dinamis dan menyesuaikannya sesuai dengan kebutuhan khusus. Perpustakaan ini mendukung penyisipan Page kosong atau penyalinan Page dari Document yang ada sambil menawarkan opsi untuk menentukan ukuran Page, orientasi, dan konten. Kemampuan ini memungkinkan ekspansi dan penyesuaian Document yang mulus. Dokumentasi mencakup petunjuk terperinci dan contoh kode untuk membantu pengembang mengimplementasikan fitur penambahan Page secara efisien dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---

## Tambahkan Page dalam File PDF

Cuplikan kode Rust yang disediakan menunjukkan cara melakukan operasi Add Page di akhir PDF menggunakan pustaka Aspose.PDF.

1. Itu [buka](https://reference.aspose.com/pdf/rust-cpp/core/open/) Fungsi memungkinkan program memuat file PDF yang ada (sample.pdf) untuk manipulasi. Ini penting untuk semua operasi terkait PDF, seperti penyuntingan, penambahan konten, atau membaca data.
1. Itu [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) Metode digunakan untuk menyisipkan halaman kosong baru ke dalam dokumen PDF yang ada. Ini berguna untuk memperluas dokumen atau menyiapkannya untuk konten tambahan.
1. Itu [simpan](https://reference.aspose.com/pdf/rust-cpp/core/save/) metode memastikan bahwa modifikasi pada PDF ditulis kembali ke file. Langkah ini penting untuk mempertahankan perubahan, seperti penambahan halaman baru.

Potongan kode ini adalah contoh yang singkat dan efisien tentang cara menggunakan pustaka Aspose.PDF Rust untuk tugas manipulasi PDF dasar.

Aspose.PDF for Rust memungkinkan Anda menyisipkan halaman ke dokumen PDF di lokasi manapun dalam file serta menambahkan halaman ke akhir file PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## Sisipkan Halaman pada File PDF

Itu [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) metode menyisipkan halaman baru pada posisi yang ditentukan. Fitur ini berguna ketika Anda perlu menambahkan halaman tambahan ke dokumen yang sudah ada, misalnya, menambahkan bagian baru atau konten ke laporan atau presentasi.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```